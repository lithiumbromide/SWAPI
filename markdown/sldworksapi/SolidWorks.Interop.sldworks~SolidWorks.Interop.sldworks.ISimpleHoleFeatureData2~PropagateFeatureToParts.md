---
title: "PropagateFeatureToParts Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "PropagateFeatureToParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~PropagateFeatureToParts.html"
---

# PropagateFeatureToParts Property (ISimpleHoleFeatureData2)

Gets whether to propagate this assembly simple hole feature to the parts that it affects in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateFeatureToParts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
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

True to propagate this assembly simple hole feature to the parts that it affects in the model, false to not

## VBA Syntax

See [SimpleHoleFeatureData2::PropagateFeatureToParts](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~PropagateFeatureToParts.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AssemblyFeatureScope.html)
[ISimpleHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html)
[ISimpleHoleFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelectComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
