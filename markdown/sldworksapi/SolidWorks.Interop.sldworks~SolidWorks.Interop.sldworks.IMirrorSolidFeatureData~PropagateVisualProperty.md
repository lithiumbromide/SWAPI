---
title: "PropagateVisualProperty Property (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "PropagateVisualProperty"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~PropagateVisualProperty.html"
---

# PropagateVisualProperty Property (IMirrorSolidFeatureData)

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all mirrored instances.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateVisualProperty As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
Dim value As System.Boolean

instance.PropagateVisualProperty = value

value = instance.PropagateVisualProperty
```

### C#

```csharp
System.bool PropagateVisualProperty {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateVisualProperty {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [MirrorSolidFeatureData::PropagateVisualProperty](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~PropagateVisualProperty.html).

## Remarks

True to propagate visual properties, false to not

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
