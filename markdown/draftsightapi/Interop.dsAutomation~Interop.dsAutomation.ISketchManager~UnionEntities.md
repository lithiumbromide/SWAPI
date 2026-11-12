---
title: "UnionEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "UnionEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~UnionEntities.html"
---

# UnionEntities Method (ISketchManager)

Unites the specified Regions or 3D solids to create a composite Region or a 3D solid.

## Syntax

### Visual Basic

```vb
Function UnionEntities( _
   ByVal EntitiesArray As System.Object, _
   ByRef ObjectsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool UnionEntities(
   System.object EntitiesArray,
   out System.object ObjectsArray
)
```

### JScript

```
function UnionEntities(
   EntitiesArray : System.Object,
   ObjectsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool UnionEntities(
   System.Object* EntitiesArray,
   [PARAMFLAG::Out] System.Object* ObjectsArray
)
```

### C++/CLI

```cpp
System.bool UnionEntities(
   System.Object^ EntitiesArray,
   [Out] System.Object^ ObjectsArray
)
```

### Parameters

- `EntitiesArray`: Array of [IRegion](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)s or [ISolid3D](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)s
- `ObjectsArray`: Array of [IRegion](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)s or [ISolid3D](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)s

### Return Value

True if successful, false if not

## Examples

[Unifying, Subtracting, and Intersecting Entities (C#)](Unifying_Subtracting_and_Intersecting_Entities_Example_CSharp.htm)
[Unifying, Subtracting, and Intersecting Entities (VB.NET)](Unifying_Subtracting_and_Intersecting_Entities_Example_VBNET.htm)
[Unifying, Subtracting, and Intersecting Entities (VBA)](Unifying_Subtracting_and_Intersecting_Entities_Example_VBA.htm)
[Unifying, Subtracting, and Intersecting Entities (JS)](Unifying_Subtracting_Intersecting_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Modifying Solids > Unifying 3D Solids or Regions** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::IntersectEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~IntersectEntities.html)
[ISketchManager::SubtractEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SubtractEntities.html)

## Availability

DraftSight 2020 SP0
