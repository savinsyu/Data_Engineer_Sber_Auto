import pandas as pd
import dill
import json
from pathlib import Path
from datetime import datetime
import os



path = os.path.expanduser('~/airflow_hw') # 'это путь до папки проекта
def predict():
    path = os.environ.get('PROJECT_PATH', '.')

    for pkl_path in Path(f"{path}/data/models").glob("*.pkl"):
        with open(pkl_path, 'rb') as file:
            model = dill.load(file)

    df_pred = pd.DataFrame(columns=['car_id', 'pred'])
    count = 0

    for json_path in Path(f"{path}/data/test").glob("*.json"):
        with open(json_path, "r") as rf:
            data = json.load(rf)
        df = pd.DataFrame(data, index=[0])
        df_pred.loc[count] = json_path.name[:-5], model.predict(df)[0]
        count += 1

    df_pred.to_csv(f'{path}/data/predictions/preds_{datetime.now().strftime("%Y%m%d%H%M")}', index=False)

if __name__ == '__main__':
    predict()
