---
title: "RotationalStiffnessValue Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "RotationalStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~RotationalStiffnessValue.html"
---

# RotationalStiffnessValue Property (ICWBearingConnector)

Obsolete. Superseded by [ICWBearingConnector::LateralStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~LateralStiffnessValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property RotationalStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.RotationalStiffnessValue = value
```

### C#

```csharp
System.double RotationalStiffnessValue {set;}
```

### C++/CLI

```cpp
property System.double RotationalStiffnessValue {
   void set (    System.double value);
}
```

### Property Value

Total rotational stiffness

## VBA Syntax

See [CWBearingConnector::RotationalStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~RotationalStiffnessValue.html).

## Remarks

This property is valid only if [ICWBearingConnector::StiffnessType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StiffnessType.html) is set to [swsBearingStiffnessType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingStiffnessType_e.html).swsBearingStiffnessFlexible.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
