# Conversor de Imagens Científicas

Processamento automático de imagens para pesquisa acadêmica com preservação de metadados.

▶ **Uso Básico:**
1. Colete imagens em `imagens_recebidas/`
2. Execute:
```bash
python src/resize_images.py
```
3. Resultados em `imagens_convertidas/` com:
   - Imagem redimensionada (85% qualidade)
   - Metadados técnicos em YAML

⚙ **Pré-requisitos:**  
Python 3.8+ e bibliotecas listadas em `requirements.txt`

📁 **Estrutura Principal:**
```
imagens_recebidas/    # Imagens originais
imagens_convertidas/  # Resultados processados
config/metadata.yaml  # Modelo de metadados
src/                  # Código-fonte
```

✅ **Versionamento Automático:**  
Todas as alterações são rastreadas via Git - não modifique arquivos manualmente.
