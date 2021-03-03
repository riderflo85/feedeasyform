from .models import Planning


def list_all_planning():
    return [
        (x.pk, f"planning n°{x.pk}") for x in Planning.objects.all()
    ]
