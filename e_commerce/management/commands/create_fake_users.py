from django.core.management.base import BaseCommand
from e_commerce.models import User
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = "Generate 50 fake users"

    def handle(self, *args, **kwargs):
        for _ in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = (first_name + last_name).lower()
            email = f"{username}@gmail.com"

            if User.objects.filter(email=email).exists():
                continue  # Skip if email already exists

            user = User.objects.create_user(
                username=username,
                email=email,
                password="password123",  # Default password
                first_name=first_name,
                last_name=last_name,
                phone=fake.phone_number(),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=60),
                is_verified=random.choice([True, False])
            )

            self.stdout.write(self.style.SUCCESS(f"Created user {email}"))
