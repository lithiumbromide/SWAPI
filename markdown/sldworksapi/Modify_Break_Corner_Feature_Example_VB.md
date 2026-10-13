---
title: "Modify Break Corner Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Break_Corner_Feature_Example_VB.htm"
---

# Modify Break Corner Feature Example (VBA)

This example shows how to create and modify a break corner feature in a sheet metal part.

```
'---------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified document.
' 2. Selects a face on Edge-Flange1.
' 3. Creates a break corner feature.
' 4. Unsuppresses the flat pattern feature.
' 5. Accesses the break corner feature and
'    and modifies it.
' 6. Suppresses the flat pattern feature.
' 7. Examine the graphics area and the Immediate window.
'
' NOTE: Because the part document is used elsewhere,
' do not save any changes.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swBreakCornerFeatureData As SldWorks.BreakCornerFeatureData
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\sm1-remove-edges.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", -0.111589911985732, 9.79999999999563E-02, 8.41212722518208E-02, True, 0, Nothing, 0)
    swModel.InsertSheetMetalBreakCorner swBreakCornerTypes_e.swBreakCornerTypeChamfer, 0.005
```

```
    'Select and unsuppress the flat pattern feature
    status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditUnsuppress2
    swModel.ClearSelection2 True
```

```
    'Select the break corner feature
    'and change some of its properties
    status = swModelDocExt.SelectByID2("Break-Corner1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, 0)
    Set swBreakCornerFeatureData = swFeature.GetDefinition
    status = swBreakCornerFeatureData.AccessSelections(swModel, Nothing)
         Debug.Print "AccessSelections:", status
         Debug.Print ""
         Debug.Print "  -------------Original--------------"
         Debug.Print "    CenteredOnBendLines:", swBreakCornerFeatureData.CenteredOnBendLines
         Debug.Print "    InternalCornersOnly:", swBreakCornerFeatureData.InternalCornersOnly
         swBreakCornerFeatureData.InternalCornersOnly = True
         swBreakCornerFeatureData.CenteredOnBendLines = True
         Debug.Print ""
         Debug.Print "  -------------Modified--------------"
         Debug.Print "    CenteredOnBendLines:", swBreakCornerFeatureData.CenteredOnBendLines
         Debug.Print "    InternalCornersOnly:", swBreakCornerFeatureData.InternalCornersOnly
         status = swFeature.ModifyDefinition(swBreakCornerFeatureData, swModel, Nothing)
         Debug.Print ""
         Debug.Print "ModifyDefinition:", status
         swModel.ClearSelection2 True
```

```
         'Select and suppress the flat pattern feature
        status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSuppress2
        swModel.ClearSelection2 True
```

```
End Sub
```
