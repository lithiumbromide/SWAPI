---
title: "DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the active view changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveViewChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ActiveViewChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyActiveViewChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
