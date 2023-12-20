class ConsoleStyleLang:
    def __init__(self):
        self.styles = {
            'font_color': None,
            'background_color': None,
            'background_image': None,
            'object_position': None,
            'bold': False,
            'underline': False,
            'italic': False
        }

    def set_font_color(self, color):
        # Validate color format (RGB tuple)
        if not isinstance(color, tuple) or len(color) != 3:
            raise ValueError("Invalid color format. Please use an RGB tuple.")
        self.styles['font_color'] = color
        return self

    def set_background_color(self, color):
        # Validate color format (RGB tuple)
        if not isinstance(color, tuple) or len(color) != 3:
            raise ValueError("Invalid color format. Please use an RGB tuple.")
        self.styles['background_color'] = color
        return self

    def set_background_image(self, image_path):
        # Validate image path
        # Add more validation based on your requirements
        self.styles['background_image'] = image_path
        return self

    # Add more style-setting methods based on your needs

    def remove_bold(self):
        self.styles['bold'] = False
        return self

    def remove_underline(self):
        self.styles['underline'] = False
        return self

    # Add other remove_style methods as needed

    def reset_styles(self):
        self.styles = {
            'font_color': None,
            'background_color': None,
            'background_image': None,
            'object_position': None,
            'bold': False,
            'underline': False,
            'italic': False
        }
        return self

    def apply_style(self, text):
        style_str = ""
        if self.styles['bold']:
            style_str += "\033[1m"
        if self.styles['underline']:
            style_str += "\033[4m"
        if self.styles['italic']:
            style_str += "\033[3m"
        if self.styles['font_color']:
            style_str += f"\033[38;2;{self.styles['font_color'][0]};{self.styles['font_color'][1]};{self.styles['font_color'][2]}m"
        if self.styles['background_color']:
            style_str += f"\033[48;2;{self.styles['background_color'][0]};{self.styles['background_color'][1]};{self.styles['background_color'][2]}m"
        if self.styles['background_image']:
            style_str += f"\033]1337;File=name={self.styles['background_image']};height=100%;width=100%;inline=1\a"
        if self.styles['object_position']:
            style_str += f"\033[{self.styles['object_position'][0]};{self.styles['object_position'][1]}H"
        return f"{style_str}{text}\033[0m"
