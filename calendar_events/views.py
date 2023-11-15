from django.shortcuts import render
from .models import UserDate
from openai import OpenAI
import os

def calendar_view(request):
    return render(request, 'calendar.html')

def fetch_facts(request):
    selected_date = request.POST.get('selected_date')
    # Call OpenAI API to get facts about the selected_date using GPT-3
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "user", "content": f"Tell me interesting facts about {selected_date}, \
                give them to me in a bulleted list."}
        ]
    )
    # Assuming 'response' is a ChatCompletion object
    facts = response.choices[0].message.content.replace("-", "").splitlines()
    return render(request, 'facts.html', {'facts': facts})