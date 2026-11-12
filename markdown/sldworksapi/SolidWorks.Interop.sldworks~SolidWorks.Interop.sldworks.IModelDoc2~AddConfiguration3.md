---
title: "AddConfiguration3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddConfiguration3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html"
---

# AddConfiguration3 Method (IModelDoc2)

Adds a new configuration to this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConfiguration3( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim value As System.Object

value = instance.AddConfiguration3(Name, Comment, AlternateName, Options)
```

### C#

```csharp
System.object AddConfiguration3(
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options
)
```

### C++/CLI

```cpp
System.Object^ AddConfiguration3(
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the new configuration
- `Comment`: Comment displayed in Configuration Properties
- `AlternateName`: Alternate configuration name; used if swConfigOption_UseAlternateName is set to true
- `Options`: Combination of one or more configuration options as defined in [swConfigurationOptions2_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html)

### Return Value

Newly created [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [ModelDoc2::AddConfiguration3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddConfiguration3.html).

## Examples

[Add Configuration and Promote Child Components in BOM (C#)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_CSharp.htm)
[Add Configuration and Promote Child Components in BOM (VB.NET)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VBNET.htm)
[Add Configuration and Promote Child Components in BOM (VBA)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.html)
[IModelDoc2::EditConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditConfiguration3.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
