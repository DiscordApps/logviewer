import pendulum
from drf_yasg import openapi
from rest_framework import status

from api.v2 import serializers

now = pendulum.now().isoformat()

archive_responses = {
    status.HTTP_201_CREATED: openapi.Response('URL Created', serializers.LogArchiveSerializer, examples={
        'application/json': {
            'url': 'https://logs.discord.website/api/v2/archive/eyJ0eXBlIjoiY2FwbmJvdCIsInVybCI6Imh0dHBzOi8vd2V'
                   'iaG9vay5zaXRlL2FjYzEwMjg0LWUyZWUtNDBhMy1hOTk4LTk2YWY4ZThkY2RmNyIsImV4cGlyZXMiOiIxMG1pbiJ9.S'
                   'HkRI3FA1wwIshEv_wLYU8G9pmM'
        }
    }),
    status.HTTP_400_BAD_REQUEST: openapi.Response('Bad Request', serializers.LogErrorSerializer, examples={
        'application/json': {
            'errors': {
                'url': [
                    'URL must lead to a valid JSON array of Discord message objects!'
                ],
                'expires': [
                    'Expiry time must be one of 10min, 30min, 1hour, 1day, 1week!'
                ],
                'privacy': [
                    'Privacy value must be one of public, guild, mods, invite!'
                ]
            }
        }
    })
}

create_responses = {
    status.HTTP_201_CREATED: openapi.Response('Log Created', serializers.LogListSerializer, examples={
        'application/json': {
            'owner': 'lorem',
            'uuid': '6kd6nYMuebE5yhwvGWohCQ',
            'url': 'https://logs.discord.website/6kd6nYMuebE5yhwvGWohCQ',
            'type': 'logger',
            'created': '1970-01-01T00:00:00.000000',
            'expires': now
        }
    }),
    status.HTTP_400_BAD_REQUEST: openapi.Response('Bad Request', serializers.LogErrorSerializer, examples={
        'application/json': {
            'errors': {
                'messages': [
                    'This field is required.'
                ],
                'expires': [
                    'Expiry time must be one of 10min, 30min, 1hour, 1day, 1week!'
                ],
                'privacy': [
                    'Privacy value must be one of public, guild, mods, invite!'
                ]
            }
        }
    })
}

list_responses = {
    status.HTTP_200_OK: openapi.Response('List Logs', serializers.LogListSerializer, examples={
        'application/json': [
            {
                'owner': 'lorem',
                'uuid': '6kd6nYMuebE5yhwvGWohCQ',
                'url': 'https://logs.discord.website/6kd6nYMuebE5yhwvGWohCQ',
                'type': 'logger',
                'created': '1970-01-01T00:00:00.000000',
                'expires': now
            },
            {
                'owner': 'ipsum',
                'uuid': 'DHYCLTzjqREHg2ttnWvbYk',
                'url': 'https://logs.discord.website/DHYCLTzjqREHg2ttnWvbYk',
                'type': 'rawgoat',
                'created': '1970-01-01T00:00:00.000000',
                'expires': now
            },
            {
                'owner': 'foobar',
                'uuid': '8hx7t3SPLJD2Zom5ZCYRb2',
                'url': 'https://logs.discord.website/8hx7t3SPLJD2Zom5ZCYRb2',
                'type': 'rosalina_bottings',
                'created': '1970-01-01T00:00:00.000000',
                'expires': now
            },
        ]
    })
}

read_responses = {
    status.HTTP_200_OK: openapi.Response('Get Log', serializers.LogListSerializer, examples={
        'application/json': {
            'owner': 'ipsum',
            'uuid': 'DHYCLTzjqREHg2ttnWvbYk',
            'url': 'https://logs.discord.website/DHYCLTzjqREHg2ttnWvbYk',
            'type': 'rawgoat',
            'created': '1970-01-01T00:00:00.000000',
            'expires': now
        },
    })
}

url_parameter = openapi.Parameter('uuid', openapi.IN_PATH, description='Log\'s UUID', type=openapi.TYPE_STRING)
