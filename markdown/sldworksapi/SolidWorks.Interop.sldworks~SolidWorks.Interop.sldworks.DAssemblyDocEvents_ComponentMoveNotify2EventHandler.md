---
title: "DAssemblyDocEvents_ComponentMoveNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentMoveNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentMoveNotify2EventHandler.html"
---

# DAssemblyDocEvents_ComponentMoveNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notification that is sent when a user releases the mouse button indicating that the components have been moved to the desired destination.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentMoveNotify2EventHandler( _
   ByRef Components As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentMoveNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentMoveNotify2EventHandler(
   ref System.object Components
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentMoveNotify2EventHandler(
   System.Object^% Components
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Components`: Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s

## VBA Syntax

See [ComponentMoveNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentMoveNotify2_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyComponentMoveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
