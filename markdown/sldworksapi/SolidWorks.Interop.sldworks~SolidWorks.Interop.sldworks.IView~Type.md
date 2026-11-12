---
title: "Type Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Type.html"
---

# Type Property (IView)

Gets the drawing view type.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of drawing view as defined by [swDrawingViewTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)

## VBA Syntax

See [View::Type](ms-its:sldworksapivb6.chm::/sldworks~View~Type.html).

## Examples

[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)
[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)
[Get Components Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)
[Get Section View (VBA)](Get_Section_View_Data_Example_VB.htm)
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)
[Get Drawing View Names and Types (VB.NET)](Get_Drawing_View_Names_and_Types_Example_VBNET.htm)
[Get Drawing View Names and Types (C#)](Get_Drawing_View_Names_and_Types_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
