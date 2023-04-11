from .forms import SubscriptionForm 

def subscribe_form(request):
    form = SubscriptionForm()
    return {'subscribe_form':form}
  