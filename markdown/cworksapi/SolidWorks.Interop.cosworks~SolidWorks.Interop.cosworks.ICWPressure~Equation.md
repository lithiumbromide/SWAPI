---
title: "Equation Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "Equation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html"
---

# Equation Property (ICWPressure)

Gets or sets the equation describing this pressure of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Property Equation As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.String

instance.Equation = value

value = instance.Equation
```

### C#

```csharp
System.string Equation {get; set;}
```

### C++/CLI

```cpp
property System.String^ Equation {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Nonuniform pressure distribution equation

## VBA Syntax

See [CWPressure::Equation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~Equation.html).

## Examples

```
For VBA:
```

```
CWPressureObj.CoordSystemType = swsCoordinateTypeCylindrical

CWPressureObj.Equation = ".4*""r"" +.8* ""t"" +.6* ""z"""
```

```
For VB.NET:
```

```
CWPressureObj.CoordSystemType = swsCoordinateType_e.swsCoordinateTypeCylindrical

CWPressureObj.Equation = ".4*""r"" +.8* ""t"" +.6* ""z"""
```

```
For C#:
```

```
CWPressureObj.CoordSystemType = (int)swsCoordinateType_e.swsCoordinateTypeCylindrical;

CWPressureObj.Equation = ".4*\"r\" +.8* \"t\" +.6* \"z\"";
```

```
See the ICWPressure examples.
```

## Remarks

This property is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to 1.

The equation is a string that contains double-quoted coordinate variables. In the example, the cylindrical coordinate system requires that the equation be specified with coordinate variables r, t, and z. Other coordinate systems use different sets of coordinate variables. See the **Defining Nonuniform Pressure Loads** topic in the SOLIDWORKS Simulation Help for more information.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::CoordSystemType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html)
[ICWPressure::EquationAngularUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationAngularUnit.html)
[ICWPressure::EquationLinearUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~EquationLinearUnit.html)
[ICWPressure::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetCoordinateSystem.html)
[ICWPressure::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
