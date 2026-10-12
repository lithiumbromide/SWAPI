---
title: "Unit Property (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~Unit.html"
---

# Unit Property (ICWElasticConnector)

Gets or sets the stiffness unit for this elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
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

See [CWElasticConnector::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~Unit.html).

## Examples

See the [ICWElasticConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html) examples.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)
[ICWElasticConnector::NormalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~NormalStiffnessValue.html)
[ICWElasticConnector::ShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~ShearStiffnessValue.html)
[ICWElasticConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~StiffnessType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
