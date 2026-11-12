---
title: "EquationLinearUnit Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "EquationLinearUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html"
---

# EquationLinearUnit Property (ICWForce)

Gets or sets the linear units for the Cartesian, cylindrical, or spherical coordinate system of this force of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Property EquationLinearUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

instance.EquationLinearUnit = value

value = instance.EquationLinearUnit
```

### C#

```csharp
System.int EquationLinearUnit {get; set;}
```

### C++/CLI

```cpp
property System.int EquationLinearUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Linear units as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWForce::EquationLinearUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~EquationLinearUnit.html).

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html) is set to -1 or true.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::Equation Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html)
[ICWForce::EquationAngularUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html)
[ICWForce::EquationCoordinateSystemType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html)
[ICWForce::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html)
[ICWForce::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
