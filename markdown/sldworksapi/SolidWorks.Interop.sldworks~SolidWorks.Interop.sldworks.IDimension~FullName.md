---
title: "FullName Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "FullName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.html"
---

# FullName Property (IDimension)

Gets the full name of a dimension including the feature and the model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FullName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.String

value = instance.FullName
```

### C#

```csharp
System.string FullName {get;}
```

### C++/CLI

```cpp
property System.String^ FullName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the dimension including the feature and model

## VBA Syntax

See [Dimension::FullName](ms-its:sldworksapivb6.chm::/sldworks~Dimension~FullName.html).

## Examples

[Determine if Display Dimension Marked for Drawing (VBA)](Determine_if_Display_Dimension_Marked_for_Drawing_Example_VB.htm)
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)

## Remarks

The syntax of the name returned is:

```vb
<Dimension Name>@<Feature Name>@<Model>
```

where:

- <Dimension Name> is the name of the dimension as returned from [IDimension::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~Name.html)
- <Feature Name> is the name of the feature that the dimension is on
- <Model> is the name of the model containing the feature

For example:

```vb
"D1@Sketch1@Part4.Part"
```

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
