import json
import re
import sys
import traceback


def traverse(list, paths=[]):
    '''Traverse web pages in list. Web pages and it's path will generate.

    This function will:
    1. Generate each web pages as a dictionary.
    2. Generate path for each pages.
    3. Folder will not generate
    4. '/;' is a pathname separator, just like '/' in UNIX.'''
    for i in list:
        if i['type'] == 'folder':
            # Go into a folder, write the path to the paths.
            paths.append('/;' + i['name'])
            for j in traverse(i['children'], paths):
                yield j
            # Go out a folder, remove the path to the paths.
            del paths[-1]
        elif i['type'] == 'url':
            # Found a URL, we got a completed path in the paths.
            # commit the paths to the lists, them empty the paths.
            paths.append('/;' + i['name'])
            yield i, ''.join(paths)
            del paths[-1]


def will_move(web_page_name):
    '''Check name of a web page by regular expression.

    return value is a tuple, first item in tuple means matched or not, 
    second one is a path, means if match, the web pages will move into it. '''
    config_file = open("keywords.conf").read()
    keywords = json.loads(config_file)
    for i in keywords.keys():
        if re.search(i, web_page_name):
            return (True, keywords[i])
    return (False, 0)


def move(dic, source, dest):
    '''Move a web page from source to dest,'''
    def convert_name(list):
        if list[0] == '/;':
            list[0] = 'roots'
        for index, value in enumerate(list):
            if value == '/;':
                list[index] = 'children'
        return list

    def replace_all_name_to_index(dic, list):
        for index, value in enumerate(list):
            if list[index] == 'children':
                try:
                    tmp1 = list[0:index + 1]
                    name = list[index + 1]
                except:
                    continue

                list_index = list_to_index(tmp1)
                list[index + 1] = get_id(eval(list_index), name)
        return list

    def list_to_index(list):
        dic = 'dic'
        for i in list:
            try:
                dic += '["' + i + '"]'
            except:
                dic += '[' + str(i) + ']'
        return dic

    def string_to_lst(string):
        tmp = []
        tmp_paths = ''
        for i, j in enumerate(string):
            if j == '/' and string[i + 1] == ';':
                if tmp_paths != '':
                    tmp.append(tmp_paths)
                    tmp_paths = ''
                tmp.append('/;')
            else:
                if j != ';' or string[i - 1] == ';':
                    tmp_paths += j
        if tmp_paths != '':
            tmp.append(tmp_paths)
        if tmp[1] != 'bookmark_bar':
            tmp.insert(1, 'bookmark_bar')
            tmp.insert(2, '/;')
        return tmp

    def get_id(lst, name):
        for i in lst:
            if i['name'] == name:
                return lst.index(i)

    import copy
    source = string_to_lst(source)
    source = convert_name(source)
    source = replace_all_name_to_index(dic, source)

    cmd = list_to_index(source)
    tmp3 = copy.deepcopy(eval(cmd))
    exec('del ' + cmd, locals())

    dest = string_to_lst(dest)
    dest = convert_name(dest)
    dest = replace_all_name_to_index(dic, dest)

    cmd = list_to_index(dest)
    exec(cmd + '.append(tmp3)', locals())

    return dic


a = json.load(open("Bookmarks"))

pages = []
for i, j in traverse(a['roots']['bookmark_bar']['children']):
    pages.append(j)

for i in pages:
    if will_move(i)[0]:
        move(a, i, will_move(i)[1])

b = json.dumps(a)
print(b)
