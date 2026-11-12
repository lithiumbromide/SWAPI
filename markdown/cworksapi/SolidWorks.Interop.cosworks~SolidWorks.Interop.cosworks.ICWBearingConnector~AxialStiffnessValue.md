---
title: "AxialStiffnessValue Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "AxialStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AxialStiffnessValue.html"
---

# AxialStiffnessValue Property (ICWBearingConnector)

Sets the total axial stiffness value for this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property AxialStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.AxialStiffnessValue = value
```

### C#

```csharp
System.double AxialStiffnessValue {set;}
```

### C++/CLI

```cpp
property System.double AxialStiffnessValue {
   void set (    System.double value);
}
```

### Property Value

Total axial stiffness

## VBA Syntax

See [CWBearingConnector::AxialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~AxialStiffnessValue.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## Remarks

This property is valid only if [ICWBearingConnector::StiffnessType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StiffnessType.html) is set to [swsBearingStiffnessType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingStiffnessType_e.html).swsBearingStiffnessFlexible.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
