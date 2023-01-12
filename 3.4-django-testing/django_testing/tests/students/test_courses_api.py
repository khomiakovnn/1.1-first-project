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
    assert response.status_code == 200, 'Ошибочный статус-код'
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
    assert response.status_code == 200
    data = response.json()
    assert len(data) == quantity
    for i, n in enumerate(data):
        assert n['name'] == courses[i].name
