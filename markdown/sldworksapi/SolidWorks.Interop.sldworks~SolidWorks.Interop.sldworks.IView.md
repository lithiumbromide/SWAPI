---
title: "IView Interface"
project: "SOLIDWORKS API Help"
interface: "IView"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html"
---

# IView Interface

Represents drawing views found in a drawing document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IView
```

### Visual Basic (Usage)

```vb
Dim instance As IView
```

### C#

```csharp
public interface IView
```

### C++/CLI

```cpp
public interface class IView
```

## VBA Syntax

See [View](ms-its:sldworksapivb6.chm::/sldworks~View.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)
[Set View Display Mode (C++)](Set_View_Display_Mode_Example_CPlusPlus_COM.htm)
[Autodimension Selected Drawing View (VBA)](Autodimension_Selected_Drawing_View_Example_VB.htm)
[Get Base Views (VBA)](Get_Base_Views_Example_VB.htm)
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)
[Insert Alternate Position View (VBA)](Insert_Alternate_Position_View_Example_VB.htm)
[Reposition Drawing Views to Avoid Overlap (VBA)](Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Insert Weldment Cut List Table (VBA)](Insert_Weldment_Cut_List_Table_Example_VB.htm)
[Insert Weldment Cut List Table (VB.NET)](Insert_Weldment_Cut_List_Table_Example_VBNET.htm)
[Insert Weldment Cut List Table (C#)](Insert_Weldment_Cut_List_Table_Example_CSharp.htm)
[Insert Weld Table (VBA)](Insert_Weld_Table_Example_VB.htm)
[Insert Weld Table (VB.NET)](Insert_Weld_Table_Example_VBNET.htm)
[Insert Weld Table (C#)](Insert_Weld_Table_Example_CSharp.htm)
[Get Break Line Data (VBA)](Get_Break_Line_Data_Example_VB.htm)
[Get Break Line Data (VB.NET)](Get_Break_Line_Data_Example_VBNET.htm)
[Get Break Line Data (C#)](Get_Break_Line_Data_Example_CSharp.htm)
[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)
[Insert Hole Table (VB.NET)](Insert_Hole_Table_Example_VBNET.htm)
[Insert Hole Table (C#)](Insert_Hole_Table_Example_CSharp.htm)

## Remarks

A drawing document can consist of one or more drawing sheets. Each drawing sheet typically contains one or more drawing views. Each drawing view is an oriented snapshot of a particular SOLIDWORKS model and a particular configuration of the model.

The IView object lets you determine the particular model and configuration being viewed and to get information about all the objects in a drawing sheet or drawing view, as well as the drawing view bounds, and transforms.

## Accessors

[IBreakLine::GetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakLine~GetView.html)

[IDetailCircle::GetDetailView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetDetailView.html)

[IDetailCircle::GetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~GetView.html)

[IDrawingComponent::View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~View.html)

[IDrawingDoc::ActiveDrawingView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html) and [IDrawingDoc::IActiveDrawingView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)

[IDrawingDoc::CreateAuxiliaryViewAt2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html) and [IDrawingDoc::ICreateAuxiliaryViewAt2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)

[IDrawingDoc::CreateDetailViewAt3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html) and [IDrawingDoc::ICreateDetailViewAt3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)

[IDrawingDoc::CreateDrawViewFromModelView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)

[IDrawingDoc::CreateRelativeView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateRelativeView.html)

[IDrawingDoc::CreateSectionViewAt4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html) and [IDrawingDoc::ICreateSectionViewAt4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)

[IDrawingDoc::CreateUnfoldedViewAt3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)

[IDrawingDoc::CreateViewport3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateViewport3.html)

[IDrawingDoc::DropDrawingViewFromPalette](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette.html)

[IDrawingDoc::GetFirstView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetFirstView.html) and [IDrawingDoc::IGetFirstView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IGetFirstView.html)

[IDrSection::GetSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~GetSectionView.html) and [IDrSection::IGetSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~IGetSectionView.html)

[IDrSection::GetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~GetView.html) and [IDrSection::IGetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~IGetView.html)

[IMacroFeatureData::GetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetSelections3.html) and [IMacroFeatureData::IGetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html)

[IProjectionArrow::GetProjectedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow~GetProjectedView.html) and [IProjectionArrow::IGetProjectedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow~IGetProjectedView.html)

[IProjectionArrow::GetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow~GetView.html) and [IProjectionArrow::IGetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow~IGetView.html)

[ISelectData::View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData~View.html)

[ISelectionMgr::GetSelectedObjectsDrawingView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)

[ISheet::GetViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetViews.html)

[ISilhouetteEdge::GetView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISilhouetteEdge~GetView.html)

[IView::GetBaseView and IView::IGetBaseView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBaseView.html)

[IView::GetDependentViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDependentViews.html) and [IView::IGetDependentViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDependentViews.html)

[IView::GetNextView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetNextView.html) and [IView::IGetNextView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetNextView.html)

[IView::InsertAlternateView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertAlternateView.html)

## Access Diagram

[View](SWObjectModel.pdf#View)

## See Also

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
