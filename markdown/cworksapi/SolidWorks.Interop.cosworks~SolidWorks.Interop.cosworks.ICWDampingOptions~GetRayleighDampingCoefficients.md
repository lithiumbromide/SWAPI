---
title: "GetRayleighDampingCoefficients Method (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "GetRayleighDampingCoefficients"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetRayleighDampingCoefficients.html"
---

# GetRayleighDampingCoefficients Method (ICWDampingOptions)

Gets the Rayleigh damping coefficients.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetRayleighDampingCoefficients( _
   ByRef DAlpha As System.Double, _
   ByRef DBeta As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim DAlpha As System.Double
Dim DBeta As System.Double

instance.GetRayleighDampingCoefficients(DAlpha, DBeta)
```

### C#

```csharp
void GetRayleighDampingCoefficients(
   out System.double DAlpha,
   out System.double DBeta
)
```

### C++/CLI

```cpp
void GetRayleighDampingCoefficients(
   [Out] System.double DAlpha,
   [Out] System.double DBeta
)
```

### Parameters

- `DAlpha`: Mass coefficient
- `DBeta`: Stiffness coefficient

## VBA Syntax

See [CWDampingOptions::GetRayleighDampingCoefficients](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDampingOptions~GetRayleighDampingCoefficients.html).

## Remarks

This method works only if [ICWDampingOptions::DampingType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions~DampingType.html) is set to [swsDampingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDampingType_e.html).swsDampingType_Rayleigh.

For more information about Rayleigh damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)
[ICWDampingOptions::SetRayleighDampingCoefficients Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetRayleighDampingCoefficients.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
