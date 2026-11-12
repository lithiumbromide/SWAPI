---
title: "AssemblyFeatureScope Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "AssemblyFeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AssemblyFeatureScope.html"
---

# AssemblyFeatureScope Property (ISimpleHoleFeatureData2)

Gets or sets whether to use scope for this assembly simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyFeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean

instance.AssemblyFeatureScope = value

value = instance.AssemblyFeatureScope
```

### C#

```csharp
System.bool AssemblyFeatureScope {get; set;}
```

### C++/CLI

```cpp
property System.bool AssemblyFeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use feature scope, false to not

## VBA Syntax

See [SimpleHoleFeatureData2::AssemblyFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~AssemblyFeatureScope.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html)
[ISimpleHoleFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelectComponents.html)
[ISimpleHoleFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
