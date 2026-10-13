---
title: "PinConnectorEndEdit Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "PinConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinConnectorEndEdit.html"
---

# PinConnectorEndEdit Method (ICWPinConnector)

Ends editing a pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function PinConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Integer

value = instance.PinConnectorEndEdit()
```

### C#

```csharp
System.int PinConnectorEndEdit()
```

### C++/CLI

```cpp
System.int PinConnectorEndEdit();
```

### Return Value

Error as defined in [swsPinConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPinConnectorEndEditError_e.html)

## VBA Syntax

See [CWPinConnector::PinConnectorEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~PinConnectorEndEdit.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

You must call [ICWPinConnector::PinConnectorBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPinConnector~PinConnectorBeginEdit.html) to start editing a pin connector. To end editing a pin connector, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
