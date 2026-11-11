---
title: "CrossSectionEntitiesByZAxis Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CrossSectionEntitiesByZAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZAxis.html"
---

# CrossSectionEntitiesByZAxis Method (ISketchManager)

Cross sections the specified solid entities at the specified point on the section plane that is normal to the specified Z-axis.

## Syntax

### Visual Basic

```vb
Function CrossSectionEntitiesByZAxis( _
   ByVal EntitiesArray As System.Object, _
   ByVal PointOnSectionPlane As MathPoint, _
   ByVal PointOnZAxis As MathPoint, _
   ByRef RegionsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CrossSectionEntitiesByZAxis(
   System.object EntitiesArray,
   MathPoint PointOnSectionPlane,
   MathPoint PointOnZAxis,
   out System.object RegionsArray
)
```

### JScript

```
function CrossSectionEntitiesByZAxis(
   EntitiesArray : System.Object,
   PointOnSectionPlane : MathPoint,
   PointOnZAxis : MathPoint,
   RegionsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CrossSectionEntitiesByZAxis(
   System.Object* EntitiesArray,
   MathPoint* PointOnSectionPlane,
   MathPoint* PointOnZAxis,
   [PARAMFLAG::Out] System.Object* RegionsArray
)
```

### C++/CLI

```cpp
System.bool CrossSectionEntitiesByZAxis(
   System.Object^ EntitiesArray,
   MathPoint^ PointOnSectionPlane,
   MathPoint^ PointOnZAxis,
   [Out] System.Object^ RegionsArray
)
```

### Parameters

- `EntitiesArray`: Array of solid entities
- `PointOnSectionPlane`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `PointOnZAxis`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on Z-axis, normal to the section plane
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
[ISketchManager::CrossSectionEntitiesByZX Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZX.html)

## Availability

DraftSight 2020 SP0
