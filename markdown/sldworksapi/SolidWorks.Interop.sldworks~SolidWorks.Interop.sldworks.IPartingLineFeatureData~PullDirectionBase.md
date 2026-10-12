---
title: "PullDirectionBase Property (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "PullDirectionBase"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase.html"
---

# PullDirectionBase Property (IPartingLineFeatureData)

Gets or sets the direction of pull for the parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PullDirectionBase As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
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

Entity that indicates the direction of pull: [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), or [axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html)

## VBA Syntax

See [PartingLineFeatureData::PullDirectionBase](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~PullDirectionBase.html).

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.html)
[IPartingLineFeatureData::PullDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.html)
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
