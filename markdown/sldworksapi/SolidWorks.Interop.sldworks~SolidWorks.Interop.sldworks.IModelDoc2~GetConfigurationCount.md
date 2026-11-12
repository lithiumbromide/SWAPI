---
title: "GetConfigurationCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetConfigurationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html"
---

# GetConfigurationCount Method (IModelDoc2)

Gets the number of configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetConfigurationCount()
```

### C#

```csharp
System.int GetConfigurationCount()
```

### C++/CLI

```cpp
System.int GetConfigurationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of configurations

## VBA Syntax

See [ModelDoc2::GetConfigurationCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetConfigurationCount.html).

## Examples

[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision NUmber 10.0
