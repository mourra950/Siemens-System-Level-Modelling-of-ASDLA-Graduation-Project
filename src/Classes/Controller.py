class Controller:

    def on_generate_files_clicked(self):
        generator = self.file_read_json()
        self.generate_model()
        self.generate_train()
