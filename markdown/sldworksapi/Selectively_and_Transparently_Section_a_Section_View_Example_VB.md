---
title: "Selectively and Transparently Section a Section View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm"
---

# Selectively and Transparently Section a Section View Example (VBA)

This example shows how to selectively and transparently section a section view.

```
'-------------------------------------------------------------------------
' Preconditions: Verify that the assembly to open exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects the component for selective sectioning.
' 3. Selects the components for transparent sectioning.
' 4. Selects the planes for sectioning.
' 5. Creates the SectionViewData object.
'    a. Sets the section method to zonal.
'    b. Sets to cap the sections.
'    c. Sets to generate a graphics-only section view.
'    d. Enables selective sectioning.
'       1. Sets the component selected in step 2 for selective
'          sectioning.
'       2. Sets the intersection zone.
'       3. Sets to exclude the component set in step 5.d.1 from
'          selective sectioning.
'    e. Enables transparent sectioning.
'       1. Sets the components selected in step 3
'          for transparent sectioning.
'       2. Sets to include the sectioned components set in step 5.e.1
'          in transparent sectioning.
'       3. Sets the level of transparency.
' 6. Creates the section view.
' 7. Examine the graphics area.
' 8. Click Section View twice in the Heads-Up View toolbar and
'    examine the Section View PropertyManager page.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim selectiveArray(0) As SldWorks.Component2
Dim selComponent As SldWorks.Component2
Dim swSelMgr As SldWorks.SelectionMgr
Dim transparentArray(1) As SldWorks.Component2
Dim transComponent As SldWorks.Component2
Dim transComponent2 As SldWorks.Component2
Dim swSectionViewData As SldWorks.SectionViewData
Dim swModelViewManager as SldWorks.ModelViewManager
Dim transArray As Variant
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim selArray As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\floxpress\ball valve\ball_valve.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    status = swModelDocExt.SelectByID2("Ball-1@ball_valve", "COMPONENT", 0, 0, 0, True, 8, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set selComponent = swSelMgr.GetSelectedObject6(1, -1)
    Set selectiveArray(0) = selComponent
    selArray = selectiveArray
```

```
    status = swModelDocExt.SelectByID2("Side-1@ball_valve", "COMPONENT", 0, 0, 0, True, 32, Nothing, 0)
    status = swModelDocExt.SelectByID2("Side-2@ball_valve", "COMPONENT", 0, 0, 0, True, 32, Nothing, 0)
    Set transComponent = swSelMgr.GetSelectedObject6(1, -1)
    Set transComponent2 = swSelMgr.GetSelectedObject6(2, -1)
    Set transparentArray(0) = transComponent
    Set transparentArray(1) = transComponent2
    transArray = transparentArray
```

```
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Plane2", "PLANE", 0, 0, 0, True, 2, Nothing, 0)
    status = swModelDocExt.SelectByID2("Plane3", "PLANE", 0, 0, 0, True, 4, Nothing, 0)

    Set swModelViewManager = swModel.ModelViewManager
    Set swSectionViewData = swModelViewManager.CreateSectionViewData()
```

```
    swSectionViewData.FirstColor = 16711680
    swSectionViewData.SecondColor = 65280
    swSectionViewData.ThirdColor = 255
    swSectionViewData.ShowSectionCap = True
    swSectionViewData.KeepCapColor = True
    swSectionViewData.GraphicsOnlySection = True
```

```
    swSectionViewData.ZonalSection = True
```

```
    swSectionViewData.SelectiveSection = True
    swSectionViewData.SelectiveSectioningList = selArray
    swSectionViewData.SectionedZones = 16 'swZonalSectionViewZones_e.swZonalSectionViewZones_swZonalSectionViewZone_5
    swSectionViewData.ExcludeSelectedItems = True
```

```
    swSectionViewData.TransparentSection = True
    swSectionViewData.TransparencyList = transArray
    swSectionViewData.SectionTransparentItemsTransparent = True
    swSectionViewData.TransparencyValue = 0.9
```

```
    status = swModelViewManager.CreateSectionView(swSectionViewData)
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
