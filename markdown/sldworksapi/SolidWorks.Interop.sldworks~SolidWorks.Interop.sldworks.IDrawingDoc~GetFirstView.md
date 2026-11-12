---
title: "GetFirstView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetFirstView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html"
---

# GetFirstView Method (IDrawingDoc)

Gets the first drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) on the current sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetFirstView()
```

### C#

```csharp
System.object GetFirstView()
```

### C++/CLI

```cpp
System.Object^ GetFirstView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) in this drawing document

## VBA Syntax

See [DrawingDoc::GetFirstView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetFirstView.html).

## Examples

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)
[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Get Crosshatches on View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)
[Traverse Drawing FeatureManager Design Tree (VBA)](Traverse_Drawing_FeatureManager_Design_Tree_Example_VB.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

## Remarks

This method might be useful for starting an iteration through all the drawing views on the current sheet.

Because the drawing sheet also has sketch geometry, notes, GTols, and so on, this method returns the current drawing sheet. The next view returned by [IView::GetNextView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetNextView.html) is the first drawing view in the current sheet.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html)
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
