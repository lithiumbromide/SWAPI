---
title: "Profile Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "Profile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Profile.html"
---

# Profile Property (ISweptFlangeFeatureData)

Gets or sets the sweep profile of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Profile As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Object

instance.Profile = value

value = instance.Profile
```

### C#

```csharp
System.object Profile {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Profile {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html) consisting of lines and arcs (see **Remarks**)

## VBA Syntax

See [SweptFlangeFeatureData::Profile](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~Profile.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) and [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

Splines are not supported in sweep profile sketches.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)
[ISweptFlangeFeatureData::FlattenAlongPath Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath.html)
[ISweptFlangeFeatureData::MaterialInside Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~MaterialInside.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
