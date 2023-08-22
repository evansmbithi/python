from flask import Flask, request, render_template, send_file
import pandas as pd

app = Flask(__name__)
# regex = '[^a-zA-Z0-9]'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    global file
    global df
    global labels
    global file_name

    if 'upload' in request.form: #'upload' button name
        file = request.files['file']
        file_name = file.filename
        try:
            df = pd.read_excel(file)
        except:
            file_error = 'Please upload an excel file'
            return render_template(
                    'index.html',
                    display_error = file_error
                    )
        
        # Extract labels (header row)
        labels = df.columns.tolist()
        # print(labels)
        
        return render_template('columns.html', elements=labels, file_name=file_name)
    
    elif 'submit' in request.form: #'submit' button name
        selected_options = request.form.getlist('checkboxes')
        replacer = request.form['replacement']
        
        try:
            replacee = request.form['replacement_choice']
        except:
            error_msg = "Please choose replacement option"
            return render_template(
                'columns.html',
                elements=labels,
                file_name=file_name
                )
            
        if selected_options == []:
            error_msg = "Please select a column to proceed"
            return render_template(
                'columns.html',
                elements=labels,
                file_name=file_name                
                )

        #clean up
        def clean_data(option,rep,*chars,col=df):
            for char in chars:
                # col['STEP_ID'] = col['STEP_ID'].str.replace(char,'_') # Error: Can only use .str accessor with string values!    
                try:
                    col[option] = col[option].str.replace(char,rep)   
                except:
                    # print('Blank cell') 
                    continue        
            return col
        
        # Remove special characters from selected Columns
        for column in selected_options:            
            alert_msg = "Blank cells will be shown as 'nan'" 
            try:
                [clean_data(column,replacer,replacee,'__') for _ in range(4)] # run four times
            except KeyError:
                column_error = f"'{column}' is not available as a column in this file."
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
                                success_message = success_message,
                                )
    elif 'back' in request.form:
        return render_template('index.html')

@app.route('/download')
def download_file():
    return send_file('./output/cleaned_example.xlsx', as_attachment=True)
    # return send_file(f"./output/{file.filename}", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

##### REF #######
# Error: Can only use .str accessor with string values!
# https://towardsdatascience.com/5-methods-to-check-for-nan-values-in-in-python-3f21ddd17eed

# https://bobbyhadz.com/blog/can-only-use-str-accessor-with-string-values-in-python

# col[option] = col[option].apply(str).str.replace(char,rep) # Convert all values to string # has a NaN issue                
# col[option] = col[option].apply(
#                             lambda x: x.replace(char,rep)
#                             if isinstance(x, str)
#                             else x
#                         )
# It only calls the replace() method if the supplied value is a string.
# Otherwise, the value is returned as is.