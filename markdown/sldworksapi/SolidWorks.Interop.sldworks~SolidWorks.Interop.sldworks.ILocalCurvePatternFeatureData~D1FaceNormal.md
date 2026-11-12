---
title: "D1FaceNormal Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D1FaceNormal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1FaceNormal.html"
---

# D1FaceNormal Property (ILocalCurvePatternFeatureData)

Gets or sets the face on which the 3D curve lies for this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1FaceNormal As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object

instance.D1FaceNormal = value

value = instance.D1FaceNormal
```

### C#

```csharp
System.object D1FaceNormal {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1FaceNormal {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [LocalCurvePatternFeatureData::D1FaceNormal](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D1FaceNormal.html).

## Remarks

If you pre-select a 3D curve for Direction 1, then before creating the feature definition, you must also pre-select the face normal entity using selection Mark = 64.

Use this property only when editing the pattern feature.

This property is valid only when specifying [ILocalCurvePatternFeatureData::D1Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html) using a 3D curve.

If you try to change this property to null or Nothing, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html) returns true but the property does not change.

For more information, see the **Curve Driven Component Pattern** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
