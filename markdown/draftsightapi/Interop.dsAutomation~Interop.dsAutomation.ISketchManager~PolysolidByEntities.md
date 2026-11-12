---
title: "PolysolidByEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "PolysolidByEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PolysolidByEntities.html"
---

# PolysolidByEntities Method (ISketchManager)

Creates a PolySolid using the specified 2D entities, height, and width.

## Syntax

### Visual Basic

```vb
Function PolysolidByEntities( _
   ByVal EntitiesArray As System.Object, _
   ByVal Height As System.Double, _
   ByVal Width As System.Double, _
   ByVal Justify As dsPolySolidJustification_e _
) As Solid3D
```

### C#

```csharp
Solid3D PolysolidByEntities(
   System.object EntitiesArray,
   System.double Height,
   System.double Width,
   dsPolySolidJustification_e Justify
)
```

### JScript

```
function PolysolidByEntities(
   EntitiesArray : System.Object,
   Height : System.double,
   Width : System.double,
   Justify : dsPolySolidJustification_e
) : Solid3D;
```

### Managed Extensions for C++

```
Solid3D* PolysolidByEntities(
   System.Object* EntitiesArray,
   System.double Height,
   System.double Width,
   dsPolySolidJustification_e Justify
)
```

### C++/CLI

```cpp
Solid3D^ PolysolidByEntities(
   System.Object^ EntitiesArray,
   System.double Height,
   System.double Width,
   dsPolySolidJustification_e Justify
)
```

### Parameters

- `EntitiesArray`: Array of 2D entities that define the shape of the polygonal walls of the PolySolid
- `Height`: Height of the PolySolid
- `Width`: Width of the PolySolid
- `Justify`: Placement of the PolySolid as defined in [dsPolySolidJustification_e](Interop.dsAutomation~Interop.dsAutomation.dsPolySolidJustification_e.html)

### Return Value

[ISolid3D](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)

## Examples

[Unifying, Subtracting, and Intersecting Entities (C#)](Unifying_Subtracting_and_Intersecting_Entities_Example_CSharp.htm)
[Creating Polysolid Entities (C#)](Creating_Polysolid_Entities_Example_CSharp.htm)
[Creating Polysolid Entities (VB.NET)](Creating_Polysolid_Entities_Example_VBNET.htm)
[Creating Polysolid Entities (VBA)](Creating_Polysolid_Entities_Example_VBA.htm)
[Creating Polysolid Entities (JS)](Creating_Polysolid_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating PolySolids** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::PolysolidByCoordinates Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PolysolidByCoordinates.html)

## Availability

DraftSight 2020 SP0
