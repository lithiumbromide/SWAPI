---
title: "Path Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "Path"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html"
---

# Path Property (ISweptFlangeFeatureData)

Gets or sets the sweep path of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Path As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Object

instance.Path = value

value = instance.Path
```

### C#

```csharp
System.object Path {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Path {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)s or a [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html) of lines and arcs

## VBA Syntax

See [SweptFlangeFeatureData::Path](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~Path.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) and [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

If the sweep path is a closed loop, then [ISweptFlangeFeatureData::StartOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~StartOffset.html) and [ISweptFlangeFeatureData::EndOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~EndOffset.html) are not valid.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)
[ISweptFlangeFeatureData::GetPathType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetPathType.html)
[ISweptFlangeFeatureData::CylindricalOrConicalEdge Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~CylindricalOrConicalEdge.html)
[ISweptFlangeFeatureData::FlattenAlongPath Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
