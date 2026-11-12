---
title: "Deactivate Method (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Deactivate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Deactivate.html"
---

# Deactivate Method (IView3D)

Restores the previously backed-up model state of a 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Deactivate()
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D

instance.Deactivate()
```

### C#

```csharp
void Deactivate()
```

### C++/CLI

```cpp
void Deactivate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [View3D::Deactivate](ms-its:sldworksapivb6.chm::/sldworks~View3D~Deactivate.html).

## Remarks

The model state includes the model's:

- active configuration
- display state
- explode, section, or Model Break view state
- view orientation, including pan and zoom

Restoring the previously backed-up model state of a 3D View might not be this 3D View.

For example:

1. Call [IView3D::Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Activate.html) and set the SaveLastState parameter to true (i.e., previous model state backed up) for 3DView1.
2. Call IView3D::Activate and set the SaveLastState parameter to false (i.e., previous model state not backed up) for 3DView2.
3. Call IView3D::Deactivate for 3DView1 or 3DView2, then the model state prior to activating 3DView1 is restored.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
