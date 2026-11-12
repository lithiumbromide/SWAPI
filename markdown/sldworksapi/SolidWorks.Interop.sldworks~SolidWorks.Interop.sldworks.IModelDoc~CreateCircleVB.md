---
title: "CreateCircleVB Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircleVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircleVB.html"
---

# CreateCircleVB Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircleVB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircleVB.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::CreateCircleVB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircleVB.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
