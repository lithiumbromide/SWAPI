---
title: "DSWPropertySheetEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSWPropertySheetEvents_DestroyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_DestroyNotifyEventHandler.html"
---

# DSWPropertySheetEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the property sheet is in the process of being destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSWPropertySheetEvents_DestroyNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSWPropertySheetEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSWPropertySheetEvents_DestroyNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSWPropertySheetEvents_DestroyNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DestroyNotify Event (SWPropertySheet)](ms-its:sldworksapivb6.chm::/SldWorks~SWPropertySheet~DestroyNotify_EV.html).

## Remarks

When this event is fired, the window associated with the destroyed property sheet is still alive, but any API pages have already been removed.

If developing a C++ application, use [swPropertySheetDestroyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
