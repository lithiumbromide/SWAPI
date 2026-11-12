---
title: "DraftAngle Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "DraftAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~DraftAngle.html"
---

# DraftAngle Property (ISMGussetFeatureData)

Gets or sets the angle by which to draft the side faces of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.DraftAngle = value

value = instance.DraftAngle
```

### C#

```csharp
System.double DraftAngle {get; set;}
```

### C++/CLI

```cpp
property System.double DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Draft angle in radians

## VBA Syntax

See [SMGussetFeatureData::DraftAngle](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~DraftAngle.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::DraftSideFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~DraftSideFaces.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
