---
title: "CrossSectionEntitiesByEntity Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CrossSectionEntitiesByEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByEntity.html"
---

# CrossSectionEntitiesByEntity Method (ISketchManager)

Cross sections the specified solid entities using the specified 2D entities.

## Syntax

### Visual Basic

```vb
Function CrossSectionEntitiesByEntity( _
   ByVal EntitiesArray As System.Object, _
   ByVal Entity2DArray As System.Object, _
   ByRef RegionsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool CrossSectionEntitiesByEntity(
   System.object EntitiesArray,
   System.object Entity2DArray,
   out System.object RegionsArray
)
```

### JScript

```
function CrossSectionEntitiesByEntity(
   EntitiesArray : System.Object,
   Entity2DArray : System.Object,
   RegionsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CrossSectionEntitiesByEntity(
   System.Object* EntitiesArray,
   System.Object* Entity2DArray,
   [PARAMFLAG::Out] System.Object* RegionsArray
)
```

### C++/CLI

```cpp
System.bool CrossSectionEntitiesByEntity(
   System.Object^ EntitiesArray,
   System.Object^ Entity2DArray,
   [Out] System.Object^ RegionsArray
)
```

### Parameters

- `EntitiesArray`: Array of solid entities
- `Entity2DArray`: Array of 2D entities: [ICircle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html), [ICircleArc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html), [IEllipseArc](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html), [ISpline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html), and/or [IPolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
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
[ISketchManager::CrossSectionEntitiesByView Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByView.html)
[ISketchManager::CrossSectionEntitiesByXY Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByXY.html)
[ISketchManager::CrossSectionEntitiesByYZ Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByYZ.html)
[ISketchManager::CrossSectionEntitiesByZAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZAxis.html)
[ISketchManager::CrossSectionEntitiesByZX Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CrossSectionEntitiesByZX.html)

## Availability

DraftSight 2020 SP0
