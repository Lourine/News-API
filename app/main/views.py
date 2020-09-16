from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_source,article_source,get_category,search_source

#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    search_source = request.args.get('source_query')
    if search_source:
        return redirect(url_for('main.search',source_name =search_source))
    else:
        return render_template('index.html',sources=source)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )

@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)

@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)