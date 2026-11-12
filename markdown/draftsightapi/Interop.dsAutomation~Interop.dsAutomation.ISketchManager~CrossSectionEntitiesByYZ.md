---
title: "CrossSectionEntitiesByYZ Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CrossSectionEntitiesByYZ"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByYZ.html"
---

# CrossSectionEntitiesByYZ Method (ISketchManager)

Cross sections the specified solid entities at the specified point on the YZ plane.

## Syntax

### Visual Basic

```vb
Function CrossSectionEntitiesByYZ( _
   ByVal EntitiesArray As System.Object, _
   ByVal PointOnYZPlane As MathPoint, _
   ByRef RegionsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CrossSectionEntitiesByYZ(
   System.object EntitiesArray,
   MathPoint PointOnYZPlane,
   out System.object RegionsArray
)
```

### JScript

```
function CrossSectionEntitiesByYZ(
   EntitiesArray : System.Object,
   PointOnYZPlane : MathPoint,
   RegionsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CrossSectionEntitiesByYZ(
   System.Object* EntitiesArray,
   MathPoint* PointOnYZPlane,
   [PARAMFLAG::Out] System.Object* RegionsArray
)
```

### C++/CLI

```cpp
System.bool CrossSectionEntitiesByYZ(
   System.Object^ EntitiesArray,
   MathPoint^ PointOnYZPlane,
   [Out] System.Object^ RegionsArray
)
```

### Parameters

- `EntitiesArray`: Array of solid entities
- `PointOnYZPlane`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
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
[ISketchManager::CrossSectionEntitiesByZAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZAxis.html)
[ISketchManager::CrossSectionEntitiesByZX Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZX.html)

## Availability

DraftSight 2020 SP0
