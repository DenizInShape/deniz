from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

from django.shortcuts import render

def SLOT(request, identifiant, score):
    template = loader.get_template('SLOT.html')
    context = {
      'identifiant': identifiant,
      'score': score,
    }  # Ensure to pass an empty context if not needed
    return HttpResponse(template.render(context, request))


def roulette(request, identifiant, score):
    template = loader.get_template('roulette.html')
    context = {
        'identifiant': identifiant,
        'score': score,
    }
    return HttpResponse(template.render(context, request))

def cards(request, identifiant, score):
    template = loader.get_template('cards.html')
    context = {
      'identifiant': identifiant,
      'score': score,
    }  
    return HttpResponse(template.render(context, request))

def account(request):
    template = loader.get_template('account.html')
    context = {}  # Ensure to pass an empty context if not needed
    return HttpResponse(template.render(context, request))


def salon(request, identifiant, score):
    template = loader.get_template('salon.html')
    context = {
        'identifiant': identifiant,
        'score': score,
    }
    return HttpResponse(template.render(context, request))





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password



from django.shortcuts import render
from django.shortcuts import redirect



@csrf_exempt
def authenticate_user(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        mot_de_passe = request.POST.get('motDePasse')

        try:
            member = Member.objects.get(identifiant=identifiant)
            if check_password(mot_de_passe, member.password):
                # Use Django's render function to render the salon page
                return render(request, 'salon.html', {'identifiant': member.identifiant, 'score': member.score})
        except Member.DoesNotExist:
            pass

    # Return a JsonResponse indicating authentication failure
    return JsonResponse({ 'error_message': 'Identifiants incorrects. Veuillez reessayer.'})







from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Member

def register_user(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        mot_de_passe = request.POST.get('motDePasse')

        # Hash the password before storing it in the database
        hashed_password = make_password(mot_de_passe)

        # Create a new Member instance and save it to the database with a default score of 1000
        Member.objects.create(identifiant=identifiant, password=hashed_password, score=1000)

        # Return a JsonResponse indicating successful registration
        return JsonResponse({'success': True})

    # Return a JsonResponse indicating registration failure
    return JsonResponse({'success': False})


