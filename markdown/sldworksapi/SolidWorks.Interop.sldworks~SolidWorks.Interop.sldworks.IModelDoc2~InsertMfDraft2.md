---
title: "InsertMfDraft2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertMfDraft2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMfDraft2.html"
---

# InsertMfDraft2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertMultifaceDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMultiFaceDraft.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertMfDraft2( _
   ByVal Angle As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal IsEdgeDraft As System.Boolean, _
   ByVal PropType As System.Integer, _
   ByVal StepDraft As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Angle As System.Double
Dim FlipDir As System.Boolean
Dim IsEdgeDraft As System.Boolean
Dim PropType As System.Integer
Dim StepDraft As System.Boolean

instance.InsertMfDraft2(Angle, FlipDir, IsEdgeDraft, PropType, StepDraft)
```

### C#

```csharp
void InsertMfDraft2(
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType,
   System.bool StepDraft
)
```

### C++/CLI

```cpp
void InsertMfDraft2(
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType,
   System.bool StepDraft
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `FlipDir`:
- `IsEdgeDraft`:
- `PropType`:
- `StepDraft`:

## VBA Syntax

See [ModelDoc2::InsertMfDraft2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertMfDraft2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
