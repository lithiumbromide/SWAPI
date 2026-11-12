---
title: "Get Bodies in Body Folders Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_in_Body_Folders_Example_VBNET.htm"
---

# Get Bodies in Body Folders Example (VB.NET)

This example shows how to get the bodies in body folder features.

```vb
 '------------------------------------------------
 ' Preconditions: Open a part document that
 ' contains a body folder that contains
 ' one or more solid, surface, cut-list,
 ' or weldment items.
 '
 ' Postconditions: Inspect the Immediate window.
 '------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swPart As ModelDoc2
     Dim swFeat As Feature
     Dim BodyFolderType(5) As String

     Sub main()

         BodyFolderType(0) = "dummy"
         BodyFolderType(1) =  "swSolidBodyFolder"
         BodyFolderType(2) =  "swSurfaceBodyFolder"
         BodyFolderType(3) =  "swBodySubFolder"
         BodyFolderType(4) =  "swWeldmentSubFolder"
         BodyFolderType(5) =  "swWeldmentCutListFolder"

         swPart = swApp.ActiveDoc

         Debug.Print("File = " & swPart.GetPathName)

         swFeat = swPart.FirstFeature
         TraverseFeatures(swFeat, True)

     End Sub

     Sub DoTheWork(ByVal thisFeat As Feature)

         Dim IsBodyFolder As Boolean
         IsBodyFolder =  False

         Dim FeatType As String
         FeatType = thisFeat.GetTypeName

         If FeatType = "SolidBodyFolder" Or FeatType = "SurfaceBodyFolder" Or FeatType = "CutListFolder" Or FeatType = "SubWeldFolder" Or FeatType = "SubAtomFolder"         Then
             IsBodyFolder =  True
         End If

         If IsBodyFolder Then

             Dim BodyFolder As BodyFolder
             BodyFolder = thisFeat.GetSpecificFeature2

             Dim BodyFolderTypeE As Long
             BodyFolderTypeE = BodyFolder.Type
             Debug.Print(thisFeat.Name   "," & FeatType & "," & BodyFolderType(BodyFolderTypeE) & " type " & BodyFolderTypeE)

             Dim BodyCount As Integer
             BodyCount = BodyFolder.GetBodyCount

             Debug.Print("   Body Count is " & BodyCount)

             Dim vBodies As Object
             vBodies = BodyFolder.GetBodies

             Dim i As  Integer

             If Not IsNothing(vBodies) Then
                 For i = LBound(vBodies) To UBound(vBodies)
                     Dim Body As Body2
                     Body = vBodies(i)
                     Debug.Print("   " & Body.Name)
                 Next i
             End If

             Dim FeatureFromBodyFolder As Feature
             FeatureFromBodyFolder = BodyFolder.GetFeature

             If Not FeatureFromBodyFolder Is thisFeat Then
                 MsgBox("Features don't match!")
             End If
         Else

         End If

     End Sub

     Sub TraverseFeatures(ByVal thisFeat As Feature, ByVal isTopLevel As Boolean)

         Dim curFeat As Feature
         curFeat = thisFeat

         While Not curFeat Is  Nothing
             DoTheWork(curFeat)  'Do the thing that we are doing this feature traversal for

             Dim subfeat As Feature
             subfeat = curFeat.GetFirstSubFeature

             While Not subfeat Is  Nothing
                 TraverseFeatures(subfeat, False)
                 Dim nextSubFeat As Feature
                 nextSubFeat = subfeat.GetNextSubFeature
                 subfeat = nextSubFeat
                 nextSubFeat = Nothing
             End While

             subfeat =  Nothing

             Dim nextFeat As Feature

             If isTopLevel Then
                 nextFeat = curFeat.GetNextFeature
             Else
                 nextFeat =  Nothing
             End If

             curFeat = nextFeat
             nextFeat = Nothing

         End While

     End Sub

     Public swApp As SldWorks

 End  Class
```
