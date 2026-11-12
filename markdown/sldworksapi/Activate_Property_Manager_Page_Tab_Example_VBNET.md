---
title: "Activate PropertyManager Page Tab Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Property_Manager_Page_Tab_Example_VBNET.htm"
---

# Activate PropertyManager Page Tab Example (VB.NET)

The following code example demonstrates how SOLIDWORKS add-ins can use IPropertyManagerPageTab.Activate to programmatically select a tab on a SOLIDWORKS PropertyManager page.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Copy Main to the main module.
' 2. Click Project > Add Class > Add and copy Class1 to Class1.vb.
' 3. Click Project > Add Reference, browse to install_dir\api\redist\, select
'    SolidWorks.Interop.swpublished.dll > OK.
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro
    Public swApp As SldWorks
    Public Part As ModelDoc2
    Public SelMgr As SelectionMgr
    Public pm As Class1

    Public Sub main()

        Part = swApp.ActiveDoc
        SelMgr = CType(Part.SelectionManager, SelectionMgr)
        'Create a new instance of the PropertyManager class
        pm = New Class1(swApp)
        pm.Show()

    End Sub

End Class
```

[Back to top](#Top)

```
'Class1
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports System
Imports System.Runtime.InteropServices

<ComVisibleAttribute(True)> _
Public Class Class1

    Implements PropertyManagerPage2Handler6
    Dim pm_Page As PropertyManagerPage2
    Dim ClickedCancel As Boolean
    Sub Show()
        pm_Page.Show()
    End Sub

    Sub New(ByVal swApp As SolidWorks.Interop.sldworks.SldWorks)
        'General objects required for the PropertyManager page
        Dim pm_Page_Tab As PropertyManagerPageTab
        Dim pm_Page_Tab_2 As PropertyManagerPageTab
        Dim pm_Group As PropertyManagerPageGroup
        Dim pm_Selection As PropertyManagerPageSelectionbox

        'Each object in the page needs a unique ID
        Const GroupID As Integer = 1
        Const SelectionID As Integer = 3
        Const Tab1ID As Integer = 1
        Const Tab2ID As Integer = 2
        Dim PageTitle As String
        Dim caption As String
        Dim tip As String
        Dim options As Integer
        Dim longerrors As Long
        Dim controlType As Integer
        Dim alignment As Integer

        'Set the variables for the page
        PageTitle = "Materials and Dimensions"
        options = swPropertyManagerPageOptions_e.swPropertyManagerOptions_OkayButton + swPropertyManagerPageOptions_e.swPropertyManagerOptions_CancelButton + swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage + swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton
        pm_Page = swApp.CreatePropertyManagerPage(PageTitle, options, Me, longerrors)
        ' Create page tabs
        pm_Page_Tab = CType(pm_Page.AddTab(Tab1ID, "Materials", "", 0), PropertyManagerPageTab)
        pm_Page_Tab_2 = CType(pm_Page.AddTab(Tab2ID, "Dimensions", "", 0), PropertyManagerPageTab)
        ' Activate the first tab
        pm_Page_Tab.Activate()
        'Begin adding the controls to the page tab
        'Create the group box
        caption = "Materials"
        options = swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded
        pm_Group = CType(pm_Page_Tab.AddGroupBox(GroupID, caption, options), PropertyManagerPageGroup)

        'Create selection box
        controlType = swPropertyManagerPageControlType_e.swControlType_Selectionbox

        caption = ""  ' No caption for selection boxes
        alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
        options = swAddControlOptions_e.swControlOptions_Visible + swAddControlOptions_e.swControlOptions_Enabled

        tip = "Select an edge, face, vertex, solid body, or a component"
        pm_Selection = CType(pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip), PropertyManagerPageSelectionbox)
        Dim filters(6) As Long
        filters(0) = swSelectType_e.swSelEDGES
        filters(1) = swSelectType_e.swSelREFEDGES
        filters(2) = swSelectType_e.swSelFACES
        filters(3) = swSelectType_e.swSelVERTICES
        filters(4) = swSelectType_e.swSelSOLIDBODIES
        filters(5) = swSelectType_e.swSelCOMPONENTS
        filters(6) = swSelectType_e.swSelCOMPSDONTOVERRIDE
        pm_Selection.SingleEntityOnly = False
        pm_Selection.AllowMultipleSelectOfSameEntity = True
        pm_Selection.Height = 50
        pm_Selection.SetSelectionFilters(filters)

    End Sub

    Private Sub PropertyManagerPage2Handler6_AfterActivation()
    End Sub

    Private Sub PropertyManagerPage2Handler6_AfterClose()
    End Sub

    Private Sub PropertyManagerPage2Handler6_OnClose(ByVal Reason As Integer)
        If Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel Then
            'Cancel button was clicked
            ClickedCancel = True
        ElseIf Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
            'OK button was clicked
            ClickedCancel = False
        End If
        'Store the density and material name values based
        'on the combo-box selection
    End Sub

    Private Function PropertyManagerPage2Handler6_OnHelp() As Boolean
    End Function

    Private Function PropertyManagerPage2Handler6_OnNextPage() As Boolean
    End Function

    Private Function PropertyManagerPage2Handler6_OnPreview() As Boolean
    End Function

    Private Function PropertyManagerPage2Handler6_OnPreviousPage() As Boolean
    End Function

    Private Sub PropertyManagerPage2Handler6_OnRedo()
    End Sub

    Private Sub PropertyManagerPage2Handler6_OnUndo()
    End Sub

    Private Sub PropertyManagerPage2Handler6_OnWhatsNew()
    End Sub

    Public Sub AfterActivation() Implements IPropertyManagerPage2Handler6.AfterActivation
    End Sub

    Public Sub AfterClose() Implements IPropertyManagerPage2Handler6.AfterClose
    End Sub

    Public Function OnActiveXControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements IPropertyManagerPage2Handler6.OnActiveXControlCreated
    End Function

    Public Sub OnButtonPress(ByVal Id As Integer) Implements IPropertyManagerPage2Handler6.OnButtonPress
    End Sub

    Public Sub OnCheckboxCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements IPropertyManagerPage2Handler6.OnCheckboxCheck
    End Sub

    Public Sub OnClose(ByVal Reason As Integer) Implements IPropertyManagerPage2Handler6.OnClose
    End Sub

    Public Sub OnComboboxEditChanged(ByVal Id As Integer, ByVal Text As String) Implements IPropertyManagerPage2Handler6.OnComboboxEditChanged
    End Sub

    Public Sub OnComboboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements IPropertyManagerPage2Handler6.OnComboboxSelectionChanged
    End Sub

    Public Sub OnGroupCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements IPropertyManagerPage2Handler6.OnGroupCheck
    End Sub

    Public Sub OnGroupExpand(ByVal Id As Integer, ByVal Expanded As Boolean) Implements IPropertyManagerPage2Handler6.OnGroupExpand
    End Sub

    Public Function OnHelp() As Boolean Implements IPropertyManagerPage2Handler6.OnHelp
    End Function

    Public Function OnKeystroke(ByVal Wparam As Integer, ByVal Message As Integer, ByVal Lparam As Integer, ByVal Id As Integer) As Boolean Implements IPropertyManagerPage2Handler6.OnKeystroke
    End Function

    Public Sub OnListboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements IPropertyManagerPage2Handler6.OnListboxSelectionChanged
    End Sub

    Public Function OnNextPage() As Boolean Implements IPropertyManagerPage2Handler6.OnNextPage
    End Function

    Public Sub OnNumberboxChanged(ByVal Id As Integer, ByVal Value As Double) Implements IPropertyManagerPage2Handler6.OnNumberboxChanged
    End Sub

    Public Sub OnOptionCheck(ByVal Id As Integer) Implements IPropertyManagerPage2Handler6.OnOptionCheck
    End Sub

    Public Sub OnPopupMenuItem(ByVal Id As Integer) Implements IPropertyManagerPage2Handler6.OnPopupMenuItem
    End Sub

    Public Sub OnPopupMenuItemUpdate(ByVal Id As Integer, ByRef retval As Integer) Implements IPropertyManagerPage2Handler6.OnPopupMenuItemUpdate
    End Sub

    Public Function OnPreview() As Boolean Implements IPropertyManagerPage2Handler6.OnPreview
    End Function

    Public Function OnPreviousPage() As Boolean Implements IPropertyManagerPage2Handler6.OnPreviousPage
    End Function

    Public Sub OnRedo() Implements IPropertyManagerPage2Handler6.OnRedo
    End Sub

    Public Sub OnSelectionboxCalloutCreated(ByVal Id As Integer) Implements IPropertyManagerPage2Handler6.OnSelectionboxCalloutCreated
    End Sub

    Public Sub OnSelectionboxCalloutDestroyed(ByVal Id As Integer) Implements IPropertyManagerPage2Handler6.OnSelectionboxCalloutDestroyed

    End Sub

    Public Sub OnSelectionboxFocusChanged(ByVal Id As Integer) Implements IPropertyManagerPage2Handler6.OnSelectionboxFocusChanged
    End Sub

    Public Sub OnSelectionboxListChanged(ByVal Id As Integer, ByVal Count As Integer) Implements IPropertyManagerPage2Handler6.OnSelectionboxListChanged
    End Sub

    Public Sub OnSliderPositionChanged(ByVal Id As Integer, ByVal Value As Double) Implements IPropertyManagerPage2Handler6.OnSliderPositionChanged
    End Sub

    Public Sub OnSliderTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements IPropertyManagerPage2Handler6.OnSliderTrackingCompleted
    End Sub

    Public Function OnSubmitSelection(ByVal Id As Integer, ByVal Selection As Object, ByVal SelType As Integer, ByRef ItemText As String) As Boolean Implements IPropertyManagerPage2Handler6.OnSubmitSelection
    End Function

    Public Function OnTabClicked(ByVal Id As Integer) As Boolean Implements IPropertyManagerPage2Handler6.OnTabClicked
    End Function

    Public Sub OnTextboxChanged(ByVal Id As Integer, ByVal Text As String) Implements IPropertyManagerPage2Handler6.OnTextboxChanged
    End Sub

    Public Sub OnUndo() Implements IPropertyManagerPage2Handler6.OnUndo
    End Sub

    Public Sub OnWhatsNew() Implements IPropertyManagerPage2Handler6.OnWhatsNew
    End Sub

End Class
```

```
Back to top
```
