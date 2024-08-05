from MakeUp.models import Main_category,Category



def menu_links(request):
    c=Main_category.objects.all()
    return {'links':c}

