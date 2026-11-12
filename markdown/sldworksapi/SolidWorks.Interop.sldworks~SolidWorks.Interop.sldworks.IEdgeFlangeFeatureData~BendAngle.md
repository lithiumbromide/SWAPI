---
title: "BendAngle Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "BendAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~BendAngle.html"
---

# BendAngle Property (IEdgeFlangeFeatureData)

Gets or sets the bend angle of the edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.BendAngle = value

value = instance.BendAngle
```

### C#

```csharp
System.double BendAngle {get; set;}
```

### C++/CLI

```cpp
property System.double BendAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flange angle; default value is 1.5707963267949 radians

## VBA Syntax

See [EdgeFlangeFeatureData::BendAngle](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~BendAngle.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

If [IEdgeFlangeFeatureData::OffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html) is set to [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetUptoEdgeAndMerge to merge two bodies in a multibody part, then [IEdgeFlangeFeatureData::LockAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~LockAngle.html) is automatically set to true. You must set IEdgeFlangeFeatureData::LockAngle to false before you can use this property to set a new bend angle.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
