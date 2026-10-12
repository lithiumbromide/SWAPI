---
title: "GetEnergyConsumption Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "GetEnergyConsumption"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetEnergyConsumption.html"
---

# GetEnergyConsumption Method (ISustainabilityEnvironmentalImpact)

Obsolete. Superseded by [ISustainabilityEnvironmentalImpact::GetEnergyConsumption2](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetEnergyConsumption2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEnergyConsumption( _
   ByRef Values As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim Values As System.Object
Dim value As System.Integer

value = instance.GetEnergyConsumption(Values)
```

### C#

```csharp
System.int GetEnergyConsumption(
   out System.object Values
)
```

### C++/CLI

```cpp
System.int GetEnergyConsumption(
   [Out] System.Object^ Values
)
```

### Parameters

- `Values`: Array of five doubles of megajoules of energy consumed by material, use, transportation, manufacturing, and end of life environmental impact factors

## VBA Syntax

See [SustainabilityEnvironmentalImpact::GetEnergyConsumption](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityEnvironmentalimpact~GetEnergyConsumption.html).

## Examples

See the examples in [ISustainabilityEnvironmentalImpact](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact.html).

## Remarks

Before calling this method, call:

1. [ISustainabilityEnvironmentalImpact::DurationOfUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html)
2. [ISustainabilityEnvironmentalImpact::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html)
3. [ISustainabilityEnvironmentalImpact::UpdateResults](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html)

## See Also

[ISustainabilityEnvironmentalImpact Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact.html)
[ISustainabilityEnvironmentalImpact Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact_members.html)
[ISustainabilityEnvironmentalImpact::IGetEnergyConsumption Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetEnergyConsumption.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
