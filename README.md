# Relógio Digital em Python com Tkinter

This is a Python program that creates a digital clock using the Tkinter and the datetime libraries to get the current time and date.
>*Este é um programa em Python que cria um relógio digital usando as biblioteca Tkinter e datetime para obter a hora e a data atual.*

## Pré-requisitos

It's necessary to have Python installed on your system. You also need to install the Pyglet library to use the custom font. You can install it using the following command:
>*É necessário Python instalado em seu sistema. Você também precisa instalar a biblioteca Pyglet para usar a fonte personalizada. Você pode instalá-la usando o seguinte comando:*

```bash
pip install pyglet
```

## Configuração da Fonte

The program uses a custom font called "Skyfont.otf" to display the clock numbers. Make sure the font is available on your system. You can add the font to Pyglet using the following command:
>*O programa usa uma fonte personalizada chamada "Skyfont.otf" para exibir os números do relógio. Certifique-se de que a fonte está disponível em seu sistema. Você pode adicionar a fonte ao Pyglet usando o seguinte comando:*

```python
import pyglet
pyglet.font.add_file(r"C:\Caminho\Para\Skyfont.otf")
```

Replace `"C:\Path\To\Skyfont.otf"` with the actual path to the font file on your system.
>*Substitua `"C:\Caminho\Para\Skyfont.otf"` pelo caminho real para o arquivo de fonte em seu sistema.*

The font was downloaded from https://www.1001fonts.com/skyfont-font.html. You can download the font and install it on your system or use any other font of your choice.
>*A fonte foi baixada no site https://www.1001fonts.com/skyfont-font.html. Você pode baixar a fonte e instalá-la em seu sistema ou usar qualquer outra fonte de sua escolha.*

## Cores

The program defines some colors to customize the appearance of the clock. You can adjust these colors by changing the values of the `color1`, `color2`, `color3`, `color4`, `color5` and `color6` variables according to your preferences.
>*O programa define algumas cores para personalizar a aparência do relógio. Você pode ajustar essas cores alterando os valores das variáveis `cor1`, `cor2`, `cor3`, `cor4`, `cor5` e `cor6` de acordo com suas preferências.*

## Interface Gráfica

The program creates a GUI window using the Tkinter library. The window is not resizable and displays the current time in the "HH:MM:SS" format with a large font in the specified color.
>*O programa cria uma janela de interface gráfica usando a biblioteca Tkinter. A janela não é redimensionável e exibe a hora atual no formato "HH:MM:SS" com uma fonte grande na cor especificada.*

The date in the "Weekday, Day/Month/Year" format is also displayed below the clock.
>*Além disso, a data completa no formato "Dia da semana, Dia/Mês/Ano" é exibida abaixo do relógio.*

## Atualização do Relógio

The `clock()` function creates the window and the labels to display the time and date. It also sets the window background color and the font size and color.
>*A função `relogio()` atualiza continuamente o relógio a cada 180 milissegundos. Ela obtém a hora e a data atual usando a biblioteca datetime e atualiza os rótulos (`Label`) na janela com os valores atualizados.*

## Executando o Programa

To run the program, simply execute the Python file `relogio.py`. The clock window will be displayed and will continue to update the time and date in real time until you close it.
>*Para executar o programa, basta executar o arquivo Python `relogio.py`. A janela do relógio será exibida e continuará atualizando a hora e a data em tempo real até que você a feche.*

```bash
python relogio.py
```

## Conclusão

This is an example of a digital clock in Python using Tkinter. You can further customize the program with additional features like alarms or a different time format as needed.
>*Este é um exemplo de um relógio digital em Python usando Tkinter. Você pode personalizar ainda mais o programa com recursos adicionais como alarmes ou um formato de hora diferente, conforme necessário.*