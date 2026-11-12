---
title: "Activate Property Manager Page Tab Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Property_Manager_Page_Tab_Example_VB.htm"
---

# Activate Property Manager Page Tab Example (VBA)

## Activate PropertyManager Page Tab Example (VBA)

The following code example demonstrates how SOLIDWORKS add-ins can use IPropertyManagerPageTab.Activate to programmatically select a tab on a SOLIDWORKS PropertyManager page.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Copy and paste Main into your macro.
' 2. Click Insert > Class Module and copy and paste Class1 into the module.
' 3. Add a reference to SOLIDWORKS <version> exposed type libraries
'    for add-in use.
' 4. Open an assembly that has multiple components.
'
' Postconditions:
' 1. Creates a PropertyManager page called Materials and Dimensions
'    with two tabs:
'    * Materials
'    * Dimensions
' 2. Selects the Materials tab.
' 3. Examine the PropertyManager page.
'----------------------------------------------------------------------------
'Main
Option Explicit
```

```
Public swApp As SldWorks.SldWorks
Public Part As SldWorks.ModelDoc2
Public SelMgr As SldWorks.SelectionMgr
Public pm As Class1
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Set SelMgr = Part.SelectionManager
```

```
    'Create a new instance of the PropertyManager class
    'Calls the Class_Initialize procedure of the class
    Set pm = New Class1
    pm.Show
```

```
End Sub
```

```
Back to top
```

```
'Class1
Option Explicit
```

```
'Required for PropertyManager page controls
Implements PropertyManagerPage2Handler6
```

```
'General objects required for the PropertyManager page
Dim pm_Page As PropertyManagerPage2
Dim pm_Page_Tab As PropertyManagerPageTab
Dim pm_Page_Tab_2 As PropertyManagerPageTab
Dim pm_Group As PropertyManagerPageGroup
Dim pm_Selection As PropertyManagerPageSelectionbox
Dim pm_Label As PropertyManagerPageLabel
Dim pm_Combo As PropertyManagerPageCombobox
```

```
'Each object in the page needs a unique ID
Const GroupID As Integer = 1
Const LabelID As Integer = 2
Const SelectionID As Integer = 3
Const ComboID As Integer = 4
Const Tab1ID As Integer = 1
Const Tab2ID As Integer = 2
```

```
Dim ClickedCancel As Boolean
Dim density As String
Dim material As String
```

```
Sub Show()
    pm_Page.Show
End Sub
Private Sub Class_Initialize()
    Dim PageTitle As String
    Dim caption As String
    Dim tip As String
    Dim options As Long
    Dim longerrors As Long
    Dim controlType As Integer
    Dim alignment As Integer
```

```
    'Set the variables for the page
    PageTitle = "Materials and Dimensions"
    options = swPropertyManager_OkayButton + swPropertyManager_CancelButton + swPropertyManagerOptions_LockedPage + swPropertyManagerOptions_PushpinButton
```

```
    'Create the PropertyManager page
    Set pm_Page = swApp.CreatePropertyManagerPage(PageTitle, options, Me, longerrors)
```

```
    'Make sure that the page was created properly
    If longerrors = swPropertyManagerPage_Okay Then
        ' Create page tabs
        Set pm_Page_Tab = pm_Page.AddTab(Tab1ID, "Materials", "", 0)
        Set pm_Page_Tab_2 = pm_Page.AddTab(Tab2ID, "Dimensions", "", 0)
```

```
        ' Activate the first tab
        pm_Page_Tab.Activate
```

```
        'Begin adding the controls to the page tab
```

```
        'Create the group box
        caption = "Materials"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded
        Set pm_Group = pm_Page_Tab.AddGroupBox(GroupID, caption, options)
```

```
        'Create selection box
          controlType = swControlType_Selectionbox
          caption = ""  ' No caption for selection boxes
          alignment = swControlAlign_Indent
          options = swControlOptions_Visible + swControlOptions_Enabled
          tip = "Select an edge, face, vertex, solid body, or a component"
          Set pm_Selection = pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip)
          Dim filters(6) As Long
          filters(0) = swSelEDGES
          filters(1) = swSelREFEDGES
          filters(2) = swSelFACES
          filters(3) = swSelVERTICES
          filters(4) = swSelSOLIDBODIES
          filters(5) = swSelCOMPONENTS
          filters(6) = swSelCOMPSDONTOVERRIDE
```

```
          pm_Selection.SingleEntityOnly = False
          pm_Selection.AllowMultipleSelectOfSameEntity = True
          pm_Selection.Height = 50
          pm_Selection.SetSelectionFilters filters
    Else  'If the page is not created
        MsgBox "An error while attempting to create the " & "PropertyManager Page", vbCritical
    End If
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_AfterActivation()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_AfterClose()
```

```
    Set pm = Nothing
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler6_OnActiveXControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler6_OnButtonPress(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnCheckboxCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnClose(ByVal Reason As Long)
```

```
    If Reason = swPropertyManagerPageClose_Cancel Then
        'Cancel button was clicked
        ClickedCancel = True
    ElseIf Reason = swPropertyManagerPageClose_Okay Then
        'OK button was clicked
        ClickedCancel = False
    End If
```

```
'Store the density and material name values based
'on the combo-box selection
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler6_OnHelp() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler6_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler6_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler6_OnNextPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler6_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnOptionCheck(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnPopupMenuItem(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnPopupMenuItemUpdate(ByVal Id As Long, retval As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler6_OnPreview() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler6_OnPreviousPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler6_OnRedo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnSelectionboxCalloutCreated(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnSelectionboxFocusChanged(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnSelectionboxListChanged(ByVal Id As Long, ByVal Count As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler6_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ItemText As String) As Boolean
```

```
     PropertyManagerPage2Handler6_OnSubmitSelection = True
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler6_OnTabClicked(ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler6_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnUndo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler6_OnWhatsNew()
```

```
End Sub
```

```
Back to top
```
