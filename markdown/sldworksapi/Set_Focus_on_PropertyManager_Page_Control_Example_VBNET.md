---
title: "Set Focus on PropertyManager Page Control Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Focus_on_PropertyManager_Page_Control_Example_VBNET.htm"
---

# Set Focus on PropertyManager Page Control Example (VB.NET)

This example shows how to set focus on a PropertyManager page control.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Copy Main to the main module.
' 3. Click Project > Add Class > Add and copy Class1 to Class1.vb.
' 4. Click Project > Add Reference > browse to install_dir\api\redist,
'    select SolidWorks.Interop.swpublished.dll > OK.
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Part As ModelDoc2
    Public WithEvents pm As Class1

    Public Sub main()

        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)
        Part = swApp.ActiveDoc

        'Create a new instance of the PropertyManager class
        pm = New Class1(swApp)
        pm.Show()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

```vb
Back to top
'Class1
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports System
 Imports System.Runtime.InteropServices
 Imports System.Diagnostics

 <ComVisibleAttribute(True)>
 Public Class Class1

     Implements PropertyManagerPage2Handler9

     Dim swApp As SldWorks

     'General objects required for the PropertyManager page
     Dim pm_Page As PropertyManagerPage2
     Dim pm_Group As PropertyManagerPageGroup
     Dim pm_Checkbox As PropertyManagerPageCheckbox
     Dim pm_Text As PropertyManagerPageTextbox

     'Each object in the page needs a unique ID
     Const checkboxID As Integer = 1
     Const textID As Integer = 2
     Const groupID As Integer = 3
     Dim ClickedCancel As Boolean

     Sub Show()
         pm_Page.Show2(0)
     End Sub

     'The following runs when a new instance
     'of the class is created
     Public Sub New(ByVal swApp As SldWorks)

         Dim PageTitle As String
         Dim options As Integer
         Dim errors As Integer
         Dim caption As String
         Dim alignment As Integer
         Dim control As Integer

         'Set the variables for the page
         PageTitle = "Test focus methods"
         options = swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton _
             + swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton _
             + swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage _
             + swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton

         'Create the PropertyManager page
         pm_Page = CType(swApp.CreatePropertyManagerPage(PageTitle,
             options, Me, errors), PropertyManagerPage2)

         'Make sure that the page was created properly
         If errors = swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay Then
             'Begin adding the controls to the page
             ' Create group box
             caption = "Group box"
             options = swAddGroupBoxOptions_e.swGroupBoxOptions_Visible +
                 swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded
             pm_Group = pm_Page.AddGroupBox(groupID, caption, options)

             ' Create check box
             alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge
             options = swAddControlOptions_e.swControlOptions_Visible +
                 swAddControlOptions_e.swControlOptions_Enabled
             control = swPropertyManagerPageControlType_e.swControlType_Checkbox
             pm_Checkbox = pm_Group.AddControl(checkboxID, control, "Focus on text box", alignment, options, "Check box")
             Debug.Print("Upon opening the PropertyManager page:")
             Debug.Print("  State of check box: (0 = Unchecked, 1 = Checked, 2 = Indeterminate): " & pm_Checkbox.State)
             pm_Checkbox.Checked = False

             ' Create text box
             control = swPropertyManagerPageControlType_e.swControlType_Textbox
             pm_Text = pm_Group.AddControl(textID, control, "Text box", alignment, options, "Text box")
         Else  'If the page is not created
             MsgBox("An error while attempting to create the PropertyManager Page", vbCritical)
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
         Debug.Print("Upon clicking the check box on the PropertyManager page:")
         Debug.Print("  State of check box: (0 = Unchecked, 1 = Checked, 2 = Indeterminate): " & pm_Checkbox.State)
         ' Set focus on the text box when check box is selected
         If Checked Then
             pm_Page.SetFocus(textID)
             Debug.Print("Focus on Text box.")
         Else
             Debug.Print("Focus off Text box.")
         End If
     End Sub

     Public Sub OnClose(ByVal Reason As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnClose
         If Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel Then
             ' Cancel button was clicked
             ClickedCancel = True
         ElseIf Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
             ' OK button was clicked
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

Back to top
```
