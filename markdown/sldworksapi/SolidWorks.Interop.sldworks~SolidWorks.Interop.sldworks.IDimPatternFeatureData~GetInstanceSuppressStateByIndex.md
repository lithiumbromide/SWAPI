---
title: "GetInstanceSuppressStateByIndex Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetInstanceSuppressStateByIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.html"
---

# GetInstanceSuppressStateByIndex Method (IDimPatternFeatureData)

Gets whether the pattern instance at the specified index in the pattern table is suppressed in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceSuppressStateByIndex( _
   ByVal TableRowIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim value As System.Boolean

value = instance.GetInstanceSuppressStateByIndex(TableRowIndex)
```

### C#

```csharp
System.bool GetInstanceSuppressStateByIndex(
   System.int TableRowIndex
)
```

### C++/CLI

```cpp
System.bool GetInstanceSuppressStateByIndex(
   System.int TableRowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableRowIndex`: Index of the pattern instance in the pattern table (see **Remarks**)

### Return Value

True if the pattern instance is suppressed, false if not

## VBA Syntax

See [DimPatternFeatureData::GetInstanceSuppressStateByIndex](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetInstanceSuppressStateByIndex.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use [IDimPatternFeatureData::GetTableRowIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.html) to get TableRowIndex.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::SetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.html)
[IDimPatternFeatureData::GetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.html)
[IDimPatternFeatureData::SetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
