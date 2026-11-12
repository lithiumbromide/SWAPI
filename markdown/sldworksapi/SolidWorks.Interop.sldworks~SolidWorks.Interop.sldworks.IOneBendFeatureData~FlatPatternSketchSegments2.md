---
title: "FlatPatternSketchSegments2 Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "FlatPatternSketchSegments2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments2.html"
---

# FlatPatternSketchSegments2 Property (IOneBendFeatureData)

Gets the sketch segments and bend lines for this bend.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FlatPatternSketchSegments2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Object

value = instance.FlatPatternSketchSegments2
```

### C#

```csharp
System.object FlatPatternSketchSegments2 {get;}
```

### C++/CLI

```cpp
property System.Object^ FlatPatternSketchSegments2 {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)s

## VBA Syntax

See [OneBendFeatureData::FlatPatternSketchSegments2](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~FlatPatternSketchSegments2.html).

## Examples

[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)

## Remarks

The sketch segments are calculated in the flattened model. Before calling this method, flatten the model either by unsuppressing the flat pattern in the FeatureManager design tree or by calling [IModelDoc2::SetBendState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBendState.html) to set BendState to [swSMBendState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html).swSMBendStateFlattened.

This property returns the bend lines for older parts that do not have flat patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::IFlatPatternSketchSegments2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.html)
[IOneBendFeatureData::GetFlatPatternSketchSegmentCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2.html)

## Availability

SOLIDWORKS 2012 SP02, Revision Number 20.2
