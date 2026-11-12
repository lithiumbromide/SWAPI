---
title: "Get Mates Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mates_Example_VBNET.htm"
---

# Get Mates Example (VB.NET)

This example shows how to get all of the mates (IMate2 and IMateInPlace objects) for all components in an assembly.

```
'----------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\bladed shaft.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the components and mates.
' 2. Examine the Immediate window.
'-----------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro
    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swComponent As Component2
        Dim swAssembly As AssemblyDoc
        Dim Components As Object
        Dim SingleComponent As Object
        Dim Mates As Object
        Dim SingleMate As Object
        Dim swMate As Mate2
        Dim swMateInPlace As MateInPlace
        Dim numMateEntities As Integer
        Dim typeOfMate As Integer
        Dim i As Integer

        swModel = swApp.ActiveDoc
        swAssembly = swModel

        Components = swAssembly.GetComponents(False)
        For Each SingleComponent In Components
            swComponent = SingleComponent
            Debug.Print("Name of component: " & swComponent.Name2)
            Mates = swComponent.GetMates()
            If Not Mates Is Nothing Then
                For Each SingleMate In Mates
                    If TypeOf SingleMate Is SolidWorks.Interop.sldworks.Mate2 Then
                        swMate = SingleMate
                        typeOfMate = swMate.Type
                        Select Case typeOfMate
                            Case 0
                                Debug.Print("  Mate type: Coincident")
                            Case 1
                                Debug.Print("  Mate type: Concentric")
                            Case 2
                                Debug.Print("  Mate type: Perpendicular")
                            Case 3
                                Debug.Print("  Mate type: Parallel")
                            Case 4
                                Debug.Print("  Mate type: Tangent")
                            Case 5
                                Debug.Print("  Mate type: Distance")
                            Case 6
                                Debug.Print("  Mate type: Angle")
                            Case 7
                                Debug.Print("  Mate type: Unknown")
                            Case 8
                                Debug.Print("  Mate type: Symmetric")
                            Case 9
                                Debug.Print("  Mate type: CAM follower")
                            Case 10
                                Debug.Print("  Mate type: Gear")
                            Case 11
                                Debug.Print("  Mate type: Width")
                            Case 12
                                Debug.Print("  Mate type: Lock to sketch")
                            Case 13
                                Debug.Print("  Mate type: Rack pinion")
                            Case 14
                                Debug.Print("  Mate type: Max mates")
                            Case 15
                                Debug.Print("  Mate type: Path")
                            Case 16
                                Debug.Print("  Mate type: Lock")
                            Case 17
                                Debug.Print("  Mate type: Screw")
                            Case 18
                                Debug.Print("  Mate type: Linear coupler")
                            Case 19
                                Debug.Print("  Mate type: Universal joint")
                            Case 20
                                Debug.Print("  Mate type: Coordinate")
                            Case 21
                                Debug.Print("  Mate type: Slot")
                            Case 22
                                Debug.Print("  Mate type: Hinge") '
                                ' Add new mate types introduced after SOLIDWORKS 2010 FCS here
                        End Select
                    End If
                    If TypeOf SingleMate Is SolidWorks.Interop.sldworks.MateInPlace Then
                        swMateInPlace = SingleMate
                        numMateEntities = swMateInPlace.GetMateEntityCount
                        For i = 0 To numMateEntities - 1
                            Debug.Print("  Mate component name: " & swMateInPlace.MateComponentName(i))
                            Debug.Print("    Type of Inplace mate entity: " & swMateInPlace.MateEntityType(i))
                        Next i
                        Debug.Print("")
                    End If
                Next
            End If
            Debug.Print("")
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
