---
title: "PushPullEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "PushPullEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PushPullEntities.html"
---

# PushPullEntities Method (ISketchManager)

Extrudes selected 2D open entities into surfaces or selected 2D closed entities into 3D solids.

## Syntax

### Visual Basic

```vb
Function PushPullEntities( _
   ByVal InternalPoint As MathPoint, _
   ByVal Height As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool PushPullEntities(
   MathPoint InternalPoint,
   System.double Height
)
```

### JScript

```
function PushPullEntities(
   InternalPoint : MathPoint,
   Height : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PushPullEntities(
   MathPoint* InternalPoint,
   System.double Height
)
```

### C++/CLI

```cpp
System.bool PushPullEntities(
   MathPoint^ InternalPoint,
   System.double Height
)
```

### Parameters

- `InternalPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the entity that you want to push or pull
- `Height`: Height of the push or pull

### Return Value

True if successful, false if not

## Examples

[Pushing and Pulling 3D Entities (C#)](Pushing_and_Pulling_3D_Entities_Example_CSharp.htm)
[Pushing and Pulling 3D Entities (VB.NET)](Pushing_and_Pulling_3D_Entities_Example_VBNET.htm)
[Pushing and Pulling 3D Entities (VBA)](Pushing_and_Pulling_3D_Entities_Example_VBA.htm)
[Pushing and Pulling 3D Entities (JS)](Pushing_and_Pulling_3D_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating and Modifying 3D Solids by Pushing and Pulling Geometry** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2020 SP0
