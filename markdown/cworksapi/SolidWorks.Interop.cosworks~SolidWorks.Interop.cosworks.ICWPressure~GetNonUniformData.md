---
title: "GetNonUniformData Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "GetNonUniformData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetNonUniformData.html"
---

# GetNonUniformData Method (ICWPressure)

Obsolete. Superseded by [ICWPressure::Equation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetNonUniformData( _
   ByRef DConstVal As System.Double, _
   ByRef DX As System.Double, _
   ByRef DY As System.Double, _
   ByRef DXY As System.Double, _
   ByRef DXX As System.Double, _
   ByRef DYY As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim DConstVal As System.Double
Dim DX As System.Double
Dim DY As System.Double
Dim DXY As System.Double
Dim DXX As System.Double
Dim DYY As System.Double

instance.GetNonUniformData(DConstVal, DX, DY, DXY, DXX, DYY)
```

### C#

```csharp
void GetNonUniformData(
   out System.double DConstVal,
   out System.double DX,
   out System.double DY,
   out System.double DXY,
   out System.double DXX,
   out System.double DYY
)
```

### C++/CLI

```cpp
void GetNonUniformData(
   [Out] System.double DConstVal,
   [Out] System.double DX,
   [Out] System.double DY,
   [Out] System.double DXY,
   [Out] System.double DXX,
   [Out] System.double DYY
)
```

### Parameters

- `DConstVal`: Constant
- `DX`: Coefficient of the X term
- `DY`: Coefficient of the Y term
- `DXY`: Coefficient of the XY term
- `DXX`: Coefficient of the X2 term
- `DYY`: Coefficient of the Y2 term

## VBA Syntax

See [CWPressure::GetNonUniformData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~GetNonUniformData.html).

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::SetNonUniformData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetNonUniformData.html)
[ICWPressure::IncludeNonUniformDistribution Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html)
[ICWPressure::EquationAngularUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationAngularUnit.html)
[ICWPressure::EquationLinearUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationLinearUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
