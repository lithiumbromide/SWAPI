---
title: "ISetPatternFeatureArray Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "ISetPatternFeatureArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFeatureArray.html"
---

# ISetPatternFeatureArray Method (ICurveDrivenPatternFeatureData)

Sets the list of pattern features for this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPatternFeatureArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Object

instance.ISetPatternFeatureArray(FeatCount, ArrayDataIn)
```

### C#

```csharp
void ISetPatternFeatureArray(
   System.int FeatCount,
   ref System.object ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetPatternFeatureArray(
   System.int FeatCount,
   System.Object^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatCount`: Number of pattern features
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of pattern features of size FeatCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetPatternFeatureCount.html)
[ICurveDrivenPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFeatureArray.html)
[ICurveDrivenPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFeatureArray.html)
[ICurveDrivenPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
