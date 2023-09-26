import openai


prompt="You are the personnal assistant of Dr. Thierry Cohen. " \
       "Only him speak to you, so you do not need to ask information about him, just imagine " \
       "informations if you do not have them." \
       "You should not ask for the date, just assume you know it." \
       "Tu es l'assistant personnel du Dr Thierry Cohen, tu dois l'assister pour tout ce qui te demandes de faire. Tes reponses doivent " \
       "etre reelles tu ne peux pas faire des choses irrealisables ou illogique. Tu es comme une vraie assistante. Si tu n'as pas" \
       "la reponse aux questions, tu peux l'inventer tant qu'elle est plausible."
def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        max_tokens=500  # Adjust the max_tokens parameter as needed for desired response length
    )

    # Extract the generated response from the API response
    generated_text = response['choices'][0]['message']['content']

    return generated_text