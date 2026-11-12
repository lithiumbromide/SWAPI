---
title: "InsertCutBlend2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCutBlend2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCutBlend2.html"
---

# InsertCutBlend2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertCutBlend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutBlend.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::InsertCutBlend2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCutBlend2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
