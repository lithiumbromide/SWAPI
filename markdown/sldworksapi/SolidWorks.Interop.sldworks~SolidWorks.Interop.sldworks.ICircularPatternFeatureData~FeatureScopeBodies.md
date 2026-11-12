---
title: "FeatureScopeBodies Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (ICircularPatternFeatureData)

Gets the bodies in this multibody part that are affected by this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Object

value = instance.FeatureScopeBodies
```

### C#

```csharp
System.object FeatureScopeBodies {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureScopeBodies {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to be affected

## VBA Syntax

See [CircularPatternFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~FeatureScopeBodies.html).

## Remarks

This property is valid only if [ICircularPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GeometryPattern.html) is true.

Call [ICircularPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Circular Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
