from django.shortcuts import render

# Create your views here.
my_data = {'name': u'Oleksandr',
        'second_name': u'Shcherbyna',
        'email' : u'sanya071186@gmail.com',
        'jabber' : u'pock@jabber.ua',
        'skype' : u'sanya071186',
        'bio' : u'My name is Oleksandr. I`m 29 years old. I`m married and have a doughter',
        'facebook': u'https://www.facebook.com/profile.php?id=100003368151652',
        'vk' : u'https://vk.com/id69128840'}
def main(request):
    return render(request, 'base.html', {'my_data' : my_data})
