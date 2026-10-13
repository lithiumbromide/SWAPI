---
title: "GetInstanceNameByIndex Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetInstanceNameByIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceNameByIndex.html"
---

# GetInstanceNameByIndex Method (IDimPatternFeatureData)

Gets the name of the pattern instance at the specified index in the pattern table in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceNameByIndex( _
   ByVal TableRowIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim value As System.String

value = instance.GetInstanceNameByIndex(TableRowIndex)
```

### C#

```csharp
System.string GetInstanceNameByIndex(
   System.int TableRowIndex
)
```

### C++/CLI

```cpp
System.String^ GetInstanceNameByIndex(
   System.int TableRowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableRowIndex`: 1-based index of the pattern instance in the pattern table (see **Remarks**)

### Return Value

Name of the pattern instance

## VBA Syntax

See [DimPatternFeatureData::GetInstanceNameByIndex](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetInstanceNameByIndex.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use [IDimPatternFeatureData::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.html) to get TableRowIndex.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
