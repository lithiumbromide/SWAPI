---
title: "ConfigurationName Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "ConfigurationName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~ConfigurationName.html"
---

# ConfigurationName Property (IView3D)

Gets or sets the name of this 3D View's configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.String

instance.ConfigurationName = value

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Configuration name

## VBA Syntax

See [View3D::ConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~View3D~ConfigurationName.html).

## Examples

See the [IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html) examples.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
