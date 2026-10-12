---
title: "GetTableRowIndex Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetTableRowIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.html"
---

# GetTableRowIndex Method (IDimPatternFeatureData)

Gets the index of the specified pattern instance in the pattern table in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableRowIndex( _
   ByVal InstanceName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim InstanceName As System.String
Dim value As System.Integer

value = instance.GetTableRowIndex(InstanceName)
```

### C#

```csharp
System.int GetTableRowIndex(
   System.string InstanceName
)
```

### C++/CLI

```cpp
System.int GetTableRowIndex(
   System.String^ InstanceName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InstanceName`: Name of the pattern instance (see **Remarks**)

### Return Value

Index in the pattern table for InstanceName (see **Remarks**)

## VBA Syntax

See [DimPatternFeatureData::GetTableRowIndex](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetTableRowIndex.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use [IDimPatternFeatureData::GetInstanceNameByIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.html) to get InstanceName.

**NOTE**: The index returned by this method is a value in a row in the **Instance** column in the pattern table.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::GetInstanceIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceIndex.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
