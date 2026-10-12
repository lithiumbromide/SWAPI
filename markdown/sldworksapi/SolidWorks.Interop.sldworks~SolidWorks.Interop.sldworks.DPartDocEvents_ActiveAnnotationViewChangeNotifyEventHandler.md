---
title: "DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler.html"
---

# DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the user changes the annotation view.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveAnnotationViewChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ActiveAnnotationViewChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartActiveAnnotationViewChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
