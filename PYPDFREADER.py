# Importando as bibliotecas necessárias
#import PdfReader
from pypdf import PdfReader
from gtts import gTTS

# Função para converter texto em voz usando gTTS
def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang='pt')
    tts.save(output_path)

# Função para ler um arquivo PDF e converter para texto
def streamAudioMP3(pdf, audio_file)
	pdf_path = pdf
	output_audio_path = audio_file
	r = PdfReader(pdf_path)
	text = ''
	for page in r.pages:
		text += page.extract_text() + "\n"
	text_to_speech(text, output_audio_path)
