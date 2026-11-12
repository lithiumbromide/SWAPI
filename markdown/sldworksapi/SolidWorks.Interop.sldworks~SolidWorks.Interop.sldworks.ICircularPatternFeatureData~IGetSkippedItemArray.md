---
title: "IGetSkippedItemArray Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "IGetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetSkippedItemArray.html"
---

# IGetSkippedItemArray Method (ICircularPatternFeatureData)

Gets an array of integers that represent the skipped items in this circular feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSkippedItemArray() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

- in-process, unmanaged C++: Pointer to an array of integers that represent the skipped items in the pattern

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This is a 0-based array, so if you skip the third and fifth items in the pattern, then:

- Array[0] = 3
- Array[1] = 5

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetSkippedItemCount.html)
[ICircularPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetSkippedItemArray.html)
[ICircularPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
