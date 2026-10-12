---
title: "Reverse Property (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "Reverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Reverse.html"
---

# Reverse Property (IProjectionCurveFeatureData)

Reverses the direction that the curve is projected.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim value As System.Boolean

instance.Reverse = value

value = instance.Reverse
```

### C#

```csharp
System.bool Reverse {get; set;}
```

### C++/CLI

```cpp
property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of this projected curve, false to not

## VBA Syntax

See [ProjectionCurveFeatureData::Reverse](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData~Reverse.html).

## Examples

See the [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html) example.

## Remarks

If all faces in [IProjectionCurveFeatureData::FaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.html) are on the same side with respect to [IProjectionCurveFeatureData::Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Sketch.html), then this property is ignored. The projection direction is calculated from the selected sketches and faces.

You can reverse the direction in which the curve is projected when the selected face wraps around the plane of the curve. For example, if the sketch being projected is surrounded by a cylindrical face, then two possible projections exist. If this property is set to true, the direction based on the normal vector of the sketch is reversed. The default direction is along the sketch normal.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
