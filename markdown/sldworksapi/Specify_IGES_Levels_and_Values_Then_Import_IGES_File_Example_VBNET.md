---
title: "Specify IGES Levels and Values, Then Import IGES File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm"
---

# Specify IGES Levels and Values, Then Import IGES File Example (VB.NET)

This example shows how to:

- specify levels and values for importing IGES data.
- import an IGES file.

```
'------------------------------------------------
' Preconditions: Substitute the path and name
' of your IGES file where noted in the code.
'
' Postconditions:
' 1. Creates a folder named Layer 25.
' 2. Imports the specified IGES file into SOLIDWORKS Design
'    and moves the imported IGES features to Layer 25.
' 3. To verify, examine the graphics area and
'    FeatureManager design tree.
'--------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim model As ModelDoc2
        Dim boolstatus As Boolean
        Dim fileName As String
        Dim argString As String
        Dim importData As ImportIgesData
        Dim Err As Integer
        Dim orgSetting As Boolean
        Dim allLevels As Boolean
        Dim vOnlyLev As Object
        Dim onlyLev(0 To 1) As Integer
        Dim oneLev As Integer
        Dim lastFeature As Feature
        Dim newFolder As Feature
        Dim newFolderName As String = ""
        Dim lastFeatureName As String

        model = swApp.ActiveDoc
        ' Substitute the path and name of your IGES file
        fileName = "path\IGES_file_name.igs"
        ' "r" means open new document
        ' "i" means insert into existing document
        If model Is Nothing Then
            argString = "r"
        Else    ' There is an existing part, so use it
            argString = "i"
        End If
        ' Fill in the import data
        importData = swApp.GetImportFileData(fileName)
        If Not importData Is Nothing Then
            ' Test the various flags
            importData.IncludeSurfaces = True
            importData.IncludeCurves = True
            importData.CurvesAsSketches = True  ' False = Curves as Curves
            importData.ProcessByLevel = False
            ' Test all levels
            '        allLevels = True
            ' False = levels specified in vOnlyLev
            '        newFolderName = "All levels"
            ' or, test multiple levels
            '        onlyLev(0) = 0
            '        onlyLev(1) = 6
            '        vOnlyLev = onlyLev
            '        newFolderName = "Layer 0 and 6"
            ' Or, test individual levels
            oneLev = 25
            vOnlyLev = oneLev
            newFolderName = "Layer " & Format(oneLev)
            boolstatus = importData.SetLevels(allLevels, (vOnlyLev))
        End If

        ' Keep the last feature to determine what's been added
        '   If this is a new document, that cannot be done, so
        '   just hard code the name of the Origin feature,
        '   which is currently the last feature in a new part document
        '   It is better to always create a new
        '   document first, and then call SldWorks::LoadFile4
        '   with "i" argString to avoid this potential problem
        If Not model Is Nothing Then
            lastFeature = model.FeatureByPositionReverse(0)
            lastFeatureName = lastFeature.Name
        Else
            lastFeatureName = "Origin"
        End If
        ' Setting this user preference to true means that the IGES
        '   dialog is displayed
        ' Setting this user preference to false means that the
        '   IGES dialog is not displayed, and the import IGES data
        '   is used if it is passed in, or, if it is not,
        '   then the default values for the dialog are used
        orgSetting = swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swIGESImportShowLevel)
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swIGESImportShowLevel, False)
        model = swApp.LoadFile4(fileName, argString, importData, Err)

        ' swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swIGESImportShowLevel, orgSetting
        ' If the SldWorks::LoadFile4 failed, do not continue
        If model Is Nothing Then
            Debug.Print("Problem loading file. Error message = " & Err.ToString)
            Exit Sub
        End If
        ' Retrieve all of the features that were created
        ' and move them into their own new folder
        model.ClearSelection2(True)
        ' Select features that are then used by FeatureManager::InsertFeatureTreeFolder2
        ' Either method of selection seems to take the same amount of time
        boolstatus = select_new_features_individually(model, lastFeatureName)
        ' boolstatus = multiselect_new_features(model, lastFeatureName)
        If (boolstatus) Then
            newFolder = model.FeatureManager.InsertFeatureTreeFolder2(swFeatureTreeFolderType_e.swFeatureTreeFolder_Containing)
            If Not newFolder Is Nothing Then
                newFolder.Name = newFolderName
            End If
            model.ClearSelection2(True)
        End If
    End Sub

    Private Function select_new_features_individually(ByVal model As ModelDoc2, ByVal lastFeatureName As String) As Boolean
        Dim testFeature As Feature
        Dim loopCount As Integer
        Dim boolstatus As Boolean
        select_new_features_individually = False
        loopCount = 0
        testFeature = model.FeatureByPositionReverse(loopCount)
        While (Not testFeature Is Nothing) And (Not testFeature.Name = lastFeatureName)
            loopCount = loopCount + 1
            boolstatus = testFeature.Select2(True, 0)
            If Not boolstatus = 0 Then
                select_new_features_individually = True
            End If
            testFeature = model.FeatureByPositionReverse(loopCount)
        End While
    End Function

    Private Function multiselect_new_features(ByVal model As ModelDoc2, ByVal lastFeatureName As String) As Boolean
        Dim testFeature As Feature
        Dim loopCount As Integer
        Dim featureList() As Feature
        Dim vFeatureList As Object
        Dim longstatus As Integer
        Dim selData As SelectData
        Dim selMgr As SelectionMgr
        multiselect_new_features = False
        loopCount = 0
        testFeature = model.FeatureByPositionReverse(loopCount)
        While (Not testFeature Is Nothing) And (Not testFeature.Name = lastFeatureName)
            loopCount = loopCount + 1
            testFeature = model.FeatureByPositionReverse(loopCount)
        End While
        ReDim featureList(0 To loopCount - 1)
        loopCount = 0
        testFeature = model.FeatureByPositionReverse(loopCount)
        While (Not testFeature Is Nothing) And (Not testFeature.Name = lastFeatureName)
            featureList(loopCount) = testFeature
            loopCount = loopCount + 1
            testFeature = model.FeatureByPositionReverse(loopCount)
        End While

        vFeatureList = featureList
        selMgr = model.SelectionManager
        selData = selMgr.CreateSelectData
        longstatus = model.Extension.MultiSelect2((vFeatureList), True, selData)
        If longstatus > 0 Then
            multiselect_new_features = True
        End If
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
