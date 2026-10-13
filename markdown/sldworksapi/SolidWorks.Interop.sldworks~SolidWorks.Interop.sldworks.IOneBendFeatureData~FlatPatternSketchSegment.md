---
title: "FlatPatternSketchSegment Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "FlatPatternSketchSegment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegment.html"
---

# FlatPatternSketchSegment Property (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::FlatPatternSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FlatPatternSketchSegment As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As SketchSegment

value = instance.FlatPatternSketchSegment
```

### C#

```csharp
SketchSegment FlatPatternSketchSegment {get;}
```

### C++/CLI

```cpp
property SketchSegment^ FlatPatternSketchSegment {
   SketchSegment^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for this bend

## VBA Syntax

See [OneBendFeatureData::FlatPatternSketchSegment](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~FlatPatternSketchSegment.html).

## Remarks

The sketch segment is not calculated until the part is unfolded through the user interface or by [IModelDoc2::SetBendState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBendState.html) with BendState of swSMBendStateFlattened.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
