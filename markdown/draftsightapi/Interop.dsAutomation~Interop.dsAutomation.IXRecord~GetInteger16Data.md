---
title: "GetInteger16Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetInteger16Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger16Data.html"
---

# GetInteger16Data Method (IXRecord)

Gets the specified XRecord data element whose data type is a signed 16-bit integer, also called Int16.

## Syntax

### Visual Basic

```vb
Function GetInteger16Data( _
   ByVal Index As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetInteger16Data(
   System.int Index
)
```

### JScript

```
function GetInteger16Data(
   Index : System.int
) : System.int;
```

### Managed Extensions for C++

```
System.int GetInteger16Data(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetInteger16Data(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

Int16

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertInteger16Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger16Data.html)
[IXRecord::SetInteger16Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger16Data.html)

## Availability

DraftSight V1R4.0
