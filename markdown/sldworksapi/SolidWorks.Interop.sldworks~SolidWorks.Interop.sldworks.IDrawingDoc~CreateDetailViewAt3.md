---
title: "CreateDetailViewAt3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDetailViewAt3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html"
---

# CreateDetailViewAt3 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateDetailViewAt4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDetailViewAt3( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Style As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal LabelIn As System.String, _
   ByVal Showtype As System.Integer, _
   ByVal FullOutline As System.Boolean _
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
Dim value As System.Object

value = instance.CreateDetailViewAt3(X, Y, Z, Style, Scale1, Scale2, LabelIn, Showtype, FullOutline)
```

### C#

```csharp
System.object CreateDetailViewAt3(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.string LabelIn,
   System.int Showtype,
   System.bool FullOutline
)
```

### C++/CLI

```cpp
System.Object^ CreateDetailViewAt3(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.String^ LabelIn,
   System.int Showtype,
   System.bool FullOutline
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
- `LabelIn`: String for the detail view label
- `Showtype`: Type of sketch profile for the detail view as defined in [swDetCircleShowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)
- `FullOutline`: True shows the full outline of the detail view, false does not

### Return Value

Detail [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DrawingDoc::CreateDetailViewAt3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDetailViewAt3.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
