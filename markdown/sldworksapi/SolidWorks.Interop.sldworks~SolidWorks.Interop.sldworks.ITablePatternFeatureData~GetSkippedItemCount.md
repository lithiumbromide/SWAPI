---
title: "GetSkippedItemCount Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetSkippedItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetSkippedItemCount.html"
---

# GetSkippedItemCount Method (ITablePatternFeatureData)

Gets the number of skipped items in this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSkippedItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Integer

value = instance.GetSkippedItemCount()
```

### C#

```csharp
System.int GetSkippedItemCount()
```

### C++/CLI

```cpp
System.int GetSkippedItemCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of skipped items

## VBA Syntax

See [TablePatternFeatureData::GetSkippedItemCount](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetSkippedItemCount.html).

## Remarks

Call this method before calling [ITablePatternFeatureData::IGetSkippedItemArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.html) to get the size of the array.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.html)
[ITablePatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetSkippedItemArray.html)
[ITablePatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
