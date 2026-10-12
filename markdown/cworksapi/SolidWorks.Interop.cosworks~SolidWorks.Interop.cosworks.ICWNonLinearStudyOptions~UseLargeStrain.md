---
title: "UseLargeStrain Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "UseLargeStrain"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeStrain.html"
---

# UseLargeStrain Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::UseLargeStrain2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeStrain2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLargeStrain As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.UseLargeStrain = value

value = instance.UseLargeStrain
```

### C#

```csharp
System.int UseLargeStrain {get; set;}
```

### C++/CLI

```cpp
property System.int UseLargeStrain {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use large strain formulation
- 0 = Do not use large strain formulation

## VBA Syntax

See [CWNonLinearStudyOptions::UseLargeStrain](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~UseLargeStrain.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid for plasticity material models only.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetZeroStrainTemperature.html)
[ICWNonLinearStudyOptions::SetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetZeroStrainTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
