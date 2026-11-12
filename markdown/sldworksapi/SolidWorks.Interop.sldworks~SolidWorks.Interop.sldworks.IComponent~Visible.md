---
title: "Visible Property (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~Visible.html"
---

# Visible Property (IComponent)

Obsolete. Superseded by [IComponent2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Visible.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim value As System.Integer

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.int Visible {get; set;}
```

### C++/CLI

```cpp
property System.int Visible {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component::Visible](ms-its:sldworksapivb6.chm::/sldworks~Component~Visible.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
