---
title: "GetHandleData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetHandleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetHandleData.html"
---

# GetHandleData Method (IXRecord)

Gets the specified XRecord data element whose data type is a handle.

## Syntax

### Visual Basic

```vb
Function GetHandleData( _
   ByVal Index As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetHandleData(
   System.int Index
)
```

### JScript

```
function GetHandleData(
   Index : System.int
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetHandleData(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetHandleData(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

String, which is the data type of a handle

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::SetHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetHandle.html)
[IXRecord::InsertHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertHandle.html)
[IXRecord::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Handle.html)
[IXRecord::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~DeleteCustomData.html)
[IXRecord::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetCustomData.html)
[IXRecord::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetCustomData.html)

## Availability

DraftSight V1R4.0
