from django.shortcuts import render

LOREM_IPSUM = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

def index_page(request):
    
    posts = [
        {
            'autor':'Neymar',
            'data':'12/12/2022',
            'Conteudo':LOREM_IPSUM
        },
        
        {
            'autor':'Ciclano',
            'data':'12/12/2022',
            'Conteudo':LOREM_IPSUM
            
        },
        
        {
            'autor':'Deltrano',
            'data':'12/12/2022',
            'Conteudo':LOREM_IPSUM
            
        }
    ]
    
    return render(request,'index.html',{'posts':posts})
    
    