---
title: "Equation Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "Equation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html"
---

# Equation Property (ICWForce)

Gets or sets the equation describing this force of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Property Equation As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
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

Nonuniform force distribution equation

## VBA Syntax

See [CWForce::Equation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~Equation.html).

## Examples

```
For VBA:
```

```
CWForceObj.CoordSystemType = swsCoordinateTypeCylindrical

CWForceObj.Equation = ".4*""r"" +.8* ""t"" +.6* ""z"""
```

```
For VB.NET:
```

```
CWForceObj.CoordSystemType = swsCoordinateType_e.swsCoordinateTypeCylindrical

CWForceObj.Equation = ".4*""r"" +.8* ""t"" +.6* ""z"""
```

```
For C#:
```

```
CWForceObj.CoordSystemType = (int)swsCoordinateType_e.swsCoordinateTypeCylindrical;

CWForceObj.Equation = ".4*\"r\" +.8* \"t\" +.6* \"z\"";
```

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html) is set to -1 or true.

The equation is a string that contains double-quoted coordinate variables. In the example, the cylindrical coordinate system requires that the equation be specified with coordinate variables r, t, and z. Other coordinate systems use different sets of coordinate variables. See the **Defining Nonuniform Force Loads** topic in the SOLIDWORKS Simulation user-interface help for more information.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::EquationAngularUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html)
[ICWForce::EquationCoordinateSystemType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html)
[ICWForce::EquationLinearUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)
[ICWForce::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html)
[ICWForce::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
