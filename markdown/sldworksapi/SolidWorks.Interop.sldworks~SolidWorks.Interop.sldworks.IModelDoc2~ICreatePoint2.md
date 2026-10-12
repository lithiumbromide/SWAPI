---
title: "ICreatePoint2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreatePoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePoint2.html"
---

# ICreatePoint2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreatePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreatePoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePoint2( _
   ByVal PointX As System.Double, _
   ByVal PointY As System.Double, _
   ByVal PointZ As System.Double _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim PointX As System.Double
Dim PointY As System.Double
Dim PointZ As System.Double
Dim value As SketchPoint

value = instance.ICreatePoint2(PointX, PointY, PointZ)
```

### C#

```csharp
SketchPoint ICreatePoint2(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

### C++/CLI

```cpp
SketchPoint^ ICreatePoint2(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointX`: X location of the point
- `PointY`: Y location of the point
- `PointZ`: Z location of the point; ignored for 2D sketches

### Return Value

Newly created [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html); this value is NULL if the operation fails

## VBA Syntax

See [ModelDoc2::ICreatePoint2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreatePoint2.html).

## Remarks

This method creates a point in the active 2D or 3D sketch. If a sketch is not active, the point is not created and NULL is returned. Use [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html) to check to see if the sketch is active.

[IModelDoc2::SetAddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAddToDB.html) and [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database. IModelDoc2::SetAddToDB also avoids inferencing.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreatePoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePoint2.html)
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
