---
title: "InsertHandle Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertHandle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertHandle.html"
---

# InsertHandle Method (ICustomData)

Inserts a handle at the specified index.

## Syntax

### Visual Basic

```vb
Sub InsertHandle( _
   ByVal Index As System.Integer, _
   ByVal Handle As System.String _
)
```

### C#

```csharp
void InsertHandle(
   System.int Index,
   System.string Handle
)
```

### JScript

```
function InsertHandle(
   Index : System.int,
   Handle : System.String
);
```

### Managed Extensions for C++

```
void InsertHandle(
   System.int Index,
   System.string* Handle
)
```

### C++/CLI

```cpp
void InsertHandle(
   System.int Index,
   System.String^ Handle
)
```

### Parameters

- `Index`: Index where to insert the custom data
- `Handle`: Value of the handle

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetHandleData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetHandleData.html)
[ICustomData::SetHandle Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetHandle.html)

## Availability

DraftSight V1R1.2
