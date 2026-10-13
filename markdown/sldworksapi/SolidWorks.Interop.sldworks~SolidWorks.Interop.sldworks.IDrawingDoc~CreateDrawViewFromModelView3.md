---
title: "CreateDrawViewFromModelView3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDrawViewFromModelView3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html"
---

# CreateDrawViewFromModelView3 Method (IDrawingDoc)

Creates a drawing view on the current drawing sheet using the specified model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDrawViewFromModelView3( _
   ByVal ModelName As System.String, _
   ByVal ViewName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ViewName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As View

value = instance.CreateDrawViewFromModelView3(ModelName, ViewName, LocX, LocY, LocZ)
```

### C#

```csharp
View CreateDrawViewFromModelView3(
   System.string ModelName,
   System.string ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

### C++/CLI

```cpp
View^ CreateDrawViewFromModelView3(
   System.String^ ModelName,
   System.String^ ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Full pathname of the model document for which to create the drawing view (see **Remarks**)
- `ViewName`: Name of the model view from which to create the drawing view (see **Remarks**)
- `LocX`: x location of drawing view center in meters
- `LocY`: y location of drawing view center in meters
- `LocZ`: z location of drawing view center in meters

### Return Value

Pointer to the newly create [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object

## VBA Syntax

See [DrawingDoc::CreateDrawViewFromModelView3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDrawViewFromModelView3.html).

## Examples

[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)

## Remarks

This method:

- Places the center of the view at the specified location.
- Uses the [swAutomaticScaling3ViewDrawings](ms-its:swconst.chm::/SO_Drawings.htm) setting to set the view scale. If this setting is set to True, then when a new drawing view is inserted, that view automatically scales to fit nicely on the drawing sheet. If there are no views on the sheet, the sheet scale is changed to the appropriate scale, and the view created uses the sheet scale.

If a model document is currently open in SOLIDWORKS and you don't know its full pathname, call [IModelDoc2::GetPathName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html) to populate ModelName. Include the **.sldprt** or **.sldasm** extension in the pathname.

ViewName must exactly match the name of the model view. For example, the names of the standard views begin with an asterisk. This asterisk is part of the view name and must be included (for example, "*Front").

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13.2
