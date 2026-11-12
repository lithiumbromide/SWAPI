---
title: "SetName Method (ICWTopologyMassConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMassConstraint"
member: "SetName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetName.html"
---

# SetName Method (ICWTopologyMassConstraint)

Sets the name of this topology study mass constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMassConstraint
Dim SName As System.String
Dim value As System.Integer

value = instance.SetName(SName)
```

### C#

```csharp
System.int SetName(
   System.string SName
)
```

### C++/CLI

```cpp
System.int SetName(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the mass constraint

### Return Value

Result code as defined in [swsTopologyStudy_MassConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MassConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyMassConstraint::SetName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMassConstraint~SetName.html).

## See Also

[ICWTopologyMassConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
[ICWTopologyMassConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint_members.html)
[ICWTopologyMassConstraint::GetName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~GetName.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
