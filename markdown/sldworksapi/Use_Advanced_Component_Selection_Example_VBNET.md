---
title: "Use Advanced Component Selection Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Advanced_Component_Selection_Example_VBNET.htm"
---

# Use Advanced Component Selection Example (VB.NET)

This example shows how to:

- load an advanced selection component query file.
- select, add, delete, and save a selection criteria.

```
'-------------------------------------------------------
' Preconditions:
' 1. An assembly document is active.
' 2. A selection criteria query file named c:\temp\QueryMassLess.02.sqy
'    exists and contains one selection criteria.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Adds a selection criteria to c:\temp\QueryMassLess.02.sqy.
' 2. Deletes first selection criteria from c:\temp\QueryMassLess.02.sqy.
' 3. Saves selection criteria file c:\temp\QueryNewCriteria.sqy.
' 4. Examine the Immediate window and c:\temp.
'-------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim ModelDoc2 As ModelDoc2
        ModelDoc2 = swApp.ActiveDoc

        Dim DocType As Integer
        DocType = ModelDoc2.GetType

        If DocType <> swDocumentTypes_e.swDocASSEMBLY Then
            Debug.Print("An assembly document is not active")
            Exit Sub
        End If

        ModelDoc2.ClearSelection2(True)

        Dim AssemblyDoc As AssemblyDoc
        AssemblyDoc = ModelDoc2

        Dim AdvancedSelectionCriteria As AdvancedSelectionCriteria
        ' Get advanced component selection
        AdvancedSelectionCriteria = AssemblyDoc.GetAdvancedSelection

        Dim Count As Integer
        ' Get number of advanced component selections before loading a query
        ' Should be 0
        Count = AdvancedSelectionCriteria.GetItemCount
        Debug.Print("Before loading a query, GetItemCount returned " & Count)

        Dim CriteriaFileName As String
        ' Query file
        CriteriaFileName = "c:\temp\QueryMassLess.02.sqy"

        Dim LoadSuccess As Boolean
        ' Load query file
        LoadSuccess = AdvancedSelectionCriteria.LoadCriteria(CriteriaFileName)
        Debug.Print("Query " & CriteriaFileName & " load was" & IIf(LoadSuccess = False, " NOT ", " ") & "successful")
        ReportAllValues(AdvancedSelectionCriteria)
        Dim SelectSuccess As Boolean
        ' Select selection criteria from query list
        SelectSuccess = AdvancedSelectionCriteria.Select
        Debug.Print("Select was" & IIf(SelectSuccess = False, " NOT ", " ") & "successful")

        Dim AddRetVal As Integer
        ' Add selection criteria to query list
        AddRetVal = AdvancedSelectionCriteria.AddItem("Document name -- SW Special", &H4, "Gear", False)
        Debug.Print("AddItem returned " & AddRetVal)

        ' Print values of advanced component selection criteria
        ReportAllValues(AdvancedSelectionCriteria)

        ' Select first advanced component selection criteria
        SelectSuccess = AdvancedSelectionCriteria.Select
        Debug.Print("Select was" & IIf(SelectSuccess = False, " NOT ", " ") & "successful")
        Dim DeleteStatus As Boolean
        ' Delete first component selection criteria
        DeleteStatus = AdvancedSelectionCriteria.DeleteItem(0)
        Debug.Print("DeleteItem was" & IIf(DeleteStatus = False, " NOT ", " ") & "successful")

        ReportAllValues(AdvancedSelectionCriteria)
        Dim SaveStatus As Boolean
        ' Save query file
        SaveStatus = AdvancedSelectionCriteria.SaveCriteria("C:\temp\QueryNewCriteria.sqy") 'If wanted, need to specify extension
        Debug.Print("SaveCriteria was" & IIf(SaveStatus = False, " NOT ", " ") & "successful")

        ' Load query file that was just saved
        LoadSuccess = AdvancedSelectionCriteria.LoadCriteria("C:\temp\QueryNewCriteria.sqy")
        Debug.Print("Query " & "c:\temp\QueryNewCriteria.sqy" & " load was" & IIf(LoadSuccess = False, " NOT ", " ") & "successful")
        ' Print contents query file
        ReportAllValues(AdvancedSelectionCriteria)
    End Sub

    Function GetStringFromEnum(ByVal EnumVal As Integer) As String
        'From enum swAdvSelecType_e
        If EnumVal = 1 Then
            GetStringFromEnum = "And"
        ElseIf EnumVal = 2 Then
            GetStringFromEnum = "Or"
        ElseIf EnumVal = 16384 Then
            GetStringFromEnum = "is yes"
        ElseIf EnumVal = 32768 Then
            GetStringFromEnum = "is no"
        ElseIf EnumVal = 8 Then
            GetStringFromEnum = "is not"
        ElseIf EnumVal = 16 Then
            GetStringFromEnum = "contains"
        ElseIf EnumVal = 32 Then
            GetStringFromEnum = "Is_Contained_By"
        ElseIf EnumVal = 64 Then
            GetStringFromEnum = "Interferes_With"
        ElseIf EnumVal = 128 Then
            GetStringFromEnum = "Does_Not_Interferes_With"
        ElseIf EnumVal = 4 Then
            GetStringFromEnum = "is (exactly)"
        ElseIf EnumVal = 8192 Then
            GetStringFromEnum = "not ="
        ElseIf EnumVal = 512 Then
            GetStringFromEnum = "<"
        ElseIf EnumVal = 2048 Then
            GetStringFromEnum = "<="
        ElseIf EnumVal = 4096 Then
            GetStringFromEnum = "="
        ElseIf EnumVal = 1024 Then
            GetStringFromEnum = ">="
        ElseIf EnumVal = 256 Then
            GetStringFromEnum = ">"
        Else
            GetStringFromEnum = "Condition NOT found"
        End If
    End Function
    Sub ReportAllValues(ByVal AdvancedSelectionCriteria As AdvancedSelectionCriteria)
        Debug.Print("")

        Dim Count As Integer
        Count = AdvancedSelectionCriteria.GetItemCount
        Debug.Print("GetItemCount returned " & Count)

        Dim i As Integer
        Dim aProperty As String = ""
        Dim Condition As Integer
        Dim Value As String = ""
        Dim IsAnd As Boolean
        Dim Rindex As Integer
        Dim ConditionString As String
        Dim PrintString As String

        Dim IndexFmt As String
        Dim RindexFmt As String
        Dim AndOrFmt As String
        Dim PropertyFmt As String
        Dim ConditionFmt As String
        Dim ValueFmt As String
        IndexFmt = "!@@@@@@@@"
        RindexFmt = "!@@@@@@@@@"
        AndOrFmt = "!@@@@@@@@@"
        PropertyFmt = "!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        ConditionFmt = "!@@@@@@@@@@@@@@@"
        ValueFmt = "#.00"

        'Debug.Print
        PrintString = String.Format("Index", IndexFmt) & "     " & String.Format("Rindex", RindexFmt) & "  " & String.Format("And/Or", AndOrFmt) & "  " & String.Format("Property", PropertyFmt) & "                     " & String.Format("Condition", ConditionFmt) & "     " & String.Format("Value", ValueFmt)
        Debug.Print(PrintString)
        For i = 0 To Count - 1
            Rindex = AdvancedSelectionCriteria.GetItem(i, aProperty, Condition, Value, IsAnd)
            ConditionString = GetStringFromEnum(Condition)
            PrintString = String.Format(i, IndexFmt) & "         " & String.Format(Rindex, RindexFmt) & "       " & String.Format(IIf(IsAnd = False, "OR", "AND"), AndOrFmt) & "      " & String.Format(aProperty, PropertyFmt) & "  " & String.Format(ConditionString, ConditionFmt) & "  " & String.Format(Value, ValueFmt)
            Debug.Print(PrintString)
        Next i
        Debug.Print("")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
