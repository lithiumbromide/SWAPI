---
title: "IGetConfigurationByName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetConfigurationByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html"
---

# IGetConfigurationByName Method (IModelDoc2)

Gets the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConfigurationByName( _
   ByVal Name As System.String _
) As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim value As Configuration

value = instance.IGetConfigurationByName(Name)
```

### C#

```csharp
Configuration IGetConfigurationByName(
   System.string Name
)
```

### C++/CLI

```cpp
Configuration^ IGetConfigurationByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Specified configuration name

### Return Value

[Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) or NULL if the operation fails

## VBA Syntax

See [ModelDoc2::IGetConfigurationByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetConfigurationByName.html).

## Remarks

If the specified configuration has not been activated, then some data may be unavailable. For example, attempting to traverse assembly components for a configuration that has not been activated results in a NULL root component being returned from [IConfiguration::IGetRootComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetRootComponent2.html). However, the IConfiguration object returned is useful for obtaining data that is stored with the IConfiguration object, such as the [IConfiguration::AlternateName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~AlternateName.html) value. The specified configuration does not have to be activated to obtain this type of stored information.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::DeleteConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
