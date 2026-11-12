---
title: "Name Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Name.html"
---

# Name Property (IView3D)

Gets or sets the name of this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of this 3D View

## VBA Syntax

See [View3D::Name](ms-its:sldworksapivb6.chm::/sldworks~View3D~Name.html).

## Examples

See the [IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html) examples.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
