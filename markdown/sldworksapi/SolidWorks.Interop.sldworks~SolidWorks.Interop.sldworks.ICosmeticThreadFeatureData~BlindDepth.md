---
title: "BlindDepth Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "BlindDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~BlindDepth.html"
---

# BlindDepth Property (ICosmeticThreadFeatureData)

Gets or sets the depth of a blind cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlindDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Double

instance.BlindDepth = value

value = instance.BlindDepth
```

### C#

```csharp
System.double BlindDepth {get; set;}
```

### C++/CLI

```cpp
property System.double BlindDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Depth of the cosmetic thread (see **Remarks**)

## VBA Syntax

See [CosmeticThreadFeatureData::BlindDepth](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~BlindDepth.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## Remarks

If [ICosmeticThreadFeatureData::ApplyThread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~ApplyThread.html) is swApplyCosmeticThread_Blind, then use this property to get or set the depth of the cosmetic thread.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
