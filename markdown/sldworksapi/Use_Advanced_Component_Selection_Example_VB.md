---
title: "Use Advanced Component Selection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Advanced_Component_Selection_Example_VB.htm"
---

# Use Advanced Component Selection Example (VBA)

This example shows how to:

- load an advanced selection component query file.
- select, add, delete, and save a selection criteria.

```vb
'-------------------------------------------------------
 ' Preconditions:
 ' 1. An assembly document is active.
 ' 2. A selection criteria query file named  c:\temp\QueryMassLess.02.sqy
 '    exists and contains one selection criteria.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Adds a selection criteria to c:\temp\QueryMassLess.02.sqy.
 ' 2. Deletes first selection criteria from c:\temp\QueryMassLess.02.sqy.
 ' 3. Saves selection criteria file c:\temp\QueryNewCriteria.sqy.
 ' 4. Examine the Immediate window and c:\temp.
 '-------------------------------------------------------
Option Explicit

Sub main()
    Dim swAppSldWorks As SldWorks.SldWorks
    Set swAppSldWorks = Application.SldWorks

    Dim ModelDoc2 As SldWorks.ModelDoc2
    Set ModelDoc2 = swAppSldWorks.ActiveDoc

    Dim DocType As Long
    DocType = ModelDoc2.GetType

    If DocType <> swDocASSEMBLY Then
        Debug.Print "An assembly document is not active"
        Exit Sub
    End If

    ModelDoc2.ClearSelection2 True

    Dim AssemblyDoc As SldWorks.AssemblyDoc
    Set AssemblyDoc = ModelDoc2

    Dim AdvancedSelectionCriteria As SldWorks.AdvancedSelectionCriteria
    ' Get advanced component selection
    Set AdvancedSelectionCriteria = AssemblyDoc.GetAdvancedSelection

    Dim Count As Long
    ' Get number of advanced component selections before loading a query
    ' Should be 0
    Count = AdvancedSelectionCriteria.GetItemCount
    Debug.Print "Before loading a query, GetItemCount returned " & Count

    Dim CriteriaFileName As String
    ' Query file
    CriteriaFileName = "c:\temp\QueryMassLess.02.sqy"

    Dim LoadSuccess As Boolean
    ' Load query file
    LoadSuccess = AdvancedSelectionCriteria.LoadCriteria(CriteriaFileName)
    Debug.Print "Query " & CriteriaFileName & " load was" & IIf(LoadSuccess = False, " NOT ", " ") & "successful"
    ReportAllValues AdvancedSelectionCriteria
    Dim SelectSuccess As Boolean
    ' Select selection criteria from query list
    SelectSuccess = AdvancedSelectionCriteria.Select
    Debug.Print "Select was" & IIf(SelectSuccess = False, " NOT ", " ") & "successful"

    Dim AddRetVal As Long
    ' Add selection criteria to query list
    AddRetVal = AdvancedSelectionCriteria.AddItem("Document name -- SW Special", &H4, "Gear", False)
    Debug.Print "AddItem returned " & AddRetVal

    ' Print values of advanced component selection criteria
    ReportAllValues AdvancedSelectionCriteria

    ' Select first advanced component selection criteria
    SelectSuccess = AdvancedSelectionCriteria.Select
    Debug.Print "Select was" & IIf(SelectSuccess = False, " NOT ", " ") & "successful"
    Dim DeleteStatus As Boolean
    ' Delete first component selection criteria
    DeleteStatus = AdvancedSelectionCriteria.DeleteItem(0)
    Debug.Print "DeleteItem was" & IIf(DeleteStatus = False, " NOT ", " ") & "successful"

    ReportAllValues AdvancedSelectionCriteria
    Dim SaveStatus As Boolean
    ' Save query file
    SaveStatus = AdvancedSelectionCriteria.SaveCriteria("C:\temp\QueryNewCriteria.sqy") 'If wanted, need to specify extension
    Debug.Print "SaveCriteria was" & IIf(SaveStatus = False, " NOT ", " ") & "successful"

    ' Load query file that was just saved
    LoadSuccess = AdvancedSelectionCriteria.LoadCriteria("C:\temp\QueryNewCriteria.sqy")
    Debug.Print "Query " & "c:\temp\QueryNewCriteria.sqy" & " load was" & IIf(LoadSuccess = False, " NOT ", " ") & "successful"
    ' Print contents query file
    ReportAllValues AdvancedSelectionCriteria
End Sub
Function GetStringFromEnum(EnumVal As Long) As String
'From enum swAdvSelecType_e
    If EnumVal = &H1 Then
        GetStringFromEnum = "And"
    ElseIf EnumVal = &H2 Then
        GetStringFromEnum = "Or"
    ElseIf EnumVal = &H4000 Then
        GetStringFromEnum = "is yes"
    ElseIf EnumVal = &H8000 Then
        GetStringFromEnum = "is no"
    ElseIf EnumVal = &H8 Then
        GetStringFromEnum = "is not"
    ElseIf EnumVal = &H10 Then
        GetStringFromEnum = "contains"
    ElseIf EnumVal = &H20 Then
        GetStringFromEnum = "Is_Contained_By"
    ElseIf EnumVal = &H40 Then
        GetStringFromEnum = "Interferes_With"
    ElseIf EnumVal = &H80 Then
        GetStringFromEnum = "Does_Not_Interferes_With"
    ElseIf EnumVal = &H4 Then
        GetStringFromEnum = "is (exactly)"
    ElseIf EnumVal = &H2000 Then
        GetStringFromEnum = "not ="
    ElseIf EnumVal = &H200 Then
        GetStringFromEnum = "<"
    ElseIf EnumVal = &H800 Then
        GetStringFromEnum = "<="
    ElseIf EnumVal = &H1000 Then
        GetStringFromEnum = "="
    ElseIf EnumVal = &H400 Then
        GetStringFromEnum = ">="
    ElseIf EnumVal = &H100 Then
        GetStringFromEnum = ">"
    Else
        GetStringFromEnum = "Condition NOT found"
    End If
End Function
Sub ReportAllValues(AdvancedSelectionCriteria As SldWorks.AdvancedSelectionCriteria)
    Debug.Print

    Dim Count As Long
    Count = AdvancedSelectionCriteria.GetItemCount
    Debug.Print "GetItemCount returned " & Count

    Dim i As Long
    Dim Property As String
    Dim Condition As Long
    Dim Value As String
    Dim IsAnd As Boolean
    Dim Rindex As Long
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
    PrintString = Format("Index", IndexFmt) & Format("Rindex", RindexFmt) & Format("And/Or", AndOrFmt) & Format("Property", PropertyFmt) & Format("Condition", ConditionFmt) & Format("Value", ValueFmt)
    Debug.Print PrintString
    For i = 0 To Count - 1
        Rindex = AdvancedSelectionCriteria.GetItem(i, Property, Condition, Value, IsAnd)
        ConditionString = GetStringFromEnum(Condition)
        PrintString = Format(i, IndexFmt) & Format(Rindex, RindexFmt) & Format(IIf(IsAnd = False, "OR", "AND"), AndOrFmt) & Format(Property, PropertyFmt) & Format(ConditionString, ConditionFmt) & Format(Value, ValueFmt)
        Debug.Print PrintString
    Next i
    Debug.Print
End Sub
```
