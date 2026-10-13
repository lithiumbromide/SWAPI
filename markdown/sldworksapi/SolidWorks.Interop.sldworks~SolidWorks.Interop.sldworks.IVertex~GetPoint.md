---
title: "GetPoint Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "GetPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetPoint.html"
---

# GetPoint Method (IVertex)

Gets the point corresponding to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPoint() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As System.Object

value = instance.GetPoint()
```

### C#

```csharp
System.object GetPoint()
```

### C++/CLI

```cpp
System.Object^ GetPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of three doubles representing the x, y, and z coordinates of the point

## VBA Syntax

See [Vertex::GetPoint](ms-its:sldworksapivb6.chm::/sldworks~Vertex~GetPoint.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)
[Get Vertex (VBA)](Get_Vertex_Example_VB.htm)
[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::IGetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetPoint.html)
