---
title: "GussetThickness Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "GussetThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~GussetThickness.html"
---

# GussetThickness Property (ISMGussetFeatureData)

Gets or sets the indent thickness of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property GussetThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.GussetThickness = value

value = instance.GussetThickness
```

### C#

```csharp
System.double GussetThickness {get; set;}
```

### C++/CLI

```cpp
property System.double GussetThickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Indent thickness

## VBA Syntax

See [SMGussetFeatureData::GussetThickness](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~GussetThickness.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html) is set to 0.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
