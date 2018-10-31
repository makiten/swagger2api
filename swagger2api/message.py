from colorama import (Fore, Style)


class Output:

    @staticmethod
    def console_message(msg, output_type, color):
        output = (Style.BRIGHT
                  + color
                  + '{0}: '.format(output_type.title())
                  + Style.RESET_ALL
                  + msg)

        return output

    @staticmethod
    def error(msg):
        return Output.console_message(msg, 'error', Fore.RED)

    @staticmethod
    def info(msg):
        return Output.console_message(msg, 'info', Fore.BLUE)

    @staticmethod
    def success(msg):
        output = (Style.BRIGHT
                  + Fore.GREEN
                  + msg
                  + Style.RESET_ALL)

        return output

    @staticmethod
    def warning(msg):
        return Output.console_message(msg, 'warning', Fore.YELLOW)
