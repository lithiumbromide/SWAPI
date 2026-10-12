---
title: "AddDimension Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "AddDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddDimension.html"
---

# AddDimension Method (IDimPatternFeatureData)

Adds the selected dimension as a column to the pattern table for this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDimension() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim value As System.Boolean

value = instance.AddDimension()
```

### C#

```csharp
System.bool AddDimension()
```

### C++/CLI

```cpp
System.bool AddDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True adds the selected dimension as a column to the pattern table, false does not

## VBA Syntax

See [DimPatternFeatureData::AddDimension](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~AddDimension.html).

## Examples

[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::DeleteDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteDimension.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
