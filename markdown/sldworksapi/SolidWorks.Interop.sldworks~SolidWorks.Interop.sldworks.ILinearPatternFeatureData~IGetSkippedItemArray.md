---
title: "IGetSkippedItemArray Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "IGetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetSkippedItemArray.html"
---

# IGetSkippedItemArray Method (ILinearPatternFeatureData)

Gets the items skipped in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSkippedItemArray() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Integer

value = instance.IGetSkippedItemArray()
```

### C#

```csharp
System.int IGetSkippedItemArray()
```

### C++/CLI

```cpp
System.int IGetSkippedItemArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of the skipped items

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This array is 0-based, so if you skipped the third and fifth items in the pattern, then Array[0] = 3 and Array[1] = 5.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetSkippedItemCount.html)
[ILinearPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetSkippedItemArray.html)
[ILinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
