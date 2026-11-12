---
title: "ISetSkippedItemArray Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "ISetSkippedItemArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetSkippedItemArray.html"
---

# ISetSkippedItemArray Method (ICurveDrivenPatternFeatureData)

Sets the list of skipped items for this curve-driven pattern feature.

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
Dim instance As ICurveDrivenPatternFeatureData
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

- `FeatCount`: Number of skipped features
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of skipped items of size FeatCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetSkippedItemCount.html)
[ICurveDrivenPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetSkippedItemArray.html)
[ICurveDrivenPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
