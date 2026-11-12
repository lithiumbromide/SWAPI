---
title: "SetFeatureScope Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "SetFeatureScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope.html"
---

# SetFeatureScope Method (ICircularPatternFeatureData)

Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFeatureScope( _
   ByVal FeatureScopeOption As System.Boolean, _
   ByVal AutoSelectBodies As System.Boolean, _
   ByVal Bodies As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim FeatureScopeOption As System.Boolean
Dim AutoSelectBodies As System.Boolean
Dim Bodies As System.Object
Dim value As System.Boolean

value = instance.SetFeatureScope(FeatureScopeOption, AutoSelectBodies, Bodies)
```

### C#

```csharp
System.bool SetFeatureScope(
   System.bool FeatureScopeOption,
   System.bool AutoSelectBodies,
   System.object Bodies
)
```

### C++/CLI

```cpp
System.bool SetFeatureScope(
   System.bool FeatureScopeOption,
   System.bool AutoSelectBodies,
   System.Object^ Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureScopeOption`: True (default) to specify affected bodies, false to apply the pattern to all bodies every time the feature regenerates (see **Remarks**)
- `AutoSelectBodies`: True (default) to automatically select all bodies intersected by this pattern feature, false to specify affected bodies (see **Remarks**)
- `Bodies`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to be affected; valid only if FeatureScopeOption is true and AutoSelectBodies is false

### Return Value

True if feature scope set successfully, false if not (see **Remarks**)

## VBA Syntax

See [CircularPatternFeatureData::SetFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~SetFeatureScope.html).

## Remarks

If this method returns false, then default values for FeatureScopeOption and AutoSelectBodies are set. A subsequent call to [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) creates the feature with a FeatureScopeOption of true and an AutoSelectBodies of true.

After calling IFeature::ModifyDefinition, call [IFeature::GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.html) to determine what's wrong and then take necessary remedial action.

For more information, see the **Circular Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AutoSelect.html)
[ICircularPatternFeatureData::FeatureScope Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScope.html)
[ICircularPatternFeatureData::FeatureScopeBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
