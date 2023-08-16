import datetime
import pandas as pd

def validate_search(input):
    menu_name = str(input).strip()
    return menu_name

def remove_csv_duplicates(file, *columns):
    df = pd.read_csv(file)
    
    # columns = ['column_name1', 'column_name2']
    data_no_duplicates = df.drop_duplicates(subset=columns)  # Remove duplicates

    # Write back to CSV
    return data_no_duplicates.to_csv(file, index=False)

# def path_to_csv(data):
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     return f"{current_directory}/data/{data}.csv"

def capture_text(file,*texts):
    with open(file, "a", encoding='utf-8') as log:
        log_date = f"\n=================={datetime.datetime.now()}=======================\n"
        log.write(log_date)
        for text in texts:
            log.write(text)

def capture_csv(file,*texts):
    with open(file, "a") as trash:
        if len(texts)>=2:
            line = f"\n{texts[0]}({texts[1]})"
        else:
            line = f"\n{texts[0]}"
        trash.write(line)

###### REF #######
# https://github.com/llSourcell/twitter_sentiment_challenge/issues/1