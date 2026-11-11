---
title: "AlignEntities1Point Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "AlignEntities1Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities1Point.html"
---

# AlignEntities1Point Method (ISketchManager)

Aligns the specified entities, without rotating them, using one pair of points.

## Syntax

### Visual Basic

```vb
Sub AlignEntities1Point( _
   ByVal SourcePoint As MathPoint, _
   ByVal DestinationPoint As MathPoint, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void AlignEntities1Point(
   MathPoint SourcePoint,
   MathPoint DestinationPoint,
   System.object EntitiesArray
)
```

### JScript

```
function AlignEntities1Point(
   SourcePoint : MathPoint,
   DestinationPoint : MathPoint,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void AlignEntities1Point(
   MathPoint* SourcePoint,
   MathPoint* DestinationPoint,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void AlignEntities1Point(
   MathPoint^ SourcePoint,
   MathPoint^ DestinationPoint,
   System.Object^ EntitiesArray
)
```

### Parameters

- `SourcePoint`: [Source point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `DestinationPoint`: [Destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `EntitiesArray`: Array of entities to align without rotating them

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::Align3DEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Align3DEntities.html)
[ISketchManager::AlignEntities2Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities2Point.html)
[ISketchManager::AlignEntities3Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities3Point.html)

## Availability

DraftSight V1R4.0
