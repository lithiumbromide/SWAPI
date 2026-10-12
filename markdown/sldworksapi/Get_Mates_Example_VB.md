---
title: "Get Mates Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mates_Example_VB.htm"
---

# Get Mates Example (VBA)

This example shows how to get all of the mates (IMate2 and IMateInPlace objects) in an assembly document.

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
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swComponent As SldWorks.Component2
Dim swAssembly As SldWorks.AssemblyDoc
Dim Components As Variant
Dim SingleComponent As Variant
Dim Mates As Variant
Dim SingleMate As Variant
Dim swMate As SldWorks.Mate2
Dim swMateInPlace As SldWorks.MateInPlace
Dim numMateEntities As Long
Dim typeOfMate As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel
```

```
    Components = swAssembly.GetComponents(False)
    For Each SingleComponent In Components
        Set swComponent = SingleComponent
        Debug.Print "Name of component: " & swComponent.Name2
        Mates = swComponent.GetMates()
        If (Not IsEmpty(Mates)) Then
            For Each SingleMate In Mates
                If TypeOf SingleMate Is SldWorks.Mate2 Then
                    Set swMate = SingleMate
                    typeOfMate = swMate.Type
                    Select Case typeOfMate
                        Case 0
                            Debug.Print "  Mate type: Coincident"
                        Case 1
                            Debug.Print "  Mate type: Concentric"
                        Case 2
                            Debug.Print "  Mate type: Perpendicular"
                        Case 3
                            Debug.Print "  Mate type: Parallel"
                        Case 4
                            Debug.Print "  Mate type: Tangent"
                        Case 5
                            Debug.Print "  Mate type: Distance"
                        Case 6
                            Debug.Print "  Mate type: Angle"
                        Case 7
                            Debug.Print "  Mate type: Unknown"
                        Case 8
                            Debug.Print "  Mate type: Symmetric"
                        Case 9
                            Debug.Print "  Mate type: CAM follower"
                        Case 10
                            Debug.Print "  Mate type: Gear"
                        Case 11
                            Debug.Print "  Mate type: Width"
                        Case 12
                            Debug.Print "  Mate type: Lock to sketch"
                        Case 13
                            Debug.Print "  Mate type: Rack pinion"
                        Case 14
                            Debug.Print "  Mate type: Max mates"
                        Case 15
                            Debug.Print "  Mate type: Path"
                        Case 16
                            Debug.Print "  Mate type: Lock"
                        Case 17
                            Debug.Print "  Mate type: Screw"
                        Case 18
                            Debug.Print "  Mate type: Linear coupler"
                        Case 19
                            Debug.Print "  Mate type: Universal joint"
                        Case 20
                            Debug.Print "  Mate type: Coordinate"
                        Case 21
                            Debug.Print "  Mate type: Slot"
                        Case 22
                            Debug.Print "  Mate type: Hinge"
                        ' Add new mate types introduced after SOLIDWORKS 2010 FCS here
                    End Select
                End If
                If TypeOf SingleMate Is SldWorks.MateInPlace Then
                    Set swMateInPlace = SingleMate
                    numMateEntities = swMateInPlace.GetMateEntityCount
                    For i = 0 To numMateEntities - 1
                        Debug.Print "  Mate component name: " & swMateInPlace.MateComponentName(i)
                        Debug.Print "    Type of Inplace mate entity: " & swMateInPlace.MateEntityType(i)
                    Next i
                End If
            Next
        End If
        Debug.Print ""
    Next
```

```
End Sub
```
