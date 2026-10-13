---
title: "SetDraftWhileExtruding Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetDraftWhileExtruding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetDraftWhileExtruding.html"
---

# SetDraftWhileExtruding Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetDraftWhileExtruding](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftWhileExtruding( _
   ByVal Forward As System.Boolean, _
   ByVal DraftWhileExtrude As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim DraftWhileExtrude As System.Boolean

instance.SetDraftWhileExtruding(Forward, DraftWhileExtrude)
```

### C#

```csharp
void SetDraftWhileExtruding(
   System.bool Forward,
   System.bool DraftWhileExtrude
)
```

### C++/CLI

```cpp
void SetDraftWhileExtruding(
   System.bool Forward,
   System.bool DraftWhileExtrude
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `DraftWhileExtrude`:

## VBA Syntax

See [ExtrudeFeatureData::SetDraftWhileExtruding](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetDraftWhileExtruding.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
