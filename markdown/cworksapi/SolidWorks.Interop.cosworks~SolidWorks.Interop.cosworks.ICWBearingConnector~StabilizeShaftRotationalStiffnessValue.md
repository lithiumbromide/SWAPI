---
title: "StabilizeShaftRotationalStiffnessValue Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "StabilizeShaftRotationalStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotationalStiffnessValue.html"
---

# StabilizeShaftRotationalStiffnessValue Property (ICWBearingConnector)

Sets the user-defined shaft rotation stabilization value.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property StabilizeShaftRotationalStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.StabilizeShaftRotationalStiffnessValue = value
```

### C#

```csharp
System.double StabilizeShaftRotationalStiffnessValue {set;}
```

### C++/CLI

```cpp
property System.double StabilizeShaftRotationalStiffnessValue {
   void set (    System.double value);
}
```

### Property Value

User-defined shaft rotation stabilization value

## VBA Syntax

See [CWBearingConnector::StabilizeShaftRotationalStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~StabilizeShaftRotationalStiffnessValue.html).

## Remarks

This property is valid only if:

[ICWBearingConnector::StabilizeShaftRotation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotation.html) is set to true

- and -

[ICWBearingConnector::StabilizeShaftRotationType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotationType.html) is set to [swsBearingStiffnessShaftStabilizeType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingStiffnessShaftStabilizeType_e.html).swsBearingStiffnessShaftStablilizeUserDef

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
