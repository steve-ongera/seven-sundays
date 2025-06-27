from django.core.management.base import BaseCommand
from e_commerce.models import Address, User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Generate at least one address for each user'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_active=True)
        address_types = ['billing', 'shipping']

        if not users.exists():
            self.stdout.write(self.style.ERROR("No users found in the database."))
            return

        created_count = 0

        for user in users:
            if user.addresses.exists():
                self.stdout.write(self.style.WARNING(f"User {user.email} already has address(es), skipping."))
                continue

            # Generate 1 or 2 addresses
            num_addresses = random.randint(1, 2)

            for i in range(num_addresses):
                addr = Address.objects.create(
                    user=user,
                    type=random.choice(address_types),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    company=fake.company() if random.choice([True, False]) else '',
                    address_line_1=fake.street_address(),
                    address_line_2=fake.secondary_address() if random.choice([True, False]) else '',
                    city=fake.city(),
                    state=fake.state(),
                    postal_code=fake.postcode(),
                    country=fake.country(),
                    phone=fake.phone_number(),
                    is_default=(i == 0)  # First address is default
                )

                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"✅ Created address for user {user.email}: {addr}"))

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Done! {created_count} addresses created."))
