from django.core.management.base import BaseCommand
from e_commerce.models import Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Generate top-level product categories'

    def handle(self, *args, **kwargs):
        categories = [
            "Electronics", "Phones & Tablets", "Computers & Accessories", "Home & Kitchen",
            "Fashion", "Health & Beauty", "Baby, Kids & Toys", "Groceries & Food",
            "Appliances", "Automotive", "Books & Stationery", "Gaming & Consoles",
            "Sports & Fitness", "TVs & Audio", "Office Equipment", "Watches & Jewelry",
            "Pet Supplies", "Musical Instruments", "Industrial & Scientific", "Travel & Luggage"
        ]

        for name in categories:
            slug = slugify(name)
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={
                    'slug': slug,
                    'description': f'{name} products and accessories',
                    'is_active': True,
                    'meta_title': name,
                    'meta_description': f'Buy {name.lower()} online at best prices',
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category already exists: {name}'))
