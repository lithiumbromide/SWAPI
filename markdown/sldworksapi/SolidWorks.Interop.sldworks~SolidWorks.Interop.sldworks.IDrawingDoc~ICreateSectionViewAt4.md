---
title: "ICreateSectionViewAt4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateSectionViewAt4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html"
---

# ICreateSectionViewAt4 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::ICreateSectionViewAt5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSectionViewAt4( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal SectionLabel As System.String, _
   ByVal Options As System.Integer, _
   ByVal NumExcludedComponents As System.Integer, _
   ByRef ExcludedComponents As System.Object _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim SectionLabel As System.String
Dim Options As System.Integer
Dim NumExcludedComponents As System.Integer
Dim ExcludedComponents As System.Object
Dim value As View

value = instance.ICreateSectionViewAt4(X, Y, Z, SectionLabel, Options, NumExcludedComponents, ExcludedComponents)
```

### C#

```csharp
View ICreateSectionViewAt4(
   System.double X,
   System.double Y,
   System.double Z,
   System.string SectionLabel,
   System.int Options,
   System.int NumExcludedComponents,
   ref System.object ExcludedComponents
)
```

### C++/CLI

```cpp
View^ ICreateSectionViewAt4(
   System.double X,
   System.double Y,
   System.double Z,
   System.String^ SectionLabel,
   System.int Options,
   System.int NumExcludedComponents,
   System.Object^% ExcludedComponents
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x position on the drawing sheet for the center of the section view
- `Y`: y position on the drawing sheet for the center of the section view
- `Z`: z position on the drawing sheet for the center of the section view
- `SectionLabel`: Letter for the label for the section view
- `Options`: Options that affect the section view as defined in [swCreateSectionViewAtOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSectionViewAtOptions_e.html)
- `NumExcludedComponents`: Number of components to exclude from the section view
- `ExcludedComponents`: Array of components to exclude from the section view

### Return Value

Pointer to the newly created [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object

## VBA Syntax

See [DrawingDoc::ICreateSectionViewAt4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateSectionViewAt4.html).

## Remarks

Before calling this method, select the section line or the lines to use as a section line.

This method runs silently; the end-user is not prompted for a label.

Use [IView::IGetSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSection.html) to get the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) object, and use [IDrSection::SetLabel2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~SetLabel2.html) to set the name for the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
