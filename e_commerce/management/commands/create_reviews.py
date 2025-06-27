from django.core.management.base import BaseCommand
from e_commerce.models import Product, Review, User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Generate 2 to 5 reviews per product from random users"

    def handle(self, *args, **kwargs):
        products = Product.objects.filter(is_active=True)
        users = User.objects.filter(is_active=True)

        if not products.exists():
            self.stdout.write(self.style.ERROR("No products found."))
            return

        if not users.exists():
            self.stdout.write(self.style.ERROR("No users found."))
            return

        total_reviews = 0

        for product in products:
            review_users = random.sample(list(users), min(random.randint(2, 5), users.count()))

            for user in review_users:
                # Ensure unique review per product-user
                if Review.objects.filter(product=product, user=user).exists():
                    continue

                rating = random.randint(1, 5)
                title = fake.sentence(nb_words=6)
                content = fake.paragraph(nb_sentences=3)

                Review.objects.create(
                    product=product,
                    user=user,
                    rating=rating,
                    title=title,
                    content=content,
                    is_verified=random.choice([True, False]),
                    is_approved=random.choice([True, False])
                )

                total_reviews += 1
                self.stdout.write(self.style.SUCCESS(
                    f"📝 Review for '{product.name}' by {user.email} ({rating}★)"
                ))

        self.stdout.write(self.style.SUCCESS(f"✅ Created {total_reviews} reviews in total."))
