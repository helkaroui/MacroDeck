from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionList(_message.Message):
    __slots__ = ("count", "actions")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    count: int
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    def __init__(self, count: _Optional[int] = ..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("title", "code")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    title: str
    code: str
    def __init__(self, title: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ActionStatus(_message.Message):
    __slots__ = ("id", "current_step", "total_steps")
    ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STEPS_FIELD_NUMBER: _ClassVar[int]
    id: int
    current_step: int
    total_steps: int
    def __init__(self, id: _Optional[int] = ..., current_step: _Optional[int] = ..., total_steps: _Optional[int] = ...) -> None: ...
