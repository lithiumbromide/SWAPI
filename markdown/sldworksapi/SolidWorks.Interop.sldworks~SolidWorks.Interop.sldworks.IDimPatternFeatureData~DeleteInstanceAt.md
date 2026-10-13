---
title: "DeleteInstanceAt Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "DeleteInstanceAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteInstanceAt.html"
---

# DeleteInstanceAt Method (IDimPatternFeatureData)

Deletes the specified pattern instance in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteInstanceAt( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.DeleteInstanceAt(Index)
```

### C#

```csharp
System.bool DeleteInstanceAt(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool DeleteInstanceAt(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index indicating where to delete this pattern instance in the pattern table and pattern; -1 indicates to delete this pattern instance at the end of the pattern table and pattern (see **Remarks**)

### Return Value

True if the pattern instance is deleted, false if not

## VBA Syntax

See [DimPatternFeatureData:DeleteInstanceAt](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~DeleteInstanceAt.html).

## Examples

[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use [IDimPatternFeatureData::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.html) to get the number of pattern instances.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::AddInstanceAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddInstanceAt.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
