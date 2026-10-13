---
title: "SetName Method (ICWTopologyFrequencyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFrequencyConstraint"
member: "SetName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~SetName.html"
---

# SetName Method (ICWTopologyFrequencyConstraint)

Sets the name of this topology study frequency constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFrequencyConstraint
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

- `SName`: Name of the frequency constraint

### Return Value

Result code as defined in [swsTopologyStudy_FrequencyConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FrequencyConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFrequencyConstraint::SetName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFrequencyConstraint~SetName.html).

## Examples

See the [ICWTopologyFrequencyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html) example.

## See Also

[ICWTopologyFrequencyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html)
[ICWTopologyFrequencyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint_members.html)
[ICWTopologyFrequencyConstraint::GetName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~GetName.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
