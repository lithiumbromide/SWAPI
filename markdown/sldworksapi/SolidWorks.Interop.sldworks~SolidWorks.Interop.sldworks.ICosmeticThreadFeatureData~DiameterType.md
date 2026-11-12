---
title: "DiameterType Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "DiameterType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~DiameterType.html"
---

# DiameterType Property (ICosmeticThreadFeatureData)

Gets the type of diameter for the cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DiameterType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer

value = instance.DiameterType
```

### C#

```csharp
System.int DiameterType {get;}
```

### C++/CLI

```cpp
property System.int DiameterType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of value for the diameter as defined in [swCosmeticThreadDiameterType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticThreadDiameterType_e.html)

## VBA Syntax

See [CosmeticThreadFeatureData::DiameterType](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~DiameterType.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## Remarks

Use [ICosmeticThreadFeatureData::Diameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~Diameter.html) to get or set the diameter of the cosmetic thread.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
