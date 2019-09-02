from google.cloud import translate_v3beta1 as translate


def translate_to_uk(text):
    """
    Translates text from English to Ukrainian.
    :param text:
    :return:
    """
    client = translate.TranslationServiceClient()
    project_id = "artful-memento-250518"
    location = 'global'

    parent = client.location_path(project_id, location)
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type='text/plain',  # mime types: text/plain, text/html
        source_language_code='en-US',
        target_language_code='uk')
    answer = ""
    for translation in response.translations:
        for text in translation.translated_text:
            answer = answer + text
    return answer
