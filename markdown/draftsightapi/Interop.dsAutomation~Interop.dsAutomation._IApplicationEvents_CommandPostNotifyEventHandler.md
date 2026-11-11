---
title: "_IApplicationEvents_CommandPostNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_CommandPostNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPostNotifyEventHandler.html"
---

# _IApplicationEvents_CommandPostNotifyEventHandler Delegate

Post-notifies an application when a command is executed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_CommandPostNotifyEventHandler( _
   ByVal CommandName As System.String, _
   ByVal Document As Document _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_CommandPostNotifyEventHandler(
   System.string CommandName,
   Document Document
)
```

### JScript

```
public delegate _IApplicationEvents_CommandPostNotifyEventHandler(
   CommandName : System.String,
   Document : Document
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_CommandPostNotifyEventHandler(
   System.string* CommandName,
   Document* Document
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_CommandPostNotifyEventHandler(
   System.String^ CommandName,
   Document^ Document
)
```

### Parameters

- `CommandName`: Name of command that executed
- `Document`: [Document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html) in which command executed (see **Remarks**)

## Examples

[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)

## Remarks

If developing a C++ application, then use [dsApplication_CommandPostNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification. See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

Document is 0 if all documents are closed after command execution (i.e., CLOSE).

## See Also

[_IApplicationEvents_CommandPostNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPostNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event CommandCancelNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandCancelNotifyEventHandler.html)
[IApplication Event CommandPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPreNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
