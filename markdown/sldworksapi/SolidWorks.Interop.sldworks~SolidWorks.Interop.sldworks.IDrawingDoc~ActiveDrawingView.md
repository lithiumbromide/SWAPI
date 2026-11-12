---
title: "ActiveDrawingView Property (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ActiveDrawingView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html"
---

# ActiveDrawingView Property (IDrawingDoc)

Gets the currently active drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveDrawingView As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.ActiveDrawingView
```

### C#

```csharp
System.object ActiveDrawingView {get;}
```

### C++/CLI

```cpp
property System.Object^ ActiveDrawingView {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Currently active drawing view

## VBA Syntax

See [DrawingDoc::ActiveDrawingView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ActiveDrawingView.html).

## Examples

[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)
[Get Number of Polylines in Shaded Mode in Drawing View (VBA)](Get_Number_of_Polylines_in_Shaded_Mode_Drawing_View_Example_VB.htm)
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)
[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)

## Remarks

This property returns the active drawing view, if one is active. If the drawing sheet is active, the property returns NULL and you can use [IDrawingDoc::GetCurrentSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html) to get the current sheet for this drawing.

This is a read-only property. Use [IDrawingDoc::ActivateView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActivateView.html) to set the active drawing view.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::InsertModelInPredefinedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelInPredefinedView.html)
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
