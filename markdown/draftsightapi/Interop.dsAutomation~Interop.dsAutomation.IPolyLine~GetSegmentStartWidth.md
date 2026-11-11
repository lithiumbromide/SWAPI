---
title: "GetSegmentStartWidth Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetSegmentStartWidth"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html"
---

# GetSegmentStartWidth Method (IPolyLine)

Gets the start width of the specified 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function GetSegmentStartWidth( _
   ByVal SegmentIndex As System.Integer, _
   ByRef StartWidth As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetSegmentStartWidth(
   System.int SegmentIndex,
   out System.double StartWidth
)
```

### JScript

```
function GetSegmentStartWidth(
   SegmentIndex : System.int,
   StartWidth : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetSegmentStartWidth(
   System.int SegmentIndex,
   [PARAMFLAG::Out] System.double StartWidth
)
```

### C++/CLI

```cpp
System.bool GetSegmentStartWidth(
   System.int SegmentIndex,
   [Out] System.double StartWidth
)
```

### Parameters

- `SegmentIndex`: Index of the vertex of the segment (see **Remarks**)
- `StartWidth`: Start width at the specified vertex

### Return Value

True if the start width is returned, false if not

## Remarks

SegmentIndex starts at 0. To determine a valid value for SegmentIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

| For this type of 2D PolyLine... | Number of vertices equals... |
| --- | --- |
| Closed | IPolyLine::GetVerticesCount |
| Open | IPolyLine::GetVerticesCount - 1 |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::SetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::SetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html)
[IPolyLine::GlobalWidth Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GlobalWidth.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)
[IPolyLine::GetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentAngle.html)
[IPolyLine::SetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html)

## Availability

DraftSight V1R1.1
