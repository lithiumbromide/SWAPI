---
title: "ICreateArc Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc.html"
---

# ICreateArc Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreateArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateArc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateArc( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal Dir As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim Dir As System.Short

instance.ICreateArc(P1, P2, P3, Dir)
```

### C#

```csharp
void ICreateArc(
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.short Dir
)
```

### C++/CLI

```cpp
void ICreateArc(
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.short Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:
- `P3`:
- `Dir`:

## VBA Syntax

See [ModelDoc2::ICreateArc](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateArc.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
