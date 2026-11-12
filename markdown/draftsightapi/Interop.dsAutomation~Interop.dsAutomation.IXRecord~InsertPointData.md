---
title: "InsertPointData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertPointData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertPointData.html"
---

# InsertPointData Method (IXRecord)

Inserts a point and marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertPointData( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Point As MathPoint _
)
```

### C#

```csharp
void InsertPointData(
   System.int Index,
   System.int Marker,
   MathPoint Point
)
```

### JScript

```
function InsertPointData(
   Index : System.int,
   Marker : System.int,
   Point : MathPoint
);
```

### Managed Extensions for C++

```
void InsertPointData(
   System.int Index,
   System.int Marker,
   MathPoint* Point
)
```

### C++/CLI

```cpp
void InsertPointData(
   System.int Index,
   System.int Marker,
   MathPoint^ Point
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert a point (see **Remarks**)
- `Marker`: Marker
- `Point`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetPointData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetPointData.html)
[IXRecord::SetPointData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetPointData.html)

## Availability

DraftSight V1R4.0
