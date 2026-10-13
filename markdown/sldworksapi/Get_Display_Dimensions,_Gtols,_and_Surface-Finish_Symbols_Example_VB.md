---
title: "Get Display Dimensions, Gtols, and Surface-Finish Symbols Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm"
---

# Get Display Dimensions, Gtols, and Surface-Finish Symbols Example (VBA)

## Get Display Dimensions, GTols, and Surface-Finish Symbols Example (VBA)

This example shows how to get all of the annotations in a part, assembly, or drawing.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing document.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Prints any annotations to the Immediate window.
' 2. Examine the Immediate window.
'-----------------------------------------------
```

```
Option Explicit
```

```
Sub ProcessAnnotation(swApp As SldWorks.SldWorks, swAnn As SldWorks.Annotation)
    Dim swAnnCThread                As SldWorks.CThread
    Dim swAnnDatumTag               As SldWorks.DatumTag
    Dim swAnnDatumTargetSym         As SldWorks.DatumTargetSym
    Dim swAnnDisplayDimension       As SldWorks.DisplayDimension
    Dim swAnnGTol                   As SldWorks.Gtol
    Dim swAnnNote                   As SldWorks.Note
    Dim swAnnSFSymbol               As SldWorks.SFSymbol
    Dim swAnnWeldSymbol             As SldWorks.WeldSymbol
    Dim swAnnCustomSymbol           As SldWorks.CustomSymbol
    Dim swAnnDowelSym               As SldWorks.DowelSymbol
    Dim swAnnLeader                 As SldWorks.MultiJogLeader
    Dim swAnnCenterMarkSym          As SldWorks.CenterMark
    Dim swAnnTable                  As SldWorks.TableAnnotation
    Dim swAnnCenterLine             As SldWorks.Centerline
    Dim swAnnDatumOrigin            As SldWorks.DatumOrigin
```

```
    Select Case swAnn.GetType
        Case swCThread
            Set swAnnCThread = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swCThread"
            Debug.Print ""
        Case swDatumTag
            Set swAnnDatumTag = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swDatumTag"
            Debug.Print ""
        Case swDatumTargetSym
            Set swAnnDatumTargetSym = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swDatumTargetSym"
            Debug.Print ""
        Case swDisplayDimension
            Set swAnnDisplayDimension = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swDisplayDimension"
            Debug.Print ""
        Case swGTol
            Set swAnnGTol = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swGTol"
            Debug.Print ""
        Case swNote
            Set swAnnNote = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swNote"
            Debug.Print ""
        Case swSFSymbol
            Set swAnnSFSymbol = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swSFSymbol"
            Debug.Print ""
        Case swWeldSymbol
            Set swAnnWeldSymbol = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swWeldSymbol"
            Debug.Print ""
        Case swCustomSymbol
            Set swAnnCustomSymbol = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swCustomSymbol"
            Debug.Print ""
        Case swDowelSym
            Set swAnnDowelSym = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swDowelSym"
            Debug.Print ""
        Case swLeader
            Set swAnnLeader = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swLeader"
            Debug.Print ""
        Case swCenterMarkSym
            Set swAnnCenterMarkSym = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swCenterMarkSym"
            Debug.Print ""
        Case swTableAnnotation
            Set swAnnTable = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swTableAnnotation"
            Debug.Print ""
        Case swCenterLine
            Set swAnnCenterLine = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swCenterLine"
            Debug.Print ""
        Case swDatumOrigin
            Set swAnnDatumOrigin = swAnn.GetSpecificAnnotation
            Debug.Print "  Annotation type (enumerator): swAnnotationType_e.swDatumOrigin"
            Debug.Print ""
        Case Else
            Debug.Print "  Unknown annotation type"
            Debug.Print ""
            Debug.Assert False
    End Select
```

```
End Sub
```

```
Sub ProcessModel(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2)
    Dim swAnn                       As SldWorks.Annotation
    Dim nNumLeader                  As Long
    Dim nNumPts                     As Long
    Dim vLeaderPt                   As Variant
    Dim i                           As Long
    Dim j                           As Long
    Dim k                           As Long
    Dim bRet                        As Boolean
```

```
    Debug.Print "Model path and file name: " & swModel.GetPathName
    Debug.Print ""
    Set swAnn = swModel.GetFirstAnnotation2
```

```
    Do While Not swAnn Is Nothing
        Debug.Print "  Annotation name: " & swAnn.GetName
        Debug.Print "  Annotation type (enumerator numeric value): " & swAnn.GetType
```

```
        If True = swAnn.GetLeader Then
        Dim nbrLeaders As Long
        nbrLeaders = swAnn.GetLeaderCount
            For i = 0 To swAnn.GetLeaderCount - 1
                If True = swAnn.GetBentLeader Then
                    nNumPts = 3
                Else
                    nNumPts = 2
                End If
```

```
                vLeaderPt = swAnn.GetLeaderPointsAtIndex(i)
                If Not IsEmpty(vLeaderPt) Then
                    Dim leaderPt() As Double
                    ReDim leaderPt(nNumPts) As Double
                    leaderPt = vLeaderPt
                    k = 0
                    For j = 0 To UBound(leaderPt)
                        Debug.Print "    Pt[" & k & "] x,y,z coordinates:"
                        Debug.Print "       " & Str(leaderPt(j)) & ", " & Str(leaderPt(j + 1)) & Str(leaderPt(j + 2))
                        j = j + 2
                        k = k + 1
                    Next j
```

```
                End If
            Next i
```

```
        End If
```

```
        ProcessAnnotation swApp, swAnn
```

```
      Set swAnn = swAnn.GetNext3
```

```
    Loop
```

```
End Sub
```

```
Sub ProcessComponent(swApp As SldWorks.SldWorks, swComp As SldWorks.Component2)
    Dim vChildArray             As Variant
    Dim swChildComp             As SldWorks.Component2
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swPart                  As SldWorks.PartDoc
    Dim i                       As Long
```

```
    vChildArray = swComp.GetChildren
```

```
    For i = 0 To UBound(vChildArray)
        Set swChildComp = vChildArray(i)
        ProcessComponent swApp, swChildComp
    Next i
```

```
    Set swModel = swComp.GetModelDoc
```

```
    If Not swModel Is Nothing Then
        If swDocPART = swModel.GetType Then
            ProcessModel swApp, swModel
        End If
```

```
    End If
```

```
End Sub
```

```
Sub ProcessDrawing(swApp As SldWorks.SldWorks, swDraw As SldWorks.DrawingDoc)
    Dim swView As SldWorks.View
    Dim swAnn As SldWorks.Annotation
```

```
    Set swView = swDraw.GetFirstView
    Do While Not Nothing Is swView
        Set swAnn = swView.GetFirstAnnotation3
        Do While Not Nothing Is swAnn
            ProcessAnnotation swApp, swAnn
            Set swAnn = swAnn.GetNext3
        Loop
```

```
        Set swView = swView.GetNextView
```

```
    Loop
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swAssy                      As SldWorks.AssemblyDoc
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swConfig                    As SldWorks.Configuration
    Dim swConfigMgr                 As SldWorks.ConfigurationManager
    Dim swRootComp                  As SldWorks.Component2
    Dim nStatus                     As Long
    Dim bRet                        As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Select Case swModel.GetType
        Case swDocPART
            ProcessModel swApp, swModel
        Case swDocASSEMBLY
            Set swAssy = swModel
            nStatus = swAssy.ResolveAllLightWeightComponents(False)
            Set swConfigMgr = swModel.ConfigurationManager
            Set swConfig = swConfigMgr.ActiveConfiguration
            Set swRootComp = swConfig.GetRootComponent
            ProcessComponent swApp, swRootComp
        Case swDocDRAWING
            Set swDraw = swModel
            ProcessDrawing swApp, swDraw
        Case Else
            Exit Sub
```

```
    End Select
```

```
End Sub
```
