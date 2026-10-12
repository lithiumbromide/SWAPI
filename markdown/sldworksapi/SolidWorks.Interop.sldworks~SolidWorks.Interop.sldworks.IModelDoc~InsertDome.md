---
title: "InsertDome Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertDome"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertDome.html"
---

# InsertDome Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertDome](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertDome.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertDome( _
   ByVal Height As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal DoEllipticSurface As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Height As System.Double
Dim ReverseDir As System.Boolean
Dim DoEllipticSurface As System.Boolean

instance.InsertDome(Height, ReverseDir, DoEllipticSurface)
```

### C#

```csharp
void InsertDome(
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
)
```

### C++/CLI

```cpp
void InsertDome(
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Height`:
- `ReverseDir`:
- `DoEllipticSurface`:

## VBA Syntax

See [ModelDoc::InsertDome](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertDome.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
