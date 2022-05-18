import os
import sys
import requests

scripts = ['slowloris_blueprint.py']

stylesheets  = ['slowloris.css']

javascripts = []

htmls = ['slowloris.html']

binarys = []

raw_repo_url = "https://raw.githubusercontent.com/DiscoveryFox/Charlie-s-Fourth-Angel-blueprints/main"

def move(filename, filetype):
    # move the file(filename) to a given directory
    match filetype:
        case 'script':
            os.rename(filename, 'blueprints/' + filename)
        case 'stylesheet':
            os.rename(filename, 'static/blueprints/css/' + filename)
        case 'javascript':
            os.rename(filename, 'static/blueprints/js/' + filename)
        case 'html':
            os.rename(filename, 'templates/services/' + filename)
        case 'binary':
            os.rename(filename, 'blueprints/' + filename)
        case _:
            raise Exception('Unknown filetype')


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
        with open(script, 'w') as f:
            f.write(script_content)
        move(script, 'script')

    for stylesheet in stylesheets:
        stylesheet_url = raw_repo_url + '/' + stylesheet

        stylesheet_content = requests.get(stylesheet_url).text

        with open(stylesheet, 'w') as f:
            f.write(stylesheet_content)
        move(stylesheet, 'stylesheet')
    for javascript in javascripts:
        javascript_url = raw_repo_url + '/' + javascript

        javascript_content = requests.get(javascript_url).text

        with open(javascript, 'w') as f:
            f.write(javascript_content)
        move(javascript, 'javascript')
    for html in htmls:
        html_url = raw_repo_url + '/' + html

        html_content = requests.get(html_url).text

        with open(html, 'w') as f:
            f.write(html_content)
        move(html, 'html')
    for binary in binarys:
        binary_url = raw_repo_url + '/' + binary

        binary_content = requests.get(binary_url).content

        with open(binary, 'wb') as f:
            f.write(binary_content)
        move(binary, 'binary')




if __name__ == '__main__':
    install(raw_repo_url)


# install('https://raw.githubusercontent.com/DiscoveryFox/Charlie-s-Fourth-Angel-blueprints/main', locations=locations)

