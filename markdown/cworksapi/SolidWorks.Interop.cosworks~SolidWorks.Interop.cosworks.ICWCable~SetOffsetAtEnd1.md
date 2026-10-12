---
title: "SetOffsetAtEnd1 Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "SetOffsetAtEnd1"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~SetOffsetAtEnd1.html"
---

# SetOffsetAtEnd1 Method (ICWCable)

Sets the offset at End 1.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOffsetAtEnd1( _
   ByVal DOffsetVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
Dim DOffsetVal As System.Double

instance.SetOffsetAtEnd1(DOffsetVal)
```

### C#

```csharp
void SetOffsetAtEnd1(
   System.double DOffsetVal
)
```

### C++/CLI

```cpp
void SetOffsetAtEnd1(
   System.double DOffsetVal
)
```

### Parameters

- `DOffsetVal`: Offset at End 1

## VBA Syntax

See [CWCable::SetOffsetAtEnd1](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~SetOffsetAtEnd1.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## Remarks

This method is not valid if End 1 is a vertex.

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
