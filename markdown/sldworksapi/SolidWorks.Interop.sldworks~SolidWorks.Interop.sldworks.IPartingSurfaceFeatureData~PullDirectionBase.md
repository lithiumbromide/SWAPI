---
title: "PullDirectionBase Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "PullDirectionBase"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionBase.html"
---

# PullDirectionBase Property (IPartingSurfaceFeatureData)

Gets or sets the entity that defines the direction of pull for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PullDirectionBase As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Object

instance.PullDirectionBase = value

value = instance.PullDirectionBase
```

### C#

```csharp
System.object PullDirectionBase {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PullDirectionBase {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), or [axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html)

## VBA Syntax

See [PartingSurfaceFeatureData::PullDirectionBase](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~PullDirectionBase.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
