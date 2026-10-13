---
title: "EdgeGetFace Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "EdgeGetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~EdgeGetFace.html"
---

# EdgeGetFace Method (IMidSurface3)

Gets the body face on which the specified midsurface edge lies.

## Syntax

### Visual Basic (Declaration)

```vb
Function EdgeGetFace( _
   ByVal EdgeInDisp As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
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

See [MidSurface3::EdgeGetFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~EdgeGetFace.html).

## Remarks

This condition occurs when a reference surface extends to meet one of the faces on the original part body. If the edge specified does not lie on one of the original part body faces, then a null is returned.

This edge is not topologically related to the face returned.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::IEdgeGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IEdgeGetFace.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
