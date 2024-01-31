from sqlproject.models import Products

def getValue():
    
    return Products.objects.filter(id=305)


