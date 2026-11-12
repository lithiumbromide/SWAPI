---
title: "InsertInteger16Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertInteger16Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger16Data.html"
---

# InsertInteger16Data Method (IXRecord)

Inserts a signed 16-bit integer, also called Int16, and a marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertInteger16Data( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void InsertInteger16Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### JScript

```
function InsertInteger16Data(
   Index : System.int,
   Marker : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void InsertInteger16Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### C++/CLI

```cpp
void InsertInteger16Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert an Int16 (see **Remarks**)
- `Marker`: Marker
- `Value`: Int16

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger16Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger16Data.html)
[IXRecord::SetInteger16Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger16Data.html)

## Availability

DraftSight V1R4.0
