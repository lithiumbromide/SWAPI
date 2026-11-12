---
title: "FilletEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "FilletEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html"
---

# FilletEntities Method (ISketchManager)

Connects two entities with a fillet arc that is tangent to both entities.

## Syntax

### Visual Basic

```vb
Sub FilletEntities( _
   ByVal FirstPointOnEntityDblArray As System.Object, _
   ByVal FirstEntityArray As System.Object, _
   ByVal SecondPointOnEntityDblArray As System.Object, _
   ByVal SecondEntityArray As System.Object _
)
```

### C#

```csharp
void FilletEntities(
   System.object FirstPointOnEntityDblArray,
   System.object FirstEntityArray,
   System.object SecondPointOnEntityDblArray,
   System.object SecondEntityArray
)
```

### JScript

```
function FilletEntities(
   FirstPointOnEntityDblArray : System.Object,
   FirstEntityArray : System.Object,
   SecondPointOnEntityDblArray : System.Object,
   SecondEntityArray : System.Object
);
```

### Managed Extensions for C++

```
void FilletEntities(
   System.Object* FirstPointOnEntityDblArray,
   System.Object* FirstEntityArray,
   System.Object* SecondPointOnEntityDblArray,
   System.Object* SecondEntityArray
)
```

### C++/CLI

```cpp
void FilletEntities(
   System.Object^ FirstPointOnEntityDblArray,
   System.Object^ FirstEntityArray,
   System.Object^ SecondPointOnEntityDblArray,
   System.Object^ SecondEntityArray
)
```

### Parameters

- `FirstPointOnEntityDblArray`: Array of doubles of x, y, and z coordinates of points on the entities in FirstEntityArray; these points define the sides of the entities to fillet
- `FirstEntityArray`: Array of entities to fillet (see **Remarks**)
- `SecondPointOnEntityDblArray`: Array of doubles of x, y, and z coordinates of points on the entities in SecondEntityArray; these points define the sides of the entities to fillet
- `SecondEntityArray`: Array of entities to fillet (see **Remarks**)

## Examples

[Fillet and Stretch Sketch Entities (JavaScript)](Fillet_and_Stretch_Sketch_Entities_Example_JS.htm)
[Fillet and Stretch Sketch Entities (VB.NET)](Fillet_and_Stretch_Sketch_Entities_Example_VBNET.htm)
[Fillet and Stretch Sketch Entities (C#)](Fillet_and_Stretch_Sketch_Entities_Example_CSharp.htm)
[Fillet and Stretch Sketch Entities (VBA)](Fillet_and_Stretch_Sketch_Entities_Example_VBA.htm)

## Remarks

This method works like the DraftSight FILLET command to create fillets, except that entities are modified even if the specified points would not select the entities. Internally, the entity closet to the pick point is taken.

This method creates a fillet for each FirstEntityArray[i] - SecondEntityArray[i] pair.

Before calling this method, set the fillet radius by calling [IDocument::SetCommandOptionDouble](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionDouble.html) with argument Var = [dsCommandOptionDouble_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionDouble_e.html).dsCommandOptionDouble_SetFltRad. A fillet radius of 0 creates an acute corner.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::FilletPolyLine Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletPolyLine.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)

## Availability

DraftSight V1R1.4
