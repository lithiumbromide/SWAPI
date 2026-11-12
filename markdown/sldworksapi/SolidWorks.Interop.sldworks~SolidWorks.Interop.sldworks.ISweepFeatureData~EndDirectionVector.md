---
title: "EndDirectionVector Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "EndDirectionVector"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndDirectionVector.html"
---

# EndDirectionVector Property (ISweepFeatureData)

Obsolete. Gets or sets the direction vector in which to end this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndDirectionVector As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Object

instance.EndDirectionVector = value

value = instance.EndDirectionVector
```

### C#

```csharp
System.object EndDirectionVector {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EndDirectionVector {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [cylinder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), or a pair of [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) that defines the direction

## VBA Syntax

See [SweepFeatureData::EndDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~EndDirectionVector.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::StartDirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartDirectionVector.html)
[ISweepFeatureData::GetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.html)
[ISweepFeatureData::SetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.html)
[ISweepFeatureData::PathAlignmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html)
[ISweepFeatureData::Path Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.html)
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
