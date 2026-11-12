---
title: "GetSegmentAngle Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetSegmentAngle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentAngle.html"
---

# GetSegmentAngle Method (IPolyLine)

Gets the angle at the specified vertex of this 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function GetSegmentAngle( _
   ByVal SegmentIndex As System.Integer, _
   ByRef Angle As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetSegmentAngle(
   System.int SegmentIndex,
   out System.double Angle
)
```

### JScript

```
function GetSegmentAngle(
   SegmentIndex : System.int,
   Angle : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetSegmentAngle(
   System.int SegmentIndex,
   [PARAMFLAG::Out] System.double Angle
)
```

### C++/CLI

```cpp
System.bool GetSegmentAngle(
   System.int SegmentIndex,
   [Out] System.double Angle
)
```

### Parameters

- `SegmentIndex`: Index of the vertex whose angle to get (see **Remarks**)
- `Angle`: Angle

### Return Value

True if the angle of the vertex is returned, false if not

## Remarks

SegmentIndex starts at 0. To determine a valid value for SegmentIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

| For this type of 2D PolyLine... | Number of vertices equals... |
| --- | --- |
| Closed | IPolyLine::GetVerticesCount |
| Open | IPolyLine::GetVerticesCount - 1 |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::IPolyLine::SetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::GetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html)
[IPolyLine::SetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html)
[IPolyLine::SetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html)

## Availability

DraftSight V1R1.1
