import pytest
from model_bakery import baker

from rest_framework.test import APIClient

from students.models import Student, Course


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture()
def students():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=1)
    href = '/api/v1/courses/' + str(courses[0].id) + '/'

    # Act
    response = client.get(href)

    # Assert
    assert response.status_code == 200, 'Ошибка статус-кода'
    data = response.json()
    assert data['name'] == courses[0].name, 'Несоответствие наименования курса'


@pytest.mark.django_db
def test_courses(client, courses_factory):
    # Arrange
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200, 'Ошибка статус-кода'
    data = response.json()
    assert len(data) == quantity, 'Несоответствие количества курса'
    for i, n in enumerate(data):
        assert n['name'] == courses[i].name, 'Несоответствие наименования курса'


@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    # Arrange
    quantity = 10
    course_id = 0
    courses = courses_factory(_quantity=quantity)
    href = '/api/v1/courses/?id=' + str(courses[course_id].id)

    # Act
    response = client.get(href)

    # Assert
    assert response.status_code == 200, 'Ошибка статус-кода'
    data = response.json()
    assert len(data) == 1, 'Ошибка уникального id'
    assert data[course_id]['name'] == courses[course_id].name, 'Несоответствие наименования курса по id'


@pytest.mark.django_db
def test_filter_name(client, courses_factory):
    # Arrange
    quantity = 10
    course_id = 0
    courses = courses_factory(_quantity=quantity)
    course_name = courses[course_id].name
    href = '/api/v1/courses/?name=' + course_name

    # Act
    response = client.get(href)

    # Assert
    assert response.status_code == 200, 'Ошибка статус-кода'
    data = response.json()
    for n in data:
        assert n['name'] == course_name, 'Ошибка выборки по имени курса'


@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    href = '/api/v1/courses/'
    data = {
        "name": "TEST",
        "students": [],
    }

    # Act
    response = client.post(href, data=data)

    # Assert
    assert response.status_code == 201, 'Ошибка статус-кода'
    response_data = response.json()
    assert response_data['name'] == data["name"], 'Ошибка наименования'
    assert response_data['students'] == data["students"], 'Ошибка списка студентов'


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    # Arrange
    quantity = 10
    course_id = 0
    courses = courses_factory(_quantity=quantity)
    href = '/api/v1/courses/' + str(courses[course_id].id) + '/'
    data = {
        "name": "TEST",
        "students": [],
    }

    # Act
    response = client.patch(href, data=data)

    # Assert
    assert response.status_code == 200, 'Ошибка статус-кода'
    response_data = response.json()
    assert response_data['name'] == data["name"], 'Ошибка наименования'
    assert response_data['students'] == data["students"], 'Ошибка списка студентов'


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    # Arrange
    quantity = 10
    course_id = 0
    courses = courses_factory(_quantity=quantity)
    href = '/api/v1/courses/' + str(courses[course_id].id) + '/'

    # Act
    response = client.delete(href)
    response_data = client.get(href)

    # Assert
    assert response.status_code == 204, 'Ошибка статус-кода delete'
    assert response_data.status_code == 404, 'Ошибка статус-кода get'
    assert response_data.json()['detail'] == 'Not found.'
