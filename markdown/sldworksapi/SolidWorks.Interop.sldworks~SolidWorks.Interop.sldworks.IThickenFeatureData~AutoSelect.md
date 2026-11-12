---
title: "AutoSelect Property (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "AutoSelect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~AutoSelect.html"
---

# AutoSelect Property (IThickenFeatureData)

Gets or sets whether to automatically select all or only specific bodies for the thicken feature to affect in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThickenFeatureData
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

True to automatically select all bodies, false to select specific bodies using [IThickenFeatureData::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IThickenFeatureData~ISetFeatureScopeBodies.html) or [IThickenFeatureData::ISetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IThickenFeatureData~ISetFeatureScopeBodies.html).

## VBA Syntax

See [ThickenFeatureData::AutoSelect](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~AutoSelect.html).

## Examples

[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)

## Remarks

This property is only available when the [IThickenFeatureData::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IThickenFeatureData~FeatureScope.html) property is true. The thicken feature is expanded along the plane on which the feature is created and selects all or only the specified bodies it intersects.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)
[IThickenFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~IGetFeatureScopeBodies.html)
[IThickenFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScope.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
