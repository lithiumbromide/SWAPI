---
title: "InsertMfDraft Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertMfDraft"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertMfDraft.html"
---

# InsertMfDraft Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertMfDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertMfDraft.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertMfDraft( _
   ByVal Angle As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal IsEdgeDraft As System.Boolean, _
   ByVal PropType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Angle As System.Double
Dim FlipDir As System.Boolean
Dim IsEdgeDraft As System.Boolean
Dim PropType As System.Integer

instance.InsertMfDraft(Angle, FlipDir, IsEdgeDraft, PropType)
```

### C#

```csharp
void InsertMfDraft(
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType
)
```

### C++/CLI

```cpp
void InsertMfDraft(
   System.double Angle,
   System.bool FlipDir,
   System.bool IsEdgeDraft,
   System.int PropType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `FlipDir`:
- `IsEdgeDraft`:
- `PropType`:

## VBA Syntax

See [ModelDoc::InsertMfDraft](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertMfDraft.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
