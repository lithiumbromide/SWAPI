---
title: "SetHandle Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetHandle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetHandle.html"
---

# SetHandle Method (ICustomData)

Sets the specified custom data element whose data type is a handle.

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

- `Index`: Index of the custom data element
- `Handle`: Value of the handle

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetHandleData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetHandleData.html)
[ICustomData::InsertHandle Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertHandle.html)

## Availability

DraftSight V1R1.2
