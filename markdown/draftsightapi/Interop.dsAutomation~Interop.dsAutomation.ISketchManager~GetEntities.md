---
title: "GetEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "GetEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html"
---

# GetEntities Method (ISketchManager)

Get the specified entities and their types.

## Syntax

### Visual Basic

```vb
Sub GetEntities( _
   ByVal Filter As SelectionFilter, _
   ByVal LayerNamesStrArray As System.Object, _
   ByRef EntityTypeLongArray As System.Object, _
   ByRef EntitiesArray As System.Object _
)
```

### C#

```csharp
void GetEntities(
   SelectionFilter Filter,
   System.object LayerNamesStrArray,
   out System.object EntityTypeLongArray,
   out System.object EntitiesArray
)
```

### JScript

```
function GetEntities(
   Filter : SelectionFilter,
   LayerNamesStrArray : System.Object,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void GetEntities(
   SelectionFilter* Filter,
   System.Object* LayerNamesStrArray,
   [PARAMFLAG::Out] System.Object* EntityTypeLongArray,
   [PARAMFLAG::Out] System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void GetEntities(
   SelectionFilter^ Filter,
   System.Object^ LayerNamesStrArray,
   [Out] System.Object^ EntityTypeLongArray,
   [Out] System.Object^ EntitiesArray
)
```

### Parameters

- `Filter`: [Selection filter](Interop.dsAutomation~Interop.dsAutomation.ISelectionFilter.html) indicating which entities to get or a null value to accept all types of entities
- `LayerNamesStrArray`: Array of strings of the [names of the Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer~Name.html) where the entities reside
- `EntityTypeLongArray`: Array of longs indicating the types of entities returned as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities returned

## Examples

[Get and Set Hatch Pattern Data (C#)](Get_and_Set_Hatch_Pattern_Data_Example_CSharp.htm)
[Get and Set Hatch Pattern Data (VB.NET)](Get_and_Set_Hatch_Pattern_Data_Example_VBNET.htm)
[Get and Set Hatch Pattern Data (VBA)](Get_and_Set_Hatch_Pattern_Data_Example_VBA.htm)
[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)
[Select and Change Entities (JavaScript)](Select_and_Change_Entities_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISelectionManager::GetSelectedObject Method](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjects Method](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)
[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)

## Availability

DraftSight V1R1.3
