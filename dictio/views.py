from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from .models import EnglishToDarija



def home(request):
    return render(request, '/home/nabil/myquiz/dictio/templates/base.html')


@require_GET
def autocomplete(request):
    term = request.GET.get('term', '')
    results = []
    if term:
        translations = EnglishToDarija.objects.filter(english_word__istartswith=term).values_list('english_word', flat=True).distinct()[:10]
        results = list(translations)
    return JsonResponse(results, safe=False)


@csrf_exempt
def search(request):
    search_term = request.GET.get('term', '')
    results = []
    if search_term:
        translations = EnglishToDarija.objects.filter(english_word__iexact=search_term)
        for t in translations:
            examples = t.example_set.all().values_list('example_text', flat=True)
            results.append({
                'value': t.darija_translation, 
                'label': f"{t.darija_translation}",
                'partofspeech':f"({t.part_of_speech})",
                'plurality': f"{t.plurality}",
                'examples': examples,
                'image_path': t.image.url if t.image else None,
                'audio_path': t.audio.url if t.audio else None,
            })

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'results': results})
    else:
        return render(request, 'search_results.html', {'search_term': search_term, 'results': results})
