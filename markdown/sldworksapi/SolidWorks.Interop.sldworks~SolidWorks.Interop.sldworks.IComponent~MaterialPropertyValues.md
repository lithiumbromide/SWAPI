---
title: "MaterialPropertyValues Property (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "MaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~MaterialPropertyValues.html"
---

# MaterialPropertyValues Property (IComponent)

Obsolete. Superseded by [IComponent2::MaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~MaterialPropertyValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialPropertyValues As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim value As System.Object

instance.MaterialPropertyValues = value

value = instance.MaterialPropertyValues
```

### C#

```csharp
System.object MaterialPropertyValues {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MaterialPropertyValues {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component::MaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Component~MaterialPropertyValues.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
