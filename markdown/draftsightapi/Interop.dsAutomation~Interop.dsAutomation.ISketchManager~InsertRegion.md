---
title: "InsertRegion Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertRegion"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRegion.html"
---

# InsertRegion Method (ISketchManager)

Constructs a Region for each selected entity.

## Syntax

### Visual Basic

```vb
Sub InsertRegion( _
   ByVal EntitiesArray As System.Object, _
   ByRef RegionArray As System.Object _
)
```

### C#

```csharp
void InsertRegion(
   System.object EntitiesArray,
   out System.object RegionArray
)
```

### JScript

```
function InsertRegion(
   EntitiesArray : System.Object,
   RegionArray : System.Object
);
```

### Managed Extensions for C++

```
void InsertRegion(
   System.Object* EntitiesArray,
   [PARAMFLAG::Out] System.Object* RegionArray
)
```

### C++/CLI

```cpp
void InsertRegion(
   System.Object^ EntitiesArray,
   [Out] System.Object^ RegionArray
)
```

### Parameters

- `EntitiesArray`: Entities to transform to Regions
- `RegionArray`: Array of [Regions](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)

## Examples

[Transform Circle to Region (C#)](Transform_Circle_to_Region_Example_CSharp.htm)
[Transform Circle to Region (VB.NET)](Transform_Circle_to_Region_Example_VBNET.htm)
[Transform Circle to Region (VBA)](Transform_Circle_to_Region_Example_VBA.htm)
[Transform Circle to Regtion (JavaScript)](Transform_Circle_to_Region_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R2.0
