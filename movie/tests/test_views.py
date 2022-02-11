from django.test import TestCase, Client
from movie.models import Movie, Actor


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(
                            name='Movie 1',
                            year=2000,
                            imdb='example.com/movie1',
                            genre='Action',
                            )
        self.movie = Movie.objects.create(
            name='Movie 2',
            year=2012,
            imdb='youtube.com/movie2',
            genre='Adventure',
        )
        self.client = Client()

    def test_get_all_list(self):
        response = self.client.get('/netflix/movies/')
        print(response)
        data = response.data
        assert response.status_code == 200
        assert len(data) >= 1
        print(data)

    def test_search_by_name(self):
        response = self.client.get('/netflix/movies/?search=movie')
        print(response)
        data = response.data
        assert response.status_code == 200
        assert len(data) >= 1
        assert data[0]['year'] == 2000

    def test_ordering_by_imdb(self):
        response = self.client.get('/netflix/movies/?ordering=-imdb')
        data = response.data
        print(data)
        assert response.status_code == 200
        assert len(data) >= 1
        assert data[0]['imdb'] == 'youtube.com/movie2'

    def test_ordering_by_minus_imdb(self):
        response = self.client.get('/netflix/movies/?ordering=imdb')
        data = response.data
        print(data)
        assert response.status_code == 200
        assert len(data) >= 1
        assert data[0]['imdb'] == 'example.com/movie1'
