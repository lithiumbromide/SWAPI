---
title: "InstancesToVary Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "InstancesToVary"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.html"
---

# InstancesToVary Property (ILinearPatternFeatureData)

Gets or sets whether to vary the spacing of pattern instances in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InstancesToVary As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

See [LinearPatternFeatureData::InstancesToVary](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~InstancesToVary.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## Remarks

This property is valid only when editing the linear pattern feature. You cannot set this property during creation of the feature.

To vary instances in a linear pattern feature:

1. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html).
2. Call [ILinearPatternFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~AccessSelections.html).
3. Set this property to true.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).
5. Call ILinearPatternFeatureData::AccessSelections.
6. Call [ILinearPatternFeatureData::GetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetInstanceToVaryOptions.html).
7. Modify [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) properties.
8. Call [ILinearPatternFeatureData::SetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetInstanceToVaryOptions.html).
9. Call IFeature::ModifyDefinition.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
