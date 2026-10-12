---
title: "OffsetPlaneReference Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "OffsetPlaneReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~OffsetPlaneReference.html"
---

# OffsetPlaneReference Property (ISMNormalCutFeatureData2)

Gets or sets the offset plane reference for the Normal Cut.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetPlaneReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Object

instance.OffsetPlaneReference = value

value = instance.OffsetPlaneReference
```

### C#

```csharp
System.object OffsetPlaneReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ OffsetPlaneReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html) or top or bottom [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) of the sheet metal body

## VBA Syntax

See [SMNormalCutFeatureData2::OffsetPlaneReference](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~OffsetPlaneReference.html).

## Remarks

This property is valid only if [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.html) is set to [swNormalCutParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
