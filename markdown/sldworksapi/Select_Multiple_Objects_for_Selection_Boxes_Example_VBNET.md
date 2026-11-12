---
title: "Select Multiple Objects for Selection Boxes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Objects_for_Selection_Boxes_Example_VBNET.htm"
---

# Select Multiple Objects for Selection Boxes Example (VB.NET)

This example shows how to select multiple objects and add the selected objects to different selection boxes on a PropertyManager page.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Copy [SolidWorksMacro.vb](#Module) to your project.
' 3. Add a class module and copy [clsPropMgr.vb](#Class) to that module.
' 4. Add the SolidWorks.Interop.swpublished primary interop assembly
' reference to your project (click **Project > Add Reference**,
' browse to `install_dir`\**api\redist**, select
' **SolidWorks.Interop.swpublished.dll > OK**).
' 5. Verify that the **Tools > Options > System Options > Stop VSTA debugger**
' **on macro exit** checkbox is clear.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Creates a PropertyManager page.
' 3. Examine the PropertyManager page to verify that
' three selected faces appear in the top selection
' box and two selected faces appear in the bottom
' selection box.
' 4. Close the PropertyManager page.
'
' NOTES:
' * Reselect the **Tools > Options > System Options > Stop VSTA debugger**
' **on macro exit** checkbox, if it was selected prior to running the macro.
' * Because the assembly document is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------

```vb
 'SolidWorksMacro.vb
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

    Public swApp As SldWorks
    Public swModel As ModelDoc2
    Public swModelDocExt As ModelDocExtension
    Public swSelectionMgr As SelectionMgr
    Public WithEvents pm As clsPropMgr
    Public Const mark As Integer = 1
    Public Const mark2 As Integer = 2

    Public Sub Main()

        Dim openDocErrors As Integer
        Dim OpenDocWarnings As Integer
        Dim fileName As String
        Dim selections1(2) As Face2
        Dim selections2(1) As Face2
        Dim i As Integer
        Dim j As Integer
        Dim status As Boolean
        Dim nbrSelections As Integer

        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", openDocErrors, OpenDocWarnings)
        swModelDocExt = swModel.Extension
        swSelectionMgr = swModel.SelectionManager

        'Create a new instance of the PropertyManager class
        pm = New clsPropMgr(swApp)
        pm.Show()

        'Selections for top selection box
        status = swModelDocExt.SelectByID2("", "FACE", 0.00369805475952489, 0.0901975482463513, 0.00315907187808762, True, mark, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.00860570843923369, 0.0737431971170679, 0.0039892160950501, True, mark, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.0100013029872912, 0.0446884591512742, 0.00996173127262523, True, mark, Nothing, 0)
        nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1)
        nbrSelections = nbrSelections - 1
        For i = 0 To nbrSelections
            selections1(i) = swSelectionMgr.GetSelectedObject6(i + 1, -1)
        Next

        swModel.ClearSelection2(True)

        'Selections for bottom selection box
        status = swModelDocExt.SelectByID2("", "FACE", -0.0264206017159268, -0.00342602957275062, 0.00987615560137556, True, mark2, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.00128130257782288, -0.00354158999988385, 0.0177003152412567, True, mark2, Nothing, 0)
        nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1)
        nbrSelections = nbrSelections - 1
        For j = 0 To nbrSelections
            selections2(j) = swSelectionMgr.GetSelectedObject6(j + 1, -1)
        Next

        swModel.ClearSelection2(True)

        'Populate selection boxes
        SelectBoxFaces1(selections1, mark)
        SelectBoxFaces2(selections2, mark2)

    End Sub
    Private Sub SelectBoxFaces1(ByVal selections() As Face2, ByVal selectionBoxMark As Integer)
        Dim swSelectData As SelectData
        swSelectData = swSelectionMgr.CreateSelectData
        swSelectData.Mark = selectionBoxMark
        swModelDocExt.MultiSelect2(selections, True, swSelectData)
    End Sub
    Private Sub SelectBoxFaces2(ByVal selections() As Face2, ByVal selectionBoxMark As Integer)
        Dim swSelectData As SelectData
        swSelectData = swSelectionMgr.CreateSelectData
        swSelectData.Mark = selectionBoxMark
        swModelDocExt.MultiSelect2(selections, True, swSelectData)
    End Sub

End Class
```

[Back to top](#Top)

```vb
 'clsPropMgr.vb
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports System
Imports System.Runtime.InteropServices
Imports System.Diagnostics

<ComVisibleAttribute(True)> Public Class clsPropMgr

    Implements IPropertyManagerPage2Handler9

    Dim swApp As SldWorks

    'General objects required for the PropertyManager page
    Dim pm_Page As PropertyManagerPage2
    Dim pm_Group As PropertyManagerPageGroup
    Dim pm_Selection As PropertyManagerPageSelectionbox
    Dim pm_Selection2 As PropertyManagerPageSelectionbox

    'Each object in the page needs a unique ID
    Const GroupID As Integer = 1
    Const LabelID As Integer = 2
    Const SelectionID As Integer = 3
    Const ComboID As Integer = 4
    Const ListID As Integer = 5
    Const Selection2ID As Integer = 6

    Dim ClickedCancel As Boolean
    Dim retVal As Integer

    Sub Show()
        pm_Page.Show2(0)
    End Sub

    'The following runs when a new instance
    'of the class is created
    Public Sub New(ByVal swApp As SldWorks)

        Dim PageTitle As String
        Dim caption As String
        Dim tip As String
        Dim options As Long
        Dim longerrors As Long
        Dim controlType As Integer
        Dim alignment As Integer

        'Set the variables for the page
        PageTitle = "MultiSelect2 Test"
        options = swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton + swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton + swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton

        'Create the PropertyManager page
        pm_Page = CType(swApp.CreatePropertyManagerPage(PageTitle, options, Me, longerrors), PropertyManagerPage2)

        'Make sure that the page was created properly
        If longerrors = swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay Then

            'Begin adding the controls to the page

            'Create the group box
            caption = ""
            options = swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded
            pm_Group = pm_Page.AddGroupBox(GroupID, caption, options)

            'Create two selection boxes
            controlType = swPropertyManagerPageControlType_e.swControlType_Selectionbox
            caption = ""  ' No caption for selection boxes
            alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
            options = swAddControlOptions_e.swControlOptions_Visible + swAddControlOptions_e.swControlOptions_Enabled
            tip = "Select multiple faces."

            pm_Selection = pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip)
            pm_Selection2 = pm_Group.AddControl(Selection2ID, controlType, caption, alignment, options, tip)
```

```
            'Only faces can populate the selection boxes
            Dim filters(0) As swSelectType_e
            filters(0) = swSelectType_e.swSelFACES

            Dim filterObj As Object
            filterObj = filters

            pm_Selection.SingleEntityOnly = False
            pm_Selection.AllowMultipleSelectOfSameEntity = True
            pm_Selection.Height = 50
            pm_Selection.SetSelectionFilters(filterObj)
            pm_Selection.Mark = SolidWorksMacro.mark

            pm_Selection2.SingleEntityOnly = False
            pm_Selection2.AllowMultipleSelectOfSameEntity = True
            pm_Selection2.Height = 50
            pm_Selection2.SetSelectionFilters(filterObj)
            pm_Selection2.Mark = SolidWorksMacro.mark2

        Else  'If the page is not created
            MsgBox("An error occurred while attempting to create the " & "PropertyManager Page", vbCritical)
        End If

    End Sub

    Public Sub AfterActivation() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterActivation

    End Sub

    Public Sub AfterClose() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterClose

    End Sub

    Public Function OnActiveXControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnActiveXControlCreated

    End Function

    Public Sub OnButtonPress(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnButtonPress

    End Sub

    Public Sub OnCheckboxCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnCheckboxCheck

    End Sub

    Public Sub OnClose(ByVal Reason As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnClose

        If Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel Then
            'Cancel button was clicked
            ClickedCancel = True
        ElseIf Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
            'OK button was clicked
            ClickedCancel = False
        End If

    End Sub

    Public Sub OnComboboxEditChanged(ByVal Id As Integer, ByVal Text As String) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnComboboxEditChanged

    End Sub

    Public Sub OnComboboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnComboboxSelectionChanged

    End Sub

    Public Sub OnGainedFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGainedFocus

    End Sub

    Public Sub OnGroupCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGroupCheck

    End Sub

    Public Sub OnGroupExpand(ByVal Id As Integer, ByVal Expanded As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGroupExpand

    End Sub

    Public Function OnHelp() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnHelp

    End Function

    Public Function OnKeystroke(ByVal Wparam As Integer, ByVal Message As Integer, ByVal Lparam As Integer, ByVal Id As Integer) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnKeystroke

    End Function

    Public Sub OnListboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnListboxSelectionChanged

    End Sub

    Public Sub OnLostFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnLostFocus

    End Sub

    Public Function OnNextPage() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNextPage

    End Function

    Public Sub OnNumberboxChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNumberboxChanged

    End Sub

    Public Sub OnOptionCheck(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnOptionCheck

    End Sub

    Public Sub OnPopupMenuItem(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPopupMenuItem

    End Sub

    Public Sub OnPopupMenuItemUpdate(ByVal Id As Integer, ByRef retval As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPopupMenuItemUpdate

    End Sub

    Public Function OnPreview() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPreview

    End Function

    Public Function OnPreviousPage() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPreviousPage

    End Function

    Public Sub OnRedo() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnRedo

    End Sub

    Public Sub OnSelectionboxCalloutCreated(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxCalloutCreated

    End Sub

    Public Sub OnSelectionboxCalloutDestroyed(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxCalloutDestroyed

    End Sub

    Public Sub OnSelectionboxFocusChanged(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxFocusChanged

    End Sub

    Public Sub OnSelectionboxListChanged(ByVal Id As Integer, ByVal Count As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxListChanged

    End Sub

    Public Sub OnSliderPositionChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderPositionChanged

    End Sub

    Public Sub OnSliderTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderTrackingCompleted

    End Sub

    Public Function OnSubmitSelection(ByVal Id As Integer, ByVal Selection As Object, ByVal SelType As Integer, ByRef ItemText As String) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSubmitSelection

        OnSubmitSelection = True
        Debug.Print("OnSubmitSelection fired.")

    End Function

    Public Function OnTabClicked(ByVal Id As Integer) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnTabClicked

    End Function

    Public Sub OnTextboxChanged(ByVal Id As Integer, ByVal Text As String) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnTextboxChanged

    End Sub

    Public Sub OnUndo() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnUndo

    End Sub

    Public Sub OnWhatsNew() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnWhatsNew

    End Sub

    Public Sub OnListBoxRMBUp(ByVal Id As Integer, ByVal posX As Integer, ByVal posY As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnListboxRMBUp

    End Sub
    Public Function OnWindowFromHandleControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnWindowFromHandleControlCreated

    End Function

    Public Sub OnNumberBoxTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNumberBoxTrackingCompleted

    End Sub

End Class
```

[Back to top](#Top)
