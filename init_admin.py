"""Create the initial administrator without changing existing accounts."""
import os


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_shop.settings")

    import django
    django.setup()

    from django.contrib.auth import get_user_model
    from django.db import transaction
    from accounts.models import Profile

    username = os.environ.get("ADMIN_USERNAME", "").strip()
    password = os.environ.get("ADMIN_PASSWORD", "")
    email = os.environ.get("ADMIN_EMAIL", "").strip()

    if not username:
        print("Admin initialization skipped: ADMIN_USERNAME is not set.")
        return

    User = get_user_model()
    with transaction.atomic():
        user = User.objects.filter(username=username).first()
        if user is None:
            if not password:
                print("Admin initialization skipped: ADMIN_PASSWORD is not set.")
                return
            user = User.objects.create_superuser(
                username=username, email=email, password=password,
            )
            print("Initial administrator created.")
        elif not (user.is_staff and user.is_superuser and user.is_active):
            raise RuntimeError(
                "ADMIN_USERNAME belongs to an existing account that is not "
                "an active administrator. Choose a different ADMIN_USERNAME."
            )
        else:
            print("Administrator already exists; credentials unchanged.")

        Profile.objects.get_or_create(user=user)


if __name__ == "__main__":
    main()
