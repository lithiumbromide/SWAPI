---
title: "NormalStiffnessValue Property (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "NormalStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~NormalStiffnessValue.html"
---

# NormalStiffnessValue Property (ICWElasticConnector)

Gets or sets the normal stiffness value for this elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
Dim value As System.Double

instance.NormalStiffnessValue = value

value = instance.NormalStiffnessValue
```

### C#

```csharp
System.double NormalStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double NormalStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Normal stiffness value

## VBA Syntax

See [CWElasticConnector::NormalStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~NormalStiffnessValue.html).

## Examples

See the [ICWElasticConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html) examples.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)
[ICWElasticConnector::ShearStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~ShearStiffnessValue.html)
[ICWElasticConnector::StiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~StiffnessType.html)
[ICWElasticConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~Unit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
