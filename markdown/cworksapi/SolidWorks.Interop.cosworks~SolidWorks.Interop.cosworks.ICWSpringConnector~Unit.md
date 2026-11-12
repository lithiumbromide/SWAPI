---
title: "Unit Property (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~Unit.html"
---

# Unit Property (ICWSpringConnector)

Gets or sets the units for stiffness.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWSpringConnector::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~Unit.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::NormalRadialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~NormalRadialStiffnessValue.html)
[ICWSpringConnector::RotationalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RotationalStiffnessValue.html)
[ICWSpringConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~StiffnessType.html)
[ICWSpringConnector::TangentialOrShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~TangentialOrShearStiffnessValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
