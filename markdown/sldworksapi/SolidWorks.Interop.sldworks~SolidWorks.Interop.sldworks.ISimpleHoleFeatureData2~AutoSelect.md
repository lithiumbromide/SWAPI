---
title: "AutoSelect Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "AutoSelect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html"
---

# AutoSelect Property (ISimpleHoleFeatureData2)

Gets or sets whether to automatically select all or only specific bodies for the simple hole feature to affect in a multibody body.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
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

True to automatically select all bodies, false to select specific bodies for [ISimpleHoleFeatureData2::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScopeBodies.html) or [ISimpleHoleFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.html)

## VBA Syntax

See [SimpleHoleFeatureData2::AutoSelect](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~AutoSelect.html).

## Remarks

Th property is only available when [ISimpleHoleFeatureData2::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScope.html) is true.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetFeatureScopeBodiesCount.html)
[ISimpleHoleFeatureData2::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
