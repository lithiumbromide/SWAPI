---
title: "GetCurrentCarbonFootPrint Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "GetCurrentCarbonFootPrint"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetCurrentCarbonFootPrint.html"
---

# GetCurrentCarbonFootPrint Method (ISustainabilityEnvironmentalImpact)

Obsolete. Superseded by [ISustainabilityEnvironmentalImpact::GetCurrentCarbonFootPrint2](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetCurrentCarbonFootPrint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentCarbonFootPrint( _
   ByRef Values As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim Values As System.Object
Dim value As System.Integer

value = instance.GetCurrentCarbonFootPrint(Values)
```

### C#

```csharp
System.int GetCurrentCarbonFootPrint(
   out System.object Values
)
```

### C++/CLI

```cpp
System.int GetCurrentCarbonFootPrint(
   [Out] System.Object^ Values
)
```

### Parameters

- `Values`: Array of five doubles of kilograms of carbon dioxide emitted as a result of material, use, transportation, manufacturing, and end of life environmental impact factors

## VBA Syntax

See [SustainabilityEnvironmentalImpact::GetCurrentCarbonFootPrint](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityEnvironmentalimpact~GetCurrentCarbonFootPrint.html).

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
[ISustainabilityEnvironmentalImpact::IGetCurrentCarbonFootPrint Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~IGetCurrentCarbonFootPrint.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
