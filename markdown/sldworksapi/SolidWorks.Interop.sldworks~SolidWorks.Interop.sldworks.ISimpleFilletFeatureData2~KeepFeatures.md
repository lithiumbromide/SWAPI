---
title: "KeepFeatures Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "KeepFeatures"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~KeepFeatures.html"
---

# KeepFeatures Property (ISimpleFilletFeatureData2)

Gets or sets whether to keep existing features on the entities selected for the fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepFeatures As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.KeepFeatures = value

value = instance.KeepFeatures
```

### C#

```csharp
System.bool KeepFeatures {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True keeps the existing features, false does not

## VBA Syntax

See [SimpleFilletFeatureData2::KeepFeatures](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~KeepFeatures.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
