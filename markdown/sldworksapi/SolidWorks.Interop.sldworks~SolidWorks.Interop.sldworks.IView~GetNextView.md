---
title: "GetNextView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetNextView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html"
---

# GetNextView Method (IView)

Gets the next drawing view in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetNextView()
```

### C#

```csharp
System.object GetNextView()
```

### C++/CLI

```cpp
System.Object^ GetNextView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [View::GetNextView](ms-its:sldworksapivb6.chm::/sldworks~View~GetNextView.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)
[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)
[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Get Crosshatches on View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)
[Get Drawing View Names and Types (VB.NET)](Get_Drawing_View_Names_and_Types_Example_VBNET.htm)
[Get Drawing View Names and Types (C#)](Get_Drawing_View_Names_and_Types_Example_CSharp.htm)
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[IView::GetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.html)
[IView::IGetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.html)
