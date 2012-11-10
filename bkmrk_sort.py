import sys
import copy
import re
import json

SEPARATOR = "->"


def loadConfig(configFile):
    config = ""
    for line in open(configFile):
        if line[0:2] != "//":
            config += line
    print(config)
    config = json.loads(config)
    for key, value in config.items():
        config[key] = value.split(SEPARATOR)
    return config


def traverse(bookmrk, paths=[]):
    for i in bookmrk:
        if i['type'] == 'folder':
            paths.append(i['name'])
            for j in traverse(i['children'], paths):
                yield j
            del paths[-1]
        elif i['type'] == 'url':
            yield paths, i


def move(bookmrks, name, src, dest):
    def getId(lst, name):
        for i in lst:
            if i['name'] == name:
                return lst.index(i)
        raise NameError('Folder is not exist')

    def get(lst, path):
        while len(path):
            lst = lst[getId(lst, path[0])]['children']
            del path[0]
        return lst

    # Must use a deepcopy here -- we don't want to change "configure"
    source = get(bookmrks, copy.deepcopy(src))
    dest = get(bookmrks, copy.deepcopy(dest))
    bookmrk = source[getId(source, name)]

    dest.append(bookmrk)
    del source[getId(source, name)]


def keywordCheck(configure, name):
    for keyword in configure.keys():
        if re.search(keyword, name):
            return configure[keyword]
    return False


bookmrk = json.loads(open("Bookmarks").read())
configure = loadConfig("keywords.conf")

# If we traverse & modify the bookmark at the same time,
# we will get in many troubles. Use a copy to solve it.
bookmrkNew = copy.deepcopy(bookmrk)


for path, web in traverse(bookmrk['roots']['bookmark_bar']['children']):

    # Must use a deepcopy here, if we forget to do that,
    # we will change path -> get(path) -> traverse(paths).
    path = copy.deepcopy(path)

    name = web['name']
    dest = keywordCheck(configure, name)

    if dest:
        try:
            move(bookmrkNew['roots']['bookmark_bar']['children'],
                 name, path, dest)
        except (TypeError, NameError):
            print('Warning: "%s" is not exist, skipped!' % dest,
                    file=sys.stderr)

bookmrkNew['checksum'] = ("Edited by chrome bookmrk sorter. "
                        "Chrome, please fix your checksum!")
print(json.dumps(bookmrkNew))
