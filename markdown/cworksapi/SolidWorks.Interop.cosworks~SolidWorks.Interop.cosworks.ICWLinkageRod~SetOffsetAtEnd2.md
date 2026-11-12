---
title: "SetOffsetAtEnd2 Method (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "SetOffsetAtEnd2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~SetOffsetAtEnd2.html"
---

# SetOffsetAtEnd2 Method (ICWLinkageRod)

Sets the offset at End 2 of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOffsetAtEnd2( _
   ByVal DOffsetVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod
Dim DOffsetVal As System.Double

instance.SetOffsetAtEnd2(DOffsetVal)
```

### C#

```csharp
void SetOffsetAtEnd2(
   System.double DOffsetVal
)
```

### C++/CLI

```cpp
void SetOffsetAtEnd2(
   System.double DOffsetVal
)
```

### Parameters

- `DOffsetVal`: Offset in meters

## VBA Syntax

See [CWLinkageRod::SetOffsetAtEnd2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~SetOffsetAtEnd2.html).

## Remarks

This method is not valid if End 2 is a vertex.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
