---
title: "AssemblyFeatureScope Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "AssemblyFeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AssemblyFeatureScope.html"
---

# AssemblyFeatureScope Property (IExtrudeFeatureData2)

Gets or sets whether to use scope for this assembly extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyFeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
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

See [ExtrudeFeatureData2::AssemblyFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~AssemblyFeatureScope.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelectComponents.html)
[IExtrudeFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.html)
[IExtrudeFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
