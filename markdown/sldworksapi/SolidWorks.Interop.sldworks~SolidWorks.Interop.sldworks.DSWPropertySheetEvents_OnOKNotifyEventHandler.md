---
title: "DSWPropertySheetEvents_OnOKNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSWPropertySheetEvents_OnOKNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnOKNotifyEventHandler.html"
---

# DSWPropertySheetEvents_OnOKNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the OK button on the property sheet is clicked.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSWPropertySheetEvents_OnOKNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSWPropertySheetEvents_OnOKNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSWPropertySheetEvents_OnOKNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSWPropertySheetEvents_OnOKNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [OnOKNotify Event (SWPropertySheet)](ms-its:sldworksapivb6.chm::/SldWorks~SWPropertySheet~OnOKNotify_EV.html).

## Remarks

Your add-in can perform clean-up activities in this event. Typically, this event calls [ISWPropertySheet::GetControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet~GetControl.html) to retrieve data from your ActiveX control.

If developing a C++ application, use [swPropertySheetOnOKNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
