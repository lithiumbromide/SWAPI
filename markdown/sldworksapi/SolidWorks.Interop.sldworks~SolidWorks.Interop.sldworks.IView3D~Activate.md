---
title: "Activate Method (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Activate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Activate.html"
---

# Activate Method (IView3D)

Activates this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Activate( _
   ByVal SaveLastState As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim SaveLastState As System.Boolean

instance.Activate(SaveLastState)
```

### C#

```csharp
void Activate(
   System.bool SaveLastState
)
```

### C++/CLI

```cpp
void Activate(
   System.bool SaveLastState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SaveLastState`: True to back up the previous model state prior to activating this 3D View, false to not back up the previous model state prior to activating this 3D view

## VBA Syntax

See [View3D::Activate](ms-its:sldworksapivb6.chm::/sldworks~View3D~Activate.html).

## Examples

See the [IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html) examples.

## Remarks

The model state includes the model's:

- active configuration
- display state
- explode, section, or Model Break view state
- view orientation, including pan and zoom

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)
[IView3D::Deactivate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Deactivate.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
