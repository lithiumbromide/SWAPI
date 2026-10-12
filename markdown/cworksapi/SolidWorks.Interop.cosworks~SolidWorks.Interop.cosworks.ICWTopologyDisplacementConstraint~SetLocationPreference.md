---
title: "SetLocationPreference Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetLocationPreference"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetLocationPreference.html"
---

# SetLocationPreference Method (ICWTopologyDisplacementConstraint)

Sets the location preference for applying this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLocationPreference( _
   ByVal NLocationPreference As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
Dim NLocationPreference As System.Integer
Dim value As System.Integer

value = instance.SetLocationPreference(NLocationPreference)
```

### C#

```csharp
System.int SetLocationPreference(
   System.int NLocationPreference
)
```

### C++/CLI

```cpp
System.int SetLocationPreference(
   System.int NLocationPreference
)
```

### Parameters

- `NLocationPreference`: Location preference as defined in [swsTopologyStudyDisplacementConstraintLocationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementConstraintLocationOption_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetLocationPreference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetLocationPreference.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

If NLocationPreference is set to swsTopologyStudyDisplacementConstraintLocationOption_e.swsTopologyDisplacementConstraintLocationOption_UserDefine, then use [ICWTopologyDisplacementConstraint::SetVertex](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetVertex.html) to set the vertex from a load-bearing face..

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
