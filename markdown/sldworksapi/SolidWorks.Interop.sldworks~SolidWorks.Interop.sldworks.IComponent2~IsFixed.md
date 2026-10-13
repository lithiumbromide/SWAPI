---
title: "IsFixed Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsFixed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsFixed.html"
---

# IsFixed Method (IComponent2)

Gets whether the component is fixed or floating.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsFixed() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsFixed()
```

### C#

```csharp
System.bool IsFixed()
```

### C++/CLI

```cpp
System.bool IsFixed();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component is fixed, false if it is floating

## VBA Syntax

See [Component2::IsFixed](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsFixed.html).

## Examples

[Get Component by Name (C#)](Get_Component_by_Name_Example_CSharp.htm)
[Get Component by Name (VB.NET)](Get_Component_by_Name_Example_VBNET.htm)
[Get Component by Name (VBA)](Get_Component_by_Name_Example_VB.htm)
[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

## Remarks

This method only applies to the top level of components. To get the actual state of sub-assemblies, you must get the [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object of the subassembly, show the desired configuration, and get the state (fixed or floating) of the lower components.

To determine if a component is fixed or floating, you must begin the traversal from the subassembly document in the appropriate configuration instead of from the root level. At the root level, all of the components in the subassembly are allowed to move.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::FixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FixComponent.html)
[IAssemblyDoc::TemporaryFixGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroup.html)
[IAssemblyDoc::TemporaryFixGroupExit Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroupExit.html)
[IAssemblyDoc::UnfixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UnfixComponent.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
