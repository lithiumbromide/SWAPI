---
title: "IGetWaterEutrophication Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "IGetWaterEutrophication"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetWaterEutrophication.html"
---

# IGetWaterEutrophication Method (ISustainabilityEnvironmentalImpact)

Obsolete. Superseded by [ISustainabilityEnvironmentalImpact::IGetWaterEutrophication2](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetWaterEutrophication2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetWaterEutrophication( _
   ByRef Values As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim Values As System.Double
Dim value As System.Integer

value = instance.IGetWaterEutrophication(Values)
```

### C#

```csharp
System.int IGetWaterEutrophication(
   ref System.double Values
)
```

### C++/CLI

```cpp
System.int IGetWaterEutrophication(
   System.double% Values
)
```

### Parameters

- `Values`: - in-process, unmanaged C++: Pointer to an array of five doubles of kilograms of phosphate released into the water as a result of material, use, transportation, manufacturing, and end of life environmental impact factors

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
[IsustainabilityEnvironmentalImpact::GetWaterEutrophication2 Method ()](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetWaterEutrophication2.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
