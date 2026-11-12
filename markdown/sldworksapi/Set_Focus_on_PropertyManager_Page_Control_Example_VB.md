---
title: "Set Focus on PropertyManager Page Control Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Focus_on_PropertyManager_Page_Control_Example_VB.htm"
---

# Set Focus on PropertyManager Page Control Example (VBA)

This example shows how to set focus on a PropertyManager page control.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Copy Main to the main module.
' 3. Click Insert > Class Module and copy Class1 to that module.
' 4. Click Tools > References > SOLIDWORKS version exposed type libraries
'    for add-in use.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates and displays a PropertyManager page.
' 2. Select the check box to set focus on Text box.
' 3. Examine the Immediate window.
' 4. Clear the check box to remove focus from Text box.
' 5. Examine the Immediate window.
' 6. Click OK to close the PropertyManager page.
'---------------------------------------------------------------------------
'Main
Option Explicit
```

```
Public swApp As SldWorks.SldWorks
Public Part As SldWorks.ModelDoc2
Public pm As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
```

```
    'Create a new instance of the PropertyManager class
    Set pm = New Class1
    pm.Show
```

```
End Sub
```

```vb
Back to top
'Class1
```

```
Option Explicit
```

```
'Required for PropertyManager page controls
Implements PropertyManagerPage2Handler9
```

```
'General objects required for the PropertyManager page
Dim pm_Page As PropertyManagerPage2
Dim pm_Checkbox As PropertyManagerPageCheckbox
Dim pm_Text As PropertyManagerPageTextbox
Dim pm_Group As PropertyManagerPageGroup
```

```
'Each object in the page needs a unique ID
Const checkboxID As Integer = 1
Const textId As Integer = 2
Const groupID As Integer = 3
```

```
Dim ClickedCancel As Boolean
```

```
Sub Show()
    pm_Page.Show2 0
End Sub
```

```
'The following runs when a new instance
'of the class is created
Private Sub Class_Initialize()
```

```
    Dim PageTitle As String
    Dim options As Long
    Dim errors As Long
    Dim caption As String
    Dim alignment As Long
    Dim control As Long
```

```
    'Set the variables for the page
    PageTitle = "Test focus methods"
    options = swPropertyManager_OkayButton + swPropertyManager_CancelButton + swPropertyManagerOptions_LockedPage + swPropertyManagerOptions_PushpinButton
```

```
    'Create the PropertyManager page
    Set pm_Page = swApp.CreatePropertyManagerPage(PageTitle, options, Me, errors)
```

```
    'Make sure that the page was created properly
    If errors = swPropertyManagerPage_Okay Then
        ' Create group box
        caption = "Group box"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded
        Set pm_Group = pm_Page.AddGroupBox(groupID, caption, options)
```

```
        ' Create check box
        alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge
        options = swAddControlOptions_e.swControlOptions_Visible + swAddControlOptions_e.swControlOptions_Enabled
```

```
        control = swControlType_Checkbox
        Set pm_Checkbox = pm_Group.AddControl(checkboxID, control, "Focus on text box", alignment, options, "Check box")
        Debug.Print "Upon opening the PropertyManager page:"
        Debug.Print "  State of check box: (0 = Unchecked, 1 = Checked, 2 = Indeterminate): " & pm_Checkbox.State
        pm_Checkbox.Checked = False
```

```
        ' Create text box
        control = swControlType_Textbox
        Set pm_Text = pm_Group.AddControl(textId, control, "Text box", alignment, options, "Text box")
```

```
    Else  'If the page is not created
        MsgBox "An error occurred while attempting to create the PropertyManager Page", vbCritical
    End If
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_AfterActivation()
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_AfterClose()
    'Destroy the class
    Set pm = Nothing
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnActiveXControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnButtonPress(ByVal Id As Long)
```

```
End Sub
Private Sub PropertyManagerPage2Handler9_OnCheckboxCheck(ByVal Id As Long, ByVal Checked As Boolean)
    ' Set focus on the text box when check box is selected
     Debug.Print "Upon clicking the check box on the PropertyManager page:"
     Debug.Print "  State of check box: (0 = Unchecked, 1 = Checked, 2 = Indeterminate): " & pm_Checkbox.State
    If Checked Then
        pm_Page.SetFocus (textId)
        Debug.Print "Focus on Text box."
    Else
        Debug.Print "Focus off Text box."
    End If
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnClose(ByVal Reason As Long)
    If Reason = swPropertyManagerPageClose_Cancel Then
        'Cancel button was clicked
        ClickedCancel = True
    ElseIf Reason = swPropertyManagerPageClose_Okay Then
        'OK button was clicked
        ClickedCancel = False
    End If
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnHelp() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler9_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnNextPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnOptionCheck(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnPopupMenuItem(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnPopupMenuItemUpdate(ByVal Id As Long, retVal As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnPreview() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler9_OnPreviousPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnRedo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxCalloutCreated(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxFocusChanged(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxListChanged(ByVal Id As Long, ByVal Count As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ItemText As String) As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler9_OnTabClicked(ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnUndo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnWhatsNew()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnLostFocus(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnGainedFocus(ByVal Id As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnWindowFromHandleControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnListboxRMBUp(ByVal Id As Long, ByVal PosX As Long, ByVal PosY As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnNumberBoxTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```vb
End Sub
Back to top
```
