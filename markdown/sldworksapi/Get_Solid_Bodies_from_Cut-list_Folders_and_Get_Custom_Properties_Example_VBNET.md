---
title: "Get Solid Bodies from Cut-list Folders and Get Custom Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm"
---

# Get Solid Bodies from Cut-list Folders and Get Custom Properties Example (VB.NET)

This example shows how to get the solid bodies from cut-list folders and how to get the custom properties for the solid bodies.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
' 2. Click Tools > Options > Document Properties > Weldments >
'    Rename cut list folders with Description property value > OK.
' 3. Right-click Cut list(31) in the FeatureManager design tree
'    and click Update.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the FeatureManager design tree.
' 2. Examine the Immediate window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swPart As ModelDoc2
    Dim swFeat As Feature

    Sub GetFeatureCustomProps(ByVal thisFeat As Feature)
        Dim CustomPropMgr As CustomPropertyManager
        CustomPropMgr = thisFeat.CustomPropertyManager
        Dim vCustomPropNames As Object
        vCustomPropNames = CustomPropMgr.GetNames
        If Not IsNothing(vCustomPropNames) Then
            Debug.Print("               Cut-list custom properties:")
            Dim i As Integer
            For i = LBound(vCustomPropNames) To UBound(vCustomPropNames)
                Dim CustomPropName As String
                CustomPropName = vCustomPropNames(i)
                Dim CustomPropType As Integer
                CustomPropType = CustomPropMgr.GetType2(CustomPropName)
                Dim CustomPropVal As String = ""
                Dim CustomPropResolvedVal As String = ""
                CustomPropMgr.Get2(CustomPropName, CustomPropVal, CustomPropResolvedVal)
                Debug.Print("                     Name: " & CustomPropName)
                Debug.Print("                         Value: " & CustomPropVal)
                Debug.Print("                         Resolved value: " & CustomPropResolvedVal)
            Next i
        End If
    End Sub

    Sub DoTheWork(ByVal thisFeat As Feature, ByVal ParentName As String)
        Static InBodyFolder As Boolean
        Static BodyFolderType(5) As String
        Static BeenHere As Boolean
        Dim bAllFeatures As Boolean
        Dim bCutListCustomProps As Boolean
        Dim vSuppressed As Object
        Dim BodyCount As Integer

        If Not BeenHere Then
            BodyFolderType(0) = "dummy"
            BodyFolderType(1) = "swSolidBodyFolder"
            BodyFolderType(2) = "swSurfaceBodyFolder"
            BodyFolderType(3) = "swBodySubFolder"
            BodyFolderType(4) = "swWeldmentSubFolder"
            BodyFolderType(5) = "swWeldmentCutListFolder"
            InBodyFolder = False
            BeenHere = True
            bAllFeatures = False
            bCutListCustomProps = False
        End If

        'Comment out next line to print information for just BodyFolders
        bAllFeatures = True 'True to print information about all features

        'Comment out next line if you do not want cut list's custom properties
        bCutListCustomProps = True

        Dim FeatType As String
        FeatType = thisFeat.GetTypeName
        If (FeatType = "SolidBodyFolder") And (ParentName = "Root Feature") Then
            InBodyFolder = True
        End If
        If (FeatType <> "SolidBodyFolder") And (ParentName = "Root Feature") Then
            InBodyFolder = False
        End If

        'Only consider the CutListFolders that are under SolidBodyFolder
        If (InBodyFolder = False) And (FeatType = "CutListFolder") Then
            'Skip the second occurrence of the CutListFolders during the feature traversal
            Exit Sub
        End If

        'Only consider the SubWeldFolder that are under the SolidBodyFolder
        If (InBodyFolder = False) And (FeatType = "SubWeldFolder") Then
            'Skip the second occurrence of the SubWeldFolders during the feature traversal
            Exit Sub
        End If

        Dim IsBodyFolder As Boolean
        If FeatType = "SolidBodyFolder" Or FeatType = "SurfaceBodyFolder" Or FeatType = "CutListFolder" Or FeatType = "SubWeldFolder" Or FeatType = "SubAtomFolder" Then
            IsBodyFolder = True
        Else
            IsBodyFolder = False
        End If
        If bAllFeatures And (Not IsBodyFolder) Then
            Debug.Print("Feature name: " & thisFeat.Name)
            Debug.Print("   Feature type: " & FeatType)
            vSuppressed = thisFeat.IsSuppressed2(swInConfigurationOpts_e.swThisConfiguration, Nothing)
            If IsNothing(vSuppressed) Then
                Debug.Print("        Suppression failed")
            Else
                Debug.Print("        Suppressed")
            End If
        End If
        If IsBodyFolder Then
            Dim BodyFolder As BodyFolder
            BodyFolder = thisFeat.GetSpecificFeature2
            BodyCount = BodyFolder.GetBodyCount
            If (FeatType = "CutListFolder") And (BodyCount < 1) Then
                'When BodyCount = 0, this cut list folder is not displayed in the
                'FeatureManager design tree, so skip it
                Exit Sub
            Else
                Debug.Print("Feature name: " & thisFeat.Name)
                Debug.Print("  Feature type: " & FeatType)
                vSuppressed = thisFeat.IsSuppressed2(swInConfigurationOpts_e.swThisConfiguration, Nothing)
                If IsNothing(vSuppressed) Then
                    Debug.Print("        Suppression failed")
                Else
                    Debug.Print("        Suppressed")
                End If
            End If
            If Not bAllFeatures Then
                Debug.Print("Feature name: " & thisFeat.Name)
                Debug.Print("  Feature type: " & FeatType)
                vSuppressed = thisFeat.IsSuppressed2(swInConfigurationOpts_e.swThisConfiguration, Nothing)
                If IsNothing(vSuppressed) Then
                    Debug.Print("        Suppression failed")
                Else
                    Debug.Print("        Suppressed")
                End If
            End If
            Dim BodyFolderTypeE As Integer
            BodyFolderTypeE = BodyFolder.Type
            Debug.Print("        Body folder: " & BodyFolderType(BodyFolderTypeE))
            Debug.Print("        Body folder type: " & BodyFolderTypeE)
            Debug.Print("        Body count: " & BodyCount)
            Dim vBodies As Object
            vBodies = BodyFolder.GetBodies
            Dim i As Integer
            If Not IsNothing(vBodies) Then
                For i = LBound(vBodies) To UBound(vBodies)
                    Dim Body As Body2
                    Body = vBodies(i)
                    Debug.Print("          Body name: " & Body.Name)
                Next i
            End If
        Else
            If bAllFeatures Then
                Debug.Print("")
            End If
        End If
        If (FeatType = "CutListFolder") Then
            'When BodyCount = 0, this cut-list folder is not displayed
            'in the FeatureManager design tree, so skip it
            If BodyCount > 0 Then
                If bCutListCustomProps Then
                    'Comment out this line if you do not want to
                    'print the cut-list folder's custom properties
                    GetFeatureCustomProps(thisFeat)
                End If
            End If
        End If

    End Sub
    Sub TraverseFeatures(ByVal thisFeat As Feature, ByVal isTopLevel As Boolean, ByVal ParentName As String)
        Dim curFeat As Feature
        curFeat = thisFeat
        While Not curFeat Is Nothing
            DoTheWork(curFeat, ParentName)
            Dim subfeat As Feature
            subfeat = curFeat.GetFirstSubFeature
            While Not subfeat Is Nothing
                TraverseFeatures(subfeat, False, curFeat.Name)
                Dim nextSubFeat As Feature
                nextSubFeat = subfeat.GetNextSubFeature
                subfeat = nextSubFeat
                nextSubFeat = Nothing
            End While
            subfeat = Nothing
            Dim nextFeat As Feature
            If isTopLevel Then
                nextFeat = curFeat.GetNextFeature
            Else
                nextFeat = Nothing
            End If
            curFeat = nextFeat
            nextFeat = Nothing
        End While
    End Sub

    Sub main()

        swPart = swApp.ActiveDoc
        Debug.Print("File: " & swPart.GetPathName)
        Dim ConfigName As String
        ConfigName = swPart.ConfigurationManager.ActiveConfiguration.Name
        Debug.Print("Active configuration name: " & ConfigName)
        swFeat = swPart.FirstFeature
        TraverseFeatures(swFeat, True, "Root Feature")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
