---
title: "Solving Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "Solving"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Solving.html"
---

# Solving Property (IComponent2)

Gets the **Solve as** option (rigid or flexible) of this component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Solving As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.Solving
```

### C#

```csharp
System.int Solving {get;}
```

### C++/CLI

```cpp
property System.int Solving {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

**Solve as** option as defined in [swComponentSolvingOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSolvingOption_e.html)

## VBA Syntax

See [Component2::Solving](ms-its:sldworksapivb6.chm::/sldworks~Component2~Solving.html).

## Examples

[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

## Remarks

You can also use [IAssemblyDoc::CompConfigProperties4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.html) to set the **Solve as** state of a component.

This property only applies to subassembly components, not part components. If you try to get the **Solve as** option of a part component, this property returns -1.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
