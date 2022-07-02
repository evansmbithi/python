# Python venv

- Fetch the project from GitHub.

- Place yourself in new_env/ and create a virtual environment inside.
<pre>
    $ python -m venv env
</pre>

- Activate the virtual environment and place yourself in the <em>src</em> directory
<pre>
    $ source env/bin/activate
    $ cd src
</pre>

- Restore the project by using <em style="color:skyblue">pip install -r requirements.txt</em>. It will look for requirements.txt and fetch and install the packages listed for that file.

- Install a specific package pip install python-dateutil===2.7.4

- Run your app.
