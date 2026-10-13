---
title: "IFlatPatternSketchSegments2 Method (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "IFlatPatternSketchSegments2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.html"
---

# IFlatPatternSketchSegments2 Method (IOneBendFeatureData)

Gets the sketch segments and bend lines for this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFlatPatternSketchSegments2( _
   ByVal SegmentsCount As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim SegmentsCount As System.Integer
Dim value As SketchSegment

value = instance.IFlatPatternSketchSegments2(SegmentsCount)
```

### C#

```csharp
SketchSegment IFlatPatternSketchSegments2(
   System.int SegmentsCount
)
```

### C++/CLI

```cpp
SketchSegment^ IFlatPatternSketchSegments2(
   System.int SegmentsCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SegmentsCount`: Number of sketch segments (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call

[IOneBendFeatureData::GetFlatPatternSketchSegmentCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2.html) to populate SegmentsCount.

The sketch segments are calculated in the flattened model. Before calling this method, flatten the model either by unsuppressing the flat pattern in the FeatureManager design tree or by calling [IModelDoc2::SetBendState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBendState.html) to set BendState to [swSMBendState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html).swSMBendStateFlattened.

This property returns the bend lines for older parts that do not have flat patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::FlatPatternSketchSegments2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments2.html)

## Availability

SOLIDWORKS 2012 SP02, Revision Number 20.2
