---
title: "Get Faces Associated with Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Associated_with_Feature_Example_VBNET.htm"
---

# Get Faces Associated with Feature Example (VB.NET)

This example shows how to eliminate multiple feature faces.

**NOTE:** In SOLIDWORKS Design, a face is the result of evaluating a feature. A face can be owned by several features. IFeature::GetFaces returns all faces owned by a feature. This is different from faces highlighted in the user interface when a feature is selected, because the user interface filters out multiple feature faces. This filter is for display purposes only. An application must use IFace::GetFeature to filter out multiple feature faces. This method returns only the oldest feature from a face; that is, the first owning feature in the FeatureManager design tree.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Select a feature in the FeatureManager design
'    tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the feature and number
'    of faces.
' 2. Colors the faces of the feature blue.
'    NOTE: The faces are the same faces as if
'    you selected the feature in the user interface.
' 3. Examine the Immediate window and graphics area.
'-----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swSelData As SelectData
        Dim swFeat As Feature
        Dim swFaceFeat As Feature
        Dim faceArr As Object
        Dim oneFace As Object
        Dim featColors As Object
        Dim swFace As Face2
        Dim swEnt As Entity
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swSelData = swSelMgr.CreateSelectData
        Debug.Print("Feature = " + swFeat.Name + " [" + swFeat.GetTypeName + "]")
        Debug.Print("  Face count = " & swFeat.GetFaceCount)
        swModel.ClearSelection2(True)
        featColors = swModel.MaterialPropertyValues
        featColors(0) = 0  'R
        featColors(1) = 0  'G
        featColors(2) = 1  'B
        faceArr = swFeat.GetFaces : If IsNothing(faceArr) Then Exit Sub
        For Each oneFace In faceArr
            swFace = oneFace
            swEnt = swFace
            swFaceFeat = swFace.GetFeature
            ' Check to see if face is owned by multiple features
            If swFaceFeat Is swFeat Then
                status = swEnt.Select4(True, swSelData) : Debug.Assert(status)
                swFace.MaterialPropertyValues = featColors
            Else
                Debug.Print("  Other feature = " & swFaceFeat.Name + " [" + swFaceFeat.GetTypeName + "]")
            End If
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
