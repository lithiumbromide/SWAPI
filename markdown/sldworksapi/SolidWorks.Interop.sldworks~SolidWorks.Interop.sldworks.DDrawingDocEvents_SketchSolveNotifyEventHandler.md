---
title: "DDrawingDocEvents_SketchSolveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_SketchSolveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SketchSolveNotifyEventHandler.html"
---

# DDrawingDocEvents_SketchSolveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. This event returns the name of the sketch feature being updated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_SketchSolveNotifyEventHandler( _
   ByVal featName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_SketchSolveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_SketchSolveNotifyEventHandler(
   System.string featName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_SketchSolveNotifyEventHandler(
   System.String^ featName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `featName`: Name of sketch feature being updated

## VBA Syntax

See [SketchSolveNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~SketchSolveNotify_EV.html).

## Remarks

Pressing the Ctrl+Q keys rebuilds drawing sketches ([IView::GetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSketch.html) or [IView::IGetSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSketch.html)), which causes this event to fire.

If developing a C++ application, use [swDrawingSketchSolveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
