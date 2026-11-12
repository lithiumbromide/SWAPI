---
title: "GetDataType Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetDataType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataType.html"
---

# GetDataType Method (ICustomData)

Gets the data type of the specified custom data element.

## Syntax

### Visual Basic

```vb
Sub GetDataType( _
   ByVal Index As System.Integer, _
   ByRef DataType As dsCustomDataType_e _
)
```

### C#

```csharp
void GetDataType(
   System.int Index,
   out dsCustomDataType_e DataType
)
```

### JScript

```
function GetDataType(
   Index : System.int,
   DataType : dsCustomDataType_e
);
```

### Managed Extensions for C++

```
void GetDataType(
   System.int Index,
   [PARAMFLAG::Out] dsCustomDataType_e DataType
)
```

### C++/CLI

```cpp
void GetDataType(
   System.int Index,
   [Out] dsCustomDataType_e DataType
)
```

### Parameters

- `Index`: Index of the custom data element
- `DataType`: Data type of specified custom data element as defined in [dsCustomDataType_e](Interop.dsAutomation~Interop.dsAutomation.dsCustomDataType_e.html)

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
[ICustomData::GetDataMarker Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataMarker.html)

## Availability

DraftSight V1R1.2
