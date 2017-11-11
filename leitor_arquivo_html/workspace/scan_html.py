from bs4 import BeautifulSoup as beautiful
from io import BytesIO
import pycurl
import pprint

def content_file():
	file = input('digite o nome do arquivo: ')
	conteudo = ''

	try:
		t_file = open(file)
		list_texto = t_file.readlines()
		conteudo = ''

		for line in list_texto:
			conteudo += line+'\n'
		return conteudo

	except FileNotFoundError as e:
		return '\nErro: Arquivo não encontrado!\n'



def set_file(text):
	file = input('digite o nome do arquivo: ')
	m_file = open(file, 'w')
	m_file.write(text)
	m_file.close()
	print('\nSuccess!!\n')

def str_html(scan):
	text = scan.getvalue()
	soup = beautiful(text, 'html.parser')
	text = soup.prettify()
	return text

def scan_url(url):
	scan = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, m_url)
	c.setopt(c.WRITEDATA, scan)
	c.perform()
	c.close()
	return scan

def main():
	op = 1

	while op != 0:
		menu = (
				'-     menu     -\n'+
				'1   -  criar novo arquivo\n'+
				'2   -  ler conteudo do arquivo\n'+
				'0   -  sair\n'
			)
		print(menu)
		op = int(input('digite a opção: '))

		if op == 0:
			print('\nprograma encerrado.\n')

		elif op == 1:
			m_url = input('Digite a url: ')
			m_scan = scan_url(m_url)
			m_text = str_html(m_scan)
			set_file(m_text)

		elif op == 2:
			file = content_file()
			print(file)

if __name__ == '__main__':
	main()