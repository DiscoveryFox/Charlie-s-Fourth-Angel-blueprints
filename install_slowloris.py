import requests

scripts = ['slowloris_blueprint.py']

stylesheets  = ['slowloris.css']

javascripts = []

htmls = ['slowloris.html']

locations = {
    'scripts': 'C:\\Users\\Flinn\\OneDrive\\Desktop\\.vscode\\Charlie-s-Fourth-Angel-blueprints\\',
    }
def install(raw_repo_url:str, locations:dict):
    for script in scripts:
        print('starting')
        # download all files from github from the given url as base and
        # save them to the given directory

        # file url's
        script_url = raw_repo_url + '/' + script
        ##stylesheet_url = raw_repo_url + '/' + stylesheet
        ##javascript_url = raw_repo_url + '/' + javascript
        ##html_url = raw_repo_url + '/' + html

        # download files

        script_content = requests.get(script_url).text
        
        # write the content in a file
        with open(f"{locations['scripts']}{script}", 'w') as f:
            f.write(script_content)


install('https://raw.githubusercontent.com/DiscoveryFox/Charlie-s-Fourth-Angel-blueprints/main', locations=locations)

