---
title: "GetSegmentEndWidth Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetSegmentEndWidth"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html"
---

# GetSegmentEndWidth Method (IPolyLine)

Gets the end width of the specified 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function GetSegmentEndWidth( _
   ByVal SegmentIndex As System.Integer, _
   ByRef EndWidth As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetSegmentEndWidth(
   System.int SegmentIndex,
   out System.double EndWidth
)
```

### JScript

```
function GetSegmentEndWidth(
   SegmentIndex : System.int,
   EndWidth : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetSegmentEndWidth(
   System.int SegmentIndex,
   [PARAMFLAG::Out] System.double EndWidth
)
```

### C++/CLI

```cpp
System.bool GetSegmentEndWidth(
   System.int SegmentIndex,
   [Out] System.double EndWidth
)
```

### Parameters

- `SegmentIndex`: Index of the vertex of the segment (see **Remarks**)
- `EndWidth`: End width at the specified vertex

### Return Value

True if the end width is returned, false if not

## Remarks

SegmentIndex starts at 0. To determine a valid value for SegmentIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

| For this type of 2D PolyLine... | Number of vertices equals... |
| --- | --- |
| Closed | IPolyLine::GetVerticesCount |
| Open | IPolyLine::GetVerticesCount - 1 |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::SetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html)
[IPolyLine::GetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html)
[IPolyLine::SetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html)
[IPolyLine::GlobalWidth Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GlobalWidth.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)
[IPolyLine::GetSegmentType Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html)

## Availability

DraftSight V1R1.1
