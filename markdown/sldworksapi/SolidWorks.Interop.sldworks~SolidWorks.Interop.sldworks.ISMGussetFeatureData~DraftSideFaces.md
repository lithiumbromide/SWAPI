---
title: "DraftSideFaces Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "DraftSideFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~DraftSideFaces.html"
---

# DraftSideFaces Property (ISMGussetFeatureData)

Gets or sets whether to draft the side faces of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftSideFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.DraftSideFaces = value

value = instance.DraftSideFaces
```

### C#

```csharp
System.bool DraftSideFaces {get; set;}
```

### C++/CLI

```cpp
property System.bool DraftSideFaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to draft the gusset side faces, false to not

## VBA Syntax

See [SMGussetFeatureData::DraftSideFaces](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~DraftSideFaces.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

After setting this property to true, set [ISMGussetFeatureData::DraftAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~DraftAngle.html).

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
