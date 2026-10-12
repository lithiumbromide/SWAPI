---
title: "EquationLinearUnit Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "EquationLinearUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationLinearUnit.html"
---

# EquationLinearUnit Property (ICWPressure)

Gets or sets the linear units for Cartesian, cylindrical, and spherical coordinate systems of the nonuniform pressure distribution equation.

## Syntax

### Visual Basic (Declaration)

```vb
Property EquationLinearUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
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

See [CWPressure::EquationLinearUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~EquationLinearUnit.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetCoordinateSystem.html)
[ICWPressure::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetCoordinateSystem.html)
[ICWPressure::CoordSystemType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html)
[ICWPressure::EquationAngularUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationAngularUnit.html)
[ICWPressure::Equation Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
