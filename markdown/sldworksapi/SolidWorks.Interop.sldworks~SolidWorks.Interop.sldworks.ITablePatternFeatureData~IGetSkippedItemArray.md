---
title: "IGetSkippedItemArray Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "IGetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.html"
---

# IGetSkippedItemArray Method (ITablePatternFeatureData)

Gets the skipped items in this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSkippedItemArray( _
   ByVal Count As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim Count As System.Integer
Dim value As System.Integer

value = instance.IGetSkippedItemArray(Count)
```

### C#

```csharp
System.int IGetSkippedItemArray(
   System.int Count
)
```

### C++/CLI

```cpp
System.int IGetSkippedItemArray(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of skipped items

### Return Value

- in-process, unmanaged C++: Pointer to an array of skipped items

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Call [ITablePatternFeatureData::GetSkippedItemCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~GetSkippedItemCount.html) before calling this method to get the size of the array.

Because this is a 0-based array, if you skipped the third feature and fifth feature in the pattern, then:

- 0 = 3
- 1 = 5

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetSkippedItemArray.html)
[ITablePatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
