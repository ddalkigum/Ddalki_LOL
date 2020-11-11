import sys
import os
import hashlib
import hmac
import base64
import requests
import time
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    nickname = models.CharField(max_length=10)
    avatar = models.ImageField(blank=True, upload_to="user_image")
    bio = models.TextField(max_length=1000)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=120, blank=True)
    birthdate = models.DateField(blank=True, null=True)


def make_signature():
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)
    accessKey = ""
    secretKey = ""
    access_key = accessKey
    secret_key = secretKey
    secret_key = bytes(secret_key, "UTF-8")
    method = "GET"
    uri = "/photos/puppy.jpg?query1=&query2"
    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, "UTF-8")
    signingKey = base64.b64encode(
        hmac.new(secret_key, message, digestmod=hashlib.sha256).digest()
    )
    return signingKey


def sms():
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)
    signkey = make_signature()
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": timestamp,
        "x-ncp-iam-access-key": "",
        "x-ncp-apigw-signature-v2": signkey,
    }
    print(signkey)

    body = {
        "type": "SMS",
        "contentType": "COMM",
        "countryCode": "82",
        "from": "01039949377",
        "content": "인증",
        "messages": [{"to": "01039949377"}],
    }
    serviceId = ""

    return requests.post(
        f"https://sens.apigw.ntruss.com/sms/v2/services/{serviceId}/messages",
        headers=headers,
        json=body,
    )
