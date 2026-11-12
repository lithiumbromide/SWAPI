---
title: "IFlatPatternSketchSegments Method (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "IFlatPatternSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments.html"
---

# IFlatPatternSketchSegments Method (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::IFlatPatternSketchSegments2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFlatPatternSketchSegments( _
   ByVal SegmentsCount As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim SegmentsCount As System.Integer
Dim value As SketchSegment

value = instance.IFlatPatternSketchSegments(SegmentsCount)
```

### C#

```csharp
SketchSegment IFlatPatternSketchSegments(
   System.int SegmentsCount
)
```

### C++/CLI

```cpp
SketchSegment^ IFlatPatternSketchSegments(
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

Before calling this method, call [IOneBendFeatureData::GetFlatPatternSketchSegmentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount.html) to populate SegmentsCount.

The sketch segments are calculated in the flattened model. Before calling this method, flatten the model either by un-suppressing the flat pattern in the FeatureManager design tree or by calling [IModelDoc2::SetBendState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBendState.html) to set BendState to [swSMBendState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html).swSMBendStateFlattened.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::FlatPatternSketchSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.html)

## Availability

SOLIDWORKS 2011 SP02, Revision Number 19.2
