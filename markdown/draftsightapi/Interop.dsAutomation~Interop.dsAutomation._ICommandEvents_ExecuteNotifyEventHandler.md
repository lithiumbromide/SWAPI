---
title: "_ICommandEvents_ExecuteNotifyEventHandler Delegate"
project: ""
interface: "_ICommandEvents_ExecuteNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._ICommandEvents_ExecuteNotifyEventHandler.html"
---

# _ICommandEvents_ExecuteNotifyEventHandler Delegate

Notifies an application when a command is executed or [IApplication::RunCommand](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html) is called.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _ICommandEvents_ExecuteNotifyEventHandler()
```

### C#

```csharp
public delegate void _ICommandEvents_ExecuteNotifyEventHandler()
```

### JScript

```
public delegate _ICommandEvents_ExecuteNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _ICommandEvents_ExecuteNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _ICommandEvents_ExecuteNotifyEventHandler();
```

## Examples

See the following code snippets:

- COM native C++
- [C++](#CPP)

##### COM native C++

**Header file**

//Register the events for the ICommand class
BEGIN_SINK_MAP(CDsAddinCommand)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__ICommandEvents, dsCommand_ExecuteNotify_id, OnExecuteNotify)
END_SINK_MAP()

//Declare the callbacks for the ICommand class
void __stdcall OnExecuteNotify();

**Source file**

void __stdcall CDsAddinCommand::OnExecuteNotify()
{
// TODO: Add your code here
}

##### C++

**Header file**

class

DSADDINSAMPLE_EXPORT myApplication :

public dsApplicationEvents_c, dsCommandEvents_c

DeclareCommandExecuteNotifyHook

bool ExecuteNotify(void);

**Source file**

RegisterCommandExecuteNotifyHook( pCmd );

ImplementCommandExecuteNotifyHook(myApplication)

bool

myApplication::ExecuteNotify(void

)

{

//TODO: Add your code here

return true

;

}

## Remarks

If developing a C++ application, use [dsCommand_ExecuteNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsCommandEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_ICommandEvents_ExecuteNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._ICommandEvents_ExecuteNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R1
