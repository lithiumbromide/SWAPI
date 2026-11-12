---
title: "SetInstanceSuppressStateByIndex Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "SetInstanceSuppressStateByIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByIndex.html"
---

# SetInstanceSuppressStateByIndex Method (IDimPatternFeatureData)

Sets whether the pattern instance with the specified index in the pattern table is suppressed in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetInstanceSuppressStateByIndex( _
   ByVal TableRowIndex As System.Integer, _
   ByVal SuppressState As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim TableRowIndex As System.Integer
Dim SuppressState As System.Boolean
Dim value As System.String

value = instance.SetInstanceSuppressStateByIndex(TableRowIndex, SuppressState)
```

### C#

```csharp
System.string SetInstanceSuppressStateByIndex(
   System.int TableRowIndex,
   System.bool SuppressState
)
```

### C++/CLI

```cpp
System.String^ SetInstanceSuppressStateByIndex(
   System.int TableRowIndex,
   System.bool SuppressState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableRowIndex`: Index of the pattern instance in the pattern table to suppress (see **Remarks**)
- `SuppressState`: True to suppress the pattern instance, false to not

### Return Value

| If the pattern instance is... | Then Return Value is an... |
| --- | --- |
| Suppressed | Empty string indicating success |
| Not suppressed | Error string |

## VBA Syntax

See [DimPatternFeatureData::SetInstanceSuppressStateByIndex](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~SetInstanceSuppressStateByIndex.html).

## Remarks

Use [IDimPatternFeatureData::GetTableRowIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetTableRowIndex.html) to get TableRowIndex.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::GetInstanceSuppressStateByIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByIndex.html)
[IDimPatternFeatureData::GetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceSuppressStateByName.html)
[IDimPatternFeatureData::SetInstanceSuppressStateByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceSuppressStateByName.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
