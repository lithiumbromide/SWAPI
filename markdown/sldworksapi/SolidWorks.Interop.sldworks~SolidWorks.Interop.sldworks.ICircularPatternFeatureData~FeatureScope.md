---
title: "FeatureScope Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScope.html"
---

# FeatureScope Property (ICircularPatternFeatureData)

Gets which bodies in this multibody part are affected by this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

value = instance.FeatureScope
```

### C#

```csharp
System.bool FeatureScope {get;}
```

### C++/CLI

```cpp
property System.bool FeatureScope {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to specify affected bodies, false to apply the pattern to all bodies every time the feature regenerates

## VBA Syntax

See [CircularPatternFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~FeatureScope.html).

## Remarks

This property is valid only if [ICircularPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GeometryPattern.html) is true.

Call [ICircularPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Circular Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
