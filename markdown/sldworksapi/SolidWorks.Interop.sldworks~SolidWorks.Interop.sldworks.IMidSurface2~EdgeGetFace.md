---
title: "EdgeGetFace Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "EdgeGetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~EdgeGetFace.html"
---

# EdgeGetFace Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::EdgeGetFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~EdgeGetFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EdgeGetFace( _
   ByVal EdgeInDisp As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim EdgeInDisp As System.Object
Dim value As System.Object

value = instance.EdgeGetFace(EdgeInDisp)
```

### C#

```csharp
System.object EdgeGetFace(
   System.object EdgeInDisp
)
```

### C++/CLI

```cpp
System.Object^ EdgeGetFace(
   System.Object^ EdgeInDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeInDisp`: Midsurface [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the original solid body

## VBA Syntax

See [MidSurface2::EdgeGetFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~EdgeGetFace.html).

## Remarks

This condition occurs when a reference surface extends to meet one of the faces on the original part body. If the edge specified does not lie on one of the original part body faces, then a NULL is returned.

This edge is not topologically related to the face returned.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::IEdgeGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IEdgeGetFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
