---
title: "InstancesToVary Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "InstancesToVary"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.html"
---

# InstancesToVary Property (ICircularPatternFeatureData)

Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InstancesToVary As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

instance.InstancesToVary = value

value = instance.InstancesToVary
```

### C#

```csharp
System.bool InstancesToVary {get; set;}
```

### C++/CLI

```cpp
property System.bool InstancesToVary {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to vary the spacing of pattern instances, false to not

## VBA Syntax

See [CircularPatternFeatureData::InstancesToVary](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~InstancesToVary.html).

## Remarks

This property is valid only when editing the circular pattern feature. You cannot set this property during creation of the feature.

To vary instances in a circular pattern feature:

1. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html).
2. Call [ICircularPatternFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AccessSelections.html).
3. Set this property to true.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).
5. Call ICircularPatternFeatureData::AccessSelections.
6. Call [ICircularPatternFeatureData::GetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetInstanceToVaryOptions.html).
7. Modify [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) properties.
8. Call [ICircularPatternFeatureData::SetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetInstanceToVaryOptions.html).
9. Call IFeature::ModifyDefinition.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
