from django.db import models


class Director(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.TextField(max_length=100)
    description = models.CharField(max_length=250)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @property
    def category_name(self):
        try:
            return self.director.name
        except:
            return 'no category'

    @property
    def filter_reviews(self):
        #return self.reviews.filter(stars__gt=3)
     return self.reviews.filter(stars__in=[4, 5])

    @property
    def rating(self):
        reviews = self.filter_reviews
        count = reviews.count()
        sum_ = 0
        for i in reviews:
            sum_+= i.stars
        try:
          return sum_ / count
        except ZeroDivisionError:
            return 0


STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)


class Review(models.Model):
    text = models.CharField(max_length=280)
    stars = models.IntegerField(default=5, choices=STARS)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text

    def stars_str(self):
        return self.stars * '*'

