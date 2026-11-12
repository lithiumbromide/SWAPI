---
title: "ShearStiffnessValue Property (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "ShearStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~ShearStiffnessValue.html"
---

# ShearStiffnessValue Property (ICWElasticConnector)

Gets or sets the shear stiffness value for this elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShearStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
Dim value As System.Double

instance.ShearStiffnessValue = value

value = instance.ShearStiffnessValue
```

### C#

```csharp
System.double ShearStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double ShearStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Shear stiffness value

## VBA Syntax

See [CWElasticConnector::ShearStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~ShearStiffnessValue.html).

## Examples

See the [ICWElasticConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html) examples.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)
[ICWElasticConnector::NormalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~NormalStiffnessValue.html)
[ICWElasticConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~StiffnessType.html)
[ICWElasticConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~Unit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
