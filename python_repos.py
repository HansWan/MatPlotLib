import requests
import pygal
#import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as LS


# Run API and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response to a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore reposit info
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description'] != None:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
            }
    else:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': 'None',
            'xlink': repo_dict['html_url'],
            }
        
    plot_dicts.append(plot_dict)

# Visualize
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config_truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

#i = 1
#for d in plot_dicts:
    #print(str(i))
    #print(d['label'])
    #i += 1

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
