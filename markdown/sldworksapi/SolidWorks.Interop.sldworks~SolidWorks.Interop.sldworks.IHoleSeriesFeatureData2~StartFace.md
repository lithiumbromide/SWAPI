---
title: "StartFace Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "StartFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~StartFace.html"
---

# StartFace Property (IHoleSeriesFeatureData2)

Gets the start face for this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StartFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Object

value = instance.StartFace
```

### C#

```csharp
System.object StartFace {get;}
```

### C++/CLI

```cpp
property System.Object^ StartFace {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Start [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [HoleSeriesFeatureData2::StartFace](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~StartFace.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::EndFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~EndFace.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
