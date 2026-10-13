---
title: "TangentialOrShearStiffnessValue Property (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "TangentialOrShearStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~TangentialOrShearStiffnessValue.html"
---

# TangentialOrShearStiffnessValue Property (ICWSpringConnector)

Gets or sets the tangential or shear stiffness.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentialOrShearStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Double

instance.TangentialOrShearStiffnessValue = value

value = instance.TangentialOrShearStiffnessValue
```

### C#

```csharp
System.double TangentialOrShearStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double TangentialOrShearStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Tangential or shear stiffness

## VBA Syntax

See [CWSpringConnector::TangentialOrShearStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~TangentialOrShearStiffnessValue.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::NormalRadialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~NormalRadialStiffnessValue.html)
[ICWSpringConnector::RotationalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RotationalStiffnessValue.html)
[ICWSpringConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~StiffnessType.html)
[ICWSpringConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~Unit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
