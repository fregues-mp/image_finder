## Image Finder

**Image Finder** é uma ferramenta de automação em Python que permite ao usuário detectar imagens específicas na tela, criadas previamente, e interagir automaticamente com elas. Este projeto facilita a criação e detecção de padrões visuais para automação de processos repetitivos que envolvem elementos gráficos.

### Funcionalidades
- **Detecção de Imagens Personalizadas**: Permite que o usuário configure imagens específicas que o programa identificará na tela.
- **Interação Automática**: Ao detectar a imagem, realiza cliques automáticos na posição exata.
- **Logs**: Cada ação é registrada em um arquivo de log com data e hora.
- **Interrupção**: Pressione "ESC" a qualquer momento para interromper a execução.

### Requisitos
- Python 3.6+
- `pyautogui`
- `cv2` (OpenCV)
- `keyboard`
- `numpy`

### Executando

1. Clone o repositório:
    ```bash
    git clone https://github.com/fregues-mp/image_finder.git
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install pyautogui opencv-python keyboard numpy
    ```

3. Execute o macro com o seguinte comando:
    ```bash
    python main.py
    ```

### Como Usar
1. Crie as imagens que deseja detectar na tela e adicione-as ao diretório do projeto. Ajuste o nome das imagens conforme necessário no código.

   Exemplo:
   ```python
   if not base.PN(r'data\test.png', name='test', value=c):
       c += 1
   ```

2. Adicione variações da mesma imagem. O programa buscará a próxima imagem somente se a anterior não for encontrada.

   Exemplo:
   ```python
   if not base.PN(r'data\test.png', r'data\test2.png', r'data\test3.png', name='test', value=c):
       c += 1
   ```

3. A função **EI()** permite parar o loop automaticamente ao detectar uma imagem específica chamada "reset" ou outra de sua escolha. Quando a imagem for detectada, o loop será interrompido.

    Exemplo:
    ```python
    if base.EI('reset'):
        c = 0
        break  
    ```

### Clique em Bordas e Cantos

Agora, você pode especificar onde deseja que o clique ocorra, utilizando funções de clique específicas que podem ser aplicadas em diferentes partes da imagem detectada, como as bordas ou os cantos.

Exemplo de uso:

```python
# Clicar no centro
base.EI_Click_PN(r'data/test.png', name='test', move_func=base.center, value=c)

# Clicar na borda esquerda
base.EI_Click_PN(r'data/test.png', name='test', move_func=base.botton_left, value=c)

# Clicar a esquerda
base.EI_Click_PN(r'data/test.png', name='test', move_func=base.left, value=c)
```

Funções de movimento disponíveis:

- `center(pos, size)` - centro
- `bottom(pos, size)` - borda inferior
- `top(pos, size)` - borda superior
- `left(pos, size)` - borda esquerda
- `right(pos, size)` - borda direita
- `top_left(pos, size)` - canto superior esquerdo
- `top_right(pos, size)` - canto superior direito
- `bottom_left(pos, size)` - canto inferior esquerdo
- `bottom_right(pos, size)` - canto inferior direito

### Formatos de Imagem Suportados

O OpenCV suporta uma variedade de formatos de imagem que podem ser usados com a função de detecção. Alguns dos formatos suportados incluem:

- **PNG** (`.png`)
- **JPEG** (`.jpg`, `.jpeg`)
- **BMP** (`.bmp`)
- **TIFF** (`.tiff`, `.tif`)
- **GIF** (`.gif`) - apenas a primeira imagem em uma sequência de GIFs animados.
- **PPM** (`.ppm`)
- **PGM** (`.pgm`)
- **PBM** (`.pbm`)
- **WebP** (`.webp`) - disponível em versões mais recentes do OpenCV.

### Contribuições

![marca_small](https://github.com/user-attachments/assets/3a29afa3-0b39-43ee-9760-cca03d978e62)

-------

Sinta-se à vontade para contribuir! Abra um *issue* ou envie um *pull request*.

### Licença

Este projeto está licenciado sob a [MIT License](https://github.com/fregues-mp/image_finder/blob/main/LICENSE).
