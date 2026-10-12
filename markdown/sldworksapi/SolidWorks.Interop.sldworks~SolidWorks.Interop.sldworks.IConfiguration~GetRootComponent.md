---
title: "GetRootComponent Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetRootComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent.html"
---

# GetRootComponent Method (IConfiguration)

Obsolete. Superseded by [IConfiguration::GetRootComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRootComponent() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Object

value = instance.GetRootComponent()
```

### C#

```csharp
System.object GetRootComponent()
```

### C++/CLI

```cpp
System.Object^ GetRootComponent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Root component and an [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object

## VBA Syntax

See [Configuration::GetRootComponent](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetRootComponent.html).

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Make All Assembly Components Visible (VBA)](Make_All_Assembly_Components_Visible_Example_VB.htm)
[Traverse Assembly At Component and Feature Levels (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)

## Remarks

Because every assembly has at least one configuration, you can use this method to begin traversing an assembly and its components.

This method returns a component object that is, essentially, a launching point for your assembly traversal. It is useful only for calling [IComponent2::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetChildren.html). Most other IComponent2 object functions do not work with this root component object and return null or Nothing or an error condition. You can call [IComponent2::IsRoot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IsRoot.html) to determine if you have the root component.

An IComponent2 object is based on the currently active configuration; one assembly configuration might suppress the component, while another might display it. Therefore, your traversal of IComponent2 objects might vary if you switch to a different configuration.

The order of calls used in a typical assembly traversal is:

1. [IConfigurationManager::ActiveConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html) (called only once)
2. IConfiguration::GetRootComponent (called only once)
3. IComponent2::GetChildren (called recursively)

From the SOLIDWORKS API, the IConfiguration and IComponent2 objects provide access to all the child components, their transforms, their bodies, as seen in a specific assembly configuration. The component body objects and component transforms can vary based on the configuration; therefore, you should traverse components for each configuration. For example, one assembly configuration might include an assembly-level feature that cuts a hole through each of the components in the assembly.

You can use [IComponent2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBody.html) on each assembly component to get the body of each component with the hole feature that was applied in this configuration. If you switch to a configuration without the assembly-level hole and re-traverse the component objects, then IComponent2::IGetBody returns the body object without the hole feature.

SOLIDWORKS generates an IAssemblyDoc [RegenNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler.html) event to indicate that a change might have taken place in one of your components. If you receive an IAssemblyDoc RegenNotify event, then you should re-traverse your components to be sure that your information is up-to-date.

If this method is called from the configuration of a part document, SOLIDWORKS returns null or Nothing.

You should use this method of assembly traversal to replace previous calls to the member class.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.html)
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html)
[IComponent2::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.html)
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html)
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html)
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.html)
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.html)
