---
title: "Get Bodies in Body Folders Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_in_Body_Folders_Example_VB.htm"
---

# Get Bodies in Body Folders Example (VBA)

This example shows how to get the bodies in body folder features.

```vb
 '----------------------------------------------
 ' Preconditions: Open a part document that
 ' contains a body folder that contains
 ' one or more solid, surface, cut-list,
 ' or weldment items.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swPart As SldWorks.ModelDoc2
 Dim swFeat As SldWorks.Feature
 Dim Indent As Long
 Dim BodyFolderType(5) As String
Sub main()
    BodyFolderType(0) = "dummy"
     BodyFolderType(1) = "swSolidBodyFolder"
     BodyFolderType(2) = "swSurfaceBodyFolder"
     BodyFolderType(3) = "swBodySubFolder"
     BodyFolderType(4) = "swWeldmentSubFolder"
     BodyFolderType(5) = "swWeldmentCutListFolder"
    Set swApp = Application.SldWorks
     Set swPart = swApp.ActiveDoc
    Debug.Print "File = " & swPart.GetPathName
    Indent = -3
    Set swFeat = swPart.FirstFeature
     TraverseFeatures swFeat, True
End Sub

Sub DoTheWork(thisFeat As SldWorks.Feature)
    Dim IsBodyFolder As Boolean
     IsBodyFolder = False
    Dim FeatType As String
     FeatType = thisFeat.GetTypeName
    If FeatType = "SolidBodyFolder" Or FeatType = "SurfaceBodyFolder" Or FeatType = "CutListFolder" Or FeatType = "SubWeldFolder" Or FeatType = "SubAtomFolder" Then
             IsBodyFolder = True
     End If
    If IsBodyFolder Then
        Debug.Print Format(String(Indent, " ") & thisFeat.Name, "!" & String(40, "@")); Format(FeatType, "!" & String(30, "@"));
        Dim BodyFolder As SldWorks.BodyFolder
         Set BodyFolder = thisFeat.GetSpecificFeature2
        Dim BodyFolderTypeE As Long
         BodyFolderTypeE = BodyFolder.Type
        Debug.Print Format(BodyFolderType(BodyFolderTypeE), "!" & String(30, "@")); Format(BodyFolderTypeE, "!@@@@");
        Dim BodyCount As Long
         BodyCount = BodyFolder.GetBodyCount
        Debug.Print "Body Count is " & BodyCount
        Dim vBodies As Variant
         vBodies = BodyFolder.GetBodies
        Dim i As Long
        If Not IsEmpty(vBodies) Then
             For i = LBound(vBodies) To UBound(vBodies)
                 Dim Body As SldWorks.Body2
                 Set Body = vBodies(i)
                 Debug.Print Format(String(Indent + 3, " ") & Body.Name, "!" & String(30, "@"))
             Next i
         End If
        Dim FeatureFromBodyFolder As SldWorks.Feature
         Set FeatureFromBodyFolder = BodyFolder.GetFeature
        If Not FeatureFromBodyFolder Is thisFeat Then
             MsgBox "Features don't match!"
         End If
     Else
    End If
End Sub
Sub TraverseFeatures(thisFeat As SldWorks.Feature, isTopLevel As Boolean)
    Dim curFeat As SldWorks.Feature
     Set curFeat = thisFeat
    Indent = Indent + 3
    While Not curFeat Is Nothing
         DoTheWork curFeat 'Do the thing that we are doing this feature traversal for
        Dim subfeat As SldWorks.Feature
         Set subfeat = curFeat.GetFirstSubFeature
        While Not subfeat Is Nothing
             TraverseFeatures subfeat, False
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
     Indent = Indent - 3
End Sub
```
