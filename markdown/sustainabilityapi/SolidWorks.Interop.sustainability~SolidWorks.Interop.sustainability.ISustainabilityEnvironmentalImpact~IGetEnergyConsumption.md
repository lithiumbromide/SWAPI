---
title: "IGetEnergyConsumption Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "IGetEnergyConsumption"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetEnergyConsumption.html"
---

# IGetEnergyConsumption Method (ISustainabilityEnvironmentalImpact)

Obsolete. Superseded by [ISustainabilityEnvironmentalImpact::IGetEnergyConsumption2](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetEnergyConsumption2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEnergyConsumption( _
   ByRef Values As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim Values As System.Double
Dim value As System.Integer

value = instance.IGetEnergyConsumption(Values)
```

### C#

```csharp
System.int IGetEnergyConsumption(
   ref System.double Values
)
```

### C++/CLI

```cpp
System.int IGetEnergyConsumption(
   System.double% Values
)
```

### Parameters

- `Values`: - in-process, unmanaged C++: Pointer to an array of five doubles of megajoules of energy consumed by material, use, transportation, manufacturing, and end of life environmental impact factors

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Error code as defined in [swSustainabilityErrors_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityErrors_e.html)

## Remarks

Before calling this method, call:

1. [ISustainabilityEnvironmentalImpact::DurationOfUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html)
2. [ISustainabilityEnvironmentalImpact::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html)
3. [ISustainabilityEnvironmentalImpact::UpdateResults](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html)

## See Also

[ISustainabilityEnvironmentalImpact Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact.html)
[ISustainabilityEnvironmentalImpact Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact_members.html)
[ISustainabilityEnvironmentalImpact::GetEnergyConsumption2 Method ()](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetEnergyConsumption2.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
