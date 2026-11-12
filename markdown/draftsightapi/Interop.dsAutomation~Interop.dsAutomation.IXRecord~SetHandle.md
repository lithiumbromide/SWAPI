---
title: "SetHandle Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetHandle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetHandle.html"
---

# SetHandle Method (IXRecord)

Sets the specified XRecord data element to a handle.

## Syntax

### Visual Basic

```vb
Sub SetHandle( _
   ByVal Index As System.Integer, _
   ByVal Handle As System.String _
)
```

### C#

```csharp
void SetHandle(
   System.int Index,
   System.string Handle
)
```

### JScript

```
function SetHandle(
   Index : System.int,
   Handle : System.String
);
```

### Managed Extensions for C++

```
void SetHandle(
   System.int Index,
   System.string* Handle
)
```

### C++/CLI

```cpp
void SetHandle(
   System.int Index,
   System.String^ Handle
)
```

### Parameters

- `Index`: Index of XRecord data element to set to a handle (see **Remarks**)
- `Handle`: String, which is the data type of a handle

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetHandleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetHandleData.html)
[IXRecord::InsertHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertHandle.html)
[IXRecord::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Handle.html)
[IXRecord::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetCustomData.html)
[IXRecord::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~DeleteCustomData.html)
[IXRecord::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetCustomData.html)

## Availability

DraftSight V1R4.0
