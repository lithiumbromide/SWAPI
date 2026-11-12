---
title: "SetInteger16Data Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetInteger16Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetInteger16Data.html"
---

# SetInteger16Data Method (ICustomData)

Sets the specified custom data element whose data type is a 16-bit signed integer, also called Int16.

## Syntax

### Visual Basic

```vb
Sub SetInteger16Data( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger16Data(
   System.int Index,
   System.int Value
)
```

### JScript

```
function SetInteger16Data(
   Index : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger16Data(
   System.int Index,
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger16Data(
   System.int Index,
   System.int Value
)
```

### Parameters

- `Index`: Index of the custom data element
- `Value`: Int16 value

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
[ICustomData::GetInteger16Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetInteger16Data.html)
[ICustomData::SetInteger16Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetInteger16Data.html)

## Availability

DraftSight V1R1.2
