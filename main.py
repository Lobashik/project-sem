"""file for rrender my html page"""
import json
import requests

from jinja2 import Template


# token = dotenv_values('.env').get('vk')
VK_PATH = 'vk.json'
GITHUB_PATH = 'github.json'
TEMPLATE_PATH = 'templates/template.html'
INDEX_TEMPLATE_PATH = 'index.html'


# def vkon(tokenn):
#     """docstring"""
#     user = 'https://api.vk.com/method/users.get'
#     req = requests.get(user, params={'access_token': tokenn,
#                                      'user_ids': 'lobashik', 'v': 5.131},
#                        timeout=10)
#     with open('vk1.json', 'w', encoding='utf-8') as file6:
#         json.dump(req.json(), file6, ensure_ascii=False, indent=4)


def github():
    """docstring"""
    user = requests.get("https://api.github.com/users/Lobashik", timeout=10)
    with open('github.json', 'w', encoding='utf-8') as file4:
        json.dump(user.json(), file4, ensure_ascii=False, indent=4)


# vkon(token)
github()


def get_vk_info(vk_path):
    """get information from vk"""
    with open(vk_path, encoding='utf-8') as file1:
        data = json.load(file1)
    return data


def get_github_info(github_path):
    """get information from github"""
    with open(github_path, encoding='utf-8') as file2:
        data = json.load(file2)
    return data


def get_template(template_path):
    """get template"""
    with open(template_path, encoding='utf-8') as file3:
        return Template(file3.read())


if __name__ == '__main__':
    vk_info = get_vk_info(VK_PATH)
    github_info = get_github_info(GITHUB_PATH)
    template = get_template(TEMPLATE_PATH)
    render_page = template.render(
        name=github_info['name'],
        github_profile='https://github.com/' + github_info['login'],
        vk_id='https://vk.com/id' + str(vk_info['response'][0]['id']),
    )

    with open(INDEX_TEMPLATE_PATH, 'w', encoding='utf-8') as file:
        file.write(render_page)
