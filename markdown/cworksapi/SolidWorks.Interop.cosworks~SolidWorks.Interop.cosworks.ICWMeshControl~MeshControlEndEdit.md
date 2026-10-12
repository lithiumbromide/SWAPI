---
title: "MeshControlEndEdit Method (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "MeshControlEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MeshControlEndEdit.html"
---

# MeshControlEndEdit Method (ICWMeshControl)

Ends editing a mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Function MeshControlEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

value = instance.MeshControlEndEdit()
```

### C#

```csharp
System.int MeshControlEndEdit()
```

### C++/CLI

```cpp
System.int MeshControlEndEdit();
```

### Return Value

Error as defined in [swsMeshControlError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshControlError_e.html)

## VBA Syntax

See [CWMeshControl::MeshControlEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~MeshControlEndEdit.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

To end editing a mesh control, you must call this method. You must call [ICWMeshControl::MeshControlBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMeshControl~MeshControlBeginEdit.html) to start editing a mesh control. Changes are not applied unless you call both methods.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
