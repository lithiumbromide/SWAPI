---
title: "AutoSelectComponents Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "AutoSelectComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelectComponents.html"
---

# AutoSelectComponents Property (IRevolveFeatureData2)

Gets or sets whether to auto-select all components that this assembly revolve feature affects in model.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelectComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
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

True to auto-select all affected components, false to not (use the selected components only or set [IRevolveFeatureData2::AutoSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~AutoSelect.html) to true)

## VBA Syntax

See [RevolveFeatureData2::AutoSelectComponents](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~AutoSelectComponents.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AssemblyFeatureScope.html)
[IRevolveFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
