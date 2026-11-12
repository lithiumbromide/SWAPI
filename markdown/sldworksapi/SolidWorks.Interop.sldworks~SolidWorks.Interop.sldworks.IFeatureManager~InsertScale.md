---
title: "InsertScale Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertScale.html"
---

# InsertScale Method (IFeatureManager)

Applies the specified scaling to either the current model or a selected graphic body.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertScale( _
   ByVal Type As System.Short, _
   ByVal Uniform As System.Boolean, _
   ByVal Xscale As System.Double, _
   ByVal YScale As System.Double, _
   ByVal ZScale As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Short
Dim Uniform As System.Boolean
Dim Xscale As System.Double
Dim YScale As System.Double
Dim ZScale As System.Double
Dim value As Feature

value = instance.InsertScale(Type, Uniform, Xscale, YScale, ZScale)
```

### C#

```csharp
Feature InsertScale(
   System.short Type,
   System.bool Uniform,
   System.double Xscale,
   System.double YScale,
   System.double ZScale
)
```

### C++/CLI

```cpp
Feature^ InsertScale(
   System.short Type,
   System.bool Uniform,
   System.double Xscale,
   System.double YScale,
   System.double ZScale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Value as defined in [swScaleType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swScaleType_e.html)
- `Uniform`: True if scaling should be uniform, false if not
- `Xscale`: X direction scale factor
- `YScale`: Y direction scale factor; valid only if Uniform is false
- `ZScale`: Z direction scale factor; valid only if Uniform is false

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) if scaling the current model; Null or Nothing if scaling a selected graphic body

## VBA Syntax

See [FeatureManager::InsertScale](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertScale.html).

## Examples

[Insert Scale Feature (VBA)](Insert_Scale_Feature_Example_VB.htm)

## Remarks

To scale a graphic body:

1. Select the graphic body in the Graphic Bodies folder of the FeatureManager design tree.
2. Call this method.

This method scales the selected graphic body up in the graphics view, but no scale feature is created.

| If Uniform is... | Then the scaling factor is... |
| --- | --- |
| True | Xscale, applied in three directions. |
| False | All three scaling factors (Xscale, YScale, and ZScale). |

Use [IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html) and [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) and [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) to gain access to the [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) object.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
