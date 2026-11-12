---
title: "SetLayerName Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetLayerName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetLayerName.html"
---

# SetLayerName Method (ICustomData)

Sets the specified custom data element whose value is the name of a Layer.

## Syntax

### Visual Basic

```vb
Sub SetLayerName( _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void SetLayerName(
   System.int Index,
   System.string Value
)
```

### JScript

```
function SetLayerName(
   Index : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void SetLayerName(
   System.int Index,
   System.string* Value
)
```

### C++/CLI

```cpp
void SetLayerName(
   System.int Index,
   System.String^ Value
)
```

### Parameters

- `Index`: Index of the custom data element
- `Value`: Name of a Layer

## Examples

[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetLayerName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetLayerName.html)
[ICustomData::InsertLayerName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertLayerName.html)

## Availability

DraftSight V1R1.2
