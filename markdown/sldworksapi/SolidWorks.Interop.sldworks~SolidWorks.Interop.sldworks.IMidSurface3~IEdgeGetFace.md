---
title: "IEdgeGetFace Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "IEdgeGetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IEdgeGetFace.html"
---

# IEdgeGetFace Method (IMidSurface3)

Gets the body face on which the specified midsurface edge lies.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEdgeGetFace( _
   ByVal EdgeInDisp As Edge _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim EdgeInDisp As Edge
Dim value As Face2

value = instance.IEdgeGetFace(EdgeInDisp)
```

### C#

```csharp
Face2 IEdgeGetFace(
   Edge EdgeInDisp
)
```

### C++/CLI

```cpp
Face2^ IEdgeGetFace(
   Edge^ EdgeInDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeInDisp`: Midsurface [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original solid body

## VBA Syntax

See [MidSurface3::IEdgeGetFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~IEdgeGetFace.html).

## Remarks

This condition occurs when a reference surface extends to meet one of the faces on the original part body. If the edge specified does not lie on one of the original part body faces, then a NULL is returned.

This edge is not topologically related to the face returned.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::EdgeGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~EdgeGetFace.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
