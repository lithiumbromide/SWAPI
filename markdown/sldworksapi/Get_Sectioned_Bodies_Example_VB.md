---
title: "Get Sectioned Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sectioned_Bodies_Example_VB.htm"
---

# Get Sectioned Bodies Example (VBA)

This example shows how to get sectioned bodies and create a new part using the sectioned bodies.

```
'-------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Verify that the specified part document template exists.
' 3. Open the Immediate window.
' 4. Step through the macro by pressing F8.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Creates a section view.
' 3. Selects a component in the section view.
' 4. Creates a new part.
' 5. Creates a feature using the body in the component
'    in the section view selected in step 3.
' 6. Examine the FeatureManager design tree, graphics
'    area, and Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not
' save changes.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swModelViewMgr As SldWorks.ModelViewManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swComp As SldWorks.Component2
Dim swModelView As SldWorks.ModelView
Dim swSectionViewData As SldWorks.SectionViewData
Dim vBodyArr As Variant
Dim vBody As Variant
Dim swBody As SldWorks.Body2
Dim swNewPart As SldWorks.PartDoc
Dim swFeat As SldWorks.Feature
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly,create section view, and select
    'a component in the section view
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\landing_gear.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
    Set swModelViewMgr = swModel.ModelViewManager
    Set swSectionViewData = swModelViewMgr.CreateSectionViewData()
    swSectionViewData.FirstPlane = Nothing
    swSectionViewData.FirstReverseDirection = False
    swSectionViewData.FirstOffset = 0
    swSectionViewData.FirstRotationX = 0
    swSectionViewData.FirstRotationY = 0
    swSectionViewData.FirstColor = 16711680
    swSectionViewData.ShowSectionCap = True
    swSectionViewData.KeepCapColor = False
    swSectionViewData.GraphicsOnlySection = False
    status = swModelViewMgr.CreateSectionView(swSectionViewData)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("oleostrut-1@landing_gear", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
```

```
    Set swModelView = swModel.ActiveView
    status = swModelView.GetDisplayState(swViewDisplayType_e.swIsViewSectioned)
    If status Then
         'Create new part using selected component
         Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2014\templates\part.prtdot", swDwgPaperAsize, 0, 0)
         Set swNewPart = swModel
         vBodyArr = swComp.GetSectionedBodies(swModelView)
         For Each vBody In vBodyArr
             Set swBody = vBody
             Set swFeat = swNewPart.CreateFeatureFromBody3(swBody, False, swCreateFeatureBodyCheck)
         Next vBody
    Else
        Debug.Print "Model view does not contain a section view."
    End If
```

```
End Sub
```
