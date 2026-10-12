---
title: "GetChildren Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html"
---

# GetChildren Method (IComponent2)

Gets all of the children components of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChildren() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetChildren()
```

### C#

```csharp
System.object GetChildren()
```

### C++/CLI

```cpp
System.Object^ GetChildren();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [Component2::GetChildren](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetChildren.html).

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Make All Assembly Components Visible (VBA)](Make_All_Assembly_Components_Visible_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

## Remarks

If this assembly component is a part document, SOLIDWORKS returns NULL. If this assembly component is the root component or a subassembly, then this method returns the child components that belong to the assembly document.

The typical order of calls needed in assembly traversal is:

1. [IConfigurationManager::ActiveConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html) (called only once)
2. [IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html) (called only once)
3. IComponent2::GetChildren (called recursively)

You must call the IComponent2::GetChildren method recursively because it returns only the immediate (one level) children. It does not get child components of the sub-assemblies. For example, if one of the child components of a component is a sub-assembly that has its own children, those children are not returned by this method. You need to call this method again from that sub-assembly component to get its children.

For a given component, this method returns all of the immediate child components. This includes suppressed, hidden, and lightweight components. Use [IComponent2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Visible.html) and [IComponent2::GetSuppression](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetSuppression.html) to detect the component states.

Results of an assembly traversal vary based on the configuration currently displayed in your main assembly and based on the configuration referenced by the subassembly component. The list of child components that this method returns can be different depending on which configuration is referenced by the component (see IConfigurationManager::ActiveConfiguration and [IComponent2::ReferencedConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~ReferencedConfiguration.html)).

For example, if one configuration of your main assembly contains a suppressed subassembly, IComponent2::GetChildren returns an empty array when you call it from that suppressed subassembly component. As another example, a subassembly document (.sldasm file) can contain several configurations, each of which has varying states of suppression for its child components. When inserted into your main assembly, this subassembly
document can reference any of these configurations. As a result, you might find that the child component suppression states vary based on which configuration is referenced by the subassembly component.

**NOTE:** Components might not be returned in the same order from call to call.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[Component2::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.html)
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
