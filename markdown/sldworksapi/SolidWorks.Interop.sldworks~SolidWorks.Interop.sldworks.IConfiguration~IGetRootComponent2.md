---
title: "IGetRootComponent2 Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IGetRootComponent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.html"
---

# IGetRootComponent2 Method (IConfiguration)

Obsolete. Superseded by [IConfiguration::GetRootComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRootComponent2() As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As Component2

value = instance.IGetRootComponent2()
```

### C#

```csharp
Component2 IGetRootComponent2()
```

### C++/CLI

```cpp
Component2^ IGetRootComponent2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the root component, an [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object

## VBA Syntax

See [Configuration::IGetRootComponent2](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IGetRootComponent2.html).

## Remarks

Because every assembly has at least one configuration, you can use this method to begin traversing an assembly and its components.

This method returns a component object that is, essentially, a launching point for your assembly traversal. It is useful only for calling [IComponent2::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetChildren.html). Most other IComponent2 object functions do not work with this root component object and return NULL or an error condition. You can call [IComponent2::IsRoot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IsRoot.html) to determine if you have the root component.

An IComponent2 object is based on the currently active configuration; one assembly configuration might suppress the component, while another might display it. Therefore, your traversal of IComponent2 objects might vary if you switch to a different configuration.

The order of calls used in a typical assembly traversal is:

1. [IConfigurationManager::ActiveConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html) (called only once)
2. IConfiguration::IGetRootComponent 2(called only once)
3. IComponent2::IGetChildren (called recursively)

From the SOLIDWORKS API, the IConfiguration and IComponent2 objects provide access to all the child components, their transforms, their bodies, as seen in a specific assembly configuration. The component body objects and component transforms can vary based on the configuration; therefore, you should traverse components for each configuration. For example, one assembly configuration might include an assembly-level feature that cuts a hole through each of the components in the assembly.

You can use [IComponent2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetBody.html) on each assembly component to get the body of each component with the hole feature that was applied in this configuration. If you switch to a configuration without the assembly-level hole and re-traverse the component objects, then IComponent2::IGetBody returns the body object without the hole feature.

SOLIDWORKS generates an IAssemblyDoc [RegenNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler.html) event to indicate that a change might have taken place in one of your components. If you receive an IAssemblyDoc RegenNotify event, then you should re-traverse your components to be sure that your information is up-to-date.

If this method is called from the configuration of a part document, SOLIDWORKS returns NULL.

You should use this method of assembly traversal to replace previous calls to the member class.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.html)
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)
[IConfiguration::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.html)
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.html)
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html)
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html)
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html)
[IComponent2::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.html)
[IComponent2::IGetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildrenCount.html)
