class Error(Exception): ...
class ErrorReply(Exception): ...
class TransactionError(Error): ...
class NotConnectedError(Error): ...
class TimeoutError(Error): ...
class ConnectionLostError(NotConnectedError): ...
class NoAvailableConnectionsInPoolError(NotConnectedError): ...
class ScriptKilledError(Error): ...
class NoRunningScriptError(Error): ...
