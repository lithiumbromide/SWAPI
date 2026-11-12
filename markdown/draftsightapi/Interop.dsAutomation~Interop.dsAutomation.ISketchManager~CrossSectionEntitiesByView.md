---
title: "CrossSectionEntitiesByView Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CrossSectionEntitiesByView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByView.html"
---

# CrossSectionEntitiesByView Method (ISketchManager)

Cross sections the specified solid entities at the specified point on the active view plane.

## Syntax

### Visual Basic

```vb
Function CrossSectionEntitiesByView( _
   ByVal EntitiesArray As System.Object, _
   ByVal PointOnActiveViewPlane As MathPoint, _
   ByRef RegionsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CrossSectionEntitiesByView(
   System.object EntitiesArray,
   MathPoint PointOnActiveViewPlane,
   out System.object RegionsArray
)
```

### JScript

```
function CrossSectionEntitiesByView(
   EntitiesArray : System.Object,
   PointOnActiveViewPlane : MathPoint,
   RegionsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CrossSectionEntitiesByView(
   System.Object* EntitiesArray,
   MathPoint* PointOnActiveViewPlane,
   [PARAMFLAG::Out] System.Object* RegionsArray
)
```

### C++/CLI

```cpp
System.bool CrossSectionEntitiesByView(
   System.Object^ EntitiesArray,
   MathPoint^ PointOnActiveViewPlane,
   [Out] System.Object^ RegionsArray
)
```

### Parameters

- `EntitiesArray`: Array of solid entities
- `PointOnActiveViewPlane`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
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
[ISketchManager::CrossSectionEntitiesByXY Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByXY.html)
[ISketchManager::CrossSectionEntitiesByYZ Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByYZ.html)
[ISketchManager::CrossSectionEntitiesByZAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZAxis.html)
[ISketchManager::CrossSectionEntitiesByZX Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZX.html)

## Availability

DraftSight 2020 SP0
