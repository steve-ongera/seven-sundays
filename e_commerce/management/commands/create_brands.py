from django.core.management.base import BaseCommand
from e_commerce.models import Brand
from django.utils.text import slugify
import random

class Command(BaseCommand):
    help = 'Generate 60 popular product brands'

    def handle(self, *args, **kwargs):
        brands = [
            "Samsung", "Apple", "Sony", "LG", "Dell", "HP", "Lenovo", "Asus", "Huawei", "Xiaomi",
            "Infinix", "Tecno", "Nokia", "Oppo", "Vivo", "Canon", "Nikon", "Hisense", "TCL", "Panasonic",
            "Adidas", "Nike", "Puma", "Reebok", "Under Armour", "Zara", "H&M", "Gucci", "Chanel", "Versace",
            "Maybelline", "L'Oréal", "Neutrogena", "Nivea", "Dove", "Garnier", "Mac", "Fenty Beauty", "Clinique", "Estée Lauder",
            "Nestlé", "Coca-Cola", "Pepsi", "Kellogg’s", "Cadbury", "Unilever", "Procter & Gamble", "Colgate", "Palmolive", "Dettol",
            "Toyota", "Honda", "BMW", "Ford", "Chevrolet", "Mercedes-Benz", "Hyundai", "Kia", "Jeep", "Volkswagen"
        ]

        for brand_name in brands:
            slug = slugify(brand_name)
            website = f"https://www.{slug}.com"

            brand, created = Brand.objects.get_or_create(
                name=brand_name,
                defaults={
                    'slug': slug,
                    'description': f"{brand_name} branded products available",
                    'website': website,
                    'is_active': True
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created brand: {brand_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Brand already exists: {brand_name}"))
