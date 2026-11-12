---
title: "Type Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~Type.html"
---

# Type Property (IHemFeatureData)

Gets or sets the hem type.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
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

Hem type as defined in [swHemTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemTypes_e.html)

## VBA Syntax

See [HemFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~Type.html).

## Examples

See [IHemFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHemFeatureData.html) examples.

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
