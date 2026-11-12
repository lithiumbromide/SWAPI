---
title: "EquationAngularUnit Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "EquationAngularUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationAngularUnit.html"
---

# EquationAngularUnit Property (ICWPressure)

Gets or sets the angular units for cylindrical and spherical coordinate systems of the nonuniform pressure distribution equation.

## Syntax

### Visual Basic (Declaration)

```vb
Property EquationAngularUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
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

See [CWPressure::EquationAngularUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~EquationAngularUnit.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true and [ICWPressure::CoordSystemType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html) is set to 2 or 3.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetCoordinateSystem.html)
[ICWPressure::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetCoordinateSystem.html)
[ICWPressure::CoordSystemType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html)
[ICWPressure::EquationLinearUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationLinearUnit.html)
[ICWPressure::Equation Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
