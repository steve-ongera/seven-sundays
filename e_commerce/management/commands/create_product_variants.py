from django.core.management.base import BaseCommand
from e_commerce.models import Product, ProductVariant
from faker import Faker
import random
from decimal import Decimal

fake = Faker()

class Command(BaseCommand):
    help = 'Generate product variants (size, color, etc.) for each product'

    def handle(self, *args, **kwargs):
        products = Product.objects.filter(is_active=True)

        variant_types = {
            "Size": ["XS", "S", "M", "L", "XL", "XXL"],
            "Color": ["Red", "Blue", "Green", "Black", "White", "Yellow", "Gray"],
            "Storage": ["32GB", "64GB", "128GB", "256GB", "512GB"]
        }

        if not products.exists():
            self.stdout.write(self.style.ERROR("No products found. Create products first."))
            return

        for product in products:
            num_variants = random.randint(1, 5)
            created_variants = 0
            used_names = set()

            while created_variants < num_variants:
                variant_type = random.choice(list(variant_types.keys()))
                variant_value = random.choice(variant_types[variant_type])
                name = f"{variant_type} {variant_value}"

                if name in used_names:
                    continue  # Avoid duplicates per product

                used_names.add(name)

                sku = fake.unique.bothify(text='VAR-#####')
                price = product.price + Decimal(str(round(random.uniform(-5, 15), 2)))
                quantity = random.randint(0, 50)

                ProductVariant.objects.create(
                    product=product,
                    name=name,
                    sku=sku,
                    price=price,
                    quantity=quantity,
                    is_active=True
                )

                self.stdout.write(self.style.SUCCESS(f"Created variant '{name}' for product '{product.name}'"))
                created_variants += 1

        self.stdout.write(self.style.SUCCESS("✅ Product variant generation completed."))
