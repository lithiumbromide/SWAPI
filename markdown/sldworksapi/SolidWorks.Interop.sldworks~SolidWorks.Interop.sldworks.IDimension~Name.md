---
title: "Name Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Name.html"
---

# Name Property (IDimension)

Gets or sets the name of a dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the dimension

## VBA Syntax

See [Dimension::Name](ms-its:sldworksapivb6.chm::/sldworks~Dimension~Name.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Component Via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)

## Remarks

If setting the name of a dimension, do not include any of the special characters reserved by SOLIDWORKS.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::FullName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.html)
