---
title: "Type Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~Type.html"
---

# Type Property (IScaleFeatureData)

Gets or sets the scale type.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of scale as defined in [swScaleType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swScaleType_e.html)

## VBA Syntax

See [ScaleFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~Type.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
