---
title: "IGetSkippedItemArray Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "IGetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSkippedItemArray.html"
---

# IGetSkippedItemArray Method (ILocalCircularPatternFeatureData)

Gets the list of skipped items in this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSkippedItemArray() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

- in-process, unmanaged C++: Pointer to an array of long values that represent the skipped items in the pattern

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This is a 0-based array, so if you skipped the third feature and the fifth feature in the pattern, then:

- Array[0] = 3
- Array[1] = 5

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSkippedItemCount.html)
[ILocalCircularPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSkippedItemArray.html)
[ILocalCircularPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
