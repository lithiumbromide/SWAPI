---
title: "MeshControlBeginEdit Method (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "MeshControlBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MeshControlBeginEdit.html"
---

# MeshControlBeginEdit Method (ICWMeshControl)

Starts editing the mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MeshControlBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl

instance.MeshControlBeginEdit()
```

### C#

```csharp
void MeshControlBeginEdit()
```

### C++/CLI

```cpp
void MeshControlBeginEdit();
```

## VBA Syntax

See [CWMeshControl::MeshControlBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~MeshControlBeginEdit.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

To start editing a mesh control, you must call this method. You must call [ICWMeshControl::MeshControlEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMeshControl~MeshControlEndEdit.html) to end editing a mesh control. Changes are not applied unless you call both methods.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
