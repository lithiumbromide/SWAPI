---
title: "AlternateName Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "AlternateName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.html"
---

# AlternateName Property (IConfiguration)

Gets or sets the configuration's alternate name (i.e., user-specified name).

## Syntax

### Visual Basic (Declaration)

```vb
Property AlternateName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.String

instance.AlternateName = value

value = instance.AlternateName
```

### C#

```csharp
System.string AlternateName {get; set;}
```

### C++/CLI

```cpp
property System.String^ AlternateName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Alternate or user-specified name for the configuration

## VBA Syntax

See [Configuration::AlternateName](ms-its:sldworksapivb6.chm::/sldworks~Configuration~AlternateName.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

## Remarks

To display the configuration's alternate name as the part number in the bill of materials, use [IConfiguration::UseAlternateNameInBOM](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.html).

Configuration names must not contain any special characters reserved by SOLIDWORKS.

If you specify [IConfiguration::BOMPartNoSource](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~BOMPartNoSource.html) with anything other than [swBOMPartNumberSource_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMPartNumberSource_e.html).swBOMPartNumber_UserSpecified, then this property is set to an empty string.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html)
