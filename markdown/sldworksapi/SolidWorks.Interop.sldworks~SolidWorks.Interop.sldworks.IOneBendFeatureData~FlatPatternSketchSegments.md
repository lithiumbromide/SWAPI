---
title: "FlatPatternSketchSegments Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "FlatPatternSketchSegments"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.html"
---

# FlatPatternSketchSegments Property (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::FlatPatternSketchSegments2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FlatPatternSketchSegments As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Object

value = instance.FlatPatternSketchSegments
```

### C#

```csharp
System.object FlatPatternSketchSegments {get;}
```

### C++/CLI

```cpp
property System.Object^ FlatPatternSketchSegments {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)s

## VBA Syntax

See [OneBendFeatureData::FlatPatternSketchSegments](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~FlatPatternSketchSegments.html).

## Examples

[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get Names of Sketch Segments (VB.NET)](Get_Names_of_Sketch_Segments_Example_VBNET.htm)
[Get Names of Sketch Segments (C#)](Get_Names_of_Sketch_Segments_Example_CSharp.htm)

## Remarks

The sketch segments are calculated in the flattened model. Before calling this method, flatten the model either by un-suppressing the flat pattern in the FeatureManager design tree or by calling [IModelDoc2::SetBendState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBendState.html) to set BendState to [swSMBendState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html).swSMBendStateFlattened.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::IFlatPatternSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments.html)
[IOneBendFeatureData::GetFlatPatternSketchSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount.html)

## Availability

SOLIDWORKS 2011 SP02, Revision Number 19.2
