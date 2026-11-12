---
title: "SetInstanceDimensionValue Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "SetInstanceDimensionValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceDimensionValue.html"
---

# SetInstanceDimensionValue Method (IDimPatternFeatureData)

Sets a new value for the pattern dimension of the specified pattern instance in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetInstanceDimensionValue( _
   ByVal TableRowIndex As System.Integer, _
   ByVal ControlDimName As System.String, _
   ByVal NewValue As System.Double _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim ControlDimName As System.String
Dim NewValue As System.Double
Dim value As System.String

value = instance.SetInstanceDimensionValue(TableRowIndex, ControlDimName, NewValue)
```

### C#

```csharp
System.string SetInstanceDimensionValue(
   System.int TableRowIndex,
   System.string ControlDimName,
   System.double NewValue
)
```

### C++/CLI

```cpp
System.String^ SetInstanceDimensionValue(
   System.int TableRowIndex,
   System.String^ ControlDimName,
   System.double NewValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableRowIndex`: Index of the pattern instance in the pattern table (see **Remarks**)
- `ControlDimName`: Name of the controlling dimension of the pattern instance (see **Remarks**)
- `NewValue`: New value for the pattern dimension

### Return Value

| If a new value for the pattern dimension is... | Then Return Value is an... |
| --- | --- |
| Set | Empty string indicating success |
| Not set | Error string |

## VBA Syntax

See [DimPatternFeatureData::SetInstanceDimensionValue](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~SetInstanceDimensionValue.html).

## Examples

[Delete and Insert Instances in Variable Pattern Feature (C#)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete and Insert Instances in Variable Pattern Feature (VB.NET)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete and Insert Instances in Variable Pattern Feature (VBA)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use:

- [IDimPatternFeatureData::GetTableRowIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.html) to get TableRowIndex.
- [IDimPatternFeatureData::GetControllingDimensionName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionName.html) to get ControlDimName.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::GetInstanceDimensionName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceDimensionName.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
