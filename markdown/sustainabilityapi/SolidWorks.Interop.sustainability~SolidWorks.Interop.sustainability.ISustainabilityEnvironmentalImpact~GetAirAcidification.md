---
title: "GetAirAcidification Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "GetAirAcidification"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetAirAcidification.html"
---

# GetAirAcidification Method (ISustainabilityEnvironmentalImpact)

Obsolete. Superseded by [ISustainabilityEnvironmentalImpact::GetAirAcidification2](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetAirAcidification2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAirAcidification( _
   ByRef Values As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim Values As System.Object
Dim value As System.Integer

value = instance.GetAirAcidification(Values)
```

### C#

```csharp
System.int GetAirAcidification(
   out System.object Values
)
```

### C++/CLI

```cpp
System.int GetAirAcidification(
   [Out] System.Object^ Values
)
```

### Parameters

- `Values`: Array of five doubles of kilograms of sulfur dioxide emitted as a result of material, use, transportation, manufacturing, and end of life environmental impact factors

## VBA Syntax

See [SustainabilityEnvironmentalImpact::GetAirAcidification](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityEnvironmentalimpact~GetAirAcidification.html).

## Remarks

Before calling this method, call:

1. [ISustainabilityEnvironmentalImpact::DurationOfUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html)
2. [ISustainabilityEnvironmentalImpact::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html)
3. [ISustainabilityEnvironmentalImpact::UpdateResults](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html)

## See Also

[ISustainabilityEnvironmentalImpact Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact.html)
[ISustainabilityEnvironmentalImpact Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact_members.html)
[ISustainabilityEnvironmentalImpact::IGetAirAcidification Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetAirAcidification.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
