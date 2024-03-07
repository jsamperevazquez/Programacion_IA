from concrete_decorator import HTMLDecorator
from concrete_component import PlainText

if __name__ == '__main__':
    plaintext = PlainText('Hola Mundo')
    print(f"Texto sin decorar: {plaintext.render()}")

    html_text = HTMLDecorator(plaintext)
    print(f"Texto deconrado en HTML: {html_text.render()}")
