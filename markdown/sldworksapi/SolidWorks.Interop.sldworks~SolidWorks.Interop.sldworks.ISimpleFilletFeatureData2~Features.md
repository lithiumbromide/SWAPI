---
title: "Features Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "Features"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Features.html"
---

# Features Property (ISimpleFilletFeatureData2)

Gets or sets the features for this simple fillet radius.

## Syntax

### Visual Basic (Declaration)

```vb
Property Features As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Object

instance.Features = value

value = instance.Features
```

### C#

```csharp
System.object Features {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Features {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [SimpleFilletFeatureData2::Features](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~Features.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFeatureCount.html)
[ISimpleFilletFeatureData2::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFeatures.html)
[ISimpleFilletFeatureData2::ISetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFeatures.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
