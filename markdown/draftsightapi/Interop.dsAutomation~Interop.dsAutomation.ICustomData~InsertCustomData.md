---
title: "InsertCustomData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertCustomData.html"
---

# InsertCustomData Method (ICustomData)

Inserts custom data at the specified index.

## Syntax

### Visual Basic

```vb
Function InsertCustomData( _
   ByVal Index As System.Integer _
) As CustomData
```

### C#

```csharp
CustomData InsertCustomData(
   System.int Index
)
```

### JScript

```
function InsertCustomData(
   Index : System.int
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* InsertCustomData(
   System.int Index
)
```

### C++/CLI

```cpp
CustomData^ InsertCustomData(
   System.int Index
)
```

### Parameters

- `Index`: Index where to insert the custom data

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetCustomData.html)

## Availability

DraftSight V1R1.2
