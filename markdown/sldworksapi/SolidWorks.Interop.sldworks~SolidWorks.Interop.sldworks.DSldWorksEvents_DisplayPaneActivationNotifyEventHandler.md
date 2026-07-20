---
title: "DSldWorksEvents_DisplayPaneActivationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_DisplayPaneActivationNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DisplayPaneActivationNotifyEventHandler.html"
---

# DSldWorksEvents_DisplayPaneActivationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Display Pane is activated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_DisplayPaneActivationNotifyEventHandler( _
   ByVal ActivePaneIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_DisplayPaneActivationNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_DisplayPaneActivationNotifyEventHandler(
   System.int ActivePaneIndex
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_DisplayPaneActivationNotifyEventHandler(
   System.int ActivePaneIndex
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `ActivePaneIndex`: Display Pane as defined by

[swDisplayPaneIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayPaneIndex_e.html)

## VBA Syntax

See

[DisplayPaneActivationNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~DisplayPaneActivationNotify_EV.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## Remarks

If developing a C++ application, use[swAppDisplayPaneActivationNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html)to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
