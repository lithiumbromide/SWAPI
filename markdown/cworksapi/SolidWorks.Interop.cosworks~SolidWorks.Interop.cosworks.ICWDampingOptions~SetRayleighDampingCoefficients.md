---
title: "SetRayleighDampingCoefficients Method (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "SetRayleighDampingCoefficients"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetRayleighDampingCoefficients.html"
---

# SetRayleighDampingCoefficients Method (ICWDampingOptions)

Sets the Rayleigh damping coefficients.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRayleighDampingCoefficients( _
   ByVal DAlpha As System.Double, _
   ByVal DBeta As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim DAlpha As System.Double
Dim DBeta As System.Double

instance.SetRayleighDampingCoefficients(DAlpha, DBeta)
```

### C#

```csharp
void SetRayleighDampingCoefficients(
   System.double DAlpha,
   System.double DBeta
)
```

### C++/CLI

```cpp
void SetRayleighDampingCoefficients(
   System.double DAlpha,
   System.double DBeta
)
```

### Parameters

- `DAlpha`: Mass coefficient
- `DBeta`: Stiffness coefficient

## VBA Syntax

See [CWDampingOptions::SetRayleighDampingCoefficients](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDampingOptions~SetRayleighDampingCoefficients.html).

## Remarks

This method works only if [ICWDampingOptions::DampingType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions~DampingType.html) is set to [swsDampingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDampingType_e.html).swsDampingType_Rayleigh.

For more information about Rayleigh damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)
[ICWDampingOptions::GetRayleighDampingCoefficients Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetRayleighDampingCoefficients.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
