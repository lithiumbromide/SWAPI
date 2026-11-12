---
title: "DPartDocEvents_SketchSolveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_SketchSolveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SketchSolveNotifyEventHandler.html"
---

# DPartDocEvents_SketchSolveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. This event returns the name of the sketch feature being updated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_SketchSolveNotifyEventHandler( _
   ByVal featName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_SketchSolveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_SketchSolveNotifyEventHandler(
   System.string featName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_SketchSolveNotifyEventHandler(
   System.String^ featName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `featName`: Name of sketch feature being updated

## VBA Syntax

See [SketchSolveNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~SketchSolveNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartSketchSolveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
