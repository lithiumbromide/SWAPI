---
title: "ReadOnly Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ReadOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReadOnly.html"
---

# ReadOnly Property (IDimension)

Gets or sets the read-only state of a dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReadOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Boolean

instance.ReadOnly = value

value = instance.ReadOnly
```

### C#

```csharp
System.bool ReadOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool ReadOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the dimension is read-only, false if it is writable

## VBA Syntax

See [Dimension::ReadOnly](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ReadOnly.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
