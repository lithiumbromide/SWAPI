---
title: "InsertCutSurface Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertCutSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCutSurface.html"
---

# InsertCutSurface Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertCutSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCutSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCutSurface( _
   ByVal Flip As System.Boolean, _
   ByVal KeepPieceIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Flip As System.Boolean
Dim KeepPieceIndex As System.Integer

instance.InsertCutSurface(Flip, KeepPieceIndex)
```

### C#

```csharp
void InsertCutSurface(
   System.bool Flip,
   System.int KeepPieceIndex
)
```

### C++/CLI

```cpp
void InsertCutSurface(
   System.bool Flip,
   System.int KeepPieceIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flip`:
- `KeepPieceIndex`:

## VBA Syntax

See [ModelDoc::InsertCutSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertCutSurface.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
