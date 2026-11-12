---
title: "ICreatePlaneFixed Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreatePlaneFixed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed.html"
---

# ICreatePlaneFixed Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreatePlaneFixed2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreatePlaneFixed( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal UseGlobal As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim UseGlobal As System.Boolean

instance.ICreatePlaneFixed(P1, P2, P3, UseGlobal)
```

### C#

```csharp
void ICreatePlaneFixed(
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.bool UseGlobal
)
```

### C++/CLI

```cpp
void ICreatePlaneFixed(
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.bool UseGlobal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:
- `P3`:
- `UseGlobal`:

## VBA Syntax

See [ModelDoc2::ICreatePlaneFixed](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreatePlaneFixed.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
