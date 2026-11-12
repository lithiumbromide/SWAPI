---
title: "DurationOfUse Property (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "DurationOfUse"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html"
---

# DurationOfUse Property (ISustainabilityEnvironmentalImpact)

Gets or sets the product use time over which to evaluate environmental impact.

## Syntax

### Visual Basic (Declaration)

```vb
Property DurationOfUse As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim value As System.Double

instance.DurationOfUse = value

value = instance.DurationOfUse
```

### C#

```csharp
System.double DurationOfUse {get; set;}
```

### C++/CLI

```cpp
property System.double DurationOfUse {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Product use time over which to evaluate environmental impact

## VBA Syntax

See [SustainabilityEnvironmentalImpact::DurationOfUse](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityEnvironmentalimpact~DurationOfUse.html).

## Examples

See the examples in [ISustainabilityEnvironmentalImpact](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact.html).

## Remarks

After calling this method, call:

1. [ISustainabilityEnvironmentalImpact::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html)
2. [ISustainabilityEnvironmentalImpact::UpdateResults](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html)
3. One or more [ISustainabilityEnvironmentalImpact](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact.html) methods

## See Also

[ISustainabilityEnvironmentalImpact Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact.html)
[ISustainabilityEnvironmentalImpact Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
