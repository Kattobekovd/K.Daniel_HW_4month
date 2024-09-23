from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class SalaryLevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = request.POST.get('experience')
            if experience == 'junior' :
                request.level = 'Ваша зарплата 500$'
            elif experience == 'middle' :
                request.level = 'Ваша зарплата 1000$'
            elif experience == 'senior' :
                request.level = 'Ваша зарплата 3000$'
            else:
                return HttpResponseBadRequest('Извините без опыта работы не принимаем')

        elif request.path  == '/register/' and request.method == 'GET':
            setattr(request, 'level', 'Ваш уровень програмирование не определен' )