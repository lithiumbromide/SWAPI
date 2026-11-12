---
title: "ICreateLine Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateLine.html"
---

# ICreateLine Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateLine2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateLine( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double

instance.ICreateLine(P1, P2)
```

### C#

```csharp
void ICreateLine(
   ref System.double P1,
   ref System.double P2
)
```

### C++/CLI

```cpp
void ICreateLine(
   System.double% P1,
   System.double% P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:

## VBA Syntax

See [ModelDoc2::ICreateLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateLine.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
