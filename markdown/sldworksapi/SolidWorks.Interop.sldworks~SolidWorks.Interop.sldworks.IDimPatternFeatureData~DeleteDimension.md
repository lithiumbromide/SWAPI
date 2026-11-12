---
title: "DeleteDimension Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "DeleteDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteDimension.html"
---

# DeleteDimension Method (IDimPatternFeatureData)

Deletes the specified column of dimensions in the pattern table in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDimension( _
   ByVal DimensionColumnName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim DimensionColumnName As System.String
Dim value As System.Boolean

value = instance.DeleteDimension(DimensionColumnName)
```

### C#

```csharp
System.bool DeleteDimension(
   System.string DimensionColumnName
)
```

### C++/CLI

```cpp
System.bool DeleteDimension(
   System.String^ DimensionColumnName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimensionColumnName`: Name of the column of dimensions to delete (see **Remarks**)

### Return Value

True if the column of dimensions is deleted, false if not

## VBA Syntax

See [DimPatternFeatureData::DeleteDimension](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~DeleteDimension.html).

## Examples

[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

The name of a column corresponds to the dimension name and feature name, separated by an @ symbol; e.g., **D3@Fillet1**.

There are various ways of getting the name of the column of dimensions to delete from a pattern table. For example, you can traverse the features, get the dimensions, and get the names of the dimensions. You can also select a dimension and get its name. See the examples for details.

**NOTE:** You cannot delete a column containing the dimensions of a parent sketch or feature.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::AddDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddDimension.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
