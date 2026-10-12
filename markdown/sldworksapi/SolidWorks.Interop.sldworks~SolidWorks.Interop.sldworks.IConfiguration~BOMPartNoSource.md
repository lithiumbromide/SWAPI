---
title: "BOMPartNoSource Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "BOMPartNoSource"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~BOMPartNoSource.html"
---

# BOMPartNoSource Property (IConfiguration)

Gets or sets the source of the part number used in the BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property BOMPartNoSource As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

instance.BOMPartNoSource = value

value = instance.BOMPartNoSource
```

### C#

```csharp
System.int BOMPartNoSource {get; set;}
```

### C++/CLI

```cpp
property System.int BOMPartNoSource {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Source of part number as defined in [swBOMPartNumberSource_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMPartNumberSource_e.html)

## VBA Syntax

See [Configuration::BOMPartNoSource](ms-its:sldworksapivb6.chm::/sldworks~Configuration~BOMPartNoSource.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)

## Remarks

If you specify this property with anything other than swBOMPartNumberSource_e.swBOMPartNumber_UserSpecified, then [IConfiguration::AlternateName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.html) is set to an empty string.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html)
[IConfiguration::UseAlternateNameInBOM Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
