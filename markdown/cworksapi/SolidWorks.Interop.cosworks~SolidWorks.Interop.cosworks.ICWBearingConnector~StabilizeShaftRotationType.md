---
title: "StabilizeShaftRotationType Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "StabilizeShaftRotationType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotationType.html"
---

# StabilizeShaftRotationType Property (ICWBearingConnector)

Sets the type of shaft rotation stabilization.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property StabilizeShaftRotationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.StabilizeShaftRotationType = value
```

### C#

```csharp
System.int StabilizeShaftRotationType {set;}
```

### C++/CLI

```cpp
property System.int StabilizeShaftRotationType {
   void set (    System.int value);
}
```

### Property Value

Shaft rotation stabilization type as defined by [swsBearingStiffnessShaftStabilizeType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingStiffnessShaftStabilizeType_e.html)

## VBA Syntax

See [CWBearingConnector::StabilizeShaftRotationType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~StabilizeShaftRotationType.html).

## Remarks

This property is valid only if [ICWBearingConnector::StabilizeShaftRotation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotation.html) is set to true.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
