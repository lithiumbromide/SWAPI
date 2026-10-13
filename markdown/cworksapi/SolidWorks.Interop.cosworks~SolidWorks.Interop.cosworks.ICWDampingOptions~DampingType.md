---
title: "DampingType Property (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "DampingType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~DampingType.html"
---

# DampingType Property (ICWDampingOptions)

Gets and sets the damping type.

## Syntax

### Visual Basic (Declaration)

```vb
Property DampingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim value As System.Integer

instance.DampingType = value

value = instance.DampingType
```

### C#

```csharp
System.int DampingType {get; set;}
```

### C++/CLI

```cpp
property System.int DampingType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Damping type as defined in [swsDampingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDampingType_e.html)

## VBA Syntax

See [CWDampingOptions::DampingType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDampingOptions~DampingType.html).

## Examples

See the [ICWDampingOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html) examples.

## Remarks

For more information about damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)
[ICWDampingOptions::GetDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetDampingRatios.html)
[ICWDampingOptions::SetDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetDampingRatios.html)
[ICWDampingOptions::GetRayleighDampingCoefficients Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetRayleighDampingCoefficients.html)
[ICWDampingOptions::SetRayleighDampingCoefficients Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetRayleighDampingCoefficients.html)
[ICWDampingOptions::ComputeFromMaterialDamping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~ComputeFromMaterialDamping.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
