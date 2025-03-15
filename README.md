A seguir, um exemplo de projeto completo com um script para percorrer todas as imagens em um diretório e redimensioná-las, além de arquivos de configuração para o VS Code e um arquivo Markdown com instruções para criar o repositório no GitHub.

---

## Estrutura do Projeto

```
image-resizer/
├── .vscode/
│   ├── settings.json
│   └── tasks.json
├── resize_images.py
├── requirements.txt
└── README.md
```

---

## 1. Script Python: `resize_images.py`

Este script percorre todas as imagens em um diretório (ou processa um arquivo único), redimensionando-as para 80% da largura de uma página A4 a 300 DPI. As imagens redimensionadas são salvas na pasta `resized_images`.

```python
import os
import sys
from PIL import Image

def resize_image(input_path, output_path, new_width):
    # Abre a imagem
    with Image.open(input_path) as img:
        orig_width, orig_height = img.size
        # Calcula a nova altura mantendo a proporção
        new_height = int((new_width / orig_width) * orig_height)
        # Redimensiona a imagem com alta qualidade
        img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)
        # Salva a imagem redimensionada
        img_resized.save(output_path)
        print(f"Salvo: {output_path} com tamanho {new_width}x{new_height}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python resize_images.py <caminho_para_imagem_ou_diretorio>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Configurações de DPI e cálculo da largura A4
    dpi = 300
    a4_width_mm = 210
    a4_width_inch = a4_width_mm / 25.4
    a4_width_px = int(a4_width_inch * dpi)
    # Calcula 80% da largura A4
    target_width = int(a4_width_px * 0.8)
    print(f"Largura alvo (80% de uma página A4 a 300 DPI): {target_width} pixels")
    
    # Cria o diretório de saída, se não existir
    output_dir = "resized_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Processa todos os arquivos se input_path for um diretório
    if os.path.isdir(input_path):
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            if os.path.isfile(file_path):
                try:
                    output_file = os.path.join(output_dir, file_name)
                    resize_image(file_path, output_file, target_width)
                except Exception as e:
                    print(f"Erro ao processar {file_path}: {e}")
    elif os.path.isfile(input_path):
        base_name = os.path.basename(input_path)
        output_file = os.path.join(output_dir, base_name)
        try:
            resize_image(input_path, output_file, target_width)
        except Exception as e:
            print(f"Erro ao processar {input_path}: {e}")
    else:
        print("Caminho inválido")

if __name__ == "__main__":
    main()
```

---

## 2. Arquivo de Dependências: `requirements.txt`

Liste as dependências necessárias (neste caso, apenas o Pillow).

```
Pillow
```

---

## 3. Configuração para o VS Code

Crie uma pasta chamada `.vscode` com os seguintes arquivos para facilitar a edição e execução do projeto.

### `.vscode/settings.json`

```json
{
    "python.pythonPath": "python",
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

### `.vscode/tasks.json`

Este exemplo cria uma task para executar o script diretamente pelo VS Code.

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Redimensionar Imagens",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}/resize_images.py",
                "${workspaceFolder}/caminho/para/imagens"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": []
        }
    ]
}
```

> **Observação:** Ajuste o argumento `"${workspaceFolder}/caminho/para/imagens"` para o caminho desejado ou modifique a task conforme sua necessidade.

---

## 4. Instruções para Criar o Repositório no GitHub: `README.md`

Este arquivo contém um guia com instruções para criar o repositório e publicar o projeto no GitHub.

```markdown
# Projeto Image Resizer

Este projeto contém um script Python que redimensiona imagens para 80% da largura de uma página A4 a 300 DPI, percorrendo todas as imagens em um diretório e salvando as imagens redimensionadas na pasta `resized_images`.

## Estrutura do Projeto

```
image-resizer/
├── .vscode/
│   ├── settings.json
│   └── tasks.json
├── resize_images.py
├── requirements.txt
└── README.md
```

## Configuração do Ambiente

1. **Clone o repositório ou baixe os arquivos.**

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Abra o projeto no VS Code:**
   ```bash
   code .
   ```

## Uso do Script

Para redimensionar uma imagem ou todas as imagens de um diretório, execute:
```bash
python resize_images.py <caminho_para_imagem_ou_diretorio>
```
As imagens redimensionadas serão salvas na pasta `resized_images`.

## Criando um Repositório no GitHub

Siga os passos abaixo para criar e publicar seu projeto no GitHub:

1. **Crie um novo repositório no GitHub:**
   - Acesse [GitHub](https://github.com) e faça login.
   - Clique em **New repository**.
   - Preencha o nome do repositório e outras configurações desejadas.
   - Clique em **Create repository**.

2. **Inicialize o Git no projeto:**
   No terminal, navegue até a pasta do projeto e execute:
   ```bash
   git init
   ```

3. **Adicione todos os arquivos e faça o primeiro commit:**
   ```bash
   git add .
   git commit -m "Primeiro commit - Projeto Image Resizer"
   ```

4. **Adicione o repositório remoto:**
   Substitua `SEU_USUARIO` e `NOME_DO_REPOSITORIO` pelo seu usuário e nome do repositório:
   ```bash
   git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   ```

5. **Envie o commit para o GitHub:**
   ```bash
   git push -u origin master
   ```

Agora, seu projeto estará publicado no GitHub e você poderá continuar editando o código no VS Code, utilizando as tasks e configurações definidas.

---

## Configuração do Git e GitHub

1. **Inicialize o repositório Git:**
```bash
git init
git add .
git commit -m "Initial commit: Configuração inicial do projeto"
```

2. **Crie um novo repositório no GitHub:**
- Acesse https://github.com/new
- Preencha o nome do repositório (ex: "image-resizer")
- Não inicialize com README ou .gitignore

3. **Conecte ao repositório remoto:**
```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

4. **Envie as alterações:**
```bash
git push -u origin main
```

## Gerenciamento do Ambiente Virtual

Para ativar o ambiente virtual e instalar dependências:
```bash
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```
```

---

Com este projeto, você tem uma solução completa para redimensionar imagens de forma padronizada e um ambiente configurado para edição no VS Code, além de orientações para publicar o repositório no GitHub. Basta clonar ou criar os arquivos conforme a estrutura acima, instalar as dependências e ajustar os caminhos conforme necessário.
