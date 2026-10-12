---
title: "Create Hole Wizard Feature Data Object and Hole Wizard Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Hole_Wizard_Feature_Data_Object_and_Hole_Wizard_Feature_Example_VB.htm"
---

# Create Hole Wizard Feature Data Object and Hole Wizard Feature Example (VBA)

This example shows how to create a hole wizard feature data object and a hole wizard feature.

```
'-------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\block20.sldprt.
'
' Postconditions:
' 1. Creates a hole wizard feature on the selected face of the part.
' 2. Examine the FeatureManager design tree and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim swFeat As SldWorks.Feature
Dim swWzdHole As WizardHoleFeatureData2
Dim swFeatDataObj As Object
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swFeatMgr = swModel.FeatureManager
```

```
    ' Create the hole wizard feature data object
    Set swFeatDataObj = swFeatMgr.CreateDefinition(swFmHoleWzd)
    Set swWzdHole = swFeatDataObj
```

```
    ' Initialize the hole wizard feature
    swWzdHole.InitializeHole swWzdCounterBore, swStandardISO, swStandardISOHexBolt, "M48", swEndCondBlind
```

```
    'Change the hole wizard feature's depth
    swWzdHole.HoleDepth = 0.15
```

```
    'Change the hole wizard feature's diameter
    swWzdHole.HoleDiameter = 0.0555

    ' Select the face on which to create the hole
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 9.30621655732011E-03, 3.96239999998897E-02, -3.32715966641217E-03, False, 0, Nothing, 0)
```

```
    ' Create the hole wizard feature
    Set swFeat = swFeatMgr.CreateFeature(swWzdHole)
```

```
End Sub
```
