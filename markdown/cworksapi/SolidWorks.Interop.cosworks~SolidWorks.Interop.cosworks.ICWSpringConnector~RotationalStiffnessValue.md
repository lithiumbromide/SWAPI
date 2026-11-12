---
title: "RotationalStiffnessValue Property (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "RotationalStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RotationalStiffnessValue.html"
---

# RotationalStiffnessValue Property (ICWSpringConnector)

Gets or sets the rotational stiffness.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationalStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Double

instance.RotationalStiffnessValue = value

value = instance.RotationalStiffnessValue
```

### C#

```csharp
System.double RotationalStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double RotationalStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Rotational stiffness

## VBA Syntax

See [CWSpringConnector::RotationalStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~RotationalStiffnessValue.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::NormalRadialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~NormalRadialStiffnessValue.html)
[ICWSpringConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~StiffnessType.html)
[ICWSpringConnector::TangentialOrShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~TangentialOrShearStiffnessValue.html)
[ICWSpringConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~Unit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
