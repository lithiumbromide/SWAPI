---
title: "SetSegmentEndWidth Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "SetSegmentEndWidth"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html"
---

# SetSegmentEndWidth Method (IPolyLine)

Sets the end width of the specified 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function SetSegmentEndWidth( _
   ByVal SegmentIndex As System.Integer, _
   ByVal EndWidth As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetSegmentEndWidth(
   System.int SegmentIndex,
   System.double EndWidth
)
```

### JScript

```
function SetSegmentEndWidth(
   SegmentIndex : System.int,
   EndWidth : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetSegmentEndWidth(
   System.int SegmentIndex,
   System.double EndWidth
)
```

### C++/CLI

```cpp
System.bool SetSegmentEndWidth(
   System.int SegmentIndex,
   System.double EndWidth
)
```

### Parameters

- `SegmentIndex`: Index of the vertex of the segment (see **Remarks**)
- `EndWidth`: End width at the specified vertex

### Return Value

True if the end width is set, false if not

## Remarks

SegmentIndex starts at 0. To determine a valid value for SegmentIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

| For this type of 2D PolyLine... | Number of vertices equals... |
| --- | --- |
| Closed | IPolyLine::GetVerticesCount |
| Open | IPolyLine::GetVerticesCount - 1 |

| To set 2D PolyLine's... | Use... |
| --- | --- |
| End width only | IPolyLine::SetSegmentEndWidth |
| Start width only | IPolyLine::SetSegmentStartWidth |
| Same width for entire length | IPolyLine::GlobalWidth instead of using IPolyLine::SetSegmentStartWidth and IPolyLine::SetSegmentEndWidth |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::GetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html)
[IPolyLine::SetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::GetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)

## Availability

DraftSight V1R1.1
