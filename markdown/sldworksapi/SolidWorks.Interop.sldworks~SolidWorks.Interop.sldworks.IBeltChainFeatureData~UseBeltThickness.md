---
title: "UseBeltThickness Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "UseBeltThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~UseBeltThickness.html"
---

# UseBeltThickness Property (IBeltChainFeatureData)

Gets and sets whether to specify belt thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseBeltThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Boolean

instance.UseBeltThickness = value

value = instance.UseBeltThickness
```

### C#

```csharp
System.bool UseBeltThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool UseBeltThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to specify belt thickness, false to not

## VBA Syntax

See [BeltChainFeatureData::UseBeltThickness](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~UseBeltThickness.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

If this property is true, use [IBeltChainFeatureData::BeltThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltThickness.html) to specify belt thickness.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
