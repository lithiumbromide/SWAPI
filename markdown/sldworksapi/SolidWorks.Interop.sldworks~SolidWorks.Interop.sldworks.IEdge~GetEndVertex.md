---
title: "GetEndVertex Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetEndVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.html"
---

# GetEndVertex Method (IEdge)

Gets the ending vertex for this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndVertex() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Object

value = instance.GetEndVertex()
```

### C#

```csharp
System.object GetEndVertex()
```

### C++/CLI

```cpp
System.Object^ GetEndVertex();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Vertex

## VBA Syntax

See [Edge::GetEndVertex](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetEndVertex.html).

## Examples

[Check Interference Using IModeler::CheckInterfence (VBA)](Check_Interference_using_Modeler_CheckInterference_Example_VB.htm)
[Get Radius of Variable Radius Fillet (VBA)](Get_Radius_of_Variable_Radius_Fillet_Example_VB.htm)
[Get Vertex (VBA)](Get_Vertex_Example_VB.htm)
[Modify Fillet Weld Bead (VBA)](Modify_Fillet_Weld_Bead_Example_VB.htm)
[Modify Fillet Weld Bead (VB.NET)](Modify_Fillet_Weld_Bead_Example_VBNET.htm)
[Modify Fillet Weld Bead (C#)](Modify_Fillet_Weld_Bead_Example_CSharp.htm)

## Remarks

If no vertex exists for this edge (such as the edge of a newly created cylinder), then this method returns NULL.

This method and [IEdge::GetStartVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetStartVertex.html) or [IEdge::IGetStartVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetStartVertex.html) return distinct vertices, unless the edge is closed. Because edges have no natural direction, you cannot necessarily predict which of the two points you will get first and which last.

Use [ICoEdge::GetCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~GetCurveParams.html) or [ICoEdge::IGetCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~IGetCurveParams.html) to get consistent start and end positions.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IGetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.html)
[IEdge::GetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.html)
[IEdge::IGetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.html)
