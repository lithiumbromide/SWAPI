---
title: "SetDirectionEntity Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "SetDirectionEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html"
---

# SetDirectionEntity Method (ICWDynamicInitialCondition)

Sets the face, edge, plane, or axis in whose direction this initial condition is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirectionEntity( _
   ByVal RefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim RefEntity As System.Object

instance.SetDirectionEntity(RefEntity)
```

### C#

```csharp
void SetDirectionEntity(
   System.object RefEntity
)
```

### C++/CLI

```cpp
void SetDirectionEntity(
   System.Object^ RefEntity
)
```

### Parameters

- `RefEntity`: Face (planar or cylindrical), edge, plane, or cylindrical axis direction reference

## VBA Syntax

See [CWDynamicInitialCondition::SetDirectionEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~SetDirectionEntity.html).

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::GetDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections.html)
[ICWDynamicInitialCondition::GetValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetValues.html)
[ICWDynamicInitialCondition::SetDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirections.html)
[ICWDynamicInitialCondition::SetValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetValues.html)
[ICWDynamicInitialCondition::GetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetReverseDirections.html)
[ICWDynamicInitialCondition::SetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetReverseDirections.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
