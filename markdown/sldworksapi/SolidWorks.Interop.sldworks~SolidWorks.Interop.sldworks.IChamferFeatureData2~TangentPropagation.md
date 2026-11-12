---
title: "TangentPropagation Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "TangentPropagation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~TangentPropagation.html"
---

# TangentPropagation Property (IChamferFeatureData2)

Gets or sets whether to extend the chamfer to all faces that are tangent to the selected faces or edges.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentPropagation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Boolean

instance.TangentPropagation = value

value = instance.TangentPropagation
```

### C#

```csharp
System.bool TangentPropagation {get; set;}
```

### C++/CLI

```cpp
property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to propagate chamfer to tangent faces, false to not

## VBA Syntax

See [ChamferFeatureData2::TangentPropagation](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~TangentPropagation.html).

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
