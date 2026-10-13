---
title: "ActivateView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ActivateView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.html"
---

# ActivateView Method (IDrawingDoc)

Activates the specified drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateView( _
   ByVal ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.ActivateView(ViewName)
```

### C#

```csharp
System.bool ActivateView(
   System.string ViewName
)
```

### C++/CLI

```cpp
System.bool ActivateView(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the drawing view

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::ActivateView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ActivateView.html).

## Examples

[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)
[Create Detail View (VBA)](Create_Detail_View_Example_VB.htm)
[Insert Autoballoons Using IDrawingDoc::AutoBalloon2 (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)
[Undo Deleted Note and Fire Undo Post-Notify Event (VB.NET)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Deleted Note and Fire Undo Post-Notify Event (C#)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)
[Undo Deleted Note and Fire Undo Post-Notify Event (VBA)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)

## Remarks

This method returns false when trying to activate a drawing sheet. To activate a drawing sheet, use [IDrawingDoc::ActivateSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActivateSheet.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
