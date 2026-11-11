---
title: "ExplodeEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ExplodeEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExplodeEntities.html"
---

# ExplodeEntities Method (ISketchManager)

Explodes a complex object comprised of the specified entities.

## Syntax

### Visual Basic

```vb
Sub ExplodeEntities( _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void ExplodeEntities(
   System.object EntitiesArray
)
```

### JScript

```
function ExplodeEntities(
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void ExplodeEntities(
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void ExplodeEntities(
   System.Object^ EntitiesArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to explode

## Remarks

Use this method to break a complex object into its component entities. You can explode [Blocks](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html) and other complex objects like [PolyLines](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html), [Hatches](Interop.dsAutomation~Interop.dsAutomation.IHatch.html), and [Dimensions](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html). You can get the resulting entities using the previous selection set.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R4.0
