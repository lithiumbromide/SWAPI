---
title: "CreateSectionViewAt5 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateSectionViewAt5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt5.html"
---

# CreateSectionViewAt5 Method (IDrawingDoc)

Creates the specified section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionViewAt5( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal SectionLabel As System.String, _
   ByVal Options As System.Integer, _
   ByVal ExcludedComponents As System.Object, _
   ByVal SectionDepth As System.Double _
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
Dim SectionDepth As System.Double
Dim value As View

value = instance.CreateSectionViewAt5(X, Y, Z, SectionLabel, Options, ExcludedComponents, SectionDepth)
```

### C#

```csharp
View CreateSectionViewAt5(
   System.double X,
   System.double Y,
   System.double Z,
   System.string SectionLabel,
   System.int Options,
   System.object ExcludedComponents,
   System.double SectionDepth
)
```

### C++/CLI

```cpp
View^ CreateSectionViewAt5(
   System.double X,
   System.double Y,
   System.double Z,
   System.String^ SectionLabel,
   System.int Options,
   System.Object^ ExcludedComponents,
   System.double SectionDepth
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
- `SectionDepth`: Distance from the selected section line (see **Remarks**)

### Return Value

Section [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DrawingDoc::CreateSectionViewAt5](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateSectionViewAt5.html).

## Examples

[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)

## Remarks

Before calling this method, select the section line or lines to use as a section line.

This method runs silently; the end-user is not prompted for a label.

Use [IView::GetSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSection.html) to get the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) object, and use [IDrSection::SetLabel2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~SetLabel2.html) to set the name for the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateSectionViewAt5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt5.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
