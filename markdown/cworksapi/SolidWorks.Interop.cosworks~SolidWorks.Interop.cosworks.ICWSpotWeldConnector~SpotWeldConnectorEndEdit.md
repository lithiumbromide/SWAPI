---
title: "SpotWeldConnectorEndEdit Method (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "SpotWeldConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~SpotWeldConnectorEndEdit.html"
---

# SpotWeldConnectorEndEdit Method (ICWSpotWeldConnector)

Ends editing a spot weld.

## Syntax

### Visual Basic (Declaration)

```vb
Function SpotWeldConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector
Dim value As System.Integer

value = instance.SpotWeldConnectorEndEdit()
```

### C#

```csharp
System.int SpotWeldConnectorEndEdit()
```

### C++/CLI

```cpp
System.int SpotWeldConnectorEndEdit();
```

### Return Value

Error as defined in [swsSpotWeldConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpotWeldConnectorEndEditError_e.html)

## VBA Syntax

See [CWSpotWeldConnector::SpotWeldConnectorEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~SpotWeldConnectorEndEdit.html).

## Examples

See the [ICWSpotWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html) examples.

## Remarks

You must call [ICWSpotWeldConnector::SpotWeldConnectorBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRigidConnector~RigidConnectorBeginEdit.html) to start editing a spot weld. To end editing a spot weld, you must call ICWSpotWeldConnector::SpotWeldEndConnectorEndEdit. Changes are not applied unless you call both methods.

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
