import pandas as pd

World = (pd.DataFrame([],
                     columns=['name', 'continent', 'area', 'population', 'gdp']).astype
                                    ({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'}))

World = pd.DataFrame([{'name':'Afghanistan', 'continent':'Asia', 'area':652230, 'population':25500100, 'gdp':20343000000},
      {'name':'Albania', 'continent':'Europe', 'area':28748, 'population':2831741, 'gdp':12960000000}])
#Data=[{'name':'Afghanistan', 'continent':'Asia', 'area':'652230', 'population':'25500100', 'gdp':'20343000000'},
 #     {'name':'Albania', 'continent':'Europe', 'area':'28748', 'population':'2831741', 'gdp':'12960000000'}]

#World=World.append(Data,ignore_index=True)

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]

print(big_countries(World))