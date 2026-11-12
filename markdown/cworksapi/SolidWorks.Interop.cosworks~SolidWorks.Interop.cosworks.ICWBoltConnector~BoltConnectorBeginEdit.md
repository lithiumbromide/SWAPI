---
title: "BoltConnectorBeginEdit Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "BoltConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltConnectorBeginEdit.html"
---

# BoltConnectorBeginEdit Method (ICWBoltConnector)

Starts editing a bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub BoltConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector

instance.BoltConnectorBeginEdit()
```

### C#

```csharp
void BoltConnectorBeginEdit()
```

### C++/CLI

```cpp
void BoltConnectorBeginEdit();
```

## VBA Syntax

See [CWBoltConnector::BoltConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~BoltConnectorBeginEdit.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

To start editing a bolt connector, you must call this method. You must call [ICWBoltConnector::BoltConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector~BoltConnectorEndEdit.html) to end editing that bolt connector. Changes are not applied unless you call both methods.

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
