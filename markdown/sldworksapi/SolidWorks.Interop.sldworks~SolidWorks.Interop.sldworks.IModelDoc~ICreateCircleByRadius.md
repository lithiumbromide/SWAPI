---
title: "ICreateCircleByRadius Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateCircleByRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateCircleByRadius.html"
---

# ICreateCircleByRadius Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateCircleByRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateCircleByRadius.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::ICreateCircleByRadius](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateCircleByRadius.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
