# Automatically generated by pb2py
import protobuf as p


class ApplySettings(p.MessageType):
    MESSAGE_WIRE_TYPE = 25
    FIELDS = {
        1: ('language', p.UnicodeType, 0),
        2: ('label', p.UnicodeType, 0),
        3: ('use_passphrase', p.BoolType, 0),
        4: ('homescreen', p.BytesType, 0),
        5: ('passphrase_source', p.UVarintType, 0),
        6: ('auto_lock_delay_ms', p.UVarintType, 0),
    }

    def __init__(
        self,
        language: str = None,
        label: str = None,
        use_passphrase: bool = None,
        homescreen: bytes = None,
        passphrase_source: int = None,
        auto_lock_delay_ms: int = None
    ) -> None:
        self.language = language
        self.label = label
        self.use_passphrase = use_passphrase
        self.homescreen = homescreen
        self.passphrase_source = passphrase_source
        self.auto_lock_delay_ms = auto_lock_delay_ms
