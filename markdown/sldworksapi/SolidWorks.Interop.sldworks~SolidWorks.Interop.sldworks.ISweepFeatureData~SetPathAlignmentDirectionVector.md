---
title: "SetPathAlignmentDirectionVector Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "SetPathAlignmentDirectionVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.html"
---

# SetPathAlignmentDirectionVector Method (ISweepFeatureData)

Sets the direction vector for path alignment in this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPathAlignmentDirectionVector( _
   ByVal Dir As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim Dir As System.Object

instance.SetPathAlignmentDirectionVector(Dir)
```

### C#

```csharp
void SetPathAlignmentDirectionVector(
   System.object Dir
)
```

### C++/CLI

```cpp
void SetPathAlignmentDirectionVector(
   System.Object^ Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Dir`: [Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [cylinder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), or a pair of [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) that defines the direction

## VBA Syntax

See [SweepFeatureData::SetPathAlignmentDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~SetPathAlignmentDirectionVector.html).

## Remarks

This method is valid only if:

- [ISweepFeatureData:TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlFollowPath.

- and -

- [ISweepFeatureData::PathAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html) is set to [swTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.html).swTangencyDirectionVector.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.html)
[ISweepFeatureData::Path Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.html)
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
