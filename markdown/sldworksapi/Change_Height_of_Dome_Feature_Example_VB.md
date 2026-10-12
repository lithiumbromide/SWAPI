---
title: "Change Height of Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Height_of_Dome_Feature_Example_VB.htm"
---

# Change Height of Dome Feature Example (VBA)

This example shows how to change the height of a dome feature.

```vb
'--------------------------------------
'
' Preconditions: Dome feature for which a distance was specified is selected.
'
' Postconditions: Height of dome feature is doubled.
'
'--------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swPart                  As SldWorks.PartDoc
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swSelData               As SldWorks.SelectData
    Dim swFeat                  As SldWorks.feature
    Dim swDome                  As SldWorks.DomeFeatureData2
    Dim swFace                  As SldWorks.face2
    Dim swEnt                   As SldWorks.Entity
    Dim bRet                    As Boolean
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swDome = swFeat.GetDefinition

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    Debug.Print "    Elliptical     = " & swDome.Elliptical
    Debug.Print "    Height         = " & swDome.Height * 1000# & " mm"
    Debug.Print "    ReverseDir     = " & swDome.ReverseDir

    ' Roll back to get access to face
    bRet = swDome.AccessSelections(swModel, Nothing): Debug.Assert bRet

    Set swFace = swDome.Face
    Set swEnt = swFace

    bRet = swEnt.Select4(False, swSelData): Debug.Assert bRet

    ' Make some changes
    swDome.Height = 2# * swDome.Height
    swDome.Elliptical = True

    ' Apply changes
    ' Assert will fire if dome cannot be changed
    bRet = swFeat.ModifyDefinition(swDome, swModel, Nothing): Debug.Assert bRet
    End Sub
```
