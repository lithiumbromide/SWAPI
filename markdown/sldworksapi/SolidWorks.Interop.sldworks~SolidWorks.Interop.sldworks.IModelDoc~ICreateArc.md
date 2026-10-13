---
title: "ICreateArc Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateArc.html"
---

# ICreateArc Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateArc.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::ICreateArc](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateArc.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
