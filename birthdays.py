import requests, json, datetime
from bs4 import BeautifulSoup as bs
from bokeh.plotting import figure, show, output_file

def wiki_search(name):
    try:
        url = 'https://en.wikipedia.org/wiki/' + name.title()
        r = requests.get(url)
        soup = bs(r.content,'lxml')
        bday = soup.find('span',{'class':'bday'})
        return bday.get_text()
    except AttributeError:
        print(name, '- could not find name')
        return False

def save():
    with open('bdays.json','w') as f:
        json.dump(names,f)
    print('List saved!')

def hlp():
    with open('readme.txt') as f:
        redovi = f.readlines()
    print()
    for i in range(3,11):
        print(redovi[i])

def listaj():
    names_sorted = dict(sorted(names.items()))
    print('List of persons:')
    for person in names_sorted:
        print(person)

def search(ime):
    if ime in names:
        vreme = datetime.datetime.strptime(names[ime],'%Y-%m-%d').strftime('%B %d, %Y')
        print(ime,'was born on',vreme)
    else:
        print('Person is not in the list.')

def add():
    ime = input('Enter name: ')
    rodj = wiki_search(ime)
    if not rodj:
        while True:
            qn = input('Add birthday manually? (y/n) ')
            if qn == 'y':
                datum = input('Enter birthday (year-month-day): ')
                try:
                    rodj = datetime.datetime.strptime(datum,'%Y-%m-%d').date()
                except ValueError:
                    print('Wrong entry')
                    continue
                if rodj > datetime.date.today():
                    print('Date entered is in the future')
                    continue
                break
            elif qn == 'n':
                return False
    names[ime.title()] = rodj
    print('Successfully added!')

def download():
    names.clear()
    with open('bdays.txt', encoding="utf8") as f:
        print('Downloading...')
        for row in f:
            n = row.strip()
            if row == '': continue
            result = wiki_search(n)
            if not result: continue
            names[n.title()] = result
        print('Loaded!')

def months():
    nr_months = {}
    for ime in names:
        month = int(names[ime].split('-')[1])
        if month not in nr_months:
            nr_months[month] = 1
        else:
            nr_months[month] += 1
    nr_months_sort = dict(sorted(nr_months.items()))
    for mnt in nr_months_sort:
        dt = datetime.datetime.strptime(str(mnt),'%m')
        print(dt.strftime('%b'),nr_months_sort[mnt])
    while True:
        g = input('Print a graphical display? (y/n) ')
        if g == 'y':
            graph(nr_months_sort)
            break
        elif g == 'n': break

def graph(mnth):
    output_file("bdays.html")
    x_months = [datetime.datetime.strptime(str(i+1),'%m').strftime('%B') for i in range(12)]
    x = [x_months[element-1] for element in mnth]
    y = list(mnth.values())
    p = figure(x_range=x_months, plot_width=600, plot_height=350)
    p.xaxis.major_label_orientation = 0.785
    p.xaxis.axis_label = "Months"
    p.xgrid.grid_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.yaxis.axis_label = "Birthdays per month"
    p.vbar(x=x, top=y, width=0.5, color="#69ded8")
    show(p)

def opt_prnt():
    opt_list = ['(d)ownload','(l)ist','(s)earch','(a)dd','(c)ount','(sav)e','(h)elp','(e)xit']
    n = int(len(opt_list)/2)
    print('\nOptions: ',end='')
    for i in range(2):
        if i > 0:
            print(9*' ',end='')
        for j in range(n):
            print("{:10}".format(opt_list[j+n*i]),end=' ')
        print()


names = {}
with open('bdays.json') as f:
    names = json.load(f)

while True:
    opt_prnt()
    q = input().strip()
    if q in ['l','list']: listaj()
    elif q in ['a','add']: add()
    elif q in ['sav','save']: save()
    elif q in ['e','exit']: break
    elif q in ['d','download']: download()
    elif q in ['c','count']: months()
    elif q in ['h','help']: hlp()
    elif q in ['s','search']:
        name = input('Enter name: ').title()
        search(name)
    else: print('Unknown command.')
