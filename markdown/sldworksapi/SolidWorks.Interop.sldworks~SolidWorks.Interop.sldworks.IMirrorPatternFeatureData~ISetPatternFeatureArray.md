---
title: "ISetPatternFeatureArray Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "ISetPatternFeatureArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetPatternFeatureArray.html"
---

# ISetPatternFeatureArray Method (IMirrorPatternFeatureData)

Sets the seed features to use to create this mirror pattern feature.

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
Dim instance As IMirrorPatternFeatureData
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

- `FeatCount`: Number of seed features to use to create this mirror pattern
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) that to use as seed feature to create the mirror pattern

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetPatternFeatureCount.html)
[IMirrorPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetPatternFeatureArray.html)
[IMirrorPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~PatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
