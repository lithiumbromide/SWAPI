---
title: "GetSegmentType Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetSegmentType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentType.html"
---

# GetSegmentType Method (IPolyLine)

Gets the type of 2D PolyLine segment.

## Syntax

### Visual Basic

```vb
Function GetSegmentType( _
   ByVal SegmentIndex As System.Integer _
) As dsPolyLineSegmentType_e
```

### C#

```csharp
dsPolyLineSegmentType_e GetSegmentType(
   System.int SegmentIndex
)
```

### JScript

```
function GetSegmentType(
   SegmentIndex : System.int
) : dsPolyLineSegmentType_e;
```

### Managed Extensions for C++

```
dsPolyLineSegmentType_e GetSegmentType(
   System.int SegmentIndex
)
```

### C++/CLI

```cpp
dsPolyLineSegmentType_e GetSegmentType(
   System.int SegmentIndex
)
```

### Parameters

- `SegmentIndex`: Type of segment as defined in [dsPolyLineSegmentType_e](Interop.dsAutomation~Interop.dsAutomation.dsPolyLineSegmentType_e.html)

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentAngle.html)
[IPolyLine::GetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentEndWidth.html)
[IPolyLine::GetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetSegmentStartWidth.html)
[IPolyLine::SetSegmentAngle Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentAngle.html)
[IPolyLine::SetSegmentStartWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html)
[IPolyLine::SetSegmentEndWidth Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html)

## Availability

DraftSight V1R3.0
