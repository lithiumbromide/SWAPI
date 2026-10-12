---
title: "PinConnectorBeginEdit Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "PinConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinConnectorBeginEdit.html"
---

# PinConnectorBeginEdit Method (ICWPinConnector)

Starts editing a pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PinConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector

instance.PinConnectorBeginEdit()
```

### C#

```csharp
void PinConnectorBeginEdit()
```

### C++/CLI

```cpp
void PinConnectorBeginEdit();
```

## VBA Syntax

See [CWPinConnector::PinConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~PinConnectorBeginEdit.html).

## Examples

[Create and Edit Bolt and Pin Connector (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connector (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

To start editing a pin connector, you must call this method. You must call [ICWPinConnector::PinConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPinConnector~PinConnectorEndEdit.html) to end editing a pin connector. Changes are not applied unless you call both methods.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
