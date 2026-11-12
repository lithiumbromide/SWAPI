---
title: "ISetSkippedItemArray Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "ISetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSkippedItemArray.html"
---

# ISetSkippedItemArray Method (ILocalCircularPatternFeatureData)

Sets the list of skipped items for this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSkippedItemArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Integer

instance.ISetSkippedItemArray(FeatCount, ArrayDataIn)
```

### C#

```csharp
void ISetSkippedItemArray(
   System.int FeatCount,
   ref System.int ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetSkippedItemArray(
   System.int FeatCount,
   System.int% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatCount`: Number of skipped items
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of skipped items

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSkippedItemCount.html)
[ILocalCircularPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSkippedItemArray.html)
[ILocalCircularPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
