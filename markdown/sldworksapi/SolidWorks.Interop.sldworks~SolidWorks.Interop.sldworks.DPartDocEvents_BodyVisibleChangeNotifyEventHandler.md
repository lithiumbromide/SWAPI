---
title: "DPartDocEvents_BodyVisibleChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_BodyVisibleChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_BodyVisibleChangeNotifyEventHandler.html"
---

# DPartDocEvents_BodyVisibleChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired whenever the visible state of a body within this part changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_BodyVisibleChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_BodyVisibleChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_BodyVisibleChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_BodyVisibleChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [BodyVisibleChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~BodyVisibleChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartBodyVisibleChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
