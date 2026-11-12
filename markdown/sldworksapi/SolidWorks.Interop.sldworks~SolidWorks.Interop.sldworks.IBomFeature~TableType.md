---
title: "TableType Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "TableType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.html"
---

# TableType Property (IBomFeature)

Gets and sets the type of table for the Bill of Materials.

## Syntax

### Visual Basic (Declaration)

```vb
Property TableType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.TableType = value

value = instance.TableType
```

### C#

```csharp
System.int TableType {get; set;}
```

### C++/CLI

```cpp
property System.int TableType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of table for the Bill of Materials as defined in [swBomType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)

## VBA Syntax

See [BomFeature::TableType](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~TableType.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::Configuration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Configuration.html)
[IBomFeature::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurationCount.html)
[IBomFeature::GetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.html)
[IBomFeature::IGetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.html)
[IBomFeature::SetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.html)
[IBomFeature::ISetConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.html)
[IBomFeature::DetailedCutList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
