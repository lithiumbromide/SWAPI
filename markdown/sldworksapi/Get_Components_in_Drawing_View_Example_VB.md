---
title: "Get Components in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_in_Drawing_View_Example_VB.htm"
---

# Get Components in Drawing View Example (VBA)

This example shows how to get the components in a drawing view and how to change their line font styles.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Drawing document opened by the macro exists.
' 2. Drawing view is selected.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Specified drawing document is opened.
' 2. Drawing View1 is selected.
' 3. Gets the root and children components for Drawing
'    View1.
' 4. For each component:
'    a. Prints whether a drawing component is selected, the
'       name of the component, and the name of the configuration
'       to the Immediate window.
'    b. Disables the use of the document defaults for the
'       the component's line font style.
'    c. Sets new line style and line thickness for the component's
'       visible edges and prints the new settings and values to
'       the Immediate window.
'    d. Prints the file name of the component to the Immediate window.
'------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swSelData                   As SldWorks.SelectData
    Dim swModelDocExt               As SldWorks.ModelDocExtension
    Dim swView                      As SldWorks.View
    Dim swRootDrawComp              As SldWorks.DrawingComponent
    Dim vDrawChildCompArr           As Variant
    Dim vDrawChildComp              As Variant
    Dim swDrawComp                  As SldWorks.DrawingComponent
    Dim swComp                      As SldWorks.Component2
    Dim swCompModel                 As SldWorks.ModelDoc2
    Dim assemblyDrawing             As String
    Dim status                      As Boolean
    Dim errors                      As Long
    Dim warnings                    As Long
    Dim lineWeight                  As Long
    Dim lineThickness               As Double
```

```
    Set swApp = Application.SldWorks
```

```
    assemblyDrawing = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\mobile gantry.slddrw"
    Set swModel = swApp.OpenDoc6(assemblyDrawing, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    Set swDraw = swModel
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
```

```
    status = swDraw.ActivateView("Drawing View4")
    status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0.104008832128, 0.1163870710783, 0, False, 0, Nothing, 0)
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ViewZoomtofit2
    Set swRootDrawComp = swView.RootDrawingComponent
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  View = " & swView.Name
```

```
    vDrawChildCompArr = swRootDrawComp.GetChildren
    For Each vDrawChildComp In vDrawChildCompArr
        Set swDrawComp = vDrawChildComp

        ' Drawing component selected?
        Debug.Print " Drawing component selected = " & swDrawComp.Select(True, Nothing)
```

```
        ' Returns NULL if underlying model is open in a different configuration
        Set swComp = swDrawComp.Component
```

```
        If Not Nothing Is swComp Then
            ' Returns NULL if drawing is lightweight
            Set swCompModel = swComp.GetModelDoc2
```

```
            Debug.Print "      Component                            = " & swComp.Name2
            Debug.Print "      Configuration                        = " & swComp.ReferencedConfiguration
```

```
            ' Turn off using document default settings for component's line font style
            swDrawComp.UseDocumentDefaults = False
            Debug.Print "      Default component line font in use   = " & swDrawComp.UseDocumentDefaults
            ' Set new line style for visible edges
            swDrawComp.SetLineStyle swDrawingComponentLineFontVisible, swLineCHAIN
            Debug.Print "        Line style for visible edges                      = " & swDrawComp.GetLineStyle(swDrawingComponentLineFontVisible)
            ' Set new line thickness for visible edges
            swDrawComp.SetLineThickness swDrawingComponentLineFontVisible, swLW_CUSTOM, 0.0003
            lineWeight = swDrawComp.GetLineThickness(swDrawingComponentLineFontVisible, lineThickness)
            Debug.Print "        Line weight style and thickness for visible edges = " & lineWeight & ", " & lineThickness * 1000 & " mm"
```

```
            If Not Nothing Is swCompModel Then
                Debug.Print "      File                                 = " & swCompModel.GetPathName
                Debug.Print " "
            End If
```

```
        End If
```

```
    Next
```

```
End Sub
```
