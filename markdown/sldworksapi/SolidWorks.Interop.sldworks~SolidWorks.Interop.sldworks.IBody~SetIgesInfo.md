---
title: "SetIgesInfo Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "SetIgesInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~SetIgesInfo.html"
---

# SetIgesInfo Method (IBody)

Obsolete. Superseded by [IBody2::SetIgesetInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~SetIgesInfo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIgesInfo( _
   ByVal SystemName As System.String, _
   ByVal Granularity As System.Double, _
   ByVal AttemptKnitting As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim SystemName As System.String
Dim Granularity As System.Double
Dim AttemptKnitting As System.Boolean

instance.SetIgesInfo(SystemName, Granularity, AttemptKnitting)
```

### C#

```csharp
void SetIgesInfo(
   System.string SystemName,
   System.double Granularity,
   System.bool AttemptKnitting
)
```

### C++/CLI

```cpp
void SetIgesInfo(
   System.String^ SystemName,
   System.double Granularity,
   System.bool AttemptKnitting
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SystemName`:
- `Granularity`:
- `AttemptKnitting`:

## VBA Syntax

See [Body::SetIgesInfo](ms-its:sldworksapivb6.chm::/sldworks~Body~SetIgesInfo.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
