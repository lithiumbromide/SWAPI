---
title: "Get Blocks Data in Any Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Blocks_Data_in_Any_Document_Example_VB.htm"
---

# Get Blocks Data in Any Document Example (VBA)

This example shows how to get blocks data in part, assembly, and drawing documents.

```vb
'--------------------------------
'
' Preconditions: Part, assembly, or drawing document containing
'                one or more block definitions
'                and block instances is open.
'
' Postconditions: None
'
'---------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim skMgr As SldWorks.SketchManager
Dim pBlock As SldWorks.SketchBlockDefinition
Dim pInst As SldWorks.SketchBlockInstance
Dim leaderPt As SldWorks.MathPoint
Dim insPt As SldWorks.MathPoint
Dim vInstPt As Variant
Dim vInstances As Variant
Dim vBlocks As Variant
Dim nInstanceCount As Long
Dim itr As Long
Dim jtr As Long
Dim bLinkToFile As Boolean
Dim strInsPoint As String

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set skMgr = swModel.SketchManager

    vBlocks = skMgr.GetSketchBlockDefinitions

    ' Exit if no blocks
    If IsEmpty(vBlocks) Then
        Exit Sub
    End If

    ' Process block definitions
    For itr = 0 To UBound(vBlocks)

        Set pBlock = vBlocks(itr)

        ' Block defintion linked to file?
        Debug.Print "   Link To File = " & pBlock.LinkToFile

        ' Block linked file name
        Debug.Print "   Link File Name = " & pBlock.FileName

        ' Block definition insertion point
        Set insPt = pBlock.InsertionPoint
        vInstPt = insPt.ArrayData
        strInsPoint = "   Insertion point: x = " + CStr(vInstPt(0) * 1000) + " , y = " + CStr(vInstPt(1) * 1000) + " , z = " + CStr(vInstPt(2) * 1000)
        Debug.Print strInsPoint

        ' Number of block instances of this block definition
        nInstanceCount = pBlock.GetInstanceCount
        Debug.Print "   Instance Count = " & nInstanceCount

        ' Process block instances
        If nInstanceCount > 0 Then
            vInstances = pBlock.GetInstances
            For jtr = 0 To UBound(vInstances)
                Set pInst = vInstances(jtr)

                ' Block instance position
                Set insPt = pInst.InstancePosition
                vInstPt = insPt.ArrayData
                strInsPoint = "        Instance position: x = " + CStr(vInstPt(0) * 1000) + " , y = " + CStr(vInstPt(1) * 1000) + " , z = " + CStr(vInstPt(2) * 1000)
                Debug.Print strInsPoint

                ' Block instance angle
                Debug.Print "        Angle = " & pInst.Angle

                ' Block instance scale
                Debug.Print "        Scale = " & pInst.Scale

                ' Block instance owner's sketch name
                Debug.Print "        Owner Sketch = " & pInst.GetSketch.Name

            Next jtr
        End If

    Next itr

End Sub
```
