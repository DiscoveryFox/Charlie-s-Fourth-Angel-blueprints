import sys
import requests

scripts = ['slowloris_blueprint.py']

stylesheets  = ['slowloris.css']

javascripts = []

htmls = ['slowloris.html']

binarys = []

raw_repo_url = "https://raw.githubusercontent.com/DiscoveryFox/Charlie-s-Fourth-Angel-blueprints/main"

def install(raw_repo_url:str):
    for script in scripts:
        ## print('starting')
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
        print(script)
        with open(script, 'w') as f:
            f.write(script_content)

    for stylesheet in stylesheets:
        stylesheet_url = raw_repo_url + '/' + stylesheet

        stylesheet_content = requests.get(stylesheet_url).text

        with open(stylesheet, 'w') as f:
            f.write(stylesheet_content)
    
    for javascript in javascripts:
        javascript_url = raw_repo_url + '/' + javascript

        javascript_content = requests.get(javascript_url).text

        with open(javascript, 'w') as f:
            f.write(javascript_content)
    
    


if __name__ == '__main__':
    install(raw_repo_url)


# install('https://raw.githubusercontent.com/DiscoveryFox/Charlie-s-Fourth-Angel-blueprints/main', locations=locations)

