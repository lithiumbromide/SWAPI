---
title: "CopyEntities2 Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CopyEntities2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities2.html"
---

# CopyEntities2 Method (ISketchManager)

Copies the specified entities, places the copies at the specified relative location, and returns the copies.

## Syntax

### Visual Basic

```vb
Function CopyEntities2( _
   ByVal DisplacementX As System.Double, _
   ByVal DisplacementY As System.Double, _
   ByVal DisplacementZ As System.Double, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
) As System.Object
```

### C#

```csharp
System.object CopyEntities2(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function CopyEntities2(
   DisplacementX : System.double,
   DisplacementY : System.double,
   DisplacementZ : System.double,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* CopyEntities2(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
System.Object^ CopyEntities2(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `DisplacementX`: x delta of the relative location for the displacement
- `DisplacementY`: y delta of the relative location for the displacement
- `DisplacementZ`: z delta of the relative location for the displacement
- `EntityTypeLongArray`: Array of longs indicating the types of entities to copy as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of entities to copy

### Return Value

Array of new entities

## Examples

[Rotate and Copy Entities (VBA)](Rotate_and_Copy_Entities_Example_VBA.htm)
[Rotate and Copy Entities (VB.NET)](Rotate_and_Copy_Entities_Example_VBNET.htm)
[Rotate and Copy Entities (C#)](Rotate_and_Copy_Entities_Example_CSharp.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2020 SP0
