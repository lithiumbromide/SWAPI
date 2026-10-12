---
title: "GetCurrentCarbonFootPrint2 Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "GetCurrentCarbonFootPrint2"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetCurrentCarbonFootPrint2.html"
---

# GetCurrentCarbonFootPrint2 Method (ISustainabilityEnvironmentalImpact)

Gets the amount of greenhouse gases emitted during the lifecycle of this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentCarbonFootPrint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim value As System.Object

value = instance.GetCurrentCarbonFootPrint2()
```

### C#

```csharp
System.object GetCurrentCarbonFootPrint2()
```

### C++/CLI

```cpp
System.Object^ GetCurrentCarbonFootPrint2();
```

### Return Value

Array of five doubles of kilograms of carbon dioxide emitted as a result of material, use, transportation, manufacturing, and end of life environmental impact factors

## VBA Syntax

See [SustainabilityEnvironmentalImpact::GetCurrentCarbonFootPrint2](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityEnvironmentalimpact~GetCurrentCarbonFootPrint2.html).

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
[ISustainabilityEnvironmentalImpact::IGetCurrentCarbonFootPrint2 Method ()](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetCurrentCarbonFootPrint2.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP03
