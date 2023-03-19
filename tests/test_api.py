import allure

import pytest
import requests

@allure.step("Проверяю статус код существующего url")
def test_send_existing_url(dog_ceo_url):
    """Check that status code of a specific existing url is 200"""
    response = requests.get(dog_ceo_url + "/dog-api")
    assert response.status_code == 200


@allure.step("Проверяю статус код несуществующего url")
def test_send_nonexistent_url(dog_ceo_url):
    """Check that status code of a nonexistent url is 404"""
    response = requests.get(dog_ceo_url + "/nonexistent-url")
    assert response.status_code == 404


@allure.step("Проверяю наличие пород в message в ответе json")
@pytest.mark.parametrize("breed", ["dachshund",
                                   "samoyed",
                                   "pug"])
def test_check_breed(dog_breed_url, breed):
    """Check that there are specific breeds in response url message"""
    response = requests.get(dog_breed_url + breed + "/images/random")
    assert breed in response.json()["message"]


@allure.step("Проверяю наличие подпород в message в ответе json")
@pytest.mark.parametrize("breed", ["hound",
                                   "mastiff"])
def test_check_subbreed(dog_breed_url, breed):
    """Check that there are sub-breeds of specific breeds (hound, mastiff) in
    response url message"""
    subbreed = requests.get(dog_breed_url + breed + "/list")
    response = requests.get(dog_breed_url + breed + "/images/random")
    for x in subbreed.json()["message"]:
        if x in response.json()["message"]:
            assert breed + "-" + x in response.json()["message"]


@allure.step("Проверяю статус код в ответе json рандомной породы")
def test_check_image_status(dog_ceo_url):
    """Check that status (in json) of a random image is Success"""
    response = requests.get(dog_ceo_url + "/api/breeds/image/random")
    assert "success" in response.json()["status"]
