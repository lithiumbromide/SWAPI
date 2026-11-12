---
title: "ShowConfiguration2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ShowConfiguration2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html"
---

# ShowConfiguration2 Method (IModelDoc2)

Shows the named configuration by switching to that configuration and making it the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowConfiguration2( _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.ShowConfiguration2(ConfigurationName)
```

### C#

```csharp
System.bool ShowConfiguration2(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool ShowConfiguration2(
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Name of the configuration to display

### Return Value

True if the configuration is activated successfully, false if not

## VBA Syntax

See [ModelDoc2::ShowConfiguration2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ShowConfiguration2.html).

## Examples

[Get Custom Property Values on Cut List Folders (VBA)](Get_Custom_Property_Values_On_Cut_List_Folders_Example_VB.htm)
[Iterate Through All Configurations (VBA)](Iterate_Through_All_Configurations_Example_VB.htm)
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)
[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)
[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

## Remarks

Configurations allow you to save certain display characteristics with each of the assembly components. This method allows you to retrieve a previously saved configuration.

If you made changes to the model and the configuration to which you are switching needs to be updated to reflect those changes, then you must rebuild the model using [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html). Otherwise, the FeatureManager design tree will show the model as needing to be rebuilt.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditConfiguration3.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IConfigurationManager::AddConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
