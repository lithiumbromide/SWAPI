---
title: "AssemblyFeatureScope Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "AssemblyFeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AssemblyFeatureScope.html"
---

# AssemblyFeatureScope Property (IRevolveFeatureData2)

Gets or sets whether to use scope for this assembly revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyFeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
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

See [RevolveFeatureData2::AssemblyFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~AssemblyFeatureScope.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelect.html)
[IRevolveFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelectComponents.html)
[IRevolveFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
