---
title: "SetPointData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetPointData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetPointData.html"
---

# SetPointData Method (IXRecord)

Sets the specified XRecord data element to a point.

## Syntax

### Visual Basic

```vb
Sub SetPointData( _
   ByVal Index As System.Integer, _
   ByVal Point As MathPoint _
)
```

### C#

```csharp
void SetPointData(
   System.int Index,
   MathPoint Point
)
```

### JScript

```
function SetPointData(
   Index : System.int,
   Point : MathPoint
);
```

### Managed Extensions for C++

```
void SetPointData(
   System.int Index,
   MathPoint* Point
)
```

### C++/CLI

```cpp
void SetPointData(
   System.int Index,
   MathPoint^ Point
)
```

### Parameters

- `Index`: Index of XRecord data element to set to a point (see **Remarks**)
- `Point`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetPointData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetPointData.html)
[IXRecord::InsertPointData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertPointData.html)

## Availability

DraftSight V1R4.0
