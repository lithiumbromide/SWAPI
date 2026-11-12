---
title: "CreateSectionViewAt4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateSectionViewAt4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html"
---

# CreateSectionViewAt4 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateSectionViewAt5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateSectionViewAt5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionViewAt4( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal SectionLabel As System.String, _
   ByVal Options As System.Integer, _
   ByVal ExcludedComponents As System.Object _
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
Dim ExcludedComponents As System.Object
Dim value As View

value = instance.CreateSectionViewAt4(X, Y, Z, SectionLabel, Options, ExcludedComponents)
```

### C#

```csharp
View CreateSectionViewAt4(
   System.double X,
   System.double Y,
   System.double Z,
   System.string SectionLabel,
   System.int Options,
   System.object ExcludedComponents
)
```

### C++/CLI

```cpp
View^ CreateSectionViewAt4(
   System.double X,
   System.double Y,
   System.double Z,
   System.String^ SectionLabel,
   System.int Options,
   System.Object^ ExcludedComponents
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x position on the drawing sheet for the center of the section view
- `Y`: y position on the drawing sheet for the center of the section view
- `Z`: z position on the drawing sheet for the center of the section view
- `SectionLabel`: Letter for the label for the section view
- `Options`: Options that affect the section view as defined in [swCreateSectionViewAtOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSectionViewAtOptions_e.html)
- `ExcludedComponents`: Array of components to exclude from the section view

### Return Value

Pointer to the newly created [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object

## VBA Syntax

See [DrawingDoc::CreateSectionViewAt4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateSectionViewAt4.html).

## Remarks

Before calling this method, select the section line or the lines to use as a section line.

This method runs silently; the end-user is not prompted for a label.

Use [IView::GetSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSection.html) to get the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) object, and use [IDrSection::SetLabel2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~SetLabel2.html) to set the name for the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
