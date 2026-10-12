---
title: "GetClosestPointOn Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "GetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.html"
---

# GetClosestPointOn Method (IVertex)

Gets the closest point on the vertex using the X, Y, Z input point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.GetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.object GetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ GetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X value of the input point
- `Y`: Y value of the input point
- `Z`: Z value of the input point

### Return Value

Array of five doubles representing the X, Y, Z point on the vertex

## VBA Syntax

See [Vertex::GetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Vertex~GetClosestPointOn.html).

## Remarks

Because a vertex is a point, you should receive the X,Y,Z location for the actual vertex.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.html)
