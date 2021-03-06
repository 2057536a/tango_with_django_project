import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url = url
	p.views=views
	p.save()
	return p



def add_cat(name, views=0, likes=0):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c

def populate():
	# First, we will create lists of dictionaries containing the pages
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.

	python_pages = [
		{"title": "Official Python Tutorial",
			"url": "http://docs.python.org/2/tutorial/",
			"views":213},
		{"title": "How to Think like a Computer Scientist",
			"url":"http://www.greenteapress.com/thinkpython/",
			"views":323},
		{"title":"Learn Python in 10 Minutes",
			"url":"http://www.korokithakis.net/tutorials/python/",
			"views":526}]


	django_pages = [
		{"title": "Official Django Tutorial",
			"url": "http://docs.djangoproject.com/en/1/9/intro/tutorial01/",
			"views":102},
		{"title": "Django Rocks",
			"url":"http://www.djangorocks.com/",
			"views":111},
		{"title":"How to Tangowith Django",
			"url":"http://www.tangowithdjango.com/",
			"views":34}]


	other_pages = [
		{"title":"Bottle",
			"url":"http://bottlepy.org/docs/dev/",
			"views":3},
		{"title":"Flask",
			"url":"http://flask.pocoo.org",
			"views":209}]




	cats = [
        {'name': 'Python',
        'views': 128,
        'likes': 64,
        'pages': python_pages},
        
        {'name': 'Django',
        'views': 64,
        'likes': 32,
        'pages': django_pages},
        
        {'name': 'Other Frameworks',
        'views': 32,
        'likes': 16,'pages': other_pages}
    ]



	# If you want to add more categories or pages,
	# add them to the dictionaries above.

	# The code below goes through the cats dictionary, then adds each category,
	# and then adds all the associated pages for that category.
	# if you are using Python 2.x the use cats.iteritems() see
	# http://docs.quantifiedcode.com/python-anti-patterns/readability/
	# for more information about how to iterate over a dictionary properly.




	for cat in cats:
		c = add_cat(cat['name'], cat['views'], cat['likes'])
		for p in cat["pages"]:
			add_page(c,p["title"], p["url"], p["views"])

	
#	# Print out the categories we have added.
#	for c in Category.objects.all():
#		for p in Page.objects.filter(category=c):
#			print("-{0} - {1}".format(str(c), str(p)))
#
#
	# Print out the categories we have added.
	for cat in cats:
		c = add_cat(cat['name'], cat['views'], cat['likes'])
		for page in cat['pages']:
			p = add_page(c, page['title'], page['url'], page['views'])
			print('- {0} - {1}'.format(str(c), str(p)))







# Start execution here!
if __name__=='__main__':
	print("Starting Rango population script...")
	populate()

