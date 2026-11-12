---
title: "InsertRadiateSurface Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertRadiateSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertRadiateSurface.html"
---

# InsertRadiateSurface Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertRadiateSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertRadiateSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRadiateSurface( _
   ByVal Distance As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal TangentPropagate As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Distance As System.Double
Dim FlipDir As System.Boolean
Dim TangentPropagate As System.Boolean

instance.InsertRadiateSurface(Distance, FlipDir, TangentPropagate)
```

### C#

```csharp
void InsertRadiateSurface(
   System.double Distance,
   System.bool FlipDir,
   System.bool TangentPropagate
)
```

### C++/CLI

```cpp
void InsertRadiateSurface(
   System.double Distance,
   System.bool FlipDir,
   System.bool TangentPropagate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Distance`:
- `FlipDir`:
- `TangentPropagate`:

## VBA Syntax

See [ModelDoc::InsertRadiateSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertRadiateSurface.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
