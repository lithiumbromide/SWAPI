---
title: "GetType Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetType.html"
---

# GetType Method (IDimension)

Gets the type of dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of dimension as defined by [swDimensionParamType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionParamType_e.html)

## VBA Syntax

See [Dimension::GetType](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetType.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)
[Get Dimension Values in Drawing (VB.NET)](Get_Dimension_Values_in_Drawing_Example_VBNET.htm)
[Get Dimension Values in Drawing (C#)](Get_Dimension_Values_in_Drawing_Example_CSharp.htm)

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
