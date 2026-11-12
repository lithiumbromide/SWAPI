---
title: "CreatePoint2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePoint2.html"
---

# CreatePoint2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreatePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreatePoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePoint2( _
   ByVal PointX As System.Double, _
   ByVal PointY As System.Double, _
   ByVal PointZ As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim PointX As System.Double
Dim PointY As System.Double
Dim PointZ As System.Double
Dim value As System.Object

value = instance.CreatePoint2(PointX, PointY, PointZ)
```

### C#

```csharp
System.object CreatePoint2(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

### C++/CLI

```cpp
System.Object^ CreatePoint2(
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

See [ModelDoc2::CreatePoint2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePoint2.html).

## Examples

[Calculate Closest Distance Between Model Components (VBA)](Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm)
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)
[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)

## Remarks

This method creates a point in the active 2D or 3D sketch. If a sketch is not active, the point is not created and NULL is returned. Use [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html) to check to see if the sketch is active.

[IModelDoc2::SetAddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAddToDB.html) and [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database. IModelDoc2::SetAddToDB also avoids inferencing.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ICreatePoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePoint2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
