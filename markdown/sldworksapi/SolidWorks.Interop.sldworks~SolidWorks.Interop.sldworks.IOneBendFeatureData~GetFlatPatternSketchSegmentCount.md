---
title: "GetFlatPatternSketchSegmentCount Method (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "GetFlatPatternSketchSegmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount.html"
---

# GetFlatPatternSketchSegmentCount Method (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::GetFlatPatternSketchSegmentCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlatPatternSketchSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

value = instance.GetFlatPatternSketchSegmentCount()
```

### C#

```csharp
System.int GetFlatPatternSketchSegmentCount()
```

### C++/CLI

```cpp
System.int GetFlatPatternSketchSegmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch segments

## VBA Syntax

See [OneBendFeatureData::GetFlatPatternSketchSegmentCount](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~GetFlatPatternSketchSegmentCount.html).

## Remarks

Call this method to populate SegmentsCount in [IOneBendFeatureData::IFlatPatternSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::FlatPatternSketchSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.html)

## Availability

SOLIDWORKS 2011 SP02, Revision Number 19.2
