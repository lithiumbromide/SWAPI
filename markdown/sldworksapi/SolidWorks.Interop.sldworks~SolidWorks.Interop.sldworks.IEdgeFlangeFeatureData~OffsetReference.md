---
title: "OffsetReference Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "OffsetReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetReference.html"
---

# OffsetReference Property (IEdgeFlangeFeatureData)

Gets or sets the flange length reference for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Object

instance.OffsetReference = value

value = instance.OffsetReference
```

### C#

```csharp
System.object OffsetReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ OffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flange length reference for this edge flange

## VBA Syntax

See [EdgeFlangeFeatureData::OffsetReference](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~OffsetReference.html).

## Remarks

This property is valid for all settings of [IEdgeFlangeFeatureData::OffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html) except [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetBlind.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::OffsetDimType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDimType.html)
[IEdgeFlangeFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDistance.html)
[IEdgeFlangeFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
