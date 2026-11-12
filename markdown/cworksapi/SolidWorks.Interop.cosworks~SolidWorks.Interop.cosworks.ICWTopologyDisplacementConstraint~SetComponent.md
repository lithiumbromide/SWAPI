---
title: "SetComponent Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetComponent.html"
---

# SetComponent Method (ICWTopologyDisplacementConstraint)

Sets the displacement component of this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponent( _
   ByVal NComponent As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
Dim NComponent As System.Integer
Dim value As System.Integer

value = instance.SetComponent(NComponent)
```

### C#

```csharp
System.int SetComponent(
   System.int NComponent
)
```

### C++/CLI

```cpp
System.int SetComponent(
   System.int NComponent
)
```

### Parameters

- `NComponent`: Displacement component as defined in [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetComponent.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

The displacement constraint equation:

```
disp_component comparator value
```

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
