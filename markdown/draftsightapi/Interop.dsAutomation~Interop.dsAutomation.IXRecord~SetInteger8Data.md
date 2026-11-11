---
title: "SetInteger8Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetInteger8Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger8Data.html"
---

# SetInteger8Data Method (IXRecord)

Sets the specified XRecord data element to a signed 8-bit integer, also called Int8.

## Syntax

### Visual Basic

```vb
Sub SetInteger8Data( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger8Data(
   System.int Index,
   System.int Value
)
```

### JScript

```
function SetInteger8Data(
   Index : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger8Data(
   System.int Index,
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger8Data(
   System.int Index,
   System.int Value
)
```

### Parameters

- `Index`: Index of XRecord data element to set to Int8 (see **Remarks**)
- `Value`: Int8

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord:;GetInteger8Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger8Data.html)
[IXRecord::InsertInteger8Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger8Data.html)

## Availability

DraftSight V1R4.0
