---
title: "ICreateBodyFromCyl2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromCyl2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html"
---

# ICreateBodyFromCyl2 Method (IModeler)

Creates a temporary body from cylinder dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromCyl2( _
   ByRef CylDimArray As System.Double _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim CylDimArray As System.Double
Dim value As Body2

value = instance.ICreateBodyFromCyl2(CylDimArray)
```

### C#

```csharp
Body2 ICreateBodyFromCyl2(
   ref System.double CylDimArray
)
```

### C++/CLI

```cpp
Body2^ ICreateBodyFromCyl2(
   System.double% CylDimArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CylDimArray`: Array containing 8 doubles (see **Remarks**)

## VBA Syntax

See [Modeler::ICreateBodyFromCyl2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromCyl2.html).

## Remarks

TheCylArray argument is the following array of doubles:

[ cylFaceCenter[3], cylAxis[3], cylRadius, cylHeight ]

where:

| cylFaceCenter[3] | XYZ location that represents the center of one of the cylinder faces |
| --- | --- |
| cylAxis[3] | XYZ direction; the cylinder is extruded along this vector from the cylFaceCenter location for a distance of cylHeight |
| cylRadius | Cylinder radius |
| cylHeight | Length to extrude along the cylAxis direction; if cylHeight is 0, then a sheet body is created of dimension cylRadius and whose normal is defined by cylAxis |

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
