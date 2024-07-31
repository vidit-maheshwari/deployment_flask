
def geminiApp(prompt):
    """
    Install the Google AI Python SDK

    $ pip install google-generativeai

    See the getting started guide for more information:
    https://ai.google.dev/gemini-api/docs/get-started/python
    """

    import google.generativeai as genai
    from GeminiHist import data

    genai.configure(api_key="AIzaSyAqYlms8gWsC85piyMToBC5NpIhPP8G7u4")


    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=data
    )


    userInput = prompt
    response = chat_session.send_message(userInput)

    return response.text