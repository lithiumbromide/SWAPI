---
title: "SetSegmentStartWidth Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "SetSegmentStartWidth"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html"
---

# SetSegmentStartWidth Method (IPolyLine)

Sets the start width of the specified 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function SetSegmentStartWidth( _
   ByVal SegmentIndex As System.Integer, _
   ByVal StartWidth As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetSegmentStartWidth(
   System.int SegmentIndex,
   System.double StartWidth
)
```

### JScript

```
function SetSegmentStartWidth(
   SegmentIndex : System.int,
   StartWidth : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetSegmentStartWidth(
   System.int SegmentIndex,
   System.double StartWidth
)
```

### C++/CLI

```cpp
System.bool SetSegmentStartWidth(
   System.int SegmentIndex,
   System.double StartWidth
)
```

### Parameters

- `SegmentIndex`: Index of the vertex of the segment (see **Remarks**)
- `StartWidth`: Start width at the specified vertex

### Return Value

True if the start width is set, false if not

## Remarks

SegmentIndex starts at 0. To determine a valid value for SegmentIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

| For this type of 2D PolyLine... | Number of vertices equals... |
| --- | --- |
| Closed | IPolyLine::GetVerticesCount |
| Open | IPolyLine::GetVerticesCount - 1 |

Same width for its entire length

| To set 2D PolyLine's... | Use... |
| --- | --- |
| Start width only | IPolyLine::SetSegmentStartWidth |
| End width only | Same width for its entire length |
| Same width for its entire length | IPolyLine::GlobalWidth instead of using IPolyLine::SetSegmentStartWidth and IPolyLine::SetSegmentEndWidth |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::SetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html)
[IPolyLine::GetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentAngle.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)
[IPolyLine::SetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html)
[IPolyLine::SetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html)

## Availability

DraftSight V1R1.1
