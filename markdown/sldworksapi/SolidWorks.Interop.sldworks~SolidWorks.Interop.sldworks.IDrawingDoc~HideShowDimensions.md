---
title: "HideShowDimensions Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "HideShowDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.html"
---

# HideShowDimensions Method (IDrawingDoc)

Sets whether to display suppressed dimensions as dimmed and hide them.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideShowDimensions()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.HideShowDimensions()
```

### C#

```csharp
void HideShowDimensions()
```

### C++/CLI

```cpp
void HideShowDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::HideShowDimensions](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~HideShowDimensions.html).

## Remarks

When SOLIDWORKS displays a suppressed dimension as dimmed, users can select it to turn off suppression.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AttachDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AttachDimensions.html)
[IDrawingDoc::DragModelDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension.html)
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.html)
[IDrawingDoc::InsertModelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions.html)
[IDrawingDoc::InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.html)
[IDrawingDoc::InsertBaseDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBaseDim.html)
[IDrawingDoc::InsertModelAnnotations3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html)
[IDrawingDoc::SketchDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SketchDim.html)
[IDrawingDoc::AutoDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoDimension.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
