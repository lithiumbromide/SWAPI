---
title: "SetIgesInfo Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetIgesInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetIgesInfo.html"
---

# SetIgesInfo Method (IBody2)

Sends IGES-specific data to the geometric modeler.

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
Dim instance As IBody2
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

- `SystemName`: Name of the system as defined in [swIGESPreferredSystem_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swIGESPreferredSystem_e.html)
- `Granularity`: Level of granularity
- `AttemptKnitting`: True knits the objects, false does not

## VBA Syntax

See [Body2::SetIgesInfo](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetIgesInfo.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
