---
title: "Type Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Type.html"
---

# Type Property (ISimpleFilletFeatureData2)

Gets the type of simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of simple fillet feature as defined in [swSimpleFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletType_e.html)

## VBA Syntax

See [SimpleFilletFeatureData2::Type](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~Type.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
