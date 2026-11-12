---
title: "PropagateFeatureToParts Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "PropagateFeatureToParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~PropagateFeatureToParts.html"
---

# PropagateFeatureToParts Property (IChamferFeatureData2)

Gets or sets whether to extend the chamfer feature to all affected parts in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateFeatureToParts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Boolean

instance.PropagateFeatureToParts = value

value = instance.PropagateFeatureToParts
```

### C#

```csharp
System.bool PropagateFeatureToParts {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateFeatureToParts {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to extend the chamfer feature to all affected parts in the assembly, false to not

## VBA Syntax

See [ChamferFeatureData2::PropagateFeatureToParts](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~PropagateFeatureToParts.html).

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
