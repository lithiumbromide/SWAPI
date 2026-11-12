---
title: "GetConfigurationByName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetConfigurationByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html"
---

# GetConfigurationByName Method (IModelDoc2)

Gets the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationByName( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim value As System.Object

value = instance.GetConfigurationByName(Name)
```

### C#

```csharp
System.object GetConfigurationByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ GetConfigurationByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Configuration name

### Return Value

[Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) or NULL if the operation fails

## VBA Syntax

See [ModelDoc2::GetConfigurationByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetConfigurationByName.html).

## Examples

[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)
[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Get Custom Properties (VBA)](Get_Custom_Properties_Example_VB.htm)
[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

## Remarks

If the specified configuration has not been activated, then some data may be unavailable. For example, attempting to traverse assembly components for a configuration that has not been activated results in a NULL root component being returned from [IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html). However, the IConfiguration object returned is useful for obtaining data that is stored with the IConfiguration object, such as the [IConfiguration::AlternateName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~AlternateName.html) value. The specified configuration does not have to be activated to obtain this type of stored information.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
