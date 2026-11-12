---
title: "AutoSelectComponents Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "AutoSelectComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelectComponents.html"
---

# AutoSelectComponents Property (ISimpleHoleFeatureData2)

Gets or sets whether to auto-select all components that this assembly simple hole feature affects in model.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelectComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean

instance.AutoSelectComponents = value

value = instance.AutoSelectComponents
```

### C#

```csharp
System.bool AutoSelectComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSelectComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to auto-select all affected components, false to not (use the selected components only or set [ISimpleHoleFeatureData2::AutoSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html) to true)

## VBA Syntax

See [SimpleHoleFeatureData2::AutoSelectComponents](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~AutoSelectComponents.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AssemblyFeatureScope.html)
[ISimpleHoleFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
