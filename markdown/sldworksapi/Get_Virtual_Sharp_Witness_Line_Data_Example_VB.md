---
title: "Get Virtual Sharp Witness Line Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Virtual_Sharp_Witness_Line_Data_Example_VB.htm"
---

# Get Virtual Sharp Witness Line Data Example (VBA)

This example shows how to get the geometry data of all of the virtual sharp witness lines in a drawing.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open the drawing of a part that contains one or more
 ' virtual sharps with witness lines.
 '
 ' Postconditions: Inspect the Immediate Window for virtual sharp witness line
 ' geometry data.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim pDrawing As SldWorks.DrawingDoc
 Dim swView As SldWorks.View
 Dim Count As Long
 Dim size As Long
 Dim entitiesData  As Variant
 Dim index As Long
 Dim entityCounts As Long
 Dim entType As Long
 Dim linesCount As Long
 Dim arcsCount As Long
 Dim VirtualSharpNum As Long
 Dim j As Long
Option Explicit
Sub main()
     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set pDrawing = swModel

    Set swView = pDrawing.GetFirstView
     While Not swView Is Nothing

       Debug.Print "Drawing view: "; swView.Name

       Count = swView.GetWitnessEntitiesCount(size)

       Debug.Print "  Number of virtual sharp witness lines: "; Count
        Debug.Print "  Size of virtual sharp witness line geometry data array: "; size

       If (Count > 0) Then
             entitiesData = swView.GetWitnessGeomInfo

            If Not IsEmpty(entitiesData) Then
                 VirtualSharpNum = 0
                 index = 0
                 entityCounts = 0
                 While entityCounts < Count - 1
                     Debug.Print "    Virtual sharp "; VirtualSharpNum
                     Debug.Print "      Color: "; entitiesData(index)
                     index = index + 1
                     Debug.Print "      Line style (swLineStyles_e): "; entitiesData(index)
                     index = index + 1
                     Debug.Print "      Line weight: (swLineWeights_e): "; entitiesData(index)
                     index = index + 1
                     Debug.Print "      Layer ID: "; entitiesData(index)
                     index = index + 1
                     Debug.Print "      Layer override (swLayerOverride_e):"; entitiesData(index)
                     index = index + 1

                    entType = entitiesData(index)
                     Debug.Print "      Entity type: "; entType
                     If (entType = 0) Then
                         index = index + 1
                         linesCount = entitiesData(index)
                         Debug.Print "      Line count: "; linesCount
                         index = index + 1

                        For j = 0 To linesCount - 1
                             Debug.Print "        Start: x ="; entitiesData(index); " y ="; entitiesData(index + 1); " z ="; entitiesData(index + 2)
                             index = index + 3
                             Debug.Print "        End:   x ="; entitiesData(index); " y ="; entitiesData(index + 1); " z ="; entitiesData(index + 2)
                             index = index + 3
                         Next j
                         entityCounts = entityCounts + linesCount
                     End If

                    entType = entitiesData(index)
                     Debug.Print "      Entity type: "; entType
                     If (entType = 1) Then
                         index = index + 1
                         arcsCount = entitiesData(index)
                         Debug.Print "      Arc count: "; arcsCount
                         index = index + 1

                        For j = 0 To arcsCount - 1
                             Debug.Print "        Start:  x ="; entitiesData(index); " y ="; entitiesData(index + 1); " z ="; entitiesData(index + 2)
                             index = index + 3
                             Debug.Print "        End:    x ="; entitiesData(index); " y ="; entitiesData(index + 1); " z ="; entitiesData(index + 2)
                             index = index + 3
                             Debug.Print "        Center: x ="; entitiesData(index); " y ="; entitiesData(index + 1); " z ="; entitiesData(index + 2)
                             index = index + 3
                             Debug.Print "        Normal: x ="; entitiesData(index); " y ="; entitiesData(index + 1); " z ="; entitiesData(index + 2)
                             index = index + 3
                         Next j

                        entityCounts = entityCounts + arcsCount

                    End If

                    VirtualSharpNum = VirtualSharpNum + 1

                Wend

            End If
        End If

        Set swView = swView.GetNextView

     Wend

End Sub
```
