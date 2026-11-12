---
title: "BoltConnectorEndEdit Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "BoltConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltConnectorEndEdit.html"
---

# BoltConnectorEndEdit Method (ICWBoltConnector)

Ends editing a bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function BoltConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

value = instance.BoltConnectorEndEdit()
```

### C#

```csharp
System.int BoltConnectorEndEdit()
```

### C++/CLI

```cpp
System.int BoltConnectorEndEdit();
```

### Return Value

Error as defined in [swsBoltConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBoltConnectorEndEditError_e.html)

## VBA Syntax

See [CWBoltConnector::BoltConnectorEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~BoltConnectorEndEdit.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

start editing a bolt connector, call [ICWBoltConnector::BoltConnectorBeginEdit.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector~BoltConnectorBeginEdit.html) You must call ICWBoltConnector::BoltConnectorEndEdit to end editing a bolt connector. Changes are not applied unless you call both methods.

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
