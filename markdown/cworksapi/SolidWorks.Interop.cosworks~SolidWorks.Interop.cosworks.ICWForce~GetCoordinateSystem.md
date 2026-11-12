---
title: "GetCoordinateSystem Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "GetCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html"
---

# GetCoordinateSystem Method (ICWForce)

Gets the coordinate system used for defining a force of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinateSystem() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Object

value = instance.GetCoordinateSystem()
```

### C#

```csharp
System.object GetCoordinateSystem()
```

### C++/CLI

```cpp
System.Object^ GetCoordinateSystem();
```

### Return Value

Coordinate system

## VBA Syntax

See [CWForce::GetCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~GetCoordinateSystem.html).

## Remarks

This property is valid only if [IC](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution.html)[ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html) is set to -1 or true.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::SetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html)
[ICWForce::Equation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html)
[ICWForce::EquationAngularUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html)
[ICWForce::EquationCoordinateSystemType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html)
[ICWForce::EquationLinearUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
