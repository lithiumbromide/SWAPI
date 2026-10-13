---
title: "ElasticConnectorEndEdit Method (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "ElasticConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~ElasticConnectorEndEdit.html"
---

# ElasticConnectorEndEdit Method (ICWElasticConnector)

Ends editing an elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Function ElasticConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
Dim value As System.Integer

value = instance.ElasticConnectorEndEdit()
```

### C#

```csharp
System.int ElasticConnectorEndEdit()
```

### C++/CLI

```cpp
System.int ElasticConnectorEndEdit();
```

### Return Value

Error as defined in [swsElasticConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsElasticConnectorEndEditError_e.html)

## VBA Syntax

See [CWElasticConnector::ElasticConnectorEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~ElasticConnectorEndEdit.html).

## Examples

See the [ICWElasticConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html) examples.

## Remarks

You must call [ICWElasticConnector::ElasticConnectorBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWElasticConnector~ElasticConnectorBeginEdit.html) to start editing an elastic support fixture. To end editing this fixture, you must call ICWElasticConnector::ElasticConnectorEndEdit. Changes are not applied unless you call both methods.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
