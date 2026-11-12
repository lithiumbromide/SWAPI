---
title: "SetStringData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetStringData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetStringData.html"
---

# SetStringData Method (ICustomData)

Sets the specified custom data element whose data type is a string.

## Syntax

### Visual Basic

```vb
Sub SetStringData( _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void SetStringData(
   System.int Index,
   System.string Value
)
```

### JScript

```
function SetStringData(
   Index : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void SetStringData(
   System.int Index,
   System.string* Value
)
```

### C++/CLI

```cpp
void SetStringData(
   System.int Index,
   System.String^ Value
)
```

### Parameters

- `Index`: Index of the custom data element
- `Value`: String

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetStringData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetStringData.html)
[ICustomData::InsertStringData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertStringData.html)

## Availability

DraftSight V1R1.2
