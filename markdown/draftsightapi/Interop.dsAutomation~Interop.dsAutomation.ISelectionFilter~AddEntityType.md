---
title: "AddEntityType Method (ISelectionFilter)"
project: ""
interface: "ISelectionFilter"
member: "AddEntityType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionFilter~AddEntityType.html"
---

# AddEntityType Method (ISelectionFilter)

Adds the specified drawing entity to the selection filter list.

## Syntax

### Visual Basic

```vb
Sub AddEntityType( _
   ByVal EntityType As dsObjectType_e _
)
```

### C#

```csharp
void AddEntityType(
   dsObjectType_e EntityType
)
```

### JScript

```
function AddEntityType(
   EntityType : dsObjectType_e
);
```

### Managed Extensions for C++

```
void AddEntityType(
   dsObjectType_e EntityType
)
```

### C++/CLI

```cpp
void AddEntityType(
   dsObjectType_e EntityType
)
```

### Parameters

- `EntityType`: Drawing entity to add to the selection filter list as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

## Examples

[Insert SimpleNote (C#)](Insert_SimpleNote_Example_CSharp.htm)
[Insert SimpleNote (VB.NET)](Insert_SimpleNote_Example_VBNET.htm)
[Insert SimpleNote (VBA)](Insert_SimpleNote_Example_VBA.htm)
[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)
[Select and Change Entities (JavaScript)](Select_and_Change_Entities_Example_JS.htm)

## See Also

[ISelectionFilter Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionFilter.html)
[ISelectionFilter Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionFilter_members.html)

## Availability

DraftSight V1R1.1
