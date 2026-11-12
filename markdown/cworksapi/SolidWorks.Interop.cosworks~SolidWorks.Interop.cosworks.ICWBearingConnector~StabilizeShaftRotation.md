---
title: "StabilizeShaftRotation Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "StabilizeShaftRotation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotation.html"
---

# StabilizeShaftRotation Property (ICWBearingConnector)

Sets whether to stabilize the shaft rotation of this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property StabilizeShaftRotation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.StabilizeShaftRotation = value
```

### C#

```csharp
System.bool StabilizeShaftRotation {set;}
```

### C++/CLI

```cpp
property System.bool StabilizeShaftRotation {
   void set (    System.bool value);
}
```

### Property Value

True to stabilize the shaft rotation, false to not

## VBA Syntax

See [CWBearingConnector::StabilizeShaftRotation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~StabilizeShaftRotation.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
