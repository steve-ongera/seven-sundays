from django.core.management.base import BaseCommand
from e_commerce.models import Product, Category, Brand
from faker import Faker
import random
from django.utils.text import slugify

fake = Faker()

class Command(BaseCommand):
    help = 'Generate 4 to 13 products per category'

    def handle(self, *args, **kwargs):
        categories = Category.objects.filter(is_active=True)
        brands = list(Brand.objects.filter(is_active=True))

        if not brands:
            self.stdout.write(self.style.ERROR("No brands available. Please create some brands first."))
            return

        for category in categories:
            num_products = random.randint(4, 13)

            for _ in range(num_products):
                name = fake.unique.sentence(nb_words=3).replace('.', '')
                slug = slugify(name)
                sku = fake.unique.bothify(text='SKU-#####')
                price = round(random.uniform(5.0, 500.0), 2)
                compare_price = price + round(random.uniform(10.0, 100.0), 2) if random.choice([True, False]) else None
                cost_price = price - round(random.uniform(1.0, 20.0), 2)
                quantity = random.randint(0, 100)
                weight = round(random.uniform(0.1, 5.0), 2)

                product = Product.objects.create(
                    name=name,
                    slug=slug,
                    description=fake.text(max_nb_chars=300),
                    short_description=fake.sentence(),
                    sku=sku,
                    category=category,
                    brand=random.choice(brands),
                    price=price,
                    compare_price=compare_price,
                    cost_price=cost_price,
                    quantity=quantity,
                    weight=weight,
                    is_active=True,
                    is_featured=random.choice([True, False]),
                    requires_shipping=True,
                    is_digital=random.choice([False, False, True]),  # Mostly physical
                    meta_title=name[:60],
                    meta_description=fake.text(max_nb_chars=150)
                )

                self.stdout.write(self.style.SUCCESS(f"Created product: {product.name} in {category.name}"))

        self.stdout.write(self.style.SUCCESS("✔️ Product generation completed."))
