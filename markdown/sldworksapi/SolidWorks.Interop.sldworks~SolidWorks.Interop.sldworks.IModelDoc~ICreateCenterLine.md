---
title: "ICreateCenterLine Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateCenterLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateCenterLine.html"
---

# ICreateCenterLine Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateCenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateCenterLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateCenterLine( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim P1 As System.Double
Dim P2 As System.Double

instance.ICreateCenterLine(P1, P2)
```

### C#

```csharp
void ICreateCenterLine(
   ref System.double P1,
   ref System.double P2
)
```

### C++/CLI

```cpp
void ICreateCenterLine(
   System.double% P1,
   System.double% P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:

## VBA Syntax

See [ModelDoc::ICreateCenterLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateCenterLine.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
