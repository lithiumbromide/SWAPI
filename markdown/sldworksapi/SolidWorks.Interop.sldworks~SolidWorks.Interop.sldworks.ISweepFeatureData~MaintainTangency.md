---
title: "MaintainTangency Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "MaintainTangency"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MaintainTangency.html"
---

# MaintainTangency Property (ISweepFeatureData)

Gets or sets whether to merge tangent faces in this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaintainTangency As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.MaintainTangency = value

value = instance.MaintainTangency
```

### C#

```csharp
System.bool MaintainTangency {get; set;}
```

### C++/CLI

```cpp
property System.bool MaintainTangency {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge tangent faces, false to not (see **Remarks**)

## VBA Syntax

See [SweepFeatureData::MaintainTangency](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~MaintainTangency.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

If the sweep profile has tangent segments, true causes the corresponding surfaces in the resulting sweep to be tangent. Faces that can be represented as a plane, cylinder, or cone are maintained. Other adjacent faces are merged, and the profiles are approximated. Sketch arcs may be converted to splines.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndTangencyType.html)
[ISweepFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartTangencyType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
