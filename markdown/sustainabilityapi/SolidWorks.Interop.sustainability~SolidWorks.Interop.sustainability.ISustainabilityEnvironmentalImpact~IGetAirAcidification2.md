---
title: "IGetAirAcidification2 Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "IGetAirAcidification2"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetAirAcidification2.html"
---

# IGetAirAcidification2 Method (ISustainabilityEnvironmentalImpact)

Gets the amount of sulfur dioxide emitted during the lifecycle of this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAirAcidification2() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim value As System.Double

value = instance.IGetAirAcidification2()
```

### C#

```csharp
System.double IGetAirAcidification2()
```

### C++/CLI

```cpp
System.double IGetAirAcidification2();
```

### Return Value

- In-process, unmanaged C++: Pointer to an array of five doubles of kilograms of sulfur dioxide emitted as a result of material, use, transportation, manufacturing, and end of life environmental impact factors

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call:

1. [ISustainabilityEnvironmentalImpact::DurationOfUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html)
2. [ISustainabilityEnvironmentalImpact::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html)
3. [ISustainabilityEnvironmentalImpact::UpdateResults](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html)

## See Also

[ISustainabilityEnvironmentalImpact Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact.html)
[ISustainabilityEnvironmentalImpact Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact_members.html)
[ISustainabilityEnvironmentalImpact::GetAirAcidification2 Method ()](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetAirAcidification2.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP03
