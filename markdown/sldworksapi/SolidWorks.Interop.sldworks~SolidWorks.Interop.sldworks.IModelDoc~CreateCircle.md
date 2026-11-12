---
title: "CreateCircle Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircle.html"
---

# CreateCircle Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircle( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double _
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
Dim value As System.Boolean

value = instance.CreateCircle(P1x, P1y, P1z, P2x, P2y, P2z)
```

### C#

```csharp
System.bool CreateCircle(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
)
```

### C++/CLI

```cpp
System.bool CreateCircle(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
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

## VBA Syntax

See [ModelDoc::CreateCircle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircle.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
