---
title: "MirrorEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "MirrorEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html"
---

# MirrorEntities Method (ISketchManager)

Mirrors the specified entities onto the opposite side of the specified mirror line.

## Syntax

### Visual Basic

```vb
Sub MirrorEntities( _
   ByVal StartPointOfMirrorLineX As System.Double, _
   ByVal StartPointOfMirrorLineY As System.Double, _
   ByVal StartPointOfMirrorLineZ As System.Double, _
   ByVal EndPointOfMirrorLineX As System.Double, _
   ByVal EndPointOfMirrorLineY As System.Double, _
   ByVal EndPointOfMirrorLineZ As System.Double, _
   ByVal DeleteSourceEntities As System.Boolean, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void MirrorEntities(
   System.double StartPointOfMirrorLineX,
   System.double StartPointOfMirrorLineY,
   System.double StartPointOfMirrorLineZ,
   System.double EndPointOfMirrorLineX,
   System.double EndPointOfMirrorLineY,
   System.double EndPointOfMirrorLineZ,
   System.bool DeleteSourceEntities,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function MirrorEntities(
   StartPointOfMirrorLineX : System.double,
   StartPointOfMirrorLineY : System.double,
   StartPointOfMirrorLineZ : System.double,
   EndPointOfMirrorLineX : System.double,
   EndPointOfMirrorLineY : System.double,
   EndPointOfMirrorLineZ : System.double,
   DeleteSourceEntities : System.boolean,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void MirrorEntities(
   System.double StartPointOfMirrorLineX,
   System.double StartPointOfMirrorLineY,
   System.double StartPointOfMirrorLineZ,
   System.double EndPointOfMirrorLineX,
   System.double EndPointOfMirrorLineY,
   System.double EndPointOfMirrorLineZ,
   System.bool DeleteSourceEntities,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void MirrorEntities(
   System.double StartPointOfMirrorLineX,
   System.double StartPointOfMirrorLineY,
   System.double StartPointOfMirrorLineZ,
   System.double EndPointOfMirrorLineX,
   System.double EndPointOfMirrorLineY,
   System.double EndPointOfMirrorLineZ,
   System.bool DeleteSourceEntities,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `StartPointOfMirrorLineX`: x coordinate of the start point of the mirror line
- `StartPointOfMirrorLineY`: y coordinate of the start point of the mirror line
- `StartPointOfMirrorLineZ`: z coordinate of the start point of the mirror line
- `EndPointOfMirrorLineX`: x coordinate of the end point of the mirror line
- `EndPointOfMirrorLineY`: y coordinate of the end point of the mirror line
- `EndPointOfMirrorLineZ`: z coordinate of the end point of the mirror line
- `DeleteSourceEntities`: True to delete the entities to mirror, false to not
- `EntityTypeLongArray`: Array of longs of the types of entities to mirror as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities to mirror

## Examples

[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::Mirror3DEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Mirror3DEntities.html)

## Availability

DraftSight V1R1.3
