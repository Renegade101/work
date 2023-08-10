import pandas as pd

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
Activity = (pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).
            astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'}))

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    #activity = activity['event_date'].sort_values(ascending=True)
    first = activity.groupby('player_id')['event_date'].idxmin()
    activity = activity.loc[first]
    activity = activity.drop(columns = {'device_id', 'games_played'})
    return activity.rename(columns={'event_date':'first_login'})

print(game_analysis(Activity))