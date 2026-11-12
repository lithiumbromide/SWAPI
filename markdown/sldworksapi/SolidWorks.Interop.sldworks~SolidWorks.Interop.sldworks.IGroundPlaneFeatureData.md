---
title: "IGroundPlaneFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IGroundPlaneFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html"
---

# IGroundPlaneFeatureData Interface

Allows access to a ground plane feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IGroundPlaneFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IGroundPlaneFeatureData
```

### C#

```csharp
public interface IGroundPlaneFeatureData
```

### C++/CLI

```cpp
public interface class IGroundPlaneFeatureData
```

## VBA Syntax

See [GroundPlaneFeatureData](ms-its:sldworksapivb6.chm::/sldworks~GroundPlaneFeatureData.html).

## Examples

'VBA

'==========================================================================

'1. Ensure that the specified model exists.
'2. Run the macro.
'3. Creates **Ground Plane1** in the Ground Planes folder of
' the FeatureManager design tree and modifies it.
'===========================================================================

Dim swApp As SldWorks.SldWorks
Dim featmgr As SldWorks.FeatureManager
Dim swGPData As SldWorks.GroundPlaneFeatureData
Dim featdata As SldWorks.GroundPlaneFeatureData
Dim ent As SldWorks.Face2
Dim feat As SldWorks.Feature
Dim Part As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem2.sldasm", 2, 0, "", longstatus, longwarnings)

Set swAssembly = Part
swApp.ActivateDoc2 "assem2.sldasm", False, longstatus
Set Part = swApp.ActiveDoc
Set featmgr = Part.FeatureManager

boolstatus = Part.Extension.SelectByRay(-0.124913770805165, 0.118854842937424, 7.02747343940473E-02, -0.620586476260429, -0.617739368127351, -0.482980846978724, 3.09726603088958E-03, 2, True, 0, 0)

Set ent = Part.SelectionManager.GetSelectedObject6(1, -1)
Set swGPData = featmgr.**CreateDefinition**(swFmGroundPlane)
swGPData.**PlanarEntity** = ent

Set feat = featmgr.**CreateFeature**(swGPData)
Part.ClearSelection2 True
Set featdata = feat.**GetDefinition**()
boolstatus = Part.Extension.SelectByRay(0.119119826446138, 5.16103810082313E-03, 0.183494239718641, -0.620586476260429, -0.617739368127351, -0.482980846978724, 3.09726603088958E-03, 2, False, 0, 0)
Set ent = Part.SelectionManager.GetSelectedObject6(1, -1)
featdata.**AccessSelections** Part, Nothing

featdata.**PlanarEntity** = ent
feat.**ModifyDefinition** featdata, Part, Nothing

End Sub

## Examples

[Create Ground Plane (C#)](Create_Ground_Plane_Example_CSharp.htm)

## Remarks

Use this interface to insert a ground plane at each level of a plant assembly. Ground planes are used as reference geometry when inserting published assets at each level.

Call [IAssemblyDoc::ActivateGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.html) to activate the ground plane on the level where you want to insert a published asset; the asset's ground face snaps to the assembly's activated ground plane. Components with magnetic mates snap only to components that are also on the active ground plane.

Only one ground plane can be active at a given time in each assembly configuration.

See **Large Assemblies > Facility Layout** in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[GroundPlaneFeatureData](SWObjectModel.pdf#GroundPlaneFeatureData)

## See Also

[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
