---
title: "GetConfigurationNames Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html"
---

# GetConfigurationNames Method (IModelDoc2)

Gets the names of the configurations in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetConfigurationNames()
```

### C#

```csharp
System.object GetConfigurationNames()
```

### C++/CLI

```cpp
System.Object^ GetConfigurationNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the names of the configurations in the order they are created in this document

## VBA Syntax

See [ModelDoc2::GetConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetConfigurationNames.html).

## Examples

[Extract Configuration-specific Parameters (VBA)](Extract_Configuration-Specific_Parameters_Example_VB.htm)
[Get Custom Properties (VBA)](Get_Custom_Properties_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Iterate Through All Configurations (VBA)](Iterate_Through_All_Configurations_Example_VB.htm)
[List Custom Properties (VBA)](List_Custom_Properties_Example_VB.htm)
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)
[Remove Material Properties from Assembly Component (VBA)](Remove_Material_Properties_from_Assembly_Component_Example_VB.htm)
[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
