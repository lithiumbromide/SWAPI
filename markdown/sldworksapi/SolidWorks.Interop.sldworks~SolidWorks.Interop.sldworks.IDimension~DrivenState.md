---
title: "DrivenState Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "DrivenState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DrivenState.html"
---

# DrivenState Property (IDimension)

Gets or sets the driven state of a dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrivenState As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Integer

instance.DrivenState = value

value = instance.DrivenState
```

### C#

```csharp
System.int DrivenState {get; set;}
```

### C++/CLI

```cpp
property System.int DrivenState {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Driven state of the dimension as defined in [swDimensionDrivenState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionDrivenState_e.html)

## VBA Syntax

See [Dimension::DrivenState](ms-its:sldworksapivb6.chm::/sldworks~Dimension~DrivenState.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
