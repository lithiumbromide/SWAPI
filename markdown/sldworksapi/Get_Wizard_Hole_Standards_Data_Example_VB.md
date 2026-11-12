---
title: "Get Hole Standards Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Wizard_Hole_Standards_Data_Example_VB.htm"
---

# Get Hole Standards Data Example (VBA)

This example shows how to retrieve hole standards data from the Hole Wizard database.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Open SOLIDWORKS Design.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Retrieves row 1 data from all three Binding Head Screw fastener tables
' of the ANSI Inch hole standard.
' 2. Inspect the Immediate window.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim holeStandards As SldWorks.HoleStandardsData
 Dim fastenerData As SldWorks.HoleDataTable
 Dim ret As Boolean
 Dim indexes As Variant
 Dim standards As Variant
 Dim fastenerIDs As Variant
 Dim fastenerNames As Variant
 Dim fastenerTableTypeIDs As Variant
 Dim columnNames As Variant
 Dim cellData As String
 Dim i As Long
 Dim j As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set holeStandards = swApp.GetHoleStandardsData(swWzdCounterBore)
     ret = holeStandards.GetHoleStandards(indexes, standards)
     ret = holeStandards.GetFastenerTypes(standards(0), fastenerIDs, fastenerNames)
     ret = holeStandards.GetFastenerTableTypes(standards(0), fastenerIDs(0), fastenerTableTypeIDs)
     For j = 0 To 2
         ret = holeStandards.GetFastenerTable(standards(0), fastenerIDs(0), fastenerTableTypeIDs(j), fastenerData)
         Debug.Print ""
         If j = 0 Then
             Debug.Print "Hole Wizard standard: " & fastenerData.StandardName
             Debug.Print "Fastener ID: " & fastenerData.FastenerID
             Debug.Print "Fastener: " & fastenerNames(0)
         End If

        Debug.Print "Fastener table type ID as defined in swFastenerTableTypes_e: " & fastenerData.TableTypeID

        ret = fastenerData.GetColumnNames(columnNames)
         If j = 0 Then
             Debug.Print "Size data in Row #1"
         ElseIf j = 1 Then
             Debug.Print "Thread data in Row #1"
         ElseIf j = 2 Then
             Debug.Print "Screw clearances data in Row #1"
         End If

        For i = 0 To UBound(columnNames)
             ret = fastenerData.GetCellData(columnNames(i), 0, cellData)
             Debug.Print columnNames(i) & ": " & cellData
         Next i
     Next j
 End Sub
```
