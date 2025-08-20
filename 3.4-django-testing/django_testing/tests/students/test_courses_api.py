import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()  # создаем курс

    url = reverse('courses-detail', args=[course.id])
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=10)

    url = reverse('courses-list')
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == len(courses)

@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    courses = course_factory(_quantity=5)
    target_course = courses[2]

    url = reverse('courses-list')
    response = api_client.get(url, data={'id': target_course.id})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == target_course.id

@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    courses = course_factory(_quantity=5)
    target_course = courses[0]

    url = reverse('courses-list')
    response = api_client.get(url, data={'name': target_course.name})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == target_course.name

@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('courses-list')
    data = {'name': 'Курс программирования'}
    response = api_client.post(url, data = data, format='json')

    assert response.status_code == 201
    assert response.data['name'] == data['name']

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(name='Old name')
    url = reverse('courses-detail', args=[course.id])

    new_data = {'name': 'New name'}
    response = api_client.patch(url, data=new_data, format='json')

    assert response.status_code == 200

@pytest.mark.django_db
def test_course_delete(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])

    response = api_client.delete(url)

    assert response.status_code == 204
    from students.models import Course
    assert not Course.objects.filter(id=course.id).exists()