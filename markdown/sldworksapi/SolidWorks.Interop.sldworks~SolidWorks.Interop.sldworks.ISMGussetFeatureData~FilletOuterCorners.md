---
title: "FilletOuterCorners Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "FilletOuterCorners"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletOuterCorners.html"
---

# FilletOuterCorners Property (ISMGussetFeatureData)

Gets or sets whether to fillet the outer corners of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property FilletOuterCorners As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.FilletOuterCorners = value

value = instance.FilletOuterCorners
```

### C#

```csharp
System.bool FilletOuterCorners {get; set;}
```

### C++/CLI

```cpp
property System.bool FilletOuterCorners {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fillet the outer corners of this gusset, false to not

## VBA Syntax

See [SMGussetFeatureData::FilletOuterCorners](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~FilletOuterCorners.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

After setting this property, set [ISMGussetFeatureData::OuterCornerFilletRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~OuterCornerFilletRadius.html).

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::FilletInnerCorners Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletInnerCorners.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
