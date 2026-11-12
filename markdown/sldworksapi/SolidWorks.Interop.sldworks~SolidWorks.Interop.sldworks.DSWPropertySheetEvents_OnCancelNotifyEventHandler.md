---
title: "DSWPropertySheetEvents_OnCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSWPropertySheetEvents_OnCancelNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnCancelNotifyEventHandler.html"
---

# DSWPropertySheetEvents_OnCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Cancel button on the property sheet is clicked. Your add-in can perform clean-up activities in this event.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSWPropertySheetEvents_OnCancelNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSWPropertySheetEvents_OnCancelNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSWPropertySheetEvents_OnCancelNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSWPropertySheetEvents_OnCancelNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [OnCancelNotify Event (SWPropertySheet)](ms-its:sldworksapivb6.chm::/SldWorks~SWPropertySheet~OnCancelNotify_EV.html).

## Remarks

If developing a C++ application, use [swPropertySheetOnCancelNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
