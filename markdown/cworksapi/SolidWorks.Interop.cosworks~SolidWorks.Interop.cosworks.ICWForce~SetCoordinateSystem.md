---
title: "SetCoordinateSystem Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetCoordinateSystem.html"
---

# SetCoordinateSystem Method (ICWForce)

Sets the coordinate system used for defining a force of nonuniform distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCoordinateSystem( _
   ByVal DispCoordinateSystem As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim DispCoordinateSystem As System.Object

instance.SetCoordinateSystem(DispCoordinateSystem)
```

### C#

```csharp
void SetCoordinateSystem(
   System.object DispCoordinateSystem
)
```

### C++/CLI

```cpp
void SetCoordinateSystem(
   System.Object^ DispCoordinateSystem
)
```

### Parameters

- `DispCoordinateSystem`: Coordinate system

## VBA Syntax

See [CWForce::SetCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetCoordinateSystem.html).

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWForce::IncludeNonUniformDistribution2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~IncludeNonUniformDistribution2.html) is set to -1 or true.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::GetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetCoordinateSystem.html)
[ICWForce::Equation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Equation.html)
[ICWForce::EquationAngularUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationAngularUnit.html)
[ICWForce::EquationCoordinateSystemType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationCoordinateSystemType.html)
[ICWForce::EquationLinearUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~EquationLinearUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
