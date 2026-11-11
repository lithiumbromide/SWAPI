---
title: "InsertInteger8Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertInteger8Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger8Data.html"
---

# InsertInteger8Data Method (IXRecord)

Inserts a signed 8-bit integer, also called Int8, and a marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertInteger8Data( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void InsertInteger8Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### JScript

```
function InsertInteger8Data(
   Index : System.int,
   Marker : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void InsertInteger8Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### C++/CLI

```cpp
void InsertInteger8Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert an Int8 (see **Remarks**)
- `Marker`: Marker
- `Value`: Int8

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger8Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger8Data.html)
[IXRecord::SetInteger8Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger8Data.html)

## Availability

DraftSight V1R4.0
