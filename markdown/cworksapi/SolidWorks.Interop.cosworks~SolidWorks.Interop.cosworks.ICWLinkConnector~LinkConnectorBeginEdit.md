---
title: "LinkConnectorBeginEdit Method (ICWLinkConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkConnector"
member: "LinkConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector~LinkConnectorBeginEdit.html"
---

# LinkConnectorBeginEdit Method (ICWLinkConnector)

Starts editing a link connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub LinkConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkConnector

instance.LinkConnectorBeginEdit()
```

### C#

```csharp
void LinkConnectorBeginEdit()
```

### C++/CLI

```cpp
void LinkConnectorBeginEdit();
```

## VBA Syntax

See [CWLinkConnector::LinkConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkConnector~LinkConnectorBeginEdit.html).

## Remarks

To start editing a link connector, you must call this method. You must call [ICWLinkConnector::LinkConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLinkConnector~LinkConnectorEndEdit.html) to end editing a link connector. Changes are not applied unless you call both methods.

## See Also

[ICWLinkConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector.html)
[ICWLinkConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector_members.html)
