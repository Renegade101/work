import pandas as pd
Scores = pd.DataFrame([], columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

Scores = pd.DataFrame([{'id':1, 'score':3.5},
                       {'id':2, 'score':3.65},
{'id':3, 'score':4.0},
{'id':4, 'score':3.85},
{'id':5, 'score':4.0},
                       {'id':6, 'score':3.65}])


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Use the rank method to assign ranks to the scores in descending order with no gaps
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    # Drop id column & Sort the DataFrame by score in descending order
    result_df = scores.drop('id', axis=1).sort_values(by='score', ascending=False)

    return result_df

print(order_scores(Scores))