---
title: "Get Components in Drawing View (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_in_Drawing_View_Example_VBNET.htm"
---

# Get Components in Drawing View (VB.NET)

This example shows how to get the components in a drawing view and how to change their line font styles.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc
         Dim swSelMgr As SelectionMgr
          Dim swSelData  As SelectData
         Dim swModelDocExt As ModelDocExtension
         Dim swView As View
         Dim swRootDrawComp As DrawingComponent
         Dim vDrawChildCompArr As Object
         Dim vDrawChildComp As Object
         Dim swDrawComp As DrawingComponent
         Dim swComp As Component2
         Dim swCompModel As ModelDoc2
         Dim assemblyDrawing As String
         Dim status As Boolean
         Dim errors As Integer
         Dim warnings As Integer
         Dim lineWeight As Integer
         Dim lineThickness As Double

         assemblyDrawing =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\mobile gantry.slddrw"
         swModel = swApp.OpenDoc6(assemblyDrawing, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         swDraw = swModel
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData

         status = swDraw.ActivateView("Drawing View4")
         status = swModelDocExt.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0.104008832128, 0.1163870710783, 0, False, 0, Nothing, 0)
         swView = swSelMgr.GetSelectedObject6(1, -1)
         swModel.ViewZoomtofit2()
         swRootDrawComp = swView.RootDrawingComponent

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  View = " & swView.Name)

         vDrawChildCompArr = swRootDrawComp.GetChildren
         For Each vDrawChildComp In vDrawChildCompArr
             swDrawComp = vDrawChildComp

            ' Drawing component selected?
            Debug.Print(" Drawing component selected = " & swDrawComp.Select(True, Nothing))

             ' Returns NULL if underlying model is open in a different configuration
             swComp = swDrawComp.Component

             If Not  Nothing  Is swComp  Then
                 ' Returns NULL if drawing is lightweight
                 swCompModel = swComp.GetModelDoc2

                 Debug.Print("      Component                            = " & swComp.Name2)
                 Debug.Print("      Configuration                        = " & swComp.ReferencedConfiguration)

                 ' Turn off using document default settings for component's line font style
                 swDrawComp.UseDocumentDefaults = False
                 Debug.Print("      Default component line font in use   = " & swDrawComp.UseDocumentDefaults)
                 ' Set new line style for visible edges
                 swDrawComp.SetLineStyle(swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible, swLineStyles_e.swLineCHAIN)
                 Debug.Print("        Line style for visible edges                      = " & swDrawComp.GetLineStyle(swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible))
                 ' Set new line thickness for visible edges
                 swDrawComp.SetLineThickness(swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible, swLineWeights_e.swLW_CUSTOM, 0.0003)
                 lineWeight = swDrawComp.GetLineThickness(swDrawingComponentLineFontOption_e.swDrawingComponentLineFontVisible, lineThickness)
                 Debug.Print("        Line weight style and thickness for visible edges = " & lineWeight & ", " & lineThickness * 1000 & " mm")

                 If Not  Nothing  Is swCompModel Then
                     Debug.Print("      File                                 = " & swCompModel.GetPathName)
                     Debug.Print(" ")
                 End If

             End If

         Next

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
