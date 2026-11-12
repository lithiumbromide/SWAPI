---
title: "SetNonUniformData Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "SetNonUniformData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetNonUniformData.html"
---

# SetNonUniformData Method (ICWPressure)

Obsolete. Superseded by [ICWPressure::Equation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetNonUniformData( _
   ByVal DConstVal As System.Double, _
   ByVal DX As System.Double, _
   ByVal DY As System.Double, _
   ByVal DXY As System.Double, _
   ByVal DXX As System.Double, _
   ByVal DYY As System.Double _
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

instance.SetNonUniformData(DConstVal, DX, DY, DXY, DXX, DYY)
```

### C#

```csharp
void SetNonUniformData(
   System.double DConstVal,
   System.double DX,
   System.double DY,
   System.double DXY,
   System.double DXX,
   System.double DYY
)
```

### C++/CLI

```cpp
void SetNonUniformData(
   System.double DConstVal,
   System.double DX,
   System.double DY,
   System.double DXY,
   System.double DXX,
   System.double DYY
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

See [CWPressure::SetNonUniformData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~SetNonUniformData.html).

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::GetNonUniformData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetNonUniformData.html)
[ICWPressure::IncludeNonUniformDistribution Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html)
[ICWPressure::EquationAngularUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationAngularUnit.html)
[ICWPressure::EquationLinearUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationLinearUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
