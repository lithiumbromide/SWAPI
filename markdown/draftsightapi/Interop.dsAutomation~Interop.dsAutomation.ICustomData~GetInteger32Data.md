---
title: "GetInteger32Data Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetInteger32Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetInteger32Data.html"
---

# GetInteger32Data Method (ICustomData)

Gets the specified custom data element whose data type is a 32-bit signed integer, also called Int32.

## Syntax

### Visual Basic

```vb
Sub GetInteger32Data( _
   ByVal Index As System.Integer, _
   ByRef Value As System.Integer _
)
```

### C#

```csharp
void GetInteger32Data(
   System.int Index,
   out System.int Value
)
```

### JScript

```
function GetInteger32Data(
   Index : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void GetInteger32Data(
   System.int Index,
   [PARAMFLAG::Out] System.int Value
)
```

### C++/CLI

```cpp
void GetInteger32Data(
   System.int Index,
   [Out] System.int Value
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
[ICustomData::SetInteger32Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetInteger32Data.html)
[ICustomData::InsertInteger32Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertInteger32Data.html)

## Availability

DraftSight V1R1.2
