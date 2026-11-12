---
title: "Delete Blended Faces Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Blended_Faces_Example_VBNET.htm"
---

# Delete Blended Faces Example (VB.NET)

This example shows how to delete blended faces.

NOTE: You can only delete blended faces from a temporary body.

```
'--------------------------------------------------
' Preconditions:
' 1. Open a part that contains one solid body
'    and at least one blended (fillet) face.
' 2. Select a blended face.
'
' Postconditions:
' 1. Creates a new part, which has the same body as
'    the original part, but the selected blended
'    face is removed.
' 2. Examine the graphics area.
'
' NOTE: It might not be possible to remove the
' selected blended face. If it's not removed, then
' the new body is the same as the original
' body.
'--------------------------------------------------
Option Explicit On

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        '   1 = Invisible
        '   0 = Visible
        Const CreateVisible As Integer = 0

        Const sAttDefName As String = "temp_attrib"
        Const sAttRootName As String = "temp"

        Dim swAttDef As AttributeDef
        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swPart As PartDoc
        Dim nSelCount As Integer
        Dim swFace As Face2
        Dim swEnt As Entity
        Dim swAtt() As SolidWorks.Interop.sldworks.Attribute
        Dim vFaceArr As Object
        Dim swFeat As Feature
        Dim vBodies As Object
        Dim swBody As Body2
        Dim swCopyBody As Body2
        Dim swNewPart As PartDoc
        Dim i As Integer
        Dim bRet As Boolean

        swAttDef = swApp.DefineAttribute(sAttDefName)
        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swPart = swModel
        bRet = swAttDef.Register

        ' Add attribute to selected faces
        nSelCount = swSelMgr.GetSelectedObjectCount
        ReDim swAtt(nSelCount)
        For i = 1 To nSelCount
            swFace = swSelMgr.GetSelectedObject6(i, -1)
            swEnt = swFace
            swAtt(i - 1) = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName & i, CreateVisible, swInConfigurationOpts_e.swAllConfiguration)
        Next i
        vBodies = swPart.GetBodies2(swBodyType_e.swAllBodies, False)
        swBody = vBodies(0)
        swCopyBody = swBody.Copy

        ' Remove attribute from faces
        For i = 1 To nSelCount
            bRet = swAtt(i - 1).Delete(True)

        Next i
        vFaceArr = GetFacesWithAttribute(swApp, swCopyBody, swAttDef)

        ' Can only delete blends from a temporary body
        Debug.Assert(swCopyBody.IsTemporaryBody)

        bRet = swCopyBody.DeleteBlends3(vFaceArr, True, True)
        swNewPart = swApp.NewPart
        swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)

    End Sub

    Public Function GetFacesWithAttribute(ByVal swApp As SldWorks, ByVal swBody As Body2, ByVal swAttDef As AttributeDef) As Object
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

            ' Only one instance of attribute should exist
            swAttCopy = swEnt.FindAttribute(swAttDef, 0)
            If Not swAttCopy Is Nothing Then
                swFaceArr(UBound(swFaceArr)) = swFace
                ReDim Preserve swFaceArr(UBound(swFaceArr) + 1)
            End If
            swFace = swFace.GetNextFace
        Loop
        ReDim Preserve swFaceArr(UBound(swFaceArr) - 1)
        GetFacesWithAttribute = swFaceArr
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>

    Public swApp As SldWorks

End Class
```
