import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType, PeopleType
from .utils import generic_model_mutation_process, add_people_to_film, update_people_to_film


class filmInput(graphene.InputObjectType):
    id = graphene.ID()


class CreatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return CreatePlanetMutation(planet=planet)


class CreatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.String(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=True)
        home_world = graphene.String(required=True)
        films = graphene.List(filmInput)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        planet_id = input.get('home_world', None)
        films = input.get('films', None)

        if films is not None:
            del input["films"]

        planet = Planet.objects.get(id=from_global_id(planet_id)[1])
        if planet:
            input['home_world'] = planet

        data = {'model': People, 'data': input}

        people = generic_model_mutation_process(**data)

        if films is not None:
            add_people_to_film(people, films)

        return CreatePeopleMutation(people=people)


class UpdatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String(required=False)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.String(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=False)
        home_world = graphene.String(required=False)
        films = graphene.List(filmInput)

    errors = graphene.List(graphene.String)
    people = graphene.Field(PeopleType)

    '''Falta Mirar lo de los films'''
    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)
        films = input.get('films', None)

        if films is not None:
            del input["films"]

        try:
            people_instance = People.objects.get(id=from_global_id(raw_id)[1])

            data = {'model': People, 'data': input}

            if raw_id:
                data['id'] = from_global_id(raw_id)[1]

            if people_instance:
                people = generic_model_mutation_process(**data)

            if films is not None:
                update_people_to_film(people, films)
                add_people_to_film(people, films)

            return UpdatePeopleMutation(people=people)
        except Exception as e:
            return UpdatePeopleMutation(people=None, errors=e)
