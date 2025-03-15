import os
import sys
from PIL import Image

def resize_image(input_path, output_path, new_width):
    # Abre a imagem
    with Image.open(input_path) as img:
        # Obtém as dimensões originais
        orig_width, orig_height = img.size
        # Calcula a nova altura para manter a proporção
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
    
    if os.path.isdir(input_path):
        # Processa todas as imagens no diretório
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            if os.path.isfile(file_path):
                try:
                    output_file = os.path.join(output_dir, file_name)
                    resize_image(file_path, output_file, target_width)
                except Exception as e:
                    print(f"Erro ao processar {file_path}: {e}")
    elif os.path.isfile(input_path):
        # Processa um único arquivo de imagem
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

