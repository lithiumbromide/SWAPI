---
title: "GetSkippedItemCount Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "GetSkippedItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetSkippedItemCount.html"
---

# GetSkippedItemCount Method (ILinearPatternFeatureData)

Gets the number of instances skipped in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSkippedItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

Number of skipped instances

## VBA Syntax

See [LinearPatternFeatureData::GetSkippedItemCount](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~GetSkippedItemCount.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetSkippedItemArray.html)
[ILinearPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetSkippedItemArray.html)
[ILinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
