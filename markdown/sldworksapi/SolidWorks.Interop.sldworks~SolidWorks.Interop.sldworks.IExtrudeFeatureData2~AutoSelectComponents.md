---
title: "AutoSelectComponents Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "AutoSelectComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelectComponents.html"
---

# AutoSelectComponents Property (IExtrudeFeatureData2)

Gets or sets whether to auto-select all components that this assembly extrude feature affects in model.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelectComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
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

True to auto-select all affected components, false to not (use the selected components only or set [IExtrudeFeatureData2::AutoSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.html) to true)

## VBA Syntax

See [ExtrudeFeatureData2::AutoSelectComponents](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~AutoSelectComponents.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AssemblyFeatureScope.html)
[IExtrudeFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
