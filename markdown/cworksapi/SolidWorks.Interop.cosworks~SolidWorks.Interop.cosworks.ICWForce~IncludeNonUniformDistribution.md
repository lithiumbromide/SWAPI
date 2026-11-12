---
title: "IncludeNonUniformDistribution Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "IncludeNonUniformDistribution"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution.html"
---

# IncludeNonUniformDistribution Property (ICWForce)

Obsolete. Superseded by [ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeNonUniformDistribution As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

instance.IncludeNonUniformDistribution = value

value = instance.IncludeNonUniformDistribution
```

### C#

```csharp
System.int IncludeNonUniformDistribution {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeNonUniformDistribution {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 if nonuniform force distribution, 0 if not

## VBA Syntax

See [CWForce::IncludeNonUniformDistribution](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~IncludeNonUniformDistribution.html).

## Examples

[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::Equation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html)
[ICWForce::EquationAngularUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html)
[ICWForce::EquationCoordinateSystemType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html)
[ICWForce::EquationLinearUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)
[ICWForce::GetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html)
[ICWForce::SetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
