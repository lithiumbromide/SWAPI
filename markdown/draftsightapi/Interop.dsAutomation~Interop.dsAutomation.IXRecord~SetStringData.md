---
title: "SetStringData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetStringData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetStringData.html"
---

# SetStringData Method (IXRecord)

Sets the specified XRecord data element to a string.

## Syntax

### Visual Basic

```vb
Sub SetStringData( _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void SetStringData(
   System.int Index,
   System.string Value
)
```

### JScript

```
function SetStringData(
   Index : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void SetStringData(
   System.int Index,
   System.string* Value
)
```

### C++/CLI

```cpp
void SetStringData(
   System.int Index,
   System.String^ Value
)
```

### Parameters

- `Index`: Index of XRecord data element to set to a string (see **Remarks**)
- `Value`: String

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetStringData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetStringData.html)
[IXRecord::InsertStringData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertStringData.html)

## Availability

DraftSight V1R4.0
