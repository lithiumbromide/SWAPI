---
title: "CreateDetailViewAt4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDetailViewAt4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt4.html"
---

# CreateDetailViewAt4 Method (IDrawingDoc)

Creates a detail view in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDetailViewAt4( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Style As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal LabelIn As System.String, _
   ByVal Showtype As System.Integer, _
   ByVal FullOutline As System.Boolean, _
   ByVal JaggedOutline As System.Boolean, _
   ByVal NoOutline As System.Boolean, _
   ByVal ShapeIntensity As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Style As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim LabelIn As System.String
Dim Showtype As System.Integer
Dim FullOutline As System.Boolean
Dim JaggedOutline As System.Boolean
Dim NoOutline As System.Boolean
Dim ShapeIntensity As System.Integer
Dim value As System.Object

value = instance.CreateDetailViewAt4(X, Y, Z, Style, Scale1, Scale2, LabelIn, Showtype, FullOutline, JaggedOutline, NoOutline, ShapeIntensity)
```

### C#

```csharp
System.object CreateDetailViewAt4(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.string LabelIn,
   System.int Showtype,
   System.bool FullOutline,
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
)
```

### C++/CLI

```cpp
System.Object^ CreateDetailViewAt4(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.String^ LabelIn,
   System.int Showtype,
   System.bool FullOutline,
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X position for the detail view
- `Y`: Y position for the detail view
- `Z`: Z position for the detail view
- `Style`: Style for the detail view as defined in [swDetViewStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetViewStyle_e.html)
- `Scale1`: Scale numerator
- `Scale2`: Scale denominator
- `LabelIn`: Detail view label
- `Showtype`: Type of sketch for the detail view as defined in [swDetCircleShowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)
- `FullOutline`: True to show a full outline, false to not; valid only if NoOutline is false
- `JaggedOutline`: True to show a jagged outline, false to not; only valid if NoOutline is false
- `NoOutline`: True to not show an outline, false to show an outline
- `ShapeIntensity`: Intensity of jagged outline; valid range is 1 (most) to 5 (least) and only valid if JaggedOutline is true and NoOutline is false

### Return Value

Detail [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

## VBA Syntax

See [DrawingDoc::CreateDetailViewAt4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDetailViewAt4.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateViewport3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::Create1stAngleViews2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateSectionViewAt5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt5.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
