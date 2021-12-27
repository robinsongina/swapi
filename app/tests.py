import json

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema

CREATE_PEOPLE_MUTATION = '''
  mutation createPeople{
    createPeopleMutation(input: {
      name: "Robinson Giraldo Naranjo"
      gender: "male"
      homeWorld: "UGxhbmV0VHlwZTox"
      eyeColor: "black"
      films:[
        {
          id: "RmlsbVR5cGU6MTAw"
        }
        {
          id: "RmlsbVR5cGU6NA=="
        }
        {
          id: "RmlsbVR5cGU6NQ=="
        }
      ]
    })
    {
      people{
        id
        name
        homeWorld{
          name
        }
        films{
          edges{
            node{
              title
              id
            }
          }
        }
      }
    }
  }
'''

UPDATE_PEOPLE_MUTATION = '''
  mutation updatePeopleMutation{
    updatePeopleMutation(input: {
      id: "UGVvcGxlVHlwZTox"
      height: "200"
      mass: "unknown"
      hairColor: "black"
      eyeColor: "brown"
      birthYear: "unknown"
      gender: "female"
      films: [
        {
          id: "RmlsbVR5cGU6MTAw"
        }
        {
          id: "RmlsbVR5cGU6NA=="
        }
      ]
    }) {
      errors
      clientMutationId
      people {
        id
        name
        height
        gender
        films{
          edges{
            node{
              title
            }
          }
        }
      }
    }
  }
'''


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)


class PeopleUnitTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_create_people_response(self):
        response = self.query(
            CREATE_PEOPLE_MUTATION,
        )

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        self.assertEqual(len(content['data']['createPeopleMutation']['people']['films']['edges']), 2)

    def test_update_people_response(self):
        response = self.query(
            UPDATE_PEOPLE_MUTATION,
        )

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        self.assertEqual(content['data']['updatePeopleMutation']['people']['height'], '200')
