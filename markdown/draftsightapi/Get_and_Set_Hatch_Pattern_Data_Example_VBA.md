---
title: "Get and Set Hatch Pattern Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Hatch_Pattern_Data_Example_VBA.htm"
---

# Get and Set Hatch Pattern Data Example (VBA)

This example shows how to get and set Hatch pattern data.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to install_dir\bin\dsAutomation.dll.
' 4. Make sure that C:\ProgramData\Dassault Systemes\DraftSight\Examples
'    exists.
' 5. Copy all .dxf and .dwg files in this folder to a backup folder.
' 6. Set all .dxf and .dwg files in
'    C:\ProgramData\Dassault Systemes\DraftSight\Examples
'    to read/write.
' 7. Start DraftSight.
' 8. Open the Immediate window.
' 9. Run the macro.
'
' Postconditions:
' 1. Each .dxf or .dwg file in
'    C:\ProgramData\Dassault Systemes\DraftSight\Examples is
'    filtered for Hatch patterns.
' 2. Hatch patterns are changed in the .dxf and .dwg files
'    that have them.
' 3. Copy all .dxf and .dwg files from back up folder to
'    C:\ProgramData\Dassault Systemes\DraftSight\Examples.
'----------------------------------------------------------------
Option Explicit
```

```
        Public i As Long
```

```
Sub main()
```

```
        Dim dsApp As DraftSight.Application
        Dim drawings() As String
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
        If dsApp Is Nothing Then
            End
        End If

        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Check if the specified folder with drawings exists
        Dim folderName As String
        folderName = "C:\ProgramData\Dassault Systemes\DraftSight\Examples\"
```

```
        'Get drawing files in the folder
        drawings = GetDrawings(folderName)
```

```
        If LBound(drawings) >= UBound(drawings) Then
            MsgBox ("There are no DWG/DXF files in """ & folderName & """ directory.")
            End
        End If
```

```
        'Iterate through all drawings
        Dim docName As String
        Dim j As Long
        For j = 0 To (i - 1)
            docName = drawings(j)
            docName = folderName & docName
                'Open document
                Dim dsDoc As DraftSight.Document
                Set dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpen_Default, dsEncoding_Default)
                If Not dsDoc Is Nothing Then
```

```
                    ' Print name of document
                    Debug.Print ("Name of document: " & dsDoc.GetPathName)
```

```
                    'Change Hatch pattern for all hatch entities in the drawing
                    ChangeHatchPattern dsDoc
```

```
                    'Save document
                    dsDoc.Save
```

```
                    'Close document
                    dsApp.CloseDocument docName, True
                Else
                    MsgBox ("""" & docName & """ document could not be opened.")
                    Return
                End If
        Next j
    End Sub
```

```
    Public Sub ChangeHatchPattern(ByVal dsDoc As Document)
        'Get model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel
```

```
        'Get Sketch Manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsModel.GetSketchManager
```

```
        'Get Selection Manager
        Dim dsSelectionMgr As DraftSight.SelectionManager
        Set dsSelectionMgr = dsDoc.GetSelectionManager
```

```
        'Get selection filter
        Dim dsSelectionFilter As DraftSight.SelectionFilter
        Set dsSelectionFilter = dsSelectionMgr.GetSelectionFilter
```

```
        'Clear selection filter
        dsSelectionFilter.Clear
```

```
        'Add Hatch entity to the selection filter
        dsSelectionFilter.AddEntityType dsObjectType_e.dsHatchType
```

```
        'Activate selection filter
        dsSelectionFilter.Active = True
```

```
        'Get all layer names
        Dim layerNames As Variant
        layerNames = GetLayers(dsDoc)
```

```
        Dim entityTypes As Variant
        Dim entityObjects As Variant
        Dim entityItem As Variant
```

```
        'Get Hatch entities
        dsSketchMgr.GetEntities dsSelectionFilter, layerNames, entityTypes, entityObjects
```

```
        If Not IsArray(entityObjects) Then
            Debug.Print ("   Document does not have Hatch patterns.")
            Debug.Print (" ")
        Else
            Debug.Print ("   Document has Hatch patterns.")
```

```
            'Iterate through hatch entities
            For Each entityItem In entityObjects
```

```
                'Cast to Hatch entity
                Dim dsHatch As DraftSight.Hatch
                Set dsHatch = entityItem
```

```
                'Get hatch pattern
                Dim patternName As String
                patternName = ""
```

```
                Dim angle As Double
                angle = 0#
```

```
                Dim hatchScale As Double
                hatchScale = 0#
```

```
                Dim patternType As Long
                patternType = dsHatchPatternType_Predefined
```

```
                Dim spacing As Double
                spacing = 1#
```

```
                Dim dsHatchPattern As DraftSight.HatchPattern
                Set dsHatchPattern = dsHatch.GetHatchPattern
```

```
                dsHatchPattern.GetHatchOrSolidData patternName, angle, hatchScale, patternType, spacing
                Debug.Print ("   Pattern name, angle, scale, pattern types, spacing: " & patternName & ", " & angle & ", " & hatchScale & ", " & patternType & ", " & spacing)
```

```
                'Update pattern
                patternName = "HOUND"
                angle = 0#
                hatchScale = 1#
                patternType = dsHatchPatternType_e.dsHatchPatternType_Predefined
                spacing = 1#
                dsHatchPattern.SetHatchOrSolidData patternName, angle, hatchScale, patternType, spacing
            Next
            Debug.Print (" ")
        End If
    End Sub
```

```
    Public Function GetLayers(ByVal dsDoc As Document) As String()
        'Get Layer Manager
        Dim dsLayerManager As DraftSight.LayerManager
        Set dsLayerManager = dsDoc.GetLayerManager
```

```
        Dim dsLayers() As Object
        dsLayers = dsLayerManager.GetLayers()
```

```
        Dim dslayerNames() As String
        Dim nbrLayers As Long
        nbrLayers = UBound(dsLayers)
        ReDim dslayerNames(nbrLayers)
```

```
        Dim index As Long
```

```
        For index = 0 To nbrLayers
            Dim dsLayer As DraftSight.Layer
            Set dsLayer = dsLayers(index)
            dslayerNames(index) = dsLayer.Name
        Next
```

```
        GetLayers = dslayerNames
```

```
    End Function
```

```
    Public Function GetDrawings(ByVal folderName As String) As String()
```

```
        'Get DWG files
        'Dim i As Long
        i = 0
        Dim dsfile As String
        Dim dsDrawings() As String
```

```
        dsfile = Dir$(folderName + "\*.dwg", vbNormal)
        ReDim dsDrawings(i)
        dsDrawings(i) = dsfile
        Do Until dsfile = vbNullString
            If dsfile <> "." Then
                i = i + 1
            End If
            dsfile = Dir$
            ReDim Preserve dsDrawings(i)
            dsDrawings(i) = dsfile
        Loop
```

```
        'Get DXF files
        dsfile = Dir$(folderName + "\*.dxf", vbNormal)
        If dsfile <> "" Then
            dsDrawings(i) = dsfile
        Else
            ReDim Preserve dsDrawings(i - 1)
        End If
        Do Until dsfile = vbNullString
            'ReDim drawings(i)
            If dsfile <> "." Then
                    i = i + 1
            End If
            dsfile = Dir$
            If dsfile <> "" Then
                ReDim Preserve dsDrawings(i)
                dsDrawings(i) = dsfile
            End If
        Loop
```

```
        GetDrawings = dsDrawings
```

```
    End Function
```
