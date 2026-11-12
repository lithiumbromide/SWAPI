---
title: "TrimAndKnit Property (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "TrimAndKnit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~TrimAndKnit.html"
---

# TrimAndKnit Property (IRuledSurfaceFeatureData)

Gets or sets whether to trim and knit the surfaces of this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimAndKnit As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim value As System.Boolean

instance.TrimAndKnit = value

value = instance.TrimAndKnit
```

### C#

```csharp
System.bool TrimAndKnit {get; set;}
```

### C++/CLI

```cpp
property System.bool TrimAndKnit {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to trim and knit surfaces, false to not

## VBA Syntax

See [RuledSurfaceFeatureData::TrimAndKnit](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~TrimAndKnit.html).

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
