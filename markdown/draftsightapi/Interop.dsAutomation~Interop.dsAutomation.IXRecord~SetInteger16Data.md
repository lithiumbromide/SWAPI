---
title: "SetInteger16Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetInteger16Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger16Data.html"
---

# SetInteger16Data Method (IXRecord)

Sets the specified XRecord data element to a signed 16-bit integer, also called Int16.

## Syntax

### Visual Basic

```vb
Sub SetInteger16Data( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger16Data(
   System.int Index,
   System.int Value
)
```

### JScript

```
function SetInteger16Data(
   Index : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger16Data(
   System.int Index,
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger16Data(
   System.int Index,
   System.int Value
)
```

### Parameters

- `Index`: Index of XRecord data element to set to Int16 (see **Remarks**)
- `Value`: Int16

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger16Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger16Data.html)
[IXRecord::InsertInteger16Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger16Data.html)

## Availability

DraftSight V1R4.0
