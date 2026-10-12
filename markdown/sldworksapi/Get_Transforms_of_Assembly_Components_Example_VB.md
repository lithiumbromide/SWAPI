---
title: "Get Transforms of Assembly Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transforms_of_Assembly_Components_Example_VB.htm"
---

# Get Transforms of Assembly Components Example (VBA)

This example shows how to recursively retrieve the transform for each child component in an assembly.

```vb
'-----------------------------------------------
'
' Preconditions:
'       (1) Assembly is open.
'       (2) Assembly is fully resolved.
'
' Postconditions: None
'
' Notes:
'       (1) Root component does not have a name
'
'       (2) Root component has a NULL transform, that is, no rotation,
'           translation, or scaling
'
'       (3) All child component transforms are relative to their
'           root component
'
'-----------------------------------------------
Option Explicit
Sub OutputCompXform
    swComp As SldWorks.Component2
    nLevel As Long

    Dim vChild                      As Variant
    Dim swChildComp                 As SldWorks.Component2
    Dim sPadStr                     As String
    Dim swCompXform                 As SldWorks.MathTransform
    Dim vXform                      As Variant
    Dim i                           As Long

    For i = 0 To nLevel
        sPadStr = sPadStr & "  "
    Next i

    ' Null for root component
    Set swCompXform = swComp.Transform2
    If Not swCompXform Is Nothing Then
        vXform = swCompXform.ArrayData

        ' Root component has no name
        Debug.Print sPadStr & "Component = " & swComp.Name2 & " (" & swComp.ReferencedConfiguration & ")"
        Debug.Print sPadStr & "  Suppr   = " & swComp.IsSuppressed
        Debug.Print sPadStr & "  Hidden  = " & swComp.IsHidden(False)

        Debug.Print sPadStr & "  Rot1  = (" + Str(vXform(0)) + ", " + Str(vXform(1)) + ", " + Str(vXform(2)) + ")"

        Debug.Print sPadStr & "  Rot2  = (" +  Str(vXform(3)) + ", " + Str(vXform(4)) + ", " + Str(vXform(5)) + ")"

        Debug.Print sPadStr & "  Rot3  = (" + Str(vXform(6)) + ", " + Str(vXform(7)) + ", " + Str(vXform(8)) + ")"

        Debug.Print sPadStr & "  Trans = (" + Str(vXform(9)) + ", " + Str(vXform(10)) + ", " + Str(vXform(11)) + ")"

        Debug.Print sPadStr & "  Scale = " + Str(vXform(12))

        Debug.Print ""
    End If

    ' Recurse into subassembly
    vChild = swComp.GetChildren
    For i = 0 To UBound(vChild)
        Set swChildComp = vChild(i)

        OutputCompXform swChildComp, nLevel + 1
    Next i
End Sub
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swConf                      As SldWorks.configuration
    Dim swRootComp                  As SldWorks.Component2
    Dim bRet                        As Boolean

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swConf = swModel.GetActiveConfiguration
    Set swRootComp = swConf.GetRootComponent

    Debug.Print "File = " & swModel.GetPathName

    OutputCompXform swRootComp, 0
End Sub
'---------------------------------------
```
