import yaml
from datetime import datetime
from PIL import Image

class MetadataHandler:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self.metadata = {
            'projeto': self.config['projeto'],
            'parametros': self.config['parametros'],
            'contato': self.config['contato'],
            'processamento': {
                'data': datetime.now().isoformat(),
                'versao_software': self.config['projeto']['versao']
            }
        }

    def _load_config(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def add_image_metadata(self, image_path, processed_image):
        with Image.open(image_path) as img:
            self.metadata['imagem'] = {
                'original': {
                    'caminho': image_path,
                    'dimensoes': img.size,
                    'formato': img.format
                },
                'processada': {
                    'dimensoes': processed_image.size,
                    'formato': self.config['parametros']['formato']
                }
            }

    def _convert_to_exif(self, metadata):
        """Converte metadados para formato EXIF usando piexif"""
        import piexif
        
        # Cria um dicionário EXIF vazio
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}
        
        # Adiciona metadados personalizados na tag UserComment
        user_comment = yaml.dump(metadata, default_flow_style=False, allow_unicode=True)
        exif_dict["Exif"][piexif.ExifIFD.UserComment] = user_comment.encode('utf-8')
        
        # Converte para bytes EXIF
        return piexif.dump(exif_dict)

    def generate_report(self, output_path):
        # Gera arquivo YAML separado
        report_path = output_path.replace('.', '_metadata.')
        with open(report_path + '.yaml', 'w') as file:
            yaml.dump(self.metadata, file, default_flow_style=False)
        
        # Insere metadados na imagem
        exif_data = self._convert_to_exif(self.metadata)
        with Image.open(output_path) as img:
            img.save(output_path, exif=exif_data)
