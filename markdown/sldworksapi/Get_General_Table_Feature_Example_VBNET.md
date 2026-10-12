---
title: "Get General Table Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_General_Table_Feature_Example_VBNET.htm"
---

# Get General Table Feature Example (VB.NET)

This example shows how to get a general table feature and some of its table annotation data.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Inserts a table annotation.
' 3. Gets the general table feature.
' 4. Prints the name of the general table feature and
'    some of its annotation table data the Immediate window.
' 5. Examine the Immediate window.
'
' NOTE: Because the drawing document is used elsewhere, do not
' save changes.
'-----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDrawing As DrawingDoc
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim swTableAnnotation As TableAnnotation
        Dim swGeneralTableFeature As GeneralTableFeature
        Dim swSelectionMgr As SelectionMgr
        Dim swModelDocExt As ModelDocExtension
        Dim swFeature As Feature
        Dim nbrTableAnnotations As Integer
        Dim tableAnnotations() As Object
        Dim i As Integer
        Dim anchorAttached As Boolean
        Dim anchorType As Integer
        Dim nbrColumns As Integer
        Dim nbrRows As Integer

        'Open drawing document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Insert table annotation
        swDrawing = swModel
        swTableAnnotation = swDrawing.InsertTableAnnotation2(False, 0.0275123456559767, 0.132124518483965, 1, "", 2, 2)
        If Not swTableAnnotation Is Nothing Then
            swTableAnnotation.BorderLineWeight = 0
            swTableAnnotation.GridLineWeight = 0
        End If

        'Select and get general table feature
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("General Table1", "GENERALTABLEFEAT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swGeneralTableFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swFeature = swGeneralTableFeature.GetFeature
        Debug.Print("General table feature name: " & swFeature.Name)

        'Get general table feature's annotation data
        nbrTableAnnotations = swGeneralTableFeature.GetTableAnnotationCount
        Debug.Print("Number of annotations = " & nbrTableAnnotations)
        tableAnnotations = swGeneralTableFeature.GetTableAnnotations
        For i = 0 To (nbrTableAnnotations - 1)
            swTableAnnotation = tableAnnotations(i)
            anchorAttached = swTableAnnotation.Anchored
            Debug.Print("Table anchored        = " & anchorAttached)
            anchorType = swTableAnnotation.AnchorType
            Debug.Print("Anchor type           = " & anchorType)
            nbrColumns = swTableAnnotation.ColumnCount
            Debug.Print("Number of columns     = " & nbrColumns)
            nbrRows = swTableAnnotation.RowCount
            Debug.Print("Number of rows        = " & nbrRows)
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
