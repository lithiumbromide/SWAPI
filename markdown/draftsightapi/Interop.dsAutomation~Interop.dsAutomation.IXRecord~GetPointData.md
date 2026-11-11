---
title: "GetPointData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetPointData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetPointData.html"
---

# GetPointData Method (IXRecord)

Gets the specified XRecord data element whose data type is a point.

## Syntax

### Visual Basic

```vb
Function GetPointData( _
   ByVal Index As System.Integer _
) As MathPoint
```

### C#

```csharp
MathPoint GetPointData(
   System.int Index
)
```

### JScript

```
function GetPointData(
   Index : System.int
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetPointData(
   System.int Index
)
```

### C++/CLI

```cpp
MathPoint^ GetPointData(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord whose data type is a point (see **Remarks**)

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertPointData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertPointData.html)
[IXRecord::SetPointData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetPointData.html)

## Availability

DraftSight V1R4.0
