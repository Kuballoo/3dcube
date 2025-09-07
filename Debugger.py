import time

class Debugger(object):
    def __init__(self, name, enabled, log_interval=0):
        """
        Initialize a debugger instance.
        :param name: Name of the module/class for prefixing logs.
        :param enabled: Whether logging is active.
        """
        self.name = name
        self.enabled = enabled
        self._log_interval = log_interval
        self._last_log_time = time.time()

    def show_debug_data(self, *args, **kwargs):
        """
        Display given data in a readable format.
        Accepts any number of positional (*args) or keyword (**kwargs) arguments.
        """
        if not self.enabled:
            return
        
        now = time.time()
        if now - self._last_log_time >= self._log_interval:
            args_str = ' | '.join(str(a) for a in args)
            kwargs_str = ' | '.join(f'{k}={v}' for k, v in kwargs.items())
            all_data = ' | '.join(filter(None, [args_str, kwargs_str]))

            print(f'[{self.name}] {all_data}')
            self._last_log_time = now