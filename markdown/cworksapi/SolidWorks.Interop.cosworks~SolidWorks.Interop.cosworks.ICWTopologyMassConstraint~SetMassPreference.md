---
title: "SetMassPreference Method (ICWTopologyMassConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMassConstraint"
member: "SetMassPreference"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetMassPreference.html"
---

# SetMassPreference Method (ICWTopologyMassConstraint)

Sets the reduce-mass-by preference for this topology study mass constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMassPreference( _
   ByVal NPreference As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMassConstraint
Dim NPreference As System.Integer
Dim value As System.Integer

value = instance.SetMassPreference(NPreference)
```

### C#

```csharp
System.int SetMassPreference(
   System.int NPreference
)
```

### C++/CLI

```cpp
System.int SetMassPreference(
   System.int NPreference
)
```

### Parameters

- `NPreference`: Reduce-mass-by preference as defined in [swsTopologyStudyMassConstraintOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyMassConstraintOption_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_MassConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MassConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyMassConstraint::SetMassPreference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMassConstraint~SetMassPreference.html).

## Examples

See the [ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html) example.

## Remarks

## See Also

[ICWTopologyMassConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
[ICWTopologyMassConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
