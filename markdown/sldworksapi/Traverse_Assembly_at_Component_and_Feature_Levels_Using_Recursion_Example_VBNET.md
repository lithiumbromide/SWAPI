---
title: "Traverse Assembly at Component and Feature Levels Using Recursion Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm"
---

# Traverse Assembly at Component and Feature Levels Using Recursion Example (VB.NET)

This example shows how to traverse an assembly at the component and feature levels using recursion.

```
'-------------------------------------------
' Preconditions:
' 1. Open an assembly document containing nested subassemblies.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the assembly.
' 2. Examine the Immediate window.
'-------------------------------------------

Option Explicit On

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Diagnostics.Stopwatch

Partial Class SolidWorksMacro

    Sub TraverseFeatureFeatures(ByVal swFeat As Feature, ByVal nLevel As Long)
        Dim swSubFeat As Feature
        Dim swSubSubFeat As Feature
        Dim swSubSubSubFeat As Feature
        Dim sPadStr As String = " "
        Dim i As Long

        For i = 0 To nLevel
            sPadStr = sPadStr + "  "
        Next i

        While Not swFeat Is Nothing
            Debug.Print(sPadStr + swFeat.Name + " [" + swFeat.GetTypeName2 + "]")
            swSubFeat = swFeat.GetFirstSubFeature

            While Not swSubFeat Is Nothing
                Debug.Print(sPadStr + "  " + swSubFeat.Name + " [" + swSubFeat.GetTypeName + "]")
                swSubSubFeat = swSubFeat.GetFirstSubFeature

                While Not swSubSubFeat Is Nothing
                    Debug.Print(sPadStr + "    " + swSubSubFeat.Name + " [" + swSubSubFeat.GetTypeName + "]")
                    swSubSubSubFeat = swSubSubFeat.GetFirstSubFeature

                    While Not swSubSubSubFeat Is Nothing
                        Debug.Print(sPadStr + "      " + swSubSubSubFeat.Name + " [" + swSubSubSubFeat.GetTypeName + "]")
                        swSubSubSubFeat = swSubSubSubFeat.GetNextSubFeature()

                    End While

                    swSubSubFeat = swSubSubFeat.GetNextSubFeature()

                End While

                swSubFeat = swSubFeat.GetNextSubFeature()

            End While

            swFeat = swFeat.GetNextFeature

        End While

    End Sub

    Sub TraverseComponentFeatures(ByVal swComp As Component2, ByVal nLevel As Long)
        Dim swFeat As Feature

        swFeat = swComp.FirstFeature
        TraverseFeatureFeatures(swFeat, nLevel)

    End Sub
    Sub TraverseComponent(ByVal swComp As Component2, ByVal nLevel As Long)
        Dim vChildComp As Object
        Dim swChildComp As Component2
        Dim sPadStr As String = " "
        Dim i As Long

        For i = 0 To nLevel - 1
            sPadStr = sPadStr + "  "
        Next i

        vChildComp = swComp.GetChildren
        For i = 0 To UBound(vChildComp)
            swChildComp = vChildComp(i)

            Debug.Print(sPadStr & "+" & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & ">")

            TraverseComponentFeatures(swChildComp, nLevel)
            TraverseComponent(swChildComp, nLevel + 1)

        Next i

    End Sub
    Sub TraverseModelFeatures(ByVal swModel As ModelDoc2, ByVal nLevel As Long)
        Dim swFeat As Feature

        swFeat = swModel.FirstFeature
        TraverseFeatureFeatures(swFeat, nLevel)

    End Sub
    Public Sub main()

        Dim swApp As SldWorks
        Dim swModel As ModelDoc2
        Dim swConfMgr As ConfigurationManager
        Dim swConf As Configuration
        Dim swRootComp As Component2
        Dim StartTime As Double
        Dim FinishTime As Double
        Dim TotalTime As Double

        swApp = CreateObject("SldWorks.Application")
        swModel = swApp.ActiveDoc
        swConfMgr = swModel.ConfigurationManager
        swConf = swConfMgr.ActiveConfiguration
        swRootComp = swConf.GetRootComponent3(True)
        StartTime = Timer ' Start time
        Debug.Print("File = " & swModel.GetPathName)
        TraverseModelFeatures(swModel, 1)

        If swModel.GetType = swDocumentTypes_e.swDocASSEMBLY Then
            TraverseComponent(swRootComp, 1)

        End If

        FinishTime = Timer ' End time
        TotalTime = FinishTime - StartTime ' Elapsed time
        Debug.Print("Time = " & TotalTime & " sec")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
