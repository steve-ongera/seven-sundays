from django.core.management.base import BaseCommand
from e_commerce.models import (
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeAssignment
)
import random

class Command(BaseCommand):
    help = 'Assign random attributes and values to products'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        attributes = ProductAttribute.objects.prefetch_related('values')

        if not products.exists():
            self.stdout.write(self.style.ERROR("No products found."))
            return

        if not attributes.exists():
            self.stdout.write(self.style.ERROR("No product attributes found."))
            return

        assignments_created = 0

        for product in products:
            selected_attributes = random.sample(list(attributes), random.randint(1, min(5, attributes.count())))

            for attribute in selected_attributes:
                # Skip if already assigned to this product
                if ProductAttributeAssignment.objects.filter(product=product, attribute=attribute).exists():
                    continue

                # Get all valid values for this attribute
                values = list(attribute.values.all())
                if not values:
                    continue

                value = random.choice(values)

                ProductAttributeAssignment.objects.create(
                    product=product,
                    attribute=attribute,
                    value=value
                )

                assignments_created += 1
                self.stdout.write(self.style.SUCCESS(
                    f"Assigned {attribute.name} = {value.value} to {product.name}"
                ))

        self.stdout.write(self.style.SUCCESS(f"🎉 Done! {assignments_created} attribute assignments created."))
