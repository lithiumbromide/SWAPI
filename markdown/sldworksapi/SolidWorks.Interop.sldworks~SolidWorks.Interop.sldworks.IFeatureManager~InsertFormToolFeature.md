---
title: "InsertFormToolFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFormToolFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFormToolFeature.html"
---

# InsertFormToolFeature Method (IFeatureManager)

Obsolete. Superseded by

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

and

[IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFormToolFeature( _
   ByVal Path As System.String, _
   ByVal Flip As System.Boolean, _
   ByVal RotAngle As System.Double, _
   ByVal Config As System.String, _
   ByVal OverrideDoc As System.Boolean, _
   ByVal ShowPunch As System.Boolean, _
   ByVal ShowProfile As System.Boolean, _
   ByVal ShowCenter As System.Boolean, _
   ByVal LinkToPart As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Path As System.String
Dim Flip As System.Boolean
Dim RotAngle As System.Double
Dim Config As System.String
Dim OverrideDoc As System.Boolean
Dim ShowPunch As System.Boolean
Dim ShowProfile As System.Boolean
Dim ShowCenter As System.Boolean
Dim LinkToPart As System.Boolean
Dim value As Feature

value = instance.InsertFormToolFeature(Path, Flip, RotAngle, Config, OverrideDoc, ShowPunch, ShowProfile, ShowCenter, LinkToPart)
```

### C#

```csharp
Feature InsertFormToolFeature(
   System.string Path,
   System.bool Flip,
   System.double RotAngle,
   System.string Config,
   System.bool OverrideDoc,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter,
   System.bool LinkToPart
)
```

### C++/CLI

```cpp
Feature^ InsertFormToolFeature(
   System.String^ Path,
   System.bool Flip,
   System.double RotAngle,
   System.String^ Config,
   System.bool OverrideDoc,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter,
   System.bool LinkToPart
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Path`: Pathname of the forming tool part file in the Design Library
- `Flip`: Whether to reverse the direction of the cut of the forming tool when inserted
- `RotAngle`: Angle of the forming tool
- `Config`: Name of the configuration of the forming tool to insert
- `OverrideDoc`: True to override the document settings in

Tools > Options > Document Properties > Sheet Metal,

false to not
- `ShowPunch`: True to display the cut of the forming tool when the part is flattened, false to not; valid only if OverrideDoc = true
- `ShowProfile`: True to display the placement sketch of the forming tool when the part is flattened, false to not; valid only if OverrideDoc = true
- `ShowCenter`: True to display the center mark where the forming tool is located in the flat pattern, false to not; valid only if OverrideDoc = true
- `LinkToPart`: True to link the forming tool feature to its part in the Design Library, false to not

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See

[FeatureManager::InsertFormToolFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFormToolFeature.html)

.

## Remarks

Before calling this method, select either a face or a 2D sketch containing points. If you select:

- face, a single instance of the Design Library forming tool is placed on it.
- sketch containing points, an instance of the Design Library forming tool is placed at each point in the sketch.

To create your own forming tool, call[IFeatureManager::CreateFormTool](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateFormTool.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

[IView::InsertPunchTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
