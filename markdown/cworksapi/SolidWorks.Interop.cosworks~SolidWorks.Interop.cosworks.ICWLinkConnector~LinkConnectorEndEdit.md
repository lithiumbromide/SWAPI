---
title: "LinkConnectorEndEdit Method (ICWLinkConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkConnector"
member: "LinkConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector~LinkConnectorEndEdit.html"
---

# LinkConnectorEndEdit Method (ICWLinkConnector)

Ends editing a link connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function LinkConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkConnector
Dim value As System.Integer

value = instance.LinkConnectorEndEdit()
```

### C#

```csharp
System.int LinkConnectorEndEdit()
```

### C++/CLI

```cpp
System.int LinkConnectorEndEdit();
```

### Return Value

Error as defined in [swsLinkConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinkConnectorEndEditError_e.html)

## Remarks

You must call [ICWLinkConnector::LinkConnectorBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLinkConnector~LinkConnectorBeginEdit.html) to start editing a link connector. To end editing a link connector, you must call ICWLinkConnector::LinkConnectorEndEdit. Changes are not applied unless you call both methods.

## See Also

[ICWLinkConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector.html)
[ICWLinkConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
