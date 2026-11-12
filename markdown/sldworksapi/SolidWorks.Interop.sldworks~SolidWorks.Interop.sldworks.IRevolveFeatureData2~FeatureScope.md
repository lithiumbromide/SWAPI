---
title: "FeatureScope Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~FeatureScope.html"
---

# FeatureScope Property (IRevolveFeatureData2)

Gets or sets whether to use scope for the revolve feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Boolean

instance.FeatureScope = value

value = instance.FeatureScope
```

### C#

```csharp
System.bool FeatureScope {get; set;}
```

### C++/CLI

```cpp
property System.bool FeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if only the specified bodies in the multibody part are affected by the feature, false if all of the bodies in the multibody part are affected by the revolve feature

## VBA Syntax

See [RevolveFeatureData2::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~FeatureScope.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelect.html)
[IRevolveFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetFeatureScopeBodiesCount.html)
[IRevolveFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetFeatureScopeBodies.html)
[IRevolveFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetFeatureScopeBodies.html)
[IRevolveFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
