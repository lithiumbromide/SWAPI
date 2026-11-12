---
title: "ICreateBrepBody Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBrepBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody.html"
---

# ICreateBrepBody Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBrepBody3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBrepBody( _
   ByVal Type As System.Integer, _
   ByVal NTopologies As System.Integer, _
   ByRef Topologies As System.Integer, _
   ByRef EdgeTolArray As System.Double, _
   ByRef VertexTolArray As System.Double, _
   ByRef PointArray As System.Double, _
   ByRef CurveArray As Curve, _
   ByRef SurfaceArray As Surface, _
   ByVal NRelations As System.Integer, _
   ByRef Parents As System.Integer, _
   ByRef Children As System.Integer, _
   ByRef Senses As System.Integer _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Type As System.Integer
Dim NTopologies As System.Integer
Dim Topologies As System.Integer
Dim EdgeTolArray As System.Double
Dim VertexTolArray As System.Double
Dim PointArray As System.Double
Dim CurveArray As Curve
Dim SurfaceArray As Surface
Dim NRelations As System.Integer
Dim Parents As System.Integer
Dim Children As System.Integer
Dim Senses As System.Integer
Dim value As Body

value = instance.ICreateBrepBody(Type, NTopologies, Topologies, EdgeTolArray, VertexTolArray, PointArray, CurveArray, SurfaceArray, NRelations, Parents, Children, Senses)
```

### C#

```csharp
Body ICreateBrepBody(
   System.int Type,
   System.int NTopologies,
   ref System.int Topologies,
   ref System.double EdgeTolArray,
   ref System.double VertexTolArray,
   ref System.double PointArray,
   ref Curve CurveArray,
   ref Surface SurfaceArray,
   System.int NRelations,
   ref System.int Parents,
   ref System.int Children,
   ref System.int Senses
)
```

### C++/CLI

```cpp
Body^ ICreateBrepBody(
   System.int Type,
   System.int NTopologies,
   System.int% Topologies,
   System.double% EdgeTolArray,
   System.double% VertexTolArray,
   System.double% PointArray,
   Curve^% CurveArray,
   Surface^% SurfaceArray,
   System.int NRelations,
   System.int% Parents,
   System.int% Children,
   System.int% Senses
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`:
- `NTopologies`:
- `Topologies`:
- `EdgeTolArray`:
- `VertexTolArray`:
- `PointArray`:
- `CurveArray`:
- `SurfaceArray`:
- `NRelations`:
- `Parents`:
- `Children`:
- `Senses`:

## VBA Syntax

See [Modeler::ICreateBrepBody](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBrepBody.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
