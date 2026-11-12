---
title: "PartingLines Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "PartingLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PartingLines.html"
---

# PartingLines Property (IPartingSurfaceFeatureData)

Gets or sets the entities for the parting lines for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartingLines As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Object

instance.PartingLines = value

value = instance.PartingLines
```

### C#

```csharp
System.object PartingLines {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PartingLines {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [parting-line features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData.html) to use as parting lines

## VBA Syntax

See [PartingSurfaceFeatureData::PartingLines](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~PartingLines.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesCount.html)
[IPartingSurfaceFeatureData::GetPartingLinesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesType.html)
[IPartingSurfaceFeatureData::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~IGetPartingLines.html)
[IPartingSurfaceFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ISetPartingLines.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
