def make_url(language, text):
    """
    Makes URL to make API response to Text-to-Speech.
    :param language:
    :param text:
    :return:
    """
    base_url = "http://api.voicerss.org/?key=b6a6c17f866b483dbfb8d6eef76b05ae&hl={0}&src={1}&f=48khz_16bit_stereo"
    url = base_url.format(language, text)
    return url
