---
title: "FeatureScope Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~FeatureScope.html"
---

# FeatureScope Property (ILinearPatternFeatureData)

Gets which bodies in this multibody part are affected by this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

See [LinearPatternFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~FeatureScope.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GeometryPattern.html) is true.

Call [ILinearPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
