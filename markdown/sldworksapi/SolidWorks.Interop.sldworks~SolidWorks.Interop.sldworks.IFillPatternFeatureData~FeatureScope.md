---
title: "FeatureScope Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScope.html"
---

# FeatureScope Property (IFillPatternFeatureData)

Gets or sets whether to use scope for this fill pattern feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
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

True if only specified bodies in a multibody part are affected by the fill pattern feature; false if all the bodies are affected

## VBA Syntax

See [FillPatternFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~FeatureScope.html).

## Remarks

This property is valid only if [IFillPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.html) is true.

If this property is true, you can use [IFillPatternFeatureData::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~AutoSelect.html) and [IFillPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScopeBodies.html) to specify affected bodies.

For more information, see the **Fill** **Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~AutoSelect.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
