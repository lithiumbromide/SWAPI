---
title: "GetBodyOutline Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "GetBodyOutline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline.html"
---

# GetBodyOutline Method (IModeler)

Obsolete. Superseded by [IModeler::GetBodyOutline2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~GetBodyOutline2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyOutline( _
   ByVal BodyVar As System.Object, _
   ByVal Direction As MathVector, _
   ByVal Tolerance As System.Double, _
   ByRef CurvesOut As System.Object, _
   ByRef TopolEntities As System.Object, _
   ByRef Outline As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim BodyVar As System.Object
Dim Direction As MathVector
Dim Tolerance As System.Double
Dim CurvesOut As System.Object
Dim TopolEntities As System.Object
Dim Outline As System.Object
Dim value As System.Integer

value = instance.GetBodyOutline(BodyVar, Direction, Tolerance, CurvesOut, TopolEntities, Outline)
```

### C#

```csharp
System.int GetBodyOutline(
   System.object BodyVar,
   MathVector Direction,
   System.double Tolerance,
   out System.object CurvesOut,
   out System.object TopolEntities,
   out System.object Outline
)
```

### C++/CLI

```cpp
System.int GetBodyOutline(
   System.Object^ BodyVar,
   MathVector^ Direction,
   System.double Tolerance,
   [Out] System.Object^ CurvesOut,
   [Out] System.Object^ TopolEntities,
   [Out] System.Object^ Outline
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyVar`: Array of bodies
- `Direction`: Direction of view
- `Tolerance`: Tolerance (Parasolid default 0.00001)
- `CurvesOut`: Array of 3D trimmed curves that form the outline
- `TopolEntities`: Array of topological entities associated with the outline
- `Outline`: Array of integers indicating which curves belong to which outline

### Return Value

Number of curves that form the outline of a body

## VBA Syntax

See [Modeler::GetBodyOutline](ms-its:sldworksapivb6.chm::/sldworks~Modeler~GetBodyOutline.html).

## Remarks

See Parasolid's documentation of PK_BODY_make_curves_outline for more information about the output.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
