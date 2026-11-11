---
title: "AlignEntities3Point Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "AlignEntities3Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities3Point.html"
---

# AlignEntities3Point Method (ISketchManager)

Aligns the specified entities using three pairs of points.

## Syntax

### Visual Basic

```vb
Sub AlignEntities3Point( _
   ByVal FirstSourcePoint As MathPoint, _
   ByVal FirstDestinationPoint As MathPoint, _
   ByVal SecondSourcePoint As MathPoint, _
   ByVal SecondDestinationPoint As MathPoint, _
   ByVal ThirdSourcePoint As MathPoint, _
   ByVal ThirdDestinationPoint As MathPoint, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void AlignEntities3Point(
   MathPoint FirstSourcePoint,
   MathPoint FirstDestinationPoint,
   MathPoint SecondSourcePoint,
   MathPoint SecondDestinationPoint,
   MathPoint ThirdSourcePoint,
   MathPoint ThirdDestinationPoint,
   System.object EntitiesArray
)
```

### JScript

```
function AlignEntities3Point(
   FirstSourcePoint : MathPoint,
   FirstDestinationPoint : MathPoint,
   SecondSourcePoint : MathPoint,
   SecondDestinationPoint : MathPoint,
   ThirdSourcePoint : MathPoint,
   ThirdDestinationPoint : MathPoint,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void AlignEntities3Point(
   MathPoint* FirstSourcePoint,
   MathPoint* FirstDestinationPoint,
   MathPoint* SecondSourcePoint,
   MathPoint* SecondDestinationPoint,
   MathPoint* ThirdSourcePoint,
   MathPoint* ThirdDestinationPoint,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void AlignEntities3Point(
   MathPoint^ FirstSourcePoint,
   MathPoint^ FirstDestinationPoint,
   MathPoint^ SecondSourcePoint,
   MathPoint^ SecondDestinationPoint,
   MathPoint^ ThirdSourcePoint,
   MathPoint^ ThirdDestinationPoint,
   System.Object^ EntitiesArray
)
```

### Parameters

- `FirstSourcePoint`: [First source point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `FirstDestinationPoint`: [First destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `SecondSourcePoint`: [Second source point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `SecondDestinationPoint`: [Second destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `ThirdSourcePoint`: [Third source point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `ThirdDestinationPoint`: [Third destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `EntitiesArray`: Array of entities to align

## Remarks

Specifying three pairs of points:

- moves FirstSourcePoint to FirstDestinationPoint
- rotates FirstSourcePoint and SecondSourcePoint and aligns them with FirstDestinationPoint and SecondDestinationPoint
- aligns FirstSourcePoint and ThirdSourcePoint to SecondDestinationPoint and ThirdDestinationPoint

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::Align3DEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Align3DEntities.html)
[ISketchManager::AlignEntities1Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities1Point.html)
[ISketchManager::AlignEntities2Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities2Point.html)

## Availability

DraftSight V1R4.0
