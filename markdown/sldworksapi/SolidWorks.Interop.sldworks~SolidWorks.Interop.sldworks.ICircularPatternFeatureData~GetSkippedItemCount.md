---
title: "GetSkippedItemCount Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GetSkippedItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetSkippedItemCount.html"
---

# GetSkippedItemCount Method (ICircularPatternFeatureData)

Gets the number of items skipped in this circular pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSkippedItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

See [CircularPatternFeatureData::GetSkippedItemCount](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GetSkippedItemCount.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetSkippedItemArray.html)
[ICircularPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetSkippedItemArray.html)
[ICircularPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
