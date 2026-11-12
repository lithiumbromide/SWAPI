---
title: "InsertViewTiles Method (IModel)"
project: ""
interface: "IModel"
member: "InsertViewTiles"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModel~InsertViewTiles.html"
---

# InsertViewTiles Method (IModel)

Inserts ViewTiles in the specified mode at the specified location in this model.

## Syntax

### Visual Basic

```vb
Function InsertViewTiles( _
   ByVal Mode As dsViewTilesMode_e, _
   ByVal ApplyTo As dsViewTilesApplyTo_e _
) As System.Object
```

### C#

```csharp
System.object InsertViewTiles(
   dsViewTilesMode_e Mode,
   dsViewTilesApplyTo_e ApplyTo
)
```

### JScript

```
function InsertViewTiles(
   Mode : dsViewTilesMode_e,
   ApplyTo : dsViewTilesApplyTo_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* InsertViewTiles(
   dsViewTilesMode_e Mode,
   dsViewTilesApplyTo_e ApplyTo
)
```

### C++/CLI

```cpp
System.Object^ InsertViewTiles(
   dsViewTilesMode_e Mode,
   dsViewTilesApplyTo_e ApplyTo
)
```

### Parameters

- `Mode`: Mode in which to insert the ViewTiles as defined in [dsViewTilesMode_e](Interop.dsAutomation~Interop.dsAutomation.dsViewTilesMode_e.html)
- `ApplyTo`: Where to insert the ViewTiles as defined in [dsViewTilesApplyTo_e](Interop.dsAutomation~Interop.dsAutomation.dsViewTilesApplyTo_e.html)

### Return Value

Array of [ViewTiles](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)

## Examples

[Insert ViewTiles in Model (C#)](Insert_ViewTiles_in_Model_Example_CSharp.htm)
[Insert ViewTiles in Model (VB.NET)](Insert_ViewTiles_in_Model_Example_VBNET.htm)
[Insert ViewTiles in Model (VBA)](Insert_ViewTiles_in_Model_Example_VBA.htm)

## See Also

[IModel Interface](Interop.dsAutomation~Interop.dsAutomation.IModel.html)
[IModel Members](Interop.dsAutomation~Interop.dsAutomation.IModel_members.html)
[IModel::GetActiveViewTile Method ()](Interop.dsAutomation~Interop.dsAutomation.IModel~GetActiveViewTile.html)
[IModel::GetViewTiles Method ()](Interop.dsAutomation~Interop.dsAutomation.IModel~GetViewTiles.html)

## Availability

DraftSight V1R6.0
