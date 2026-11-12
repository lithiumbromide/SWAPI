---
title: "IGetSkippedItemArray Method (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "IGetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~IGetSkippedItemArray.html"
---

# IGetSkippedItemArray Method (IDerivedPatternFeatureData)

Gets the list of skipped items for this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSkippedItemArray() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
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

- in-process, unmanaged C++:: Pointer to an array of longs of the items skipped

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetSkippedItemCount.html)
[IDerivedPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ISetSkippedItemArray.html)
[IDerivedPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
