---
title: "Get Solid Bodies from Cut-list Folders and Get Custom Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm"
---

# Get Solid Bodies from Cut-list Folders and Get Custom Properties Example (VBA)

This example shows how to get the solid bodies from cut-list folders and how to get the custom properties for the solid bodies.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that c:\temp\outputFile.txt does not exist; this macro
'    creates and writes to this file.
' 2. Add a reference to Microsoft Scripting Runtime (click
'    Tools > References > Browse > C:\windows\system32\scrrun.dll).
' 3. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
' 4. Click Tools > Options > Document Properties > Weldments >
'    Rename cut list folders with Description property value > OK.
' 5. Right-click Cut list(31) in the FeatureManager design tree
'    and click Update.
' 6. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the FeatureManager design tree.
' 2. Writes Done! to the Immediate window when
'    the macro finishes executing.
' 3. Open and examine c:\temp\outputFile.txt.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.ModelDoc2
Dim swFeat As SldWorks.Feature
Dim fs As Scripting.FileSystemObject
Dim a As Scripting.TextStream
```

```
Sub GetFeatureCustomProps(thisFeat As SldWorks.Feature)
```

```
    Dim CustomPropMgr As SldWorks.CustomPropertyManager
    Set CustomPropMgr = thisFeat.CustomPropertyManager
    Dim vCustomPropNames As Variant
```

```
    vCustomPropNames = CustomPropMgr.GetNames
    If Not IsEmpty(vCustomPropNames) Then
        a.WriteLine "               Cut-list custom properties:"
        Dim i As Long
        For i = LBound(vCustomPropNames) To UBound(vCustomPropNames)
            Dim CustomPropName As String
            CustomPropName = vCustomPropNames(i)
            Dim CustomPropType As Long
            CustomPropType = CustomPropMgr.GetType2(CustomPropName)
            Dim CustomPropVal As String
            Dim CustomPropResolvedVal As String
            CustomPropMgr.Get2 CustomPropName, CustomPropVal, CustomPropResolvedVal
            a.WriteLine "                     Name: " & CustomPropName
            a.WriteLine "                         Value: " & CustomPropVal
            a.WriteLine "                         Resolved value: " & CustomPropResolvedVal
        Next i
    End If
End Sub
```

```
Sub DoTheWork(thisFeat As SldWorks.Feature, ParentName As String)
```

```
    Static InBodyFolder As Boolean
    Static BodyFolderType(5) As String
    Static BeenHere As Boolean
    Dim bAllFeatures As Boolean
    Dim bCutListCustomProps As Boolean
    Dim vSuppressed As Variant
```

```
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
```

```
    'Comment out next line to print information for just BodyFolders
    bAllFeatures = True 'True to print information about all features
```

```
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
```

```
    'Only consider the CutListFolders that are under SolidBodyFolder
    If (InBodyFolder = False) And (FeatType = "CutListFolder") Then
        'Skip the second occurrence of the CutListFolders during the feature traversal
        Exit Sub
    End If
```

```
    'Only consider the SubWeldFolder that are under the SolidBodyFolder
    If (InBodyFolder = False) And (FeatType = "SubWeldFolder") Then
        'Skip the second occurrence of the SubWeldFolders during the feature traversal
        Exit Sub
    End If
```

```
    Dim IsBodyFolder As Boolean
    If FeatType = "SolidBodyFolder" Or FeatType = "SurfaceBodyFolder" Or FeatType = "CutListFolder" Or FeatType = "SubWeldFolder" Or FeatType = "SubAtomFolder" Then
        IsBodyFolder = True
    Else
        IsBodyFolder = False
    End If
```

```
    If bAllFeatures And (Not IsBodyFolder) Then
        a.WriteLine "Feature name: " & thisFeat.Name
        a.WriteLine "   Feature type: " & FeatType
        vSuppressed = thisFeat.IsSuppressed2(swInConfigurationOpts_e.swThisConfiguration, Nothing)
        If IsEmpty(vSuppressed) Then
            a.WriteLine "        Suppression failed"
        Else
            a.WriteLine "        Suppressed"
        End If
    End If
```

```
    If IsBodyFolder Then
        Dim BodyFolder As SldWorks.BodyFolder
        Set BodyFolder = thisFeat.GetSpecificFeature2
        Dim BodyCount As Long
        BodyCount = BodyFolder.GetBodyCount
```

```
        If (FeatType = "CutListFolder") And (BodyCount < 1) Then
            'When BodyCount = 0, this cut list folder is not displayed in the
            'FeatureManager design tree, so skip it
            Exit Sub
        Else
            a.WriteLine "Feature name: " & thisFeat.Name
            vSuppressed = thisFeat.IsSuppressed2(swInConfigurationOpts_e.swThisConfiguration, Empty)
            If IsEmpty(vSuppressed) Then
                a.WriteLine "       Suppression failed"
            Else
                a.WriteLine "       Suppressed"
            End If
        End If
```

```
        If Not bAllFeatures Then
            a.WriteLine "Feature name: " & thisFeat.Name
            vSuppressed = thisFeat.IsSuppressed2(swInConfigurationOpts_e.swThisConfiguration, Empty)
            If IsEmpty(vSuppressed) Then
                a.WriteLine "       Suppression failed"
            Else
                a.WriteLine "       Suppressed"
            End If
        End If
```

```
        Dim BodyFolderTypeE As Long
        BodyFolderTypeE = BodyFolder.Type
        a.WriteLine "        Body folder: " & BodyFolderType(BodyFolderTypeE)
        a.WriteLine "        Body folder type: BodyFolderTypeE"
        a.WriteLine "        Body count: " & BodyCount
```

```
        Dim vBodies As Variant
        vBodies = BodyFolder.GetBodies
        Dim i As Long
        If Not IsEmpty(vBodies) Then
            For i = LBound(vBodies) To UBound(vBodies)
                Dim Body As SldWorks.Body2
                Set Body = vBodies(i)
                a.WriteLine "           Body name: " & Body.Name
            Next i
        End If
    Else
        If bAllFeatures Then
            a.WriteLine ""
        End If
    End If
```

```
    If (FeatType = "CutListFolder") Then
        'When BodyCount = 0, this cut list folder is not displayed
        'in the FeatureManager design tree, so skip it
        If BodyCount > 0 Then
            If bCutListCustomProps Then
                'Comment out this line if you do not want to
                'print the cut list folder's custom properties
                GetFeatureCustomProps thisFeat
            End If
        End If
    End If
```

```
End Sub
```

```
Sub TraverseFeatures(thisFeat As SldWorks.Feature, isTopLevel As Boolean, ParentName As String)
```

```
    Dim curFeat As SldWorks.Feature
    Set curFeat = thisFeat
```

```
    While Not curFeat Is Nothing
        DoTheWork curFeat, ParentName
        Dim subfeat As SldWorks.Feature
        Set subfeat = curFeat.GetFirstSubFeature
        While Not subfeat Is Nothing
            TraverseFeatures subfeat, False, curFeat.Name
            Dim nextSubFeat As SldWorks.Feature
            Set nextSubFeat = subfeat.GetNextSubFeature
            Set subfeat = nextSubFeat
            Set nextSubFeat = Nothing
        Wend
        Set subfeat = Nothing
        Dim nextFeat As SldWorks.Feature
        If isTopLevel Then
            Set nextFeat = curFeat.GetNextFeature
        Else
            Set nextFeat = Nothing
        End If
        Set curFeat = nextFeat
        Set nextFeat = Nothing
    Wend
```

```
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swPart = swApp.ActiveDoc
    Set fs = CreateObject("Scripting.FileSystemObject")
    Set a = fs.CreateTextFile("c:\temp\outputFile.txt", True)
    a.WriteLine "File: " & swPart.GetPathName
    Dim ConfigName As String
    ConfigName = swPart.ConfigurationManager.ActiveConfiguration.Name
    a.WriteLine "Active configuration name: " & ConfigName
    Set swFeat = swPart.FirstFeature
    TraverseFeatures swFeat, True, "Root Feature"
    a.Close
    Debug.Print "Done!"
```

```
End Sub
```
