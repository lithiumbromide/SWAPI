---
title: "IsVirtual Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsVirtual"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html"
---

# IsVirtual Property (IComponent2)

Gets whether this component is a virtual component.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsVirtual As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

instance.IsVirtual = value

value = instance.IsVirtual
```

### C#

```csharp
System.bool IsVirtual {get; set;}
```

### C++/CLI

```cpp
property System.bool IsVirtual {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the component is a virtual component, false if not

## VBA Syntax

See [Component2::IsVirtual](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsVirtual.html).

## Examples

[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)
[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)

## Remarks

When you create components in the context of an assembly, the software can save them inside the assembly file, and you can immediately begin modeling. Later, you can save the components to external files or delete them. Also, no **In-Place** mate is created, so you can position and constrain the component however you want.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.html)
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.html)
[IComponent2::SaveVirtualComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent.html)
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
