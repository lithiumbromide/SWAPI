---
title: "GetFlatPatternSketchSegmentCount2 Method (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "GetFlatPatternSketchSegmentCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2.html"
---

# GetFlatPatternSketchSegmentCount2 Method (IOneBendFeatureData)

Gets the number of sketch segments, including bend lines, in this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlatPatternSketchSegmentCount2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

value = instance.GetFlatPatternSketchSegmentCount2()
```

### C#

```csharp
System.int GetFlatPatternSketchSegmentCount2()
```

### C++/CLI

```cpp
System.int GetFlatPatternSketchSegmentCount2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch segments in this bend

## VBA Syntax

See [OneBendFeatureData::GetFlatPatternSketchSegmentCount2](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~GetFlatPatternSketchSegmentCount2.html).

## Examples

[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)

## Remarks

Call this method to populate SegmentsCount in [IOneBendFeatureData::IFlatPatternSketchSegments2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::FlatPatternSketchSegments2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments2.html)

## Availability

SOLIDWORKS 2012 SP02, Revision Number 20.2
