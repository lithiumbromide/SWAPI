---
title: "Align3DEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "Align3DEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Align3DEntities.html"
---

# Align3DEntities Method (ISketchManager)

Aligns the specified entities in 3D space.

## Syntax

### Visual Basic

```vb
Sub Align3DEntities( _
   ByVal FirstBasePoint As MathPoint, _
   ByVal SecondBasePoint As MathPoint, _
   ByVal ThirdBasePoint As MathPoint, _
   ByVal FirstDestinationPoint As MathPoint, _
   ByVal SecondDestinationPoint As MathPoint, _
   ByVal ThirdDestinationPoint As MathPoint, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void Align3DEntities(
   MathPoint FirstBasePoint,
   MathPoint SecondBasePoint,
   MathPoint ThirdBasePoint,
   MathPoint FirstDestinationPoint,
   MathPoint SecondDestinationPoint,
   MathPoint ThirdDestinationPoint,
   System.object EntitiesArray
)
```

### JScript

```
function Align3DEntities(
   FirstBasePoint : MathPoint,
   SecondBasePoint : MathPoint,
   ThirdBasePoint : MathPoint,
   FirstDestinationPoint : MathPoint,
   SecondDestinationPoint : MathPoint,
   ThirdDestinationPoint : MathPoint,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void Align3DEntities(
   MathPoint* FirstBasePoint,
   MathPoint* SecondBasePoint,
   MathPoint* ThirdBasePoint,
   MathPoint* FirstDestinationPoint,
   MathPoint* SecondDestinationPoint,
   MathPoint* ThirdDestinationPoint,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void Align3DEntities(
   MathPoint^ FirstBasePoint,
   MathPoint^ SecondBasePoint,
   MathPoint^ ThirdBasePoint,
   MathPoint^ FirstDestinationPoint,
   MathPoint^ SecondDestinationPoint,
   MathPoint^ ThirdDestinationPoint,
   System.Object^ EntitiesArray
)
```

### Parameters

- `FirstBasePoint`: [First base point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) to determine the source plane and orientation; the first point is the base point for the move (see **Remarks**)
- `SecondBasePoint`: [Second base point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `ThirdBasePoint`: [Third base point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `FirstDestinationPoint`: [First destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `SecondDestinationPoint`: [Second destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `ThirdDestinationPoint`: [Third destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `EntitiesArray`: Array of entities to align in 3D space

## Remarks

FirstBasePoint moves to FirstDestinationPoint. SecondBasePoint is aligned to SecondDestinationPoint. ThirdBasePoint is aligned to ThirdDestinationPoint. The specified entities are not scaled.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::AlignEntities1Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities1Point.html)
[ISketchManager::AlignEntities2Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities2Point.html)
[ISketchManager::AlignEntities3Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities3Point.html)

## Availability

DraftSight V1R4.0
