# Importando as bibliotecas necessárias
#import PyPDF2
from pypdf import PdfReader
from gtts import gTTS

# Função para ler um arquivo PDF e converter para texto
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        text = ''
        for page in range(num_pages):
            text += reader.getPage(page).extractText()
        return text

# Função para converter texto em voz usando gTTS
def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang='pt')
    tts.save(output_path)

# Exemplo de uso
def streamAudioMP3(pdf, audio_file)
	pdf_path = 'ibm_python.pdf'
	output_audio_path = 'ibm_pyton.mp3'
	r = PdfReader(pdf_path)
	text = ''
	for page in r.pages:
		text += page.extract_text() + "\n"
	text_to_speech(texto, output_audio_path)