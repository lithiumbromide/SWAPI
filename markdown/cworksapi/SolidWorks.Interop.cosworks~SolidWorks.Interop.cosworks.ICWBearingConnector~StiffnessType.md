---
title: "StiffnessType Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "StiffnessType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StiffnessType.html"
---

# StiffnessType Property (ICWBearingConnector)

Sets the stiffness type of this bearing connecgtor.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property StiffnessType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.StiffnessType = value
```

### C#

```csharp
System.int StiffnessType {set;}
```

### C++/CLI

```cpp
property System.int StiffnessType {
   void set (    System.int value);
}
```

### Property Value

Bearing stiffness type as defined in [swsBearingStiffnessType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingStiffnessType_e.html)

## VBA Syntax

See [CWBearingConnector::StiffnessType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~StiffnessType.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
