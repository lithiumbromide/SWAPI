---
title: "SetDoubleData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetDoubleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetDoubleData.html"
---

# SetDoubleData Method (ICustomData)

Sets the specified custom data element whose data type is double.

## Syntax

### Visual Basic

```vb
Sub SetDoubleData( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Double _
)
```

### C#

```csharp
void SetDoubleData(
   System.int Index,
   System.double Value
)
```

### JScript

```
function SetDoubleData(
   Index : System.int,
   Value : System.double
);
```

### Managed Extensions for C++

```
void SetDoubleData(
   System.int Index,
   System.double Value
)
```

### C++/CLI

```cpp
void SetDoubleData(
   System.int Index,
   System.double Value
)
```

### Parameters

- `Index`: Index of the custom data element
- `Value`: Double value

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
[ICustomData::GetDoubleData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDoubleData.html)
[ICustomData::InsertDoubleData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertDoubleData.html)

## Availability

DraftSight V1R1.2
