---
title: "RigidConnectorEndEdit Method (ICWRigidConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRigidConnector"
member: "RigidConnectorEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RigidConnectorEndEdit.html"
---

# RigidConnectorEndEdit Method (ICWRigidConnector)

Ends editing a rigid connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function RigidConnectorEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRigidConnector
Dim value As System.Integer

value = instance.RigidConnectorEndEdit()
```

### C#

```csharp
System.int RigidConnectorEndEdit()
```

### C++/CLI

```cpp
System.int RigidConnectorEndEdit();
```

### Return Value

Error as defined in [swsRigidConnectorEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRigidConnectorEndEditError_e.html)

## VBA Syntax

See [CWRigidConnector::RigidConnectorEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRigidConnector~RigidConnectorEndEdit.html).

## Examples

See the [ICWRigidConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html) examples.

## Remarks

You must call [ICWRigidConnector::RigidConnectorBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRigidConnector~RigidConnectorBeginEdit.html) to start editing a rigid connector. To end editing a rigid connector, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWRigidConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html)
[ICWRigidConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
