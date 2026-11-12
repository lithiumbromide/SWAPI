---
title: "DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a component is changed to hidden or shown.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ComponentVisibleChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentVisibleChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyComponentVisibleChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.1
