---
title: "Mirror3DEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "Mirror3DEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Mirror3DEntities.html"
---

# Mirror3DEntities Method (ISketchManager)

Creates a mirror image of the specified entities in a 3D plane around a 3D axis.

## Syntax

### Visual Basic

```vb
Sub Mirror3DEntities( _
   ByVal FirstPointOnMirrorPlane As MathPoint, _
   ByVal SecondPointOnMirrorPlane As MathPoint, _
   ByVal ThirdPointOnMirrorPlane As MathPoint, _
   ByVal DeleteSourceEntities As System.Boolean, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void Mirror3DEntities(
   MathPoint FirstPointOnMirrorPlane,
   MathPoint SecondPointOnMirrorPlane,
   MathPoint ThirdPointOnMirrorPlane,
   System.bool DeleteSourceEntities,
   System.object EntitiesArray
)
```

### JScript

```
function Mirror3DEntities(
   FirstPointOnMirrorPlane : MathPoint,
   SecondPointOnMirrorPlane : MathPoint,
   ThirdPointOnMirrorPlane : MathPoint,
   DeleteSourceEntities : System.boolean,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void Mirror3DEntities(
   MathPoint* FirstPointOnMirrorPlane,
   MathPoint* SecondPointOnMirrorPlane,
   MathPoint* ThirdPointOnMirrorPlane,
   System.bool DeleteSourceEntities,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void Mirror3DEntities(
   MathPoint^ FirstPointOnMirrorPlane,
   MathPoint^ SecondPointOnMirrorPlane,
   MathPoint^ ThirdPointOnMirrorPlane,
   System.bool DeleteSourceEntities,
   System.Object^ EntitiesArray
)
```

### Parameters

- `FirstPointOnMirrorPlane`: [First point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on mirror plane
- `SecondPointOnMirrorPlane`: [Second point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on mirror plane
- `ThirdPointOnMirrorPlane`: [Third point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on mirror plane
- `DeleteSourceEntities`: True to delete the source entities, false to keep them
- `EntitiesArray`: Array of entities from which to create a mirror image in a 3D plane

## Remarks

What is originally visible in this 3D plane is copied as a reverse image on the other side of the axis.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::MirrorEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)

## Availability

DraftSight V1R4.0
