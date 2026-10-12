---
title: "ICreateWireBody Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateWireBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html"
---

# ICreateWireBody Method (IModeler)

Creates a wire body from the input entities, which can be edges or curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateWireBody( _
   ByVal Count As System.Integer, _
   ByRef EntArr As System.Object, _
   ByVal Option As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Count As System.Integer
Dim EntArr As System.Object
Dim Option As System.Integer
Dim value As Body2

value = instance.ICreateWireBody(Count, EntArr, Option)
```

### C#

```csharp
Body2 ICreateWireBody(
   System.int Count,
   ref System.object EntArr,
   System.int Option
)
```

### C++/CLI

```cpp
Body2^ ICreateWireBody(
   System.int Count,
   System.Object^% EntArr,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of input entities ([curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) or [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html))
- `EntArr`: Array of input entities ([curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) or [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html))
- `Option`: Option as defined in [swCreateWireBodyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateWireBodyOptions_e.html) (see **Remarks**)

## VBA Syntax

See [Modeler::ICreateWireBody](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateWireBody.html).

## Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, from shells.

The swCreateWireBodyMergeCurves option only works for curves with position and tangent continuity.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[ICurve::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateWireBody.html)
[IEdge::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~CreateWireBody.html)
[IImportedCurveFeatureData::SetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~SetBody.html)
[ISketchSegment::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::ICreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::ICreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::ICreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::ICreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::ICreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::IICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::IICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::IICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::IICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::IICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
