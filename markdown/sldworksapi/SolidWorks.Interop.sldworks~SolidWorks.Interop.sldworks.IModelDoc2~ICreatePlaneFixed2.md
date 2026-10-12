---
title: "ICreatePlaneFixed2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreatePlaneFixed2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2.html"
---

# ICreatePlaneFixed2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertRefPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRefPlane.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlaneFixed2( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal UseGlobal As System.Boolean _
) As RefPlane
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim UseGlobal As System.Boolean
Dim value As RefPlane

value = instance.ICreatePlaneFixed2(P1, P2, P3, UseGlobal)
```

### C#

```csharp
RefPlane ICreatePlaneFixed2(
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.bool UseGlobal
)
```

### C++/CLI

```cpp
RefPlane^ ICreatePlaneFixed2(
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.bool UseGlobal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`: Array of 3 doubles (x, y, z) in meters; this is the first of three model-space points used to define the plane orientation; it is also used as the origin for the plane coordinate system
- `P2`: Array of 3 doubles (x, y, z) in meters; this is the second of three model-space points used to define the plane orientation; the planes X-axis is directed from P1 to P2 unless useGlobal is set to True
- `P3`: Array of 3 doubles (x, y, z) in meters; this is the final model-space point used to define the plane orientation
- `UseGlobal`: Controls x-axis orientation (see **Remarks**)

### Return Value

Newly created [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) or NULL if the creation of the plan fails

## VBA Syntax

See [ModelDoc2::ICreatePlaneFixed2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreatePlaneFixed2.html).

## Remarks

The resulting plane is not parametric.

The planes normal vector is calculated using the cross product of the vectors (P2 - P1) and (P3 - P1), respectively.

The x-axis of the planes' coordinate system are a vector from P1 to P2 or a vector projected from the x-axis of the global coordinate system onto the plane.

The useGlobal argument denotes whether to align the x-axis of the plane with global orientation.

| If useGlobal... | Then x-axis of the... |
| --- | --- |
| True | global (model) coordinate system is projected onto the plane. That vector is used to determine the direction of the plane's x-axis. This does not reorient the plane. Instead, it rotates the plane coordinate system about P1 until the x-axis of the plane aligns with the projected vector. P1, P2, and P3 are still required because they define the plane. |
| false | plane is aligned based on your input points, P1 and P2. |

This method creates the plane in the model that is currently being edited. This behavior is consistent with the other plane creation APIs, but it is different from the original IModelDoc2::ICreatePlaneFixed, which created the plane in this model, regardless of whether a component was currently being edited.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.html)
[IModelDoc2::CreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.html)
[IModelDoc2::CreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface3.html)
[IModelDoc2::CreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.html)
[IModelDoc2::CreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThru3Points3.html)
[IModelDoc2::CreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruLineAndPt.html)
[IModelDoc2::CreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::GetVisibilityOfConstructPlanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetVisibilityOfConstructPlanes.html)
[IModelDoc2::ICreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.html)
[IModelDoc2::ICreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.html)
[IModelDoc2::ICreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.html)
[IModelDoc2::ICreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::ICreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3.html)
[IModelDoc2::ICreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruLineAndPt.html)
[IModelDoc2::ICreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::ViewDispRefplanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDispRefplanes.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
