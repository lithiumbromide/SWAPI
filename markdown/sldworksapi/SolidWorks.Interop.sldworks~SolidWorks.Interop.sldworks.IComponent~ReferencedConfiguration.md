---
title: "ReferencedConfiguration Property (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "ReferencedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~ReferencedConfiguration.html"
---

# ReferencedConfiguration Property (IComponent)

Obsolete. Superseded by [IComponent2::ReferencedConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~ReferencedConfiguration.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencedConfiguration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim value As System.String

instance.ReferencedConfiguration = value

value = instance.ReferencedConfiguration
```

### C#

```csharp
System.string ReferencedConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component::ReferencedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~Component~ReferencedConfiguration.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
