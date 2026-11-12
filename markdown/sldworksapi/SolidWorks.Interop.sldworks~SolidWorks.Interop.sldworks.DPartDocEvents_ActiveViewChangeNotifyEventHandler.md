---
title: "DPartDocEvents_ActiveViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ActiveViewChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveViewChangeNotifyEventHandler.html"
---

# DPartDocEvents_ActiveViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the active view changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ActiveViewChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ActiveViewChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ActiveViewChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ActiveViewChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveViewChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ActiveViewChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartActiveViewChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
