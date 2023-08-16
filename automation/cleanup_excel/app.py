from flask import Flask, request, render_template, send_file
import pandas as pd

app = Flask(__name__)
regex = '[^a-zA-Z0-9]'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    global file
    file = request.files['file']
    try:
        df = pd.read_excel(file)
    except:
        file_error = 'Please upload a TestCase template'
        return render_template(
                'index.html',
                display_error = file_error
                )
    
    def clean_data(*chars,col=df):
        for char in chars:
            col['NAME'] = col['NAME'].str.replace(char,'_')
            # col['STEP_ID'] = col['STEP_ID'].str.replace(char,'_')
        return col
    
    # Remove special characters from Column 'NAME'
    try:
        [clean_data(regex,'__') for _ in range(5)] # run five times
    except KeyError:
        column_error = "'Name' column is not available in this file. Please upload a TestCase template"
        return render_template(
            'index.html',
            display_error = column_error
            )
         

    # Save the cleaned DataFrame to a new Excel file
    df.to_excel("./output/cleaned_example.xlsx", index=False)
    # df.to_excel(f"./output/{file.filename}", index=False)

    print('\nClean up completed successfully! ✨')
    # Return a link to download the processed data
    # btn = f'<a href="/download">Download processed data</a>'
    success_message = "Clean up completed successfully! ✨"
    return render_template(
                            'index.html',
                            success_message = success_message
                            )
   

@app.route('/download')
def download_file():
    return send_file('./output/cleaned_example.xlsx', as_attachment=True)
    # return send_file(f"./output/{file.filename}", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

