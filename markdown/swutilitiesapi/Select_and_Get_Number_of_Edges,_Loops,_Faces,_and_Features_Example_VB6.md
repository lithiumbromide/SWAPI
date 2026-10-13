---
title: "Select and Get Number of Edges, Loops, Faces, and Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm"
---

# Select and Get Number of Edges, Loops, Faces, and Features Example (VBA)

This examples shows how to select the edges, loops, faces, and features of all red faces using the SOLIDWORKS Utilities API.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Open a part that has one or more  faces colored red
'    (RGB(255, 0, 0) in the Appearances PropertyManager page;
'    to verify the color of the faces, click DisplayManager >
'    Edit Appearance > color to open this PropertyManager page).
'
' Postconditions:
' 1. Selects the edges, loops, faces, and features
'    of all red faces.
' 2. Examine the graphics area.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim longstatus As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    swApp.ActiveDoc.ActiveView.FrameState = 1

    '--------------------Block Recording--------------------
    #If 0 Then
    #End If
    '--------------------UnBlock Recording------------------
    '--------------------Power Select-----------------------

    Dim swUtil As gtcocswUtilities
    Dim swUtilPsl As gtcocswPowerSelect

    Set swUtil = swApp.GetAddInObject("Utilities.UtilitiesApp")
    'Get the powerSelect object
    'You can also use gtcocswUtilities::GetToolInterface)
    Set swUtilPsl = swUtil.PowerSelect
    longstatus = swUtilPsl.Init()
```

```
    'Select only faces
    longstatus = swUtilPsl.SetSelectEntitiesTypes(gtPslSelectionType_Face)
```

```
    'Select all red faces
    longstatus = swUtilPsl.SetFaceColorFilter(1#, 0#, 0#)

    'Run the selection and get the number of
    'edges, loops, faces, and features selected
    Dim varEntCount As Variant
    varEntCount = swUtilPsl.RunPowerSelect(gtResultNoUI, longstatus)

    'Select the results
    longstatus = swUtilPsl.SelectResults()
```

```
    longstatus = swUtilPsl.Close()

    '--------------------Power Select-----------------------
```

```
End Sub
```
