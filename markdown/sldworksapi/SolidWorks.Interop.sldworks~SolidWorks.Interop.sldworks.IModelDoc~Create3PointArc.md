---
title: "Create3PointArc Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "Create3PointArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Create3PointArc.html"
---

# Create3PointArc Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::Create3PointArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Create3PointArc.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Create3PointArc( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double, _
   ByVal P3x As System.Double, _
   ByVal P3y As System.Double, _
   ByVal P3z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim P3x As System.Double
Dim P3y As System.Double
Dim P3z As System.Double
Dim value As System.Boolean

value = instance.Create3PointArc(P1x, P1y, P1z, P2x, P2y, P2z, P3x, P3y, P3z)
```

### C#

```csharp
System.bool Create3PointArc(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.double P3x,
   System.double P3y,
   System.double P3z
)
```

### C++/CLI

```cpp
System.bool Create3PointArc(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.double P3x,
   System.double P3y,
   System.double P3z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1x`:
- `P1y`:
- `P1z`:
- `P2x`:
- `P2y`:
- `P2z`:
- `P3x`:
- `P3y`:
- `P3z`:

## VBA Syntax

See [ModelDoc::Create3PointArc](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~Create3PointArc.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
