---
title: "CreateRelativeView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateRelativeView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.html"
---

# CreateRelativeView Method (IDrawingDoc)

Creates a relative drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRelativeView( _
   ByVal ModelName As System.String, _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ViewDirFront As System.Integer, _
   ByVal ViewDirRight As System.Integer _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim XPos As System.Double
Dim YPos As System.Double
Dim ViewDirFront As System.Integer
Dim ViewDirRight As System.Integer
Dim value As View

value = instance.CreateRelativeView(ModelName, XPos, YPos, ViewDirFront, ViewDirRight)
```

### C#

```csharp
View CreateRelativeView(
   System.string ModelName,
   System.double XPos,
   System.double YPos,
   System.int ViewDirFront,
   System.int ViewDirRight
)
```

### C++/CLI

```cpp
View^ CreateRelativeView(
   System.String^ ModelName,
   System.double XPos,
   System.double YPos,
   System.int ViewDirFront,
   System.int ViewDirRight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Path and filename of the model for which to create a relative drawing view
- `XPos`: x coordinate where to create the relative drawing view
- `YPos`: y coordinate where to create a relative drawing view
- `ViewDirFront`: Orientation as defined by [swRelativeViewCreationDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRelativeViewCreationDirection_e.html)
- `ViewDirRight`: Orientation as defined by [swRelativeViewCreationDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRelativeViewCreationDirection_e.html)

### Return Value

[View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DrawingDoc::CreateRelativeView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateRelativeView.html).

## Examples

[Create Relative Drawing View (C#)](Create_Relative_Drawing_View_Example_CSharp.htm)
[Create Relative Drawing View (VB.NET)](Create_Relative_Drawing_View_Example_VBNET.htm)
[Create Relative Drawing View (VBA)](Create_Relative_Drawing_View_Example_VB.htm)

## Remarks

Select:

- the first orientation component using selection mark 1.
- the second orientation component using selection mark 2.

For multi-body parts only, select bodies to be shown in the created view using selection mark 4.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
