---
title: "DeleteConfiguration2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeleteConfiguration2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.html"
---

# DeleteConfiguration2 Method (IModelDoc2)

Deletes a configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteConfiguration2( _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.DeleteConfiguration2(ConfigurationName)
```

### C#

```csharp
System.bool DeleteConfiguration2(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool DeleteConfiguration2(
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Name of the configuration to delete

### Return Value

True if the configuration is deleted, false if not

## VBA Syntax

See [ModelDoc2::DeleteConfiguration2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeleteConfiguration2.html).

## Remarks

The configuration cannot be the active configuration.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::EditConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditConfiguration3.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
