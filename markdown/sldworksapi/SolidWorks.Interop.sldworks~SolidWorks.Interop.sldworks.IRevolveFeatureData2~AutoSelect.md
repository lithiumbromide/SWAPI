---
title: "AutoSelect Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "AutoSelect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelect.html"
---

# AutoSelect Property (IRevolveFeatureData2)

Gets or sets whether to automatically select all or only specific bodies for the revolve feature to affect in a multibody body.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Boolean

instance.AutoSelect = value

value = instance.AutoSelect
```

### C#

```csharp
System.bool AutoSelect {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSelect {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically select all bodies, false to select specific bodies for [IRevolveFeatureData2::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~FeatureScopeBodies.html) or [IRevolveFeatureData2::ISetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~ISetFeatureScopeBodies.html)

## VBA Syntax

See [RevolveFeatureData2::AutoSelect](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~AutoSelect.html).

## Remarks

This property is only available when the [IRevolveFeatureData2::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~FeatureScope.html) property is true. The revolve feature is expanded along the plane on which the feature is created and selects all or only the specified bodies it intersects.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetFeatureScopeBodiesCount.html)
[IRevolveFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetFeatureScopeBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
