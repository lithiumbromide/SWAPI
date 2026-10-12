---
title: "SpringConnectorBeginEdit Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "SpringConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~SpringConnectorBeginEdit.html"
---

# SpringConnectorBeginEdit Method (ICWSpringConnector)

Starts editing a spring connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SpringConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector

instance.SpringConnectorBeginEdit()
```

### C#

```csharp
void SpringConnectorBeginEdit()
```

### C++/CLI

```cpp
void SpringConnectorBeginEdit();
```

## VBA Syntax

See [CWSpringConnector::SpringConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~SpringConnectorBeginEdit.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## Remarks

To start editing a spring, you must call this method. You must call [ICWSpringConnector::SpringConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpringConnector~SpringConnectorEndEdit.html) to end editing a spring. Changes are not applied unless you call both methods.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
