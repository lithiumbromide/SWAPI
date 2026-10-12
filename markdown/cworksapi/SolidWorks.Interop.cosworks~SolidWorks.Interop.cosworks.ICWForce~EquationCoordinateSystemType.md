---
title: "EquationCoordinateSystemType Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "EquationCoordinateSystemType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html"
---

# EquationCoordinateSystemType Property (ICWForce)

Gets or sets the type of coordinate system used to define this force of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Property EquationCoordinateSystemType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

instance.EquationCoordinateSystemType = value

value = instance.EquationCoordinateSystemType
```

### C#

```csharp
System.int EquationCoordinateSystemType {get; set;}
```

### C++/CLI

```cpp
property System.int EquationCoordinateSystemType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of coordinate system as defined in [swsCoordinateType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCoordinateType_e.html)

## VBA Syntax

See [CWForce::EquationCoordinateSystemType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~EquationCoordinateSystemType.html).

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
[ICWForce::EquationLinearUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)
[ICWForce::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html)
[ICWForce::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
