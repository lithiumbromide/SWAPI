---
title: "_ILispFunctionEvents_ExecuteFunctionNotifyEventHandler Delegate"
project: ""
interface: "_ILispFunctionEvents_ExecuteFunctionNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._ILispFunctionEvents_ExecuteFunctionNotifyEventHandler.html"
---

# _ILispFunctionEvents_ExecuteFunctionNotifyEventHandler Delegate

Notifies an application when a LISP function is executed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _ILispFunctionEvents_ExecuteFunctionNotifyEventHandler()
```

### C#

```csharp
public delegate void _ILispFunctionEvents_ExecuteFunctionNotifyEventHandler()
```

### JScript

```
public delegate _ILispFunctionEvents_ExecuteFunctionNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _ILispFunctionEvents_ExecuteFunctionNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _ILispFunctionEvents_ExecuteFunctionNotifyEventHandler();
```

## Remarks

If developing a C++ application, use [dsLispFunction_ExecuteFunctionNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsLispFunctionEvent_id_e.html) to register for this notification. You must add one event handler for each [ILispFunction](Interop.dsAutomation~Interop.dsAutomation.ILispFunction.html) to distinguish LISP functions.

## See Also

[_ILispFunctionEvents_ExecuteFunctionNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._ILispFunctionEvents_ExecuteFunctionNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
