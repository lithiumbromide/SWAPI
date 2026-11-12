---
title: "SetSegmentAngle Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "SetSegmentAngle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html"
---

# SetSegmentAngle Method (IPolyLine)

Sets the angle at the specified vertex of this 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function SetSegmentAngle( _
   ByVal SegmentIndex As System.Integer, _
   ByVal Angle As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetSegmentAngle(
   System.int SegmentIndex,
   System.double Angle
)
```

### JScript

```
function SetSegmentAngle(
   SegmentIndex : System.int,
   Angle : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetSegmentAngle(
   System.int SegmentIndex,
   System.double Angle
)
```

### C++/CLI

```cpp
System.bool SetSegmentAngle(
   System.int SegmentIndex,
   System.double Angle
)
```

### Parameters

- `SegmentIndex`: Index of the vertex whose angle to set (see **Remarks**)
- `Angle`: Angle

### Return Value

True if the angle of the vertex is set, false if not

## Remarks

SegmentIndex starts at 0. To determine a valid value for SegmentIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

| For this type of 2D PolyLine... | Number of vertices equals... |
| --- | --- |
| Closed | IPolyLine::GetVerticesCount |
| Open | IPolyLine::GetVerticesCount - 1 |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentAngle.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::GetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)
[IPolyLine::SetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html)
[IPolyLine::SetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html)

## Availability

DraftSight V1R1.1
