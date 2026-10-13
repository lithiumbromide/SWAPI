---
title: "SetNonUniformData Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetNonUniformData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetNonUniformData.html"
---

# SetNonUniformData Method (ICWForce)

Obsolete. Superseded by [ICWForce::Equation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetNonUniformData( _
   ByVal DConstVal As System.Double, _
   ByVal DX As System.Double, _
   ByVal DY As System.Double, _
   ByVal DXY As System.Double, _
   ByVal DX2 As System.Double, _
   ByVal DY2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim DConstVal As System.Double
Dim DX As System.Double
Dim DY As System.Double
Dim DXY As System.Double
Dim DX2 As System.Double
Dim DY2 As System.Double

instance.SetNonUniformData(DConstVal, DX, DY, DXY, DX2, DY2)
```

### C#

```csharp
void SetNonUniformData(
   System.double DConstVal,
   System.double DX,
   System.double DY,
   System.double DXY,
   System.double DX2,
   System.double DY2
)
```

### C++/CLI

```cpp
void SetNonUniformData(
   System.double DConstVal,
   System.double DX,
   System.double DY,
   System.double DXY,
   System.double DX2,
   System.double DY2
)
```

### Parameters

- `DConstVal`: Constant
- `DX`: Coefficient of the X term
- `DY`: Coefficient of the Y term
- `DXY`: Coefficient of the XY term
- `DX2`: Coefficient of the X2 term
- `DY2`: Coefficient of the Y2 term

## VBA Syntax

See [CWForce::SetNonUniformData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetNonUniformData.html).

## Remarks

This property is valid only if [ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html) is set to -1 or true.

See the SOLIDWORKS Simulation user-interface help for details.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::GetNonUniformData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetNonUniformData.html)
[ICWForce::SetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)
[ICWForce::Equation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html)
[ICWForce::EquationAngularUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html)
[ICWForce::EquationCoordinateSystemType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html)
[ICWForce::EquationLinearUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
