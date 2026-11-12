---
title: "InsertHandle Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertHandle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertHandle.html"
---

# InsertHandle Method (IXRecord)

Inserts a handle and marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertHandle( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Handle As System.String _
)
```

### C#

```csharp
void InsertHandle(
   System.int Index,
   System.int Marker,
   System.string Handle
)
```

### JScript

```
function InsertHandle(
   Index : System.int,
   Marker : System.int,
   Handle : System.String
);
```

### Managed Extensions for C++

```
void InsertHandle(
   System.int Index,
   System.int Marker,
   System.string* Handle
)
```

### C++/CLI

```cpp
void InsertHandle(
   System.int Index,
   System.int Marker,
   System.String^ Handle
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert the handle (see **Remarks**)
- `Marker`: Marker
- `Handle`: Handle, whose data type is string

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetHandleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetHandleData.html)
[IXRecord::SetHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetHandle.html)
[IXRecord::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Handle.html)
[IXRecord::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetCustomData.html)
[IXRecord::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~DeleteCustomData.html)
[IXRecord::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetCustomData.html)

## Availability

DraftSight V1R4.0
