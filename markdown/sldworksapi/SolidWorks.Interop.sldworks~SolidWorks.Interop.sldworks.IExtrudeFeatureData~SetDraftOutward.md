---
title: "SetDraftOutward Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetDraftOutward"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetDraftOutward.html"
---

# SetDraftOutward Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetDraftOutward](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftOutward( _
   ByVal Forward As System.Boolean, _
   ByVal DraftOutward As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim DraftOutward As System.Boolean

instance.SetDraftOutward(Forward, DraftOutward)
```

### C#

```csharp
void SetDraftOutward(
   System.bool Forward,
   System.bool DraftOutward
)
```

### C++/CLI

```cpp
void SetDraftOutward(
   System.bool Forward,
   System.bool DraftOutward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `DraftOutward`:

## VBA Syntax

See [ExtrudeFeatureData::SetDraftOutward](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetDraftOutward.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
