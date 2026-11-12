---
title: "FilletInnerCorners Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "FilletInnerCorners"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletInnerCorners.html"
---

# FilletInnerCorners Property (ISMGussetFeatureData)

Gets or sets whether to fillet the inner corners of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property FilletInnerCorners As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.FilletInnerCorners = value

value = instance.FilletInnerCorners
```

### C#

```csharp
System.bool FilletInnerCorners {get; set;}
```

### C++/CLI

```cpp
property System.bool FilletInnerCorners {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fillet the inner corners of this gusset, false to not

## VBA Syntax

See [SMGussetFeatureData::FilletInnerCorners](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~FilletInnerCorners.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

After setting this property, set [ISMGussetFeatureData::InnerCornerFilletRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~InnerCornerFilletRadius.html).

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::FilletOuterCorners Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletOuterCorners.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
