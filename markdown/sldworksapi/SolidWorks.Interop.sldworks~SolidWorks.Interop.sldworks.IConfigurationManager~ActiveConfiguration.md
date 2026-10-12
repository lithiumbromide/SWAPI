---
title: "ActiveConfiguration Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "ActiveConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html"
---

# ActiveConfiguration Property (IConfigurationManager)

Gets the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveConfiguration As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As Configuration

value = instance.ActiveConfiguration
```

### C#

```csharp
Configuration ActiveConfiguration {get;}
```

### C++/CLI

```cpp
property Configuration^ ActiveConfiguration {
   Configuration^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) object

## VBA Syntax

See [ConfigurationManager::ActiveConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~ActiveConfiguration.html).

## Examples

[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

## Remarks

If this document is an assembly, then you could use this property to begin your traversal of the assembly components by making a subsequent call to [IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html) or [IConfiguration::IGetRootComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetRootComponent2.html).

An [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object is based on the currently active configuration; one assembly configuration might suppress the component, while another might display it. Therefore, your traversal of IComponent2 objects might vary if you switch to a different configuration.

You should use this method of assembly traversal to replace previous calls to the Member class.

The order of calls used in a typical assembly traversal is:

1. IConfigurationManager::ActiveConfiguration (called only once)
2. IConfiguration::GetRootComponent or IConfiguration::IGetRootComponent2 (called only once)
3. [IComponent2::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetChildren.html) or [IComponent::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetChildren.html). (called recursively)

From the SOLIDWORKS API, the I[Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) and IComponent2 objects provide access to all the child components, their transforms, their bodies, as seen in a specific assembly configuration. The component body objects and component transforms can vary based on the configuration; therefore, you should traverse components for each configuration.

You can use [IComponent2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBody.html) on each assembly component to get the body of each component with the hole feature that was applied in this configuration. If you switch to a configuration without the assembly-level hole and re-traverse the component objects, then IComponent2::IGetBody returns the body object without the hole feature.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IAssemblyDoc::AddComponentConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::AddConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
