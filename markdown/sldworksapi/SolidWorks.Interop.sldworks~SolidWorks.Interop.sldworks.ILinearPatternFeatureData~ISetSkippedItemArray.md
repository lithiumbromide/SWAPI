---
title: "ISetSkippedItemArray Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "ISetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetSkippedItemArray.html"
---

# ISetSkippedItemArray Method (ILinearPatternFeatureData)

Sets the list of items skipped for this linear pattern feature.

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
Dim instance As ILinearPatternFeatureData
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

- `FeatCount`: Number of instances to skip
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of skipped instances of size FeatCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetSkippedItemCount.html)
[ILinearPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetSkippedItemArray.html)
[ILinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
