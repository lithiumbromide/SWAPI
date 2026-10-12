---
title: "TangentPropagation Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "TangentPropagation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TangentPropagation.html"
---

# TangentPropagation Property (ISweepFeatureData)

Gets or sets whether to propagate the sweep to the next tangent edge for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentPropagation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.TangentPropagation = value

value = instance.TangentPropagation
```

### C#

```csharp
System.bool TangentPropagation {get; set;}
```

### C++/CLI

```cpp
property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to propagate the sweep to the next tangent edge, false to cause the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge

## VBA Syntax

See [SweepFeatureData::TangentPropagation](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~TangentPropagation.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndTangencyType.html)
[ISweepFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartTangencyType.html)
[ISweepFeatureData::MaintainTangency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MaintainTangency.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
