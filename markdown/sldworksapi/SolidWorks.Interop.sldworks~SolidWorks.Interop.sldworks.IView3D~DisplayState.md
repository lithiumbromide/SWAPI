---
title: "DisplayState Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "DisplayState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~DisplayState.html"
---

# DisplayState Property (IView3D)

Gets or sets the name this 3D View's display state.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayState As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.String

instance.DisplayState = value

value = instance.DisplayState
```

### C#

```csharp
System.string DisplayState {get; set;}
```

### C++/CLI

```cpp
property System.String^ DisplayState {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display state name

## VBA Syntax

See [View3D::DisplayState](ms-its:sldworksapivb6.chm::/sldworks~View3D~DisplayState.html).

## Examples

See the [IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html) examples.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
