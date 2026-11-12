---
title: "GetLayerName Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetLayerName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetLayerName.html"
---

# GetLayerName Method (ICustomData)

Gets the specified custom data element whose value is the name of a Layer.

## Syntax

### Visual Basic

```vb
Sub GetLayerName( _
   ByVal Index As System.Integer, _
   ByRef Value As System.String _
)
```

### C#

```csharp
void GetLayerName(
   System.int Index,
   out System.string Value
)
```

### JScript

```
function GetLayerName(
   Index : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void GetLayerName(
   System.int Index,
   [PARAMFLAG::Out] System.string* Value
)
```

### C++/CLI

```cpp
void GetLayerName(
   System.int Index,
   [Out] System.String^ Value
)
```

### Parameters

- `Index`: Index of the custom data element
- `Value`: Name of a Layer

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
[ICustomData::SetLayerName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetLayerName.html)
[ICustomData::InsertLayerName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertLayerName.html)

## Availability

DraftSight V1R1.2
