---
title: "GetName2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetName2.html"
---

# GetName2 Method (IView)

Gets the name of this drawing view displayed in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetName2() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

value = instance.GetName2()
```

### C#

```csharp
System.string GetName2()
```

### C++/CLI

```cpp
System.String^ GetName2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the drawing view

## VBA Syntax

See [View::GetName2](ms-its:sldworksapivb6.chm::/sldworks~View~GetName2.html).

## Examples

[Activate Each View On Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)
[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)
[Get the Number of Lines of Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)
[Get the Number of Lines of Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)
[Get the Number of Lines of Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)
[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)
[Get Centerlines In Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

## Remarks

This method does not return unique names for section views. Call [IView::GetUniqueName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetUniqueName.html) to get the unique name of a section view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::SetName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetName2.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
