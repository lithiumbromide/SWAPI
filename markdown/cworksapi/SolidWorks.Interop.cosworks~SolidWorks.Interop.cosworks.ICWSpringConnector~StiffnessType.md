---
title: "StiffnessType Property (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "StiffnessType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~StiffnessType.html"
---

# StiffnessType Property (ICWSpringConnector)

Gets or sets the type of stiffness.

## Syntax

### Visual Basic (Declaration)

```vb
Property StiffnessType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Integer

instance.StiffnessType = value

value = instance.StiffnessType
```

### C#

```csharp
System.int StiffnessType {get; set;}
```

### C++/CLI

```cpp
property System.int StiffnessType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Stiffness types as defined in [swsStiffnessType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStiffnessType_e.html)

## VBA Syntax

See [CWSpringConnector::StiffnessType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~StiffnessType.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::NormalRadialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~NormalRadialStiffnessValue.html)
[ICWSpringConnector::RotationalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RotationalStiffnessValue.html)
[ICWSpringConnector::TangentialOrShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~TangentialOrShearStiffnessValue.html)
[ICWSpringConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~Unit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
