---
title: "CrossSectionEntitiesByZX Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CrossSectionEntitiesByZX"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZX.html"
---

# CrossSectionEntitiesByZX Method (ISketchManager)

Cross sections the specified solid entities at the specified point on the ZX plane.

## Syntax

### Visual Basic

```vb
Function CrossSectionEntitiesByZX( _
   ByVal EntitiesArray As System.Object, _
   ByVal PointOnZXPlane As MathPoint, _
   ByRef RegionsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CrossSectionEntitiesByZX(
   System.object EntitiesArray,
   MathPoint PointOnZXPlane,
   out System.object RegionsArray
)
```

### JScript

```
function CrossSectionEntitiesByZX(
   EntitiesArray : System.Object,
   PointOnZXPlane : MathPoint,
   RegionsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CrossSectionEntitiesByZX(
   System.Object* EntitiesArray,
   MathPoint* PointOnZXPlane,
   [PARAMFLAG::Out] System.Object* RegionsArray
)
```

### C++/CLI

```cpp
System.bool CrossSectionEntitiesByZX(
   System.Object^ EntitiesArray,
   MathPoint^ PointOnZXPlane,
   [Out] System.Object^ RegionsArray
)
```

### Parameters

- `EntitiesArray`: Array of solid entities
- `PointOnZXPlane`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `RegionsArray`: Array of [IRegion](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)s

### Return Value

True if cross section is successful, false if not

## Examples

[Cross-sectioning Entities (C#)](Cross-sectioning_Entities_Example_CSharp.htm)
[Cross-sectioning Entities (VB.NET)](Cross-sectioning_Entities_Example_VBNET.htm)
[Cross-sectioning Entities (VBA)](Cross-sectioning_Entities_Example_VBA.htm)
[Cross-sectioning Entities (JS)](Cross-sectioning_Entities_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CrossSectionEntitiesBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesBy3Points.html)
[ISketchManager::CrossSectionEntitiesByEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByEntity.html)
[ISketchManager::CrossSectionEntitiesByView Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByView.html)
[ISketchManager::CrossSectionEntitiesByXY Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByXY.html)
[ISketchManager::CrossSectionEntitiesByYZ Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByYZ.html)
[ISketchManager::CrossSectionEntitiesByZAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZAxis.html)

## Availability

DraftSight 2020 SP0
