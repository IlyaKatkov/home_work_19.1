from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostname = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """
           Специальный класс, который отвечает за
           обработку входящих запросов от клиентов
       """
    @staticmethod
    def __get_html_content():
        with open('index.html', encoding='utf-8') as f:
            return f.read()

    def do_GET(self):
        page = self.__get_html_content()

        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page, "utf-8")) # Тело ответа


if __name__ == '__main__':
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    web_server = HTTPServer((hostname, server_port), MyServer)
    print('Server started at address http://%s:%s' % (hostname, server_port))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        web_server.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass
    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    web_server.server_close()
    print('Server stopped')