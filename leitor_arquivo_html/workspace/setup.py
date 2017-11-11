from bs4 import BeautifulSoup as beautiful
from io import BytesIO
import pycurl
import pprint

def get_file():
	file = input('digite o nome do arquivo: ')

	try:
		t_file = open(file)

	except FileNotFoundError as e:
		t_file = open(file, 'w')
		t_file = open(file)

	return t_file

def set_file(text):
	file = input('digite o nome do arquivo: ')
	m_file = open(file, 'w')
	m_file.write(text)
	m_file.close()
	print('Success!! ; ) ')

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
			print('programa encerrado.')

		elif op == 1:
			m_url = input('Digite a url: ')
			m_scan = scan_url(m_url)
			m_text = str_html(m_scan)
			set_file(m_text)

		elif op == 2:
			file = get_file()
			list_texto = file.readlines()
			conteudo = ''

			for line in list_texto:
				conteudo += line+'\n'

			print(conteudo)

if __name__ == '__main__':
	main()