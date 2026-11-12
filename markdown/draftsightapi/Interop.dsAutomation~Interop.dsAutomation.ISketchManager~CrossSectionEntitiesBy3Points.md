---
title: "CrossSectionEntitiesBy3Points Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CrossSectionEntitiesBy3Points"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesBy3Points.html"
---

# CrossSectionEntitiesBy3Points Method (ISketchManager)

Cross sections the specified solid entities using the plane described by the specified points.

## Syntax

### Visual Basic

```vb
Function CrossSectionEntitiesBy3Points( _
   ByVal EntitiesArray As System.Object, _
   ByVal FirstPoint As MathPoint, _
   ByVal SecondPoint As MathPoint, _
   ByVal ThirdPoint As MathPoint, _
   ByRef RegionsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CrossSectionEntitiesBy3Points(
   System.object EntitiesArray,
   MathPoint FirstPoint,
   MathPoint SecondPoint,
   MathPoint ThirdPoint,
   out System.object RegionsArray
)
```

### JScript

```
function CrossSectionEntitiesBy3Points(
   EntitiesArray : System.Object,
   FirstPoint : MathPoint,
   SecondPoint : MathPoint,
   ThirdPoint : MathPoint,
   RegionsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CrossSectionEntitiesBy3Points(
   System.Object* EntitiesArray,
   MathPoint* FirstPoint,
   MathPoint* SecondPoint,
   MathPoint* ThirdPoint,
   [PARAMFLAG::Out] System.Object* RegionsArray
)
```

### C++/CLI

```cpp
System.bool CrossSectionEntitiesBy3Points(
   System.Object^ EntitiesArray,
   MathPoint^ FirstPoint,
   MathPoint^ SecondPoint,
   MathPoint^ ThirdPoint,
   [Out] System.Object^ RegionsArray
)
```

### Parameters

- `EntitiesArray`: Array of solid entities
- `FirstPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `SecondPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `ThirdPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `RegionsArray`: Array of [IRegion](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)s

### Return Value

True if cross section is successful, false if not

## Examples

[Cross-sectioning Entities (C#)](Cross-sectioning_Entities_Example_CSharp.htm)
[Cross-sectioning Entities (VB.NET)](Cross-sectioning_Entities_Example_VBNET.htm)
[Cross-sectioning Entities (VBA)](Cross-sectioning_Entities_Example_VBA.htm)
[Cross-sectioning Entities (JS)](Cross-sectioning_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Modifying Solids > Creating Sections from 3D Solids** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CrossSectionEntitiesByEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByEntity.html)
[ISketchManager::CrossSectionEntitiesByView Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByView.html)
[ISketchManager::CrossSectionEntitiesByXY Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByXY.html)
[ISketchManager::CrossSectionEntitiesByYZ Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByYZ.html)
[ISketchManager::CrossSectionEntitiesByZAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZAxis.html)
[ISketchManager::CrossSectionEntitiesByZX Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZX.html)

## Availability

DraftSight 2020 SP0
