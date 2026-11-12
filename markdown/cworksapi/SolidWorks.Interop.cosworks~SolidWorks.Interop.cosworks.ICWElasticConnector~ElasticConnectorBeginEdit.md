---
title: "ElasticConnectorBeginEdit Method (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "ElasticConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~ElasticConnectorBeginEdit.html"
---

# ElasticConnectorBeginEdit Method (ICWElasticConnector)

Starts editing an elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ElasticConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector

instance.ElasticConnectorBeginEdit()
```

### C#

```csharp
void ElasticConnectorBeginEdit()
```

### C++/CLI

```cpp
void ElasticConnectorBeginEdit();
```

## VBA Syntax

See [CWElasticConnector::ElasticConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~ElasticConnectorBeginEdit.html).

## Examples

See the [ICWElasticConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html) examples.

## Remarks

To start editing an elastic support fixture, you must call this method. You must call [ICWElasticConnector::ElasticConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWElasticConnector~ElasticConnectorEndEdit.html) to end editing that fixture. Changes are not applied unless you call both methods.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
