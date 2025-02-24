from botcity.core import DesktopBot
from botcity.maestro import *
import time

BotMaestroSDK.RAISE_NOT_CONNECTED = False

class MyBot:
    def __init__(self):
        self.bot = DesktopBot() #atributo que gerencia as ações do bot
        self.maestro = None
        self.execution = None

    def connect_maestro(self):
        try:
            self.maestro = BotMaestroSDK.from_sys_args()
            self.execution = self.maestro.get_execution()
            print(f"Task ID: {self.execution.task_id}")
            print(f"Task Parameters: {self.execution.parameters}")
        except Exception as e:
            print(f"Erro ao conectar com BotMaestro: {e}")
            self.maestro = None

    def alerts(self):
        print('Iniciando a Automação...')
        if self.maestro and self.execution:
            self.maestro.finish_task(
                task_id=self.execution.task_id,
                status=AutomationTaskFinishStatus.SUCCESS,
                message="Task Finished OK.",
                total_items=0,
                processed_items=0,
                failed_items=0
            )

    def open_site(self):
        url = 'http://www.botcity.dev'
        self.bot.browse(url)

    def run(self):
        #chama os métodos, coloque sua lógica aqui
        self.connect_maestro()
        self.alerts()
        self.open_site()

def main():
    
    #inicializa a instancia do bot
    try:
        deskbot = MyBot()
        deskbot.run()
    except Exception as ex:
        print(f"Erro: {ex}")
        deskbot.bot.save_screenshot("error_screenshot.png")
    finally:
        print('Finalizando a automação...')
        time.sleep(5)

if __name__ == '__main__':
    main()
