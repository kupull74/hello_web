from bs4 import BeautifulSoup

# from file
path = 'datas/sample03.html'

with open(path) as fp:						# shared github
    soup = BeautifulSoup(fp, features='lxml')
    title_data = soup.find('h1')									# tag로 검색
    print(type(title_data), title_data, title_data.string)
    title_data = soup.find_all(id='h1_id_name')					# id로 검색
    print(title_data, title_data[0].get_text())
    title_data = soup.find_all('p', class_='public_class_name')	# tag와 class로 검색
    print(title_data, title_data[0].attrs)
    # [<p class="public_class_name" id="p01_id_name">웹페이지에서 ... 하는 것</p>]
    # {'class': ['public_class_name'], 'id': 'p01_id_name'}
    title_data = soup.find_all('p', attrs = {'align': 'center'})		# 속성:속성값으로 검색
    print(title_data, title_data[0].string)
    title_data = soup.find_all('a', href=True)					# 속성 존재 여부 검색
    print(title_data, title_data[0].string)


with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup), soup.attrs, soup.getText())
    # <class 'bs4.BeautifulSoup'> {} The Dormouse's story ...

    elements = soup.findAll(name='a')
    print(type(elements), len(list(elements)))
    # <class 'bs4.element.ResultSet'> 3
    for element in elements:
        print(type(element), element.attrs, element['href'])
        print(element.getText(), len(element.getText()))    # need trip()
        # <class 'bs4.element.Tag'> {'class': ['sister']...} http://example01.com/elsie Elsie 14
        # ...
        
    body_tag = soup.body
    bodychildren = body_tag.children
    print(type(bodychildren), len(list(bodychildren)))
    # <class 'list_iterator'> 7
    
    from bs4.element import NavigableString
    for child in body_tag.children:
        if isinstance(child, NavigableString):
            print(type(child), repr(child.string), len(child.string))
        else:
            print(type(child), child.attrs, child.getText(), len(child.getText()))
            # <class 'bs4.element.NavigableString'> '\n' 1
            # <class 'bs4.element.Tag'> {'class': ['title']} 
            # The Dormouse's story
            # ...
            # <class 'bs4.element.NavigableString'>