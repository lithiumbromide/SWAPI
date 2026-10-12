---
title: "CreateCircleVB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateCircleVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircleVB.html"
---

# CreateCircleVB Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreateCircle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreateCircleVB( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim Radius As System.Double

instance.CreateCircleVB(P1x, P1y, P1z, Radius)
```

### C#

```csharp
void CreateCircleVB(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double Radius
)
```

### C++/CLI

```cpp
void CreateCircleVB(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1x`:
- `P1y`:
- `P1z`:
- `Radius`:

## VBA Syntax

See [ModelDoc2::CreateCircleVB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateCircleVB.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
