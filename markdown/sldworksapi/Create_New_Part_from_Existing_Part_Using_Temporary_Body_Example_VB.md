---
title: "Create New Part from Existing Part Using Temporary Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_VB.htm"
---

# Create New Part from Existing Part Using Temporary Body Example (VBA)

This example shows how to delete faces from a temporary body and how to create a new part using that temporary body.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\toolbox\braceright.sldprt.
' 2. Verify that the specified part template exists..
'
' Postconditions:
' 1. Creates a new part; the new part has same body as original part
'    but with selected faces deleted.
' 2. Close the new part without saving it.
' 3. Close braceright.sldprt without saving it.
'----------------------------------------------------------------------------
```

```vb
Option Explicit

Function GetFacesWithAttribute(swApp As SldWorks.SldWorks, swBody As SldWorks.Body2, swAttDef As SldWorks.AttributeDef) As Variant

    Dim swFace                  As SldWorks.Face2
    Dim swEnt                   As SldWorks.Entity
    Dim swAttCopy               As SldWorks.Attribute
    Dim swFaceArr()             As SldWorks.Face2

    ' Search for faces on temporary body based on copied attributes
    ReDim swFaceArr(0)
    Set swFace = swBody.GetFirstFace

    Do While Not Nothing Is swFace
        Set swEnt = swFace
        Set swAttCopy = Nothing
        ' Only one instance of attribute on a face should exist
        Set swAttCopy = swEnt.FindAttribute(swAttDef, 0)
        If Not swAttCopy Is Nothing Then
            Set swFaceArr(UBound(swFaceArr)) = swFace
            ReDim Preserve swFaceArr(UBound(swFaceArr) + 1)
        End If
        Set swFace = swFace.GetNextFace
    Loop

    Debug.Assert UBound(swFaceArr) >= 1
    ReDim Preserve swFaceArr(UBound(swFaceArr) - 1)
    GetFacesWithAttribute = swFaceArr
End Function

Sub main()
    '   1 = invisible
    '   0 = visible
    Const CreateVisible As Long = 0
    Const sAttDefName As String = "temp_attrib"
    Const sAttRootName As String = "root_attrib"
    Dim swApp As SldWorks.SldWorks
    Dim swAttDef As SldWorks.AttributeDef
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim swCopyBody As SldWorks.Body2
    Dim swSelMg As SldWorks.SelectionMgr
    Dim nSelCount As Long
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swAtt() As SldWorks.Attribute
    Dim vFaceArr As Variant
    Dim swNewPart As SldWorks.PartDoc
    Dim swNewModel As SldWorks.ModelDoc2
    Dim swFeat As SldWorks.Feature
    Dim swFaultEntity As SldWorks.FaultEntity
    Dim vBodies As Variant
    Dim boolstatus As Boolean
    Dim i As Long
    Dim bLocChk As Boolean
    Dim bRet As Boolean

    Set swApp = Application.SldWorks
    Set swAttDef = swApp.DefineAttribute(sAttDefName)
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set swPart = swModel
    bRet = swAttDef.Register: Debug.Assert bRet

    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02203398034251, 0.2107859236428, 0.005471558832284, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03651723484872, 0.1911276369938, 0.007226351471076, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01524, 0.1384548315647, 0.004444480215071, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1306826750488, 0.0172129316129, 0.006448917397336, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1068570742154, 0.01524000000001, 0.00670683128584, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01652926606039, 0.01775444632528, 0.004157527166058, True, 0, Nothing, 0)
    ' Add attribute to selected faces
    nSelCount = swSelMgr.GetSelectedObjectCount2(-1)
    ReDim swAtt(nSelCount)
    For i = 1 To nSelCount
        Set swFace = swSelMgr.GetSelectedObject6(i, -1)
        Set swEnt = swFace
        Set swAtt(i - 1) = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName & i, CreateVisible, swAllConfiguration): Debug.Assert Not swAtt(i - 1) Is Nothing
    Next i
    vBodies = swPart.GetBodies2(swAllBodies, True)
    Set swBody = vBodies(0)
    Set swCopyBody = swBody.Copy

    ' Remove attribute from faces
    For i = 1 To nSelCount
        bRet = swAtt(i - 1).Delete(True): Debug.Assert bRet
    Next i

    vFaceArr = GetFacesWithAttribute(swApp, swCopyBody, swAttDef)
    Debug.Assert nSelCount = UBound(vFaceArr) + 1

    ' Can only delete faces from a temporary body
    Debug.Assert swCopyBody.IsTemporaryBody

    ' Should not assert because it may fail to delete faces or fail local check or both
    bRet = swCopyBody.DeleteFaces5(vFaceArr, swHealAction_Shrink, swLoopProcess_Auto, True, vBodies, bLocChk): Debug.Assert bRet: Debug.Assert bLocChk

    Set swNewPart = swApp.NewDocument("C:\Documents and Settings\All Users\Application Data\SOLIDWORKS\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
    Set swNewModel = swNewPart
    Set swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyCheck): Debug.Assert Not swFeat Is Nothing

End Sub
```
