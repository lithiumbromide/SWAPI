---
title: "SpotWeldConnectorBeginEdit Method (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "SpotWeldConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~SpotWeldConnectorBeginEdit.html"
---

# SpotWeldConnectorBeginEdit Method (ICWSpotWeldConnector)

Starts editing a spot-weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SpotWeldConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector

instance.SpotWeldConnectorBeginEdit()
```

### C#

```csharp
void SpotWeldConnectorBeginEdit()
```

### C++/CLI

```cpp
void SpotWeldConnectorBeginEdit();
```

## VBA Syntax

See [CWSpotWeldConnector::SpotWeldConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~SpotWeldConnectorBeginEdit.html).

## Examples

See the [ICWSpotWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html) examples.

## Remarks

To start editing a spot weld, you must call this method. You must call [ICWSpotWeldConnector::SpotWeldConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpotWeldConnector~SpotWeldConnectorEndEdit.html) to end editing a spot weld. Changes are not applied unless you call both methods.

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
