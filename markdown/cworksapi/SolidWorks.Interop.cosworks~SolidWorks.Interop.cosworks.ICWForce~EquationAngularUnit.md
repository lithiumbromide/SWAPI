---
title: "EquationAngularUnit Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "EquationAngularUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html"
---

# EquationAngularUnit Property (ICWForce)

Gets or sets the angular units for the cylindrical or spherical coordinate system of this force of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Property EquationAngularUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

instance.EquationAngularUnit = value

value = instance.EquationAngularUnit
```

### C#

```csharp
System.int EquationAngularUnit {get; set;}
```

### C++/CLI

```cpp
property System.int EquationAngularUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Angular units as defined in [swsPhaseAngleUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPhaseAngleUnit_e.html)

## VBA Syntax

See [CWForce::EquationAngularUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~EquationAngularUnit.html).

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html) is set to -1 or true, and [ICWForce::EquationCoordinateSystemType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html) is set to 2 or 3.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::Equation Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html)
[ICWForce::EquationLinearUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)
[ICWForce::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html)
[ICWForce::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
