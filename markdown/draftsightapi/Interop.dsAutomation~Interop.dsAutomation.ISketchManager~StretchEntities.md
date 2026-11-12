---
title: "StretchEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "StretchEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html"
---

# StretchEntities Method (ISketchManager)

Changes the relative positions of a sketch entity's nodes, retaining their relations to other nodes in the entity.

## Syntax

### Visual Basic

```vb
Sub StretchEntities( _
   ByVal DisplacementX As System.Double, _
   ByVal DisplacementY As System.Double, _
   ByVal DisplacementZ As System.Double, _
   ByVal EntitiesArray As System.Object, _
   ByVal CrossingBoxStartCornerDblArray As System.Object, _
   ByVal CrossingBoxOppositeCornerDblArray As System.Object _
)
```

### C#

```csharp
void StretchEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.object EntitiesArray,
   System.object CrossingBoxStartCornerDblArray,
   System.object CrossingBoxOppositeCornerDblArray
)
```

### JScript

```
function StretchEntities(
   DisplacementX : System.double,
   DisplacementY : System.double,
   DisplacementZ : System.double,
   EntitiesArray : System.Object,
   CrossingBoxStartCornerDblArray : System.Object,
   CrossingBoxOppositeCornerDblArray : System.Object
);
```

### Managed Extensions for C++

```
void StretchEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object* EntitiesArray,
   System.Object* CrossingBoxStartCornerDblArray,
   System.Object* CrossingBoxOppositeCornerDblArray
)
```

### C++/CLI

```cpp
void StretchEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object^ EntitiesArray,
   System.Object^ CrossingBoxStartCornerDblArray,
   System.Object^ CrossingBoxOppositeCornerDblArray
)
```

### Parameters

- `DisplacementX`: Distance to move the sketch entity's nodes along the x axis
- `DisplacementY`: Distance to move the sketch entity's nodes along the y axis
- `DisplacementZ`: Distance to move the sketch entity's nodes along the z axis
- `EntitiesArray`: Array of entities to stretch (see **Remarks**)
- `CrossingBoxStartCornerDblArray`: Array of the doubles of x, y, and z coordinates of the corner of the crossing rectangle that encloses the entity nodes to stretch
- `CrossingBoxOppositeCornerDblArray`: Array of the doubles of x, y, and z coordinates of the opposite corner of the crossing rectangle that encloses the entity nodes to stretch

## Examples

[Fillet and Stretch Sketch Entities (JavaScript)](Fillet_and_Stretch_Sketch_Entities_Example_JS.htm)
[Fillet and Stretch Sketch Entities (VB.NET)](Fillet_and_Stretch_Sketch_Entities_Example_VBNET.htm)
[Fillet and Stretch Sketch Entities (C#)](Fillet_and_Stretch_Sketch_Entities_Example_CSharp.htm)
[Fillet and Stretch Sketch Entities (VBA)](Fillet_and_Stretch_Sketch_Entities_Example_VBA.htm)

## Remarks

This method works like the DraftSight STRETCH command to change the position of a sketch entity's nodes. You can stretch Lines, PolyLine segments, Rays, Arcs, elliptical Arcs, and Splines.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)

## Availability

DraftSight V1R1.4
