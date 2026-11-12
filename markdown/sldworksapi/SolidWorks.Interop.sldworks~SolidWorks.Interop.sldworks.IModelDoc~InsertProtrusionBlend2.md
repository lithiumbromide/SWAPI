---
title: "InsertProtrusionBlend2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertProtrusionBlend2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertProtrusionBlend2.html"
---

# InsertProtrusionBlend2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertProtrusionBlend2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertProtrusionBlend2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertProtrusionBlend2( _
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

instance.InsertProtrusionBlend2(Closed, KeepTangency, ForceNonRational)
```

### C#

```csharp
void InsertProtrusionBlend2(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

### C++/CLI

```cpp
void InsertProtrusionBlend2(
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

See [ModelDoc::InsertProtrusionBlend2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertProtrusionBlend2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
