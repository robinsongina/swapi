from .models import Film
from graphql_relay import from_global_id


def generic_model_mutation_process(model, data, id=None, commit=True):
    '''
    Funcion generica para procesar una mutacion de un modelo,
    Esta funcion se debe llamar desde las mutaciones de los modelos que se
    van a usar, para guardar o actualizar los datos de un modelo.

    :param model: Nombre del Modelo a procesar
    :param data: Informacion del modelo a Guardar o Actualizar
    :param id: ID del modelo
    :param commit: Boolean para indicar si se debe guardar o no

    :return: retorna la instancia del modelo creado o actualizado
    '''
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item


def add_people_to_film(people, films):
    '''
    Funcion para agregar los personajes que pertenecen a una pelicula

    :param people: Instancia del personaje
    :param film: Lista de Peliculas
    '''
    for item_film in films:
        try:
            film_instance = Film.objects.get(id=from_global_id(item_film.id)[1])
            film_instance.characters.add(people)
            film_instance.save()
        except Film.DoesNotExist:
            pass


def update_people_to_film(people, films):
    '''
    Funcion para actualiar los personajes que pertenecen a una pelicula

    :param people: Instancia del personaje
    :param film: Lista de Peliculas
    '''
    films = [{'id': from_global_id(film['id'])[1]} for film in films]
    films_character = Film.objects.filter(characters=people)

    for film in films_character:
        if {'id': film.id} not in films:
            film.characters.remove(people)
            film.save()
