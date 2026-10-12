---
title: "Preload Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "Preload"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Preload.html"
---

# Preload Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::Preload](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~Preload.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Preload As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.String

value = instance.Preload
```

### C#

```csharp
System.string Preload {get;}
```

### C++/CLI

```cpp
property System.String^ Preload {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Preload information

## VBA Syntax

See [HoleSeriesFeatureData::Preload](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~Preload.html).

## Remarks

The preload value is not available in the SOLIDWORKS Toolbox database.

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
