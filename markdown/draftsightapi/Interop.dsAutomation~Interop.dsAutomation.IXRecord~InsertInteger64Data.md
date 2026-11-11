---
title: "InsertInteger64Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertInteger64Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger64Data.html"
---

# InsertInteger64Data Method (IXRecord)

Inserts a signed 64-bit integer, also called Int64, and a marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertInteger64Data( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Long _
)
```

### C#

```csharp
void InsertInteger64Data(
   System.int Index,
   System.int Marker,
   System.long Value
)
```

### JScript

```
function InsertInteger64Data(
   Index : System.int,
   Marker : System.int,
   Value : System.long
);
```

### Managed Extensions for C++

```
void InsertInteger64Data(
   System.int Index,
   System.int Marker,
   System.long Value
)
```

### C++/CLI

```cpp
void InsertInteger64Data(
   System.int Index,
   System.int Marker,
   System.int64 Value
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert an Int64 (see **Remarks**)
- `Marker`: Marker
- `Value`: Int64

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger64Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger64Data.html)
[IXRecord::SetInteger64Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger64Data.html)

## Availability

DraftSight V1R4.0
