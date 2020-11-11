import requests
from django.core.management.base import BaseCommand
from champions.models import Champion


def get_champion():
    name = []
    champions = []

    result = requests.get(
        "http://ddragon.leagueoflegends.com/cdn/10.19.1/data/ko_KR/champion.json"
    )
    champ_json = result.json()
    champ_name = champ_json.get("data")
    for champ in champ_name:
        name.append(champ)

    for c in name:
        champ_info = champ_json.get("data").get(c)
        champ_id = champ_info["id"]
        key = champ_info["key"]
        title = champ_info["title"]
        bio = champ_info["blurb"]
        position = champ_info["tags"]
        image_full = champ_info.get("image")["full"]
        square_image = (
            f"http://ddragon.leagueoflegends.com/cdn/10.19.1/img/champion/{image_full}"
        )
        loading_image_name = f"{champ_id}_0.jpg"
        loading_image = f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{loading_image_name}"

        champ_dict = {
            "champ_id": champ_id,
            "key": key,
            "title": title,
            "bio": bio,
            "position": position,
            "square_image": square_image,
            "loading_image": loading_image,
        }
        champions.append(champ_dict)
    return champions


class Command(BaseCommand):
    help = "Champion create"

    def handle(self, *args, **options):
        champ = get_champion()
        for c in champ:
            Champion.objects.create(
                name=c.get("champ_id"),
                title=c.get("title"),
                bio=c.get("bio"),
                square_image=c.get("square_image"),
                loading_image=c.get("loading_image"),
            )

        return self.stdout.write(self.style.SUCCESS("Champion Created!"))