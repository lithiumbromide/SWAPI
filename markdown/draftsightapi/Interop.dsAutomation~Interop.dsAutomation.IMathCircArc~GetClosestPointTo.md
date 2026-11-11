---
title: "GetClosestPointTo Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "GetClosestPointTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointTo.html"
---

# GetClosestPointTo Method (IMathCircArc)

Gets the point on this mathematical circular Arc that is closest to the specified point.

## Syntax

### Visual Basic

```vb
Function GetClosestPointTo( _
   ByVal Point As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointTo(
   MathPoint Point
)
```

### JScript

```
function GetClosestPointTo(
   Point : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointTo(
   MathPoint* Point
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointTo(
   MathPoint^ Point
)
```

### Parameters

- `Point`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical circular Arc that is closest to Point

## Examples

[Create Mathematical Circular Arcs (C#)](Create_Mathemetical_Circular_Arcs_Example_CSharp.htm)
[Create Mathematical Circular Arcs (VB.NET)](Create_Mathematical_Circular_Arcs_Example_VBNET.htm)
[Create Mathematical Circular Arcs (VBA)](Create_Mathematical_Circular_Arcs_Example_VBA.htm)

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToCircArc.html)
[IMathCircArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToEllipArc.html)
[IMathCircArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToLinearObject.html)
[IMathCircArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToPlane.html)
[IMathCircArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetEndPoint.html)
[IMathCircArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetStartPoint.html)
[IMathCircArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~Center.html)

## Availability

DraftSight V1R5.0
