---
title: "DisplayMode Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "DisplayMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~DisplayMode.html"
---

# DisplayMode Property (IView3D)

Gets or sets the display mode of this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.Integer

instance.DisplayMode = value

value = instance.DisplayMode
```

### C#

```csharp
System.int DisplayMode {get; set;}
```

### C++/CLI

```cpp
property System.int DisplayMode {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display mode as defined in [swDisplayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html)

## VBA Syntax

See [View3D::DisplayMode](ms-its:sldworksapivb6.chm::/sldworks~View3D~DisplayMode.html).

## Examples

See the [IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html) examples.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
