---
title: "IMaterialPropertyValues Property (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "IMaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IMaterialPropertyValues.html"
---

# IMaterialPropertyValues Property (IComponent)

Obsolete. Superseded by [IComponent2::IMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IMaterialPropertyValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IMaterialPropertyValues As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim value As System.Double

instance.IMaterialPropertyValues = value

value = instance.IMaterialPropertyValues
```

### C#

```csharp
System.double IMaterialPropertyValues {get; set;}
```

### C++/CLI

```cpp
property System.double IMaterialPropertyValues {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component::IMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Component~IMaterialPropertyValues.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
