---
title: "LateralStiffnessValue Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "LateralStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~LateralStiffnessValue.html"
---

# LateralStiffnessValue Property (ICWBearingConnector)

Sets the total rotational (lateral) stiffness value for this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property LateralStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.LateralStiffnessValue = value
```

### C#

```csharp
System.double LateralStiffnessValue {set;}
```

### C++/CLI

```cpp
property System.double LateralStiffnessValue {
   void set (    System.double value);
}
```

### Property Value

Total lateral stiffness

## VBA Syntax

See [CWBearingConnector::LateralStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~LateralStiffnessValue.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## Remarks

This property is valid only if [ICWBearingConnector::StiffnessType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StiffnessType.html) is set to [swsBearingStiffnessType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingStiffnessType_e.html).swsBearingStiffnessFlexible.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
