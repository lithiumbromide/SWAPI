---
title: "CreateTangentArc2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateTangentArc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateTangentArc2.html"
---

# CreateTangentArc2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateTangentArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateTangentArc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTangentArc2( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double, _
   ByVal ArcTypeIn As System.Integer _
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
Dim ArcTypeIn As System.Integer
Dim value As System.Boolean

value = instance.CreateTangentArc2(P1x, P1y, P1z, P2x, P2y, P2z, ArcTypeIn)
```

### C#

```csharp
System.bool CreateTangentArc2(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.int ArcTypeIn
)
```

### C++/CLI

```cpp
System.bool CreateTangentArc2(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.int ArcTypeIn
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
- `ArcTypeIn`:

## VBA Syntax

See [ModelDoc::CreateTangentArc2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateTangentArc2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
