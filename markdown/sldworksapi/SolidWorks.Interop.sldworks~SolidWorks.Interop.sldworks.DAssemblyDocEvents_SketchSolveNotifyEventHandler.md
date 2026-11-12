---
title: "DAssemblyDocEvents_SketchSolveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_SketchSolveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SketchSolveNotifyEventHandler.html"
---

# DAssemblyDocEvents_SketchSolveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_SketchSolveNotifyEventHandler( _
   ByVal featName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_SketchSolveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_SketchSolveNotifyEventHandler(
   System.string featName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_SketchSolveNotifyEventHandler(
   System.String^ featName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `featName`: Name of the sketch feature being updated

## VBA Syntax

See [SketchSolveNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~SketchSolveNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblySketchSolveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This event returns the name of the sketch feature being updated.

Pressing the Ctrl+Q keys in an assembly-level sketch does not always result in a sketch being solved. A sketch is only solved if it needs to be updated. If the sketch is not solved, then this event is not fired.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
