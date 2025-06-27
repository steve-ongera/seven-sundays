from django.core.management.base import BaseCommand
from e_commerce.models import ProductAttribute
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Generate common product attributes (color, size, material, etc.)'

    def handle(self, *args, **kwargs):
        attributes = [
            "Color", "Size", "Material", "Weight", "Storage Capacity",
            "Screen Size", "Battery Life", "Resolution", "Fabric", "Style",
            "Flavor", "Scent", "Wattage", "Voltage", "Speed",
            "Length", "Height", "Width", "Connectivity", "Operating System",
            "Gender", "Age Group", "Shape", "Finish", "Compatibility"
        ]

        for attr_name in attributes:
            attr_slug = slugify(attr_name)
            attribute, created = ProductAttribute.objects.get_or_create(
                name=attr_name,
                defaults={'slug': attr_slug}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created attribute: {attr_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Attribute already exists: {attr_name}"))

        self.stdout.write(self.style.SUCCESS("✅ Product attributes generation complete."))
