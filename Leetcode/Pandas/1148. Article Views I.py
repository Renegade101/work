import pandas as pd
Views = (pd.DataFrame([], columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype
         ({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'}))

Views = pd.DataFrame([{'article_id':1, 'author_id':3, 'viewer_id':5, 'view_date':'2019-08-01'},
{'article_id':1, 'author_id':3, 'viewer_id':6, 'view_date': '2019-08-02'},
                      {'article_id':2, 'author_id':7, 'viewer_id':7, 'view_date':'2019-08-01'},
                      {'article_id':2, 'author_id':7, 'viewer_id':6, 'view_date':'2019-08-02'},
                      {'article_id':4, 'author_id':7, 'viewer_id':1, 'view_date':'2019-07-22'},
                      {'article_id':3, 'author_id':4, 'viewer_id':4, 'view_date':'2019-07-21'},
                      {'article_id':3, 'author_id':4, 'viewer_id':4, 'view_date':'2019-07-21'}])


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors_viewed_own_articles = views[views['author_id'] == views['viewer_id']]

    unique_authors = authors_viewed_own_articles['author_id'].unique()

    unique_authors = sorted(unique_authors)

    result_df = pd.DataFrame({'id': unique_authors})

    return result_df

print(article_views(Views))