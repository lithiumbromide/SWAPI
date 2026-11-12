---
title: "ConfigurationManager Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ConfigurationManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html"
---

# ConfigurationManager Property (IModelDoc2)

Gets the [IConfigurationManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager.html) object, which allows access to a configuration in a model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationManager As ConfigurationManager
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As ConfigurationManager

value = instance.ConfigurationManager
```

### C#

```csharp
ConfigurationManager ConfigurationManager {get;}
```

### C++/CLI

```cpp
property ConfigurationManager^ ConfigurationManager {
   ConfigurationManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IConfigurationManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager.html) object

## VBA Syntax

See [ModelDoc2::ConfigurationManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ConfigurationManager.html).

## Examples

[Get Configuration Parameters (C++)](Get_Configuration_Parameters_Example_CPlusPlus_COM.htm)
[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)
[Extract Configuration-specific Parameters (VBA)](Extract_Configuration-Specific_Parameters_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
