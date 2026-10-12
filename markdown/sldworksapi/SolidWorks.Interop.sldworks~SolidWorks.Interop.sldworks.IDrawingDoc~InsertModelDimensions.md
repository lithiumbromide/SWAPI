---
title: "InsertModelDimensions Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertModelDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions.html"
---

# InsertModelDimensions Method (IDrawingDoc)

Inserts model dimensions into the selected drawing view according to the option specified.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertModelDimensions( _
   ByVal Option As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Option As System.Integer

instance.InsertModelDimensions(Option)
```

### C#

```csharp
void InsertModelDimensions(
   System.int Option
)
```

### C++/CLI

```cpp
void InsertModelDimensions(
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: - 0 - All dimensions in the view
  - 1 - All dimensions of the currently selected component (for assembly drawings)
  - 2 - All dimensions of the currently selected feature
  - 3 - All dimensions of the assembly

## VBA Syntax

See [DrawingDoc::InsertModelDimensions](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertModelDimensions.html).

## Remarks

The **Insert Model Items** dialog is not displayed.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.html)
[IDrawingDoc::DragModelDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension.html)
[IDrawingDoc::HideShowDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.html)
[IDrawingDoc::InsertModelAnnotations3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html)
[IDrawingDoc::InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.html)
