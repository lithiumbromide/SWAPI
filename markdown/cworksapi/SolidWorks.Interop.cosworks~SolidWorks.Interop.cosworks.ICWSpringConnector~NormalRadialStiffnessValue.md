---
title: "NormalRadialStiffnessValue Property (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "NormalRadialStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~NormalRadialStiffnessValue.html"
---

# NormalRadialStiffnessValue Property (ICWSpringConnector)

Gets or sets the normal or radial stiffness (stiffness normal to faces).

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalRadialStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Double

instance.NormalRadialStiffnessValue = value

value = instance.NormalRadialStiffnessValue
```

### C#

```csharp
System.double NormalRadialStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double NormalRadialStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Normal or radial stiffness

## VBA Syntax

See [CWSpringConnector::NormalRadialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~NormalRadialStiffnessValue.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::RotationalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RotationalStiffnessValue.html)
[ICWSpringConnector::TangentialOrShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~TangentialOrShearStiffnessValue.html)
[ICWSpringConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~Unit.html)
[ICWSpringConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~StiffnessType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
