---
title: "GetHandleData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetHandleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetHandleData.html"
---

# GetHandleData Method (ICustomData)

Gets the specified custom data element whose data is a handle.

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

- `Index`: Index of the handle of the custom data

### Return Value

Value of the handle

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::InsertHandle Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertHandle.html)
[ICustomData::SetHandle Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetHandle.html)

## Availability

DraftSight V1R1.2
