---
title: "Multiselect Same and Different Objects Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Multiselect_Same and_Different_Objects_Example_VBNET.htm"
---

# Multiselect Same and Different Objects Example (VB.NET)

This example shows how to select multiple faces, multiple edges, and multiple faces and edges.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects and adds three faces to an array of faces.
' 3. Selects and adds two edges to an array of edges.
' 4. Selects one face and three edges and adds them to an
'    array of entities.
' 5. Multiselects each array of faces, edges, and entities.
' 6. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere do not save
' changes.
'---------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim faceArray(2) As Face2
        Dim edgeArray(1) As Edge
        Dim entitiesArray(3) As Entity
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim nbrSelections As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager

        'Select three faces and add them to an array of faces
        status = swModelDocExt.SelectByID2("", "FACE", 0.00339003579642849, 0.0165689832048201, 0.0460521566345733, False, 0, Nothing, 0)
        faceArray(0) = swSelMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "FACE", -0.00464858017755887, 0.0299999999999159, -0.00213158882201014, False, 0, Nothing, 0)
        faceArray(1) = swSelMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0310506911185371, 0.0299999999999159, -0.016600178364456, False, 0, Nothing, 0)
        faceArray(2) = swSelMgr.GetSelectedObject6(1, -1)
        swModel.ClearSelection2(True)

        'Select two edges and them to an array of edges
        status = swModelDocExt.SelectByID2("", "EDGE", -0.0103092369793103, 0.0304904435424191, 0.0457189565300382, False, 0, Nothing, 0)
        edgeArray(0) = swSelMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0437175784318242, 0.0301364202527452, 0.028332486890065, False, 0, Nothing, 0)
        edgeArray(1) = swSelMgr.GetSelectedObject6(1, -1)
        swModel.ClearSelection2(True)

        'Select one face and three edges and add them to an array of entities
        status = swModelDocExt.SelectByID2("", "FACE", -0.00725501009526397, 0.0299999999999159, -0.00236379374842954, False, 0, Nothing, 0)
        entitiesArray(0) = swSelMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0435139962395397, 0.0148277472299014, 0.0462522660892546, False, 0, Nothing, 0)
        entitiesArray(1) = swSelMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0441251049156222, -0.000180110278279244, 0.0139372949385006, False, 0, Nothing, 0)
        entitiesArray(2) = swSelMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0303098420922652, 0.000354499639115602, 0.0458113148115444, False, 0, Nothing, 0)
        entitiesArray(3) = swSelMgr.GetSelectedObject6(1, -1)
        swModel.ClearSelection2(True)

        'Multiselect faces, edges, and entities using IModelDocExtension::MultiSelect2
        Debug.Print("Number of selections in:")
        nbrSelections = swModelDocExt.MultiSelect2(faceArray, False, Nothing)
        Debug.Print("  face array: " & nbrSelections)
        swModel.ClearSelection2(True)
        nbrSelections = swModelDocExt.MultiSelect2(edgeArray, False, Nothing)
        Debug.Print("  edge array: " & nbrSelections)
        swModel.ClearSelection2(True)
        nbrSelections = swModelDocExt.MultiSelect2(entitiesArray, False, Nothing)
        Debug.Print("  entities (face and edges) array: " & nbrSelections)
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
