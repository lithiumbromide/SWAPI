---
title: "GetPathAlignmentDirectionVector Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetPathAlignmentDirectionVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.html"
---

# GetPathAlignmentDirectionVector Method (ISweepFeatureData)

Gets the direction vector of the specified type for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathAlignmentDirectionVector( _
   ByRef Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim Type As System.Integer
Dim value As System.Object

value = instance.GetPathAlignmentDirectionVector(Type)
```

### C#

```csharp
System.object GetPathAlignmentDirectionVector(
   out System.int Type
)
```

### C++/CLI

```cpp
System.Object^ GetPathAlignmentDirectionVector(
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of direction vector as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

  - swSelDATAMAXES (axis)
  - swSelDATUMPLANES (plane)
  - swSelEDGES (edge)
  - swSelFACES (face)

### Return Value

[Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [cylinder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), or a pair of [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) that defines the direction

## VBA Syntax

See [SweepFeatureData::GetPathAlignmentDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetPathAlignmentDirectionVector.html).

## Remarks

This method is valid only if:

- [ISweepFeatureData:TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlFollowPath.

- and -

- [ISweepFeatureData::PathAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html) is set to [swTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.html).swTangencyDirectionVector.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::SetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.html)
[ISweepFeatureData::PathAlignmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html)
[ISweepFeatureData::Path Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.html)
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
