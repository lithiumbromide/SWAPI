---
title: "Create New Part from Existing Part Using Temporary Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_VBNET.htm"
---

# Create New Part from Existing Part Using Temporary Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Function GetFacesWithAttribute(ByVal swApp As SldWorks, ByVal swBody As Body2, ByVal swAttDef As AttributeDef) As Object

       Dim swFace As Face2
        Dim swEnt As Entity
        Dim swAttCopy As SolidWorks.Interop.sldworks.Attribute
        Dim swFaceArr() As Face2

        ' Search for faces on temporary body based on copied attributes
        ReDim swFaceArr(0)
        swFace = swBody.GetFirstFace
        Do While Not Nothing Is swFace
            swEnt = swFace
            swAttCopy = Nothing
            ' Only one instance of attribute on a face should exist
            swAttCopy = swEnt.FindAttribute(swAttDef, 0)
            If Not swAttCopy Is Nothing Then
                swFaceArr(UBound(swFaceArr)) = swFace
                ReDim Preserve swFaceArr(UBound(swFaceArr) + 1)
            End If
            swFace = swFace.GetNextFace
        Loop

        Debug.Assert(UBound(swFaceArr) >= 1)
        ReDim Preserve swFaceArr(UBound(swFaceArr) - 1)
        GetFacesWithAttribute = swFaceArr

    End Function

    Public Sub main()

        '   1 = invisible
        '   0 = visible
        Const CreateVisible As Long = 0
        Const sAttDefName As String = "temp_attrib"
        Const sAttRootName As String = "root_attrib"
        Dim swAttDef As AttributeDef
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swPart As PartDoc
        Dim swBody As Body2
        Dim swCopyBody As Body2
        Dim swSelMgr As SelectionMgr
        Dim nSelCount As Long
        Dim swFace As Face2
        Dim swEnt As Entity
        Dim swAtt() As SolidWorks.Interop.sldworks.Attribute
        Dim vFaceArr As Object
        Dim swNewPart As PartDoc
        Dim swNewModel As ModelDoc2
        Dim swFeat As Feature
        Dim vBodies As Object
        Dim boolstatus As Boolean
        Dim i As Long
        Dim bLocChk As Boolean
        Dim bRet As Boolean

        swAttDef = swApp.DefineAttribute(sAttDefName)
        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        swPart = swModel
        bRet = swAttDef.Register : Debug.Assert(bRet)
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
            swFace = swSelMgr.GetSelectedObject6(i, -1)
            swEnt = swFace
            swAtt(i - 1) = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName & i, CreateVisible, swInConfigurationOpts_e.swAllConfiguration) : Debug.Assert(Not swAtt(i - 1) Is Nothing)
        Next i

        vBodies = swPart.GetBodies2(swBodyType_e.swAllBodies, True)
        swBody = vBodies(0)
        swCopyBody = swBody.Copy

        ' Remove attribute from faces
        For i = 1 To nSelCount
            bRet = swAtt(i - 1).Delete(True) : Debug.Assert(bRet)
        Next i

        vFaceArr = GetFacesWithAttribute(swApp, swCopyBody, swAttDef)
        Debug.Assert(nSelCount = UBound(vFaceArr) + 1)

        ' Can only delete faces from a temporary body
        Debug.Assert(swCopyBody.IsTemporaryBody)

        ' Should not assert because it may fail to delete faces or fail local check or both
        bRet = swCopyBody.DeleteFaces5(vFaceArr, swHealActionType_e.swHealAction_Shrink, swLoopProcessOption_e.swLoopProcess_Auto, True, vBodies, bLocChk) : Debug.Assert(bRet) : Debug.Assert(bLocChk)
        swNewPart = swApp.NewDocument("C:\Documents and Settings\All Users\Application Data\SOLIDWORKS\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
        swNewModel = swNewPart
        swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck) : Debug.Assert(Not swFeat Is Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
