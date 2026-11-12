---
title: "InsertCutBlend2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertCutBlend2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCutBlend2.html"
---

# InsertCutBlend2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertCutBlend2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCutBlend2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCutBlend2( _
   ByVal Closed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Closed As System.Boolean
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean

instance.InsertCutBlend2(Closed, KeepTangency, ForceNonRational)
```

### C#

```csharp
void InsertCutBlend2(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

### C++/CLI

```cpp
void InsertCutBlend2(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Closed`:
- `KeepTangency`:
- `ForceNonRational`:

## VBA Syntax

See [ModelDoc::InsertCutBlend2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertCutBlend2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
