---
title: "SetInteger32Data Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetInteger32Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetInteger32Data.html"
---

# SetInteger32Data Method (ICustomData)

Sets the specified custom data element whose data type is a 32-bit signed integer, also called Int32.

## Syntax

### Visual Basic

```vb
Sub SetInteger32Data( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger32Data(
   System.int Index,
   System.int Value
)
```

### JScript

```
function SetInteger32Data(
   Index : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger32Data(
   System.int Index,
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger32Data(
   System.int Index,
   System.int Value
)
```

### Parameters

- `Index`: Index of the custom data element
- `Value`: Int32 value

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
[ICustomData::GetInteger32Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetInteger32Data.html)
[ICustomData::InsertInteger32Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertInteger32Data.html)

## Availability

DraftSight V1R1.2
