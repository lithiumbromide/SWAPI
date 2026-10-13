---
title: "StiffnessType Property (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "StiffnessType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~StiffnessType.html"
---

# StiffnessType Property (ICWElasticConnector)

Gets or sets the type of stiffness for this elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Property StiffnessType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
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

See [CWElasticConnector::StiffnessType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~StiffnessType.html).

## Examples

See the [ICWElasticConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html) examples.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)
[ICWElasticConnector::NormalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~NormalStiffnessValue.html)
[ICWElasticConnector::ShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~ShearStiffnessValue.html)
[ICWElasticConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~Unit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
