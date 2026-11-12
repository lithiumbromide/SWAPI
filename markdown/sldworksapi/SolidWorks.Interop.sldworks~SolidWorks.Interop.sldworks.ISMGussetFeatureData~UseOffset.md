---
title: "UseOffset Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "UseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseOffset.html"
---

# UseOffset Property (ISMGussetFeatureData)

Gets or sets whether to offset the gusset section plane from a specified [reference point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.UseOffset = value

value = instance.UseOffset
```

### C#

```csharp
System.bool UseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool UseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset the gusset section plane, false to not

## VBA Syntax

See [SMGussetFeatureData::UseOffset](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~UseOffset.html).

## Examples

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) examples.

## Remarks

After setting this property to true, set the [offset distance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~OffsetDistance.html).

If a reference point is not set, the offset is applied to an assumed reference point. For insertion of the first gusset, the assumed reference point is on the end of the sheet metal bend. For second and subsequent gusset insertions, the assumed reference point is on the edge of the gusset last inserted.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::FlipOffset Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipOffset.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
