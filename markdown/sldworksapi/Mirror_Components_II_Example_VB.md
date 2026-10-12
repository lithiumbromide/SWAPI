---
title: "Mirror Components II Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Components_II_Example_VB.htm"
---

# Mirror Components II Example (VBA)

This example shows how to mirror components in an assembly.

```vb
  '---------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\advdrawings\98food processor.sldasm.
 ' 2. Ensure that c:\API\MirrorComps exists.
```

```vb
 ' Postconditions:
 ' 1. Creates Plane4 mirror plane.
 ' 2. Creates mirror copies of gear- caddy-1 and middle-gear-1, both aligned to component origins.
 ' 3. Creates mirror copies of shaft gear-1 and middle-gear plate-1, aligned to PLANE2 and PLANE3, respectively.
 ' 4. Creates opposite-hand versions of base plate-1 and shaft gear insert-1, called FileName1.sldprt and FileName2.sldprt, respectively, and stored in c:\API\MirrorComps.
 ' 5. Replaces FileName1.sldprt with check1.sldprt in c:\API\MirrorComps.
 ' 6. Creates MirrorComponent1 in the FeatureManager design tree.
 ' 7. Modifies MirrorComponent1 to change the mirror type, the align to origin component orientations, and the align to selection orientations.
 ' NOTE: Because the model is used elsewhere, do not save any changes to it.
  '---------------------------------------------------------------------------------------
```

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swAssem As SldWorks.AssemblyDoc

Dim swFeat As SldWorks.Feature

Dim mirrorPlane As SldWorks.Feature

Dim FeatMgr As SldWorks.FeatureManager

Dim swMirroCompFeatData As SldWorks.MirrorComponentFeatureData

Dim myRefPlane As SldWorks.RefPlane

Dim compsToInstance(0 To 3) As Object

Dim compsToSelectionPlane(0 To 1) As Object

Dim compToMirrorOppositeHand(0 To 1) As Object

Dim compsToMirrorOrientationonOrigin(0 To 1) As swMirrorComponentOrientation2_e

Dim compsToMirrorOrientationonPlane(0 To 1) As swMirrorComponentOrientation2_e

Dim mirrorPlane2 As SldWorks.Feature

Dim mirrorPlane3 As SldWorks.Feature

Dim alignmentref(0 To 1) As Object

Dim FlipDir(0 To 1) As Boolean

Dim flipDirVar As Variant

Dim orientationArray As Variant

Dim orientationSelPlanArray As Variant

Dim mirrorCompFileNames(0 To 1) As String

Dim mirrorCompFolder As String

Dim namesVar As Variant

Dim replaceLocations(0 To 1) As String

Dim replaceLocationsArray As Variant

Dim importOptions As Long

Dim modifyFeatdef As MirrorComponentFeatureData

Dim compsToMirrorOrientationonOrigin2(0 To 1) As swMirrorComponentOrientation2_e

Dim compsToMirrorOrientationonPlane2(0 To 1) As swMirrorComponentOrientation2_e

Dim orientationArray2 As Variant

Dim orientationArrayPlane2 As Variant

Dim boolstatus As Boolean

Dim retVal As Boolean

Option Explicit

Sub main()

```vb
        Set swApp = Application.SldWorks
```

```vb
        Set swModel = swApp.ActiveDoc
        Set FeatMgr = swModel.FeatureManager
```

```vb
        ' Create mirror component feature data object
        Set swMirroCompFeatData = FeatMgr.CreateDefinition(swFmMirrorComponent)
```

```vb
        ' Create mirror plane
        boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.104250921669188, -2.36987012272039E-04, -5.97199999999418E-02, True, 0, Nothing, 0)
        Set myRefPlane = swModel.FeatureManager.InsertRefPlane(8, 0.01, 0, 0, 0, 0)
```

```vb
        Set swAssem = swModel
```

```vb
        Set mirrorPlane = swAssem.FeatureByName("PLANE4")
```

```vb
        ' Specify components to instance align to component origins
        Set compsToInstance(0) = swAssem.GetComponentByName("gear- caddy-1")
        Set compsToInstance(1) = swAssem.GetComponentByName("middle-gear-1")
```

```vb
        ' Specify components to instance align to alignment references
        Set compsToSelectionPlane(0) = swAssem.GetComponentByName("shaft gear-1")
        Set compsToSelectionPlane(1) = swAssem.GetComponentByName("middle-gear plate-1")
```

```vb
        ' Specify components for which to create new opposite-hand versions
        Set compToMirrorOppositeHand(0) = swAssem.GetComponentByName("base plate-1")
        Set compToMirrorOppositeHand(1) = swAssem.GetComponentByName("shaft gear insert-1")
```

```vb
        ' Specify align to origins component orientations
         compsToMirrorOrientationonOrigin(0) = swOrientation_MirroredX_MirroredY
         compsToMirrorOrientationonOrigin(1) = swOrientation_MirroredAndFlippedX_MirroredY
        orientationArray = compsToMirrorOrientationonOrigin
```

```vb
        ' Specify align to selection component orientations
         compsToMirrorOrientationonPlane(0) = swOrientation_MirroredX_MirroredAndFlippedY
         compsToMirrorOrientationonPlane(1) = swOrientation_MirroredAndFlippedX_MirroredAndFlippedY
        orientationSelPlanArray = compsToMirrorOrientationonPlane
```

```vb
        ' Specify the alignment references for the align to selection components
        Set mirrorPlane2 = swAssem.FeatureByName("PLANE2")
        Set mirrorPlane3 = swAssem.FeatureByName("PLANE3")
        Set alignmentref(0) = mirrorPlane2
        Set alignmentref(1) = mirrorPlane3
```

```vb
        ' Specify whether to reverse the direction of alignment
        FlipDir(0) = False
        FlipDir(1) = False
        flipDirVar = FlipDir
```

```vb
        ' Specify the opposite-hand version folder
        mirrorCompFolder = "C:\API\MirrorComps"
```

```vb
        ' Specify opposite-hand version file names
        mirrorCompFileNames(0) = ("FileName1")
        mirrorCompFileNames(1) = ("FileName2")
        namesVar = mirrorCompFileNames
```

```vb
        ' Specify replacement locations for the opposite-hand versions
        replaceLocations(0) = ("C:\API\check1.SLDPRT")
        replaceLocations(1) = ("")
        replaceLocationsArray = replaceLocations
```

```vb
        ' Specify transfer options for the opposite-hand versions
        importOptions = swMirrorPartOptions_ImportSolids
```

```vb
         swMirroCompFeatData.mirrorPlane = mirrorPlane
         swMirroCompFeatData.MirrorType = swMirrorType_ComponentOrigin
         swMirroCompFeatData.ComponentsToInstanceAlignToComponentOrigin = compsToInstance
         swMirroCompFeatData.ComponentOrientationsAlignToComponentOrigin = orientationArray
         swMirroCompFeatData.ComponentsToInstanceAlignToSelection = compsToSelectionPlane
         swMirroCompFeatData.ComponentOrientationsAlignToSelection = orientationSelPlanArray
         swMirroCompFeatData.AlignmentReferences = alignmentref
         swMirroCompFeatData.FlipDirections = flipDirVar
         swMirroCompFeatData.SyncFlexibleSubAssemblies = True
         swMirroCompFeatData.OppositeHandComponents = compToMirrorOppositeHand
         swMirroCompFeatData.CreateDerivedConfigurations = False
         swMirroCompFeatData.PlaceFilesInOneFolder = True
         swMirroCompFeatData.MirrorComponentsFolderLocation = mirrorCompFolder
         swMirroCompFeatData.MirroredComponentFilenames = namesVar
         swMirroCompFeatData.nameModifierType = swMirrorComponentName_Custom
         swMirroCompFeatData.ReplaceFileLocations = replaceLocationsArray
         swMirroCompFeatData.MirrorTransferOptions = importOptions
         swMirroCompFeatData.DimXpertScheme = True
         swMirroCompFeatData.BreakLinksToOriginalPart = False
         swMirroCompFeatData.preserveZAxis = True
         swMirroCompFeatData.PropagateFromOriginalPart = False
```

```vb
        ' Create MirrorComponent1
        Set swFeat = FeatMgr.CreateFeature(swMirroCompFeatData)
```

```vb
        ' Modify MirrorComponent1
        Set modifyFeatdef = swFeat.GetDefinition
```

```vb
        ' Change mirror type to center of mass
         modifyFeatdef.MirrorType = swMirrorType_CenterOfMass
```

```vb
        ' Modify align to origin component orientations
         compsToMirrorOrientationonOrigin2(0) = swOrientation_MirroredAndFlippedX_MirroredAndFlippedY
         compsToMirrorOrientationonOrigin2(1) = swOrientation_MirroredX_MirroredAndFlippedY
        orientationArray2 = compsToMirrorOrientationonOrigin2
         modifyFeatdef.ComponentOrientationsAlignToComponentOrigin = orientationArray2
```

```vb
        ' Modify align to selection component orientations
         compsToMirrorOrientationonPlane2(0) = swOrientation_MirroredAndFlippedX_MirroredY
         compsToMirrorOrientationonPlane2(1) = swOrientation_MirroredX_MirroredY
        orientationArrayPlane2 = compsToMirrorOrientationonPlane2
         modifyFeatdef.ComponentOrientationsAlignToSelection = orientationArrayPlane2
```

```vb
        retVal = swFeat.ModifyDefinition(modifyFeatdef, swModel, Nothing)
```

```vb
 End Sub
```
