---
title: "InsertLayerName Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertLayerName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertLayerName.html"
---

# InsertLayerName Method (ICustomData)

Inserts the name of a Layer at the specified index.

## Syntax

### Visual Basic

```vb
Sub InsertLayerName( _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void InsertLayerName(
   System.int Index,
   System.string Value
)
```

### JScript

```
function InsertLayerName(
   Index : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void InsertLayerName(
   System.int Index,
   System.string* Value
)
```

### C++/CLI

```cpp
void InsertLayerName(
   System.int Index,
   System.String^ Value
)
```

### Parameters

- `Index`: Index where to insert custom data
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
[ICustomData::GetLayerName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetLayerName.html)
[ICustomData::SetLayerName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetLayerName.html)

## Availability

DraftSight V1R1.2
