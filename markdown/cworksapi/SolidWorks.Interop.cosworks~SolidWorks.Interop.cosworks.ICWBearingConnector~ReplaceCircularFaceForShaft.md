---
title: "ReplaceCircularFaceForShaft Method (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "ReplaceCircularFaceForShaft"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~ReplaceCircularFaceForShaft.html"
---

# ReplaceCircularFaceForShaft Method (ICWBearingConnector)

Replaces the circular face of the shaft with the specified circular face.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceCircularFaceForShaft( _
   ByVal CircularFace As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector
Dim CircularFace As System.Object
Dim value As System.Integer

value = instance.ReplaceCircularFaceForShaft(CircularFace)
```

### C#

```csharp
System.int ReplaceCircularFaceForShaft(
   System.object CircularFace
)
```

### C++/CLI

```cpp
System.int ReplaceCircularFaceForShaft(
   System.Object^ CircularFace
)
```

### Parameters

- `CircularFace`: Circular face

### Return Value

Error code as defined by [swsBearingConnectorErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html)

## VBA Syntax

See [CWBearingConnector::ReplaceCircularFaceForShaft](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~ReplaceCircularFaceForShaft.html).

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
