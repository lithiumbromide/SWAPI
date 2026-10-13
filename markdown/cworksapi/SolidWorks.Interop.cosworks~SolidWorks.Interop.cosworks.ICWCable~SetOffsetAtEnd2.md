---
title: "SetOffsetAtEnd2 Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "SetOffsetAtEnd2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~SetOffsetAtEnd2.html"
---

# SetOffsetAtEnd2 Method (ICWCable)

Sets the offset at End 2.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOffsetAtEnd2( _
   ByVal DOffsetVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
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

- `DOffsetVal`: Offset at End 2

## VBA Syntax

See [CWCable::SetOffsetAtEnd2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~SetOffsetAtEnd2.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## Remarks

This method is not valid if End 2 is a vertex.

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
