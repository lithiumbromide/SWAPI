---
title: "SetInteger32Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetInteger32Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger32Data.html"
---

# SetInteger32Data Method (IXRecord)

Sets the specified XRecord data element to a signed 32-bit integer, also called Int32.

## Syntax

### Visual Basic

```vb
Sub SetInteger32Data( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger32Data(
   System.int Index,
   System.int Value
)
```

### JScript

```
function SetInteger32Data(
   Index : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger32Data(
   System.int Index,
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger32Data(
   System.int Index,
   System.int Value
)
```

### Parameters

- `Index`: Index of XRecord data element to set to Int32 (see **Remarks**)
- `Value`: Int32

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger32Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger32Data.html)
[IXRecord::InsertInteger32Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger32Data.html)

## Availability

DraftSight V1R4.0
