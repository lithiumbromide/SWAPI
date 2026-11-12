---
title: "GetInteger64Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetInteger64Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger64Data.html"
---

# GetInteger64Data Method (IXRecord)

Gets the specified XRecord data element whose data type is a signed 64-bit integer, also called Int64.

## Syntax

### Visual Basic

```vb
Function GetInteger64Data( _
   ByVal Index As System.Integer _
) As System.Long
```

### C#

```csharp
System.long GetInteger64Data(
   System.int Index
)
```

### JScript

```
function GetInteger64Data(
   Index : System.int
) : System.long;
```

### Managed Extensions for C++

```
System.long GetInteger64Data(
   System.int Index
)
```

### C++/CLI

```cpp
System.int64 GetInteger64Data(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

Int64

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertInteger64Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger64Data.html)
[IXRecord::SetInteger64Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger64Data.html)

## Availability

DraftSight V1R4.0
