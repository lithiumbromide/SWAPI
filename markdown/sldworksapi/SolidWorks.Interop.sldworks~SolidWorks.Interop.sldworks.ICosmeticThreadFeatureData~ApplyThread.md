---
title: "ApplyThread Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "ApplyThread"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~ApplyThread.html"
---

# ApplyThread Property (ICosmeticThreadFeatureData)

Gets or sets how to apply the cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyThread As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer

instance.ApplyThread = value

value = instance.ApplyThread
```

### C#

```csharp
System.int ApplyThread {get; set;}
```

### C++/CLI

```cpp
property System.int ApplyThread {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

How to apply the thread as defined in [swCosmeticThreadType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticThreadType_e.html) (see **Remarks**)

## VBA Syntax

See [CosmeticThreadFeatureData::ApplyThread](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~ApplyThread.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## Remarks

If the value is swApplyCosmeticThread_Blind, then call [ICosmeticThreadFeatureData::BlindDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~BlindDepth.html) to get or set the depth of the thread.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)
[ICosmeticThreadFeatureData::BlindDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~BlindDepth.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
