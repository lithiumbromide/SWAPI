---
title: "SpringConnectorEndEdit Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "SpringConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~SpringConnectorEndEdit.html"
---

# SpringConnectorEndEdit Method (ICWSpringConnector)

Ends editing a spring connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function SpringConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Integer

value = instance.SpringConnectorEndEdit()
```

### C#

```csharp
System.int SpringConnectorEndEdit()
```

### C++/CLI

```cpp
System.int SpringConnectorEndEdit();
```

### Return Value

Error as defined in [swsSpringConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringConnectorEndEditError_e.html)

## VBA Syntax

See [CWSpringConnector::SpringConnectorEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~SpringConnectorEndEdit.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## Remarks

You must call [ICWSpringConnector::SpringConnectorBeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~SpringConnectorBeginEdit.html) to start editing a spring. To end editing a spring, you must call ICWSpringConnector::SpringConnectorEndEdit. Changes are not applied unless you call both methods.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
