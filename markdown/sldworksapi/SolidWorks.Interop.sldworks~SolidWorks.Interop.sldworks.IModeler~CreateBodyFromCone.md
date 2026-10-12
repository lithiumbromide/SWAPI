---
title: "CreateBodyFromCone Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateBodyFromCone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html"
---

# CreateBodyFromCone Method (IModeler)

Creates a temporary body from cone dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBodyFromCone( _
   ByVal ConeDimArray As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim ConeDimArray As System.Object
Dim value As System.Object

value = instance.CreateBodyFromCone(ConeDimArray)
```

### C#

```csharp
System.object CreateBodyFromCone(
   System.object ConeDimArray
)
```

### C++/CLI

```cpp
System.Object^ CreateBodyFromCone(
   System.Object^ ConeDimArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConeDimArray`: Array containing 9 doubles (see **Remarks**)

### Return Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateBodyFromCone](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateBodyFromCone.html).

## Examples

[Create Solid Bodies Using Geometry and Topology (C#)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_CSharp.htm)
[Create Solid Bodies Using Geometry and Topology (VB.NET)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_VBNET.htm)
[Create Solid Bodies Using Geometry and Topology (VBA)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_VB.htm)

## Remarks

The ConeArray argument is the following array of doubles:

[ coneFaceCenter[3], coneAxis[3], coneBaseRadius, coneTopRadius, coneHeight ]

where:

| coneFaceCenter[3] | XYZ location that represents the center of one of the cone faces |
| --- | --- |
| coneAxis[3] | XYZ direction; the cone is extruded along this vector from the coneFaceCenter location, a distance of coneHeight |
| coneBaseRadius | Cone radius at the coneFaceCenter plane |
| coneTopRadius | Cone radius at coneHeight from the coneFaceCenter along the axis |
| coneHeight | Length to extrude along the coneAxis direction; if coneHeight is 0, then a sheet body is created of dimension coneBaseRadius and normal is defined by coneAxis |

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)
