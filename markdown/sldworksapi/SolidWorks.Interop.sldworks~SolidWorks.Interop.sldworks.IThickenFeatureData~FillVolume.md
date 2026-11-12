---
title: "FillVolume Property (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "FillVolume"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FillVolume.html"
---

# FillVolume Property (IThickenFeatureData)

Gets or sets whether to fill a volume with this thicken feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FillVolume As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThickenFeatureData
Dim value As System.Boolean

instance.FillVolume = value

value = instance.FillVolume
```

### C#

```csharp
System.bool FillVolume {get; set;}
```

### C++/CLI

```cpp
property System.bool FillVolume {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fill a volume, false to not

## VBA Syntax

See [ThickenFeatureData::FillVolume](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~FillVolume.html).

## Examples

See the [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html) examples.

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
