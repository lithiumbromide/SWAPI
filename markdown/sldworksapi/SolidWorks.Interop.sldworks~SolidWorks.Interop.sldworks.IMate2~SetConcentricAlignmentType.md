---
title: "SetConcentricAlignmentType Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "SetConcentricAlignmentType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetConcentricAlignmentType.html"
---

# SetConcentricAlignmentType Method (IMate2)

Sets the alignment type of this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetConcentricAlignmentType( _
   ByVal PositionType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim PositionType As System.Integer

instance.SetConcentricAlignmentType(PositionType)
```

### C#

```csharp
void SetConcentricAlignmentType(
   System.int PositionType
)
```

### C++/CLI

```cpp
void SetConcentricAlignmentType(
   System.int PositionType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionType`: Alignment type as defined in [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html)

## VBA Syntax

See [Mate2::SetConcentricAlignmentType](ms-its:sldworksapivb6.chm::/sldworks~Mate2~SetConcentricAlignmentType.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetConcentricAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
