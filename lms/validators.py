from rest_framework.serializers import ValidationError


def validate_video_link(value):
    if value.lower()[:17] != "https://youtu.be/" and value.lower()[:24] != "https://www.youtube.com/":
        raise ValidationError("Можно использовать только ссылки начинающиеся: "
                              "https://youtu.be/ или https://www.youtube.com/")
