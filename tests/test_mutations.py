import pytest
from swapi.schema import schema
from graphene.test import Client
from app.tests import CREATE_PEOPLE_MUTATION, UPDATE_PEOPLE_MUTATION


@pytest.fixture
def client_query():
    return Client(schema)


@pytest.fixture
def query_all_planets():
    return '''
        query {
            allPlanets {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
        }
    '''


@pytest.mark.django_db
def test_query_all_planets(client_query, query_all_planets):
    response = client_query.execute(
        query_all_planets,
    )

    assert 'errors' not in response

    assert len(response['data']['allPlanets']['edges']) == 61


@pytest.mark.django_db
def test_create_people_mutation(client_query):
    response = client_query.execute(
        CREATE_PEOPLE_MUTATION,
    )

    assert 'errors' not in response

    assert len(response['data']['createPeopleMutation']['people']['films']['edges']) == 2


@pytest.mark.django_db
def test_update_people_mutation(client_query):
    response = client_query.execute(
        UPDATE_PEOPLE_MUTATION,
    )

    assert 'errors' not in response

    print(response['data']['updatePeopleMutation']['people']['height'])

    assert response['data']['updatePeopleMutation']['people']['height'] == '200'
