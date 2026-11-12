---
title: "SetInteger64Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetInteger64Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger64Data.html"
---

# SetInteger64Data Method (IXRecord)

Sets the specified XRecord data element to a signed 64-bit integer, also called Int64.

## Syntax

### Visual Basic

```vb
Sub SetInteger64Data( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Long _
)
```

### C#

```csharp
void SetInteger64Data(
   System.int Index,
   System.long Value
)
```

### JScript

```
function SetInteger64Data(
   Index : System.int,
   Value : System.long
);
```

### Managed Extensions for C++

```
void SetInteger64Data(
   System.int Index,
   System.long Value
)
```

### C++/CLI

```cpp
void SetInteger64Data(
   System.int Index,
   System.int64 Value
)
```

### Parameters

- `Index`: Index of XRecord data element to set to Int64 (see **Remarks**)
- `Value`: Int64

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger64Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger64Data.html)
[IXRecord::InsertInteger64Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger64Data.html)

## Availability

DraftSight V1R4.0
