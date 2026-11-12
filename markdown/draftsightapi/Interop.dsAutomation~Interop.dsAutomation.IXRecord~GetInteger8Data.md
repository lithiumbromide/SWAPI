---
title: "GetInteger8Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetInteger8Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger8Data.html"
---

# GetInteger8Data Method (IXRecord)

Gets the specified XRecord data element whose data type is a signed 8-bit integer, also called Int8.

## Syntax

### Visual Basic

```vb
Function GetInteger8Data( _
   ByVal Index As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetInteger8Data(
   System.int Index
)
```

### JScript

```
function GetInteger8Data(
   Index : System.int
) : System.int;
```

### Managed Extensions for C++

```
System.int GetInteger8Data(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetInteger8Data(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

Int8

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertInteger8Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger8Data.html)
[IXRecord::SetInteger8Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger8Data.html)

## Availability

DraftSight V1R4.0
