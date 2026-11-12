---
title: "GetCustomData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetCustomData.html"
---

# GetCustomData Method (ICustomData)

Gets the specified custom data element.

## Syntax

### Visual Basic

```vb
Sub GetCustomData( _
   ByVal Index As System.Integer, _
   ByRef Data As CustomData _
)
```

### C#

```csharp
void GetCustomData(
   System.int Index,
   out CustomData Data
)
```

### JScript

```
function GetCustomData(
   Index : System.int,
   Data : CustomData
);
```

### Managed Extensions for C++

```
void GetCustomData(
   System.int Index,
   [PARAMFLAG::Out] CustomData* Data
)
```

### C++/CLI

```cpp
void GetCustomData(
   System.int Index,
   [Out] CustomData^ Data
)
```

### Parameters

- `Index`: Index of the custom data element
- `Data`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::InsertCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertCustomData.html)

## Availability

DraftSight V1R1.2
