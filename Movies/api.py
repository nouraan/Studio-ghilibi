from io import StringIO
from urllib.parse import urljoin
from typing import Dict, List, Union

import requests


Films_Persons_Dict = Dict[str, Union[str, List[str]]]
Films_Dict = Dict[str, str]
Person_Dict = Dict[str, List[str]]
Films_Persons_Dict_Filter = Dict[str, Union[str, List[str]]]
Films_Dict_Filter = Dict[str, str]
Person_Dict_Filtered= Dict[str, List[str]]

class StudioGhibliApi:
   
    #The URLS
    base_url = 'https://ghibliapi.herokuapp.com'
    films_url = urljoin(base_url, '/films')
    people_url = urljoin(base_url, '/people')

#Movies from the Ghibli API,For each movie the people that appear in it
    @classmethod
    def Get_Films_And_People(self) -> List[Films_Persons_Dict]:
        films_with_people = self.Films_Query().copy()
      

        # for every person get all film's id
        for person in self.People_Query():
            for person_film_id in person['films_id']:

                # and compare film id with person's film id
                for film in films_with_people:
                    if person_film_id == film['id']:

                        # people key don't exist. create it.
                        if not isinstance(film.get('people'), list):
                            film['people'] = []

                        film['people'].append(person['name'])
     
        return films_with_people
 
    #Return Films Name and ID
    @classmethod
    def Films_Query(self) -> List[Films_Persons_Dict]:
        films_data = requests.get(self.films_url).json()
        films = [self.parse_film_title_and_id(film) for film in films_data]

        return films

    @classmethod
    def People_Query(self) -> List[Films_Persons_Dict]:
        people_data = requests.get(self.people_url).json()
        people = [
            self.parse_name_and_films_id(person)
            for person in people_data
        ]

        return people

    #return film Title & ID
    @classmethod
    def parse_film_title_and_id(self, film: Films_Persons_Dict) -> Films_Dict: 
        return {
            'id': film.get('id'),
            'title': film.get('title'),
        }
   #return person name & film id
    @classmethod
    def parse_name_and_films_id(self, person: Films_Persons_Dict) -> Person_Dict:
        return {
            'name': person.get('name'),
            'films_id': [
                self.Parse_Film_ID_From_URL(film)
                for film in person.get('films')
            ],
        }

    @classmethod
    def Parse_Film_ID_From_URL(self, film: str) -> str:
        return film.split('/')[-1]



#Find Film Filter
    @classmethod
    def Films_Filter(self,FinalDict,FilmName) -> List[Films_Persons_Dict_Filter]:
        FilmName=FilmName.translate({ord('/'): None})
        return [element for element in FinalDict if element['title'] == FilmName]


    @classmethod
    def People_Filter(self,FinalDict,PersonName) -> List[Films_Persons_Dict_Filter]:
         return [element for element in FinalDict if element['people'].items() == PersonName]
        #  return [k for k, v in FinalDict.items() if PersonName in v]
