---
title: "ICreateCircleByRadius Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateCircleByRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCircleByRadius.html"
---

# ICreateCircleByRadius Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreateCircleByRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateCircleByRadius2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateCircleByRadius( _
   ByRef P1 As System.Double, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Double
Dim Radius As System.Double

instance.ICreateCircleByRadius(P1, Radius)
```

### C#

```csharp
void ICreateCircleByRadius(
   ref System.double P1,
   System.double Radius
)
```

### C++/CLI

```cpp
void ICreateCircleByRadius(
   System.double% P1,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `Radius`:

## VBA Syntax

See [ModelDoc2::ICreateCircleByRadius](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateCircleByRadius.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
