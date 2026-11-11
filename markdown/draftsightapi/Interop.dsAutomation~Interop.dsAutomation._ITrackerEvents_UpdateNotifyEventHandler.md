---
title: "_ITrackerEvents_UpdateNotifyEventHandler Delegate"
project: ""
interface: "_ITrackerEvents_UpdateNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._ITrackerEvents_UpdateNotifyEventHandler.html"
---

# _ITrackerEvents_UpdateNotifyEventHandler Delegate

Notifies the application when the cursor position has changed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _ITrackerEvents_UpdateNotifyEventHandler( _
   ByVal CursorPosition As MathPoint _
)
```

### C#

```csharp
public delegate void _ITrackerEvents_UpdateNotifyEventHandler(
   MathPoint CursorPosition
)
```

### JScript

```
public delegate _ITrackerEvents_UpdateNotifyEventHandler(
   CursorPosition : MathPoint
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _ITrackerEvents_UpdateNotifyEventHandler(
   MathPoint* CursorPosition
)
```

### C++/CLI

```cpp
public delegate void _ITrackerEvents_UpdateNotifyEventHandler(
   MathPoint^ CursorPosition
)
```

### Parameters

- `CursorPosition`: [Current cursor position](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

## Examples

[Create Tracker (C#)](Create_Tracker_Example_CSharp.htm)
[Create Tracker (VB.NET)](Create_Tracker_Example_VBNET.htm)
[Create Tracker (VBA)](Create_Tracker_Example_VBA.htm)

## Remarks

This event allows you to update the tracker's temporary entities that are dependent on the current cursor position.

If developing a C++ application, use [dsTracker_UpdateNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsTrackerEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_ITrackerEvents_UpdateNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._ITrackerEvents_UpdateNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R4.0
