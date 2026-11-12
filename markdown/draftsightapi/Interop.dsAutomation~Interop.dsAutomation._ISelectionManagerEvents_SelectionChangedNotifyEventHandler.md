---
title: "_ISelectionManagerEvents_SelectionChangedNotifyEventHandler Delegate"
project: ""
interface: "_ISelectionManagerEvents_SelectionChangedNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionChangedNotifyEventHandler.html"
---

# _ISelectionManagerEvents_SelectionChangedNotifyEventHandler Delegate

Notifies an application when an entity is selected.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _ISelectionManagerEvents_SelectionChangedNotifyEventHandler()
```

### C#

```csharp
public delegate void _ISelectionManagerEvents_SelectionChangedNotifyEventHandler()
```

### JScript

```
public delegate _ISelectionManagerEvents_SelectionChangedNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _ISelectionManagerEvents_SelectionChangedNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _ISelectionManagerEvents_SelectionChangedNotifyEventHandler();
```

## Examples

##### COM native C++

**Header file**

//Register the events for the ISelectionManager class

BEGIN_SINK_MAP(CDsAddinSelectionManager)

SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__ISelectionManagerEvents, dsSelectionManager_SelectionChangedNotify_id, OnSelectionChangedNotify)

END_SINK_MAP()

//Declare the callbacks for ISelectionManager class
void __stdcall OnSelectionChangedNotify();

**Source file**

void

__stdcall CDsAddinSelectionManager::OnSelectionChangedNotify()

{

// TODO: Add your code here

}

## Remarks

If developing a C++ application, use [dsSelectionManager_SelectionChangedNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsSelectionManagerEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_ISelectionManagerEvents_SelectionChangedNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionChangedNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ISelectionManager Event SelectionPreNotify](Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionPreNotifyEventHandler.html)

## Availability

DraftSight V1R1
