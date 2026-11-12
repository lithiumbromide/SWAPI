---
title: "Delete Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "Delete"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~Delete.html"
---

# Delete Method (ICustomData)

Deletes the specified custom data element.

## Syntax

### Visual Basic

```vb
Sub Delete( _
   ByVal Index As System.Integer _
)
```

### C#

```csharp
void Delete(
   System.int Index
)
```

### JScript

```
function Delete(
   Index : System.int
);
```

### Managed Extensions for C++

```
void Delete(
   System.int Index
)
```

### C++/CLI

```cpp
void Delete(
   System.int Index
)
```

### Parameters

- `Index`: Index of the custom data element

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::Empty Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~Empty.html)

## Availability

DraftSight V1R1.2
