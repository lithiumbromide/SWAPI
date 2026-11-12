---
title: "ISetSkippedItemArray Method (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "ISetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ISetSkippedItemArray.html"
---

# ISetSkippedItemArray Method (IDerivedPatternFeatureData)

Sets the list of items to skip for this derived pattern feature.

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
Dim instance As IDerivedPatternFeatureData
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

- `FeatCount`: Number of items to skip
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of longs of the items to skip

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetSkippedItemCount.html)
[IDerivedPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~IGetSkippedItemArray.html)
[IDerivedPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
