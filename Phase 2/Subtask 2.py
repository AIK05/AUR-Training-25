from time import time
from rich.console import Console
console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data
    
    @property
    def style(self):
        return '' # BaseMsg-specific
        
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self._data # BaseMsg-specific
    
    def __len__(self):
        return len(str(self))
    
    def __eq__(self, other):
        if not isinstance(other, BaseMsg):
            return False
        return str(self) == str(other)
    
    def __add__(self, other):
        cls = type(self)
        new_data = str(self) + (other._data if isinstance(other, BaseMsg) else str(other))
        return cls(new_data)


class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = int(time())

    @property
    def style(self) -> str: #type:ignore
        return "default on yellow" 

    def __str__(self) -> str:
        return f"[{self._timestamp}] {self._data}"


class WarnMsg(LogMsg):
    @property
    def style(self) -> str:
        return "white on red"  

    def __str__(self) -> str:
        return f"[!WARN][{self._timestamp}] {self._data}"


if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)