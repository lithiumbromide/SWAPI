---
title: "RigidConnectorBeginEdit Method (ICWRigidConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRigidConnector"
member: "RigidConnectorBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RigidConnectorBeginEdit.html"
---

# RigidConnectorBeginEdit Method (ICWRigidConnector)

Starts editing a rigid connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RigidConnectorBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRigidConnector

instance.RigidConnectorBeginEdit()
```

### C#

```csharp
void RigidConnectorBeginEdit()
```

### C++/CLI

```cpp
void RigidConnectorBeginEdit();
```

## VBA Syntax

See [CWRigidConnector::RigidConnectorBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRigidConnector~RigidConnectorBeginEdit.html).

## Examples

See the [ICWRigidConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html) examples.

## Remarks

To start editing a rigid connector, you must call this method. You must call [ICWRigidConnector::RigidConnectorEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRigidConnector~RigidConnectorEndEdit.html) to end editing a rigid connector. Changes are not applied unless you call both methods.

## See Also

[ICWRigidConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html)
[ICWRigidConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
