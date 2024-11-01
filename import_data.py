import pandas as pd
from src.config.db import createSession
from model.model import Data
file_path = 'dataset/smart_app_data.pkl'

if __name__ == '__main__':
    print('import data from pickle file...')
    df = pd.read_pickle(file_path)
    data = []
    for row in df.itertuples(index=True, name='Row'):
        Data(
            time=row.time,
            asset_id=row.asset_id,
            name=row.name,
            kpi=row.kpi,
            sum=row.sum,
            avg=row.avg,
            min=row.min,
            max=row.max
        )
        data.append(d)
    print('start inserting data into db...')
    session = createSession()
    session.add_all(data)
    session.commit()
    session.close()
    print('insert operation completed')