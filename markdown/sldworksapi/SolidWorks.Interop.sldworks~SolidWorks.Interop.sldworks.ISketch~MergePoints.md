---
title: "MergePoints Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "MergePoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.html"
---

# MergePoints Method (ISketch)

Merges sketch points within a specified distance.

## Syntax

### Visual Basic (Declaration)

```vb
Function MergePoints( _
   ByVal Distance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Distance As System.Double
Dim value As System.Boolean

value = instance.MergePoints(Distance)
```

### C#

```csharp
System.bool MergePoints(
   System.double Distance
)
```

### C++/CLI

```cpp
System.bool MergePoints(
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Distance`: Distance at which points are considered coincident

### Return Value

True if successful, false if not

## VBA Syntax

See [Sketch::MergePoints](ms-its:sldworksapivb6.chm::/sldworks~Sketch~MergePoints.html).

## Remarks

This method requires that only one open contour exists in the sketch. To specify a distance below which points are automatically merged while creating the segments, use [ISketchRelationManager::AddRelation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~AddRelation.html) or [ISketchRelationManager::IAddRelation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~IAddRelation.html) and swConstraintType_COINCIDENT.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2.html)
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.html)
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
