from django.http import JsonResponse
import jwt
import requests
import openai

def login(request):
    code = request.GET.get('code')
    openid = exchange_code_for_openid(code)

    token = jwt.encode({'openid': openid}, 'secret', algorithm='HS256')
    return JsonResponse({'token': token.decode()})

def send_message(request):
    token = request.headers.get('Authorization')
    if not verify_token(token):
        return JsonResponse({'error': 'Invalid token'}, status=401)

    message = request.data['message']
    response = call_external_api(message)
    return JsonResponse({'response': response})

def verify_token(token):
    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

def exchange_code_for_openid(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': '你的小程序appid',
        'secret': '你的小程序secret',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    r = requests.get(url, params=params)
    return r.json()['openid']

def call_external_api(message):
    openai.api_key = "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" # 这里填写你的OpenAI API Key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=100
    )
    return response.choices[0].text.strip()
