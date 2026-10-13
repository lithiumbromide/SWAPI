---
title: "SetDraftAngle Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetDraftAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetDraftAngle.html"
---

# SetDraftAngle Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetDraftAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftAngle( _
   ByVal Forward As System.Boolean, _
   ByVal DraftAngle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim DraftAngle As System.Double

instance.SetDraftAngle(Forward, DraftAngle)
```

### C#

```csharp
void SetDraftAngle(
   System.bool Forward,
   System.double DraftAngle
)
```

### C++/CLI

```cpp
void SetDraftAngle(
   System.bool Forward,
   System.double DraftAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `DraftAngle`:

## VBA Syntax

See [ExtrudeFeatureData::SetDraftAngle](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetDraftAngle.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
