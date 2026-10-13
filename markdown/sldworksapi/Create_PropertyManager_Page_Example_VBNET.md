---
title: "Create PropertyManager Page Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_PropertyManager_Page_Example_VBNET.htm"
---

# Create PropertyManager Page Example (VB.NET)

This example shows how to create a PropertyManager page that contains these controls:

- ActiveX
- Bitmap
- Bitmap buttons
- Button
- Combo box
- Group box
- Label
- List box
- Number box
- Radio button
- Selection box
- Slider
- Tab

This example also shows how to handle focus events for these controls.

NOTE: If the model is an assembly that contains multiple components, and you want to allow the user to select edges, faces, or vertices, then you must specify swSelectType_e.swSelCOMPSDONTOVERRIDE for parameter SelType of IPropertyManagerPageSelectionbox::SetSelectionFilters. Otherwise, if the user attempts to select an edge, face, or vertex, then the entire component might get selected and not the edge, face, or vertex. This example demonstrates how to specify SelType.

```vb
'----------------------------------------------------------------------------
 '    Preconditions:
 '  1. Create a VB.NET macro.
 '  2. Copy and paste  Main into SolidWorksMacro.vb.
 '  3. Add a class named clsPropMgr and copy and paste  clsPropMgr into that class.
 '  4. Click Project >  Add Reference, browse to install_dir\api\redist\, select
 '     SolidWorks.Interop.swpublished.dll > OK.
  '  5. Verify that the specified assembly document exists.
 '  6. Modify ClassID and LicenseKey parameters in
 '     IPropertyManagerPageActiveX::SetClass to add your ActiveX control
 '     to the PropertyManager page.
 '  7. Replace the ImageList and ImageListMasks array elements with the pathnames of
 '     your image files.
 '  8. Open an Immediate window.
 '
 '   Postconditions:
 '  1. Opens the specified assembly.
 '  2. Creates a PropertyManager page.
 '  3. Creates the specified controls.
 '  4. Examine the Immediate Window as you use the specified controls.
 '     Note the size of the button at the bottom of the PropertyManager page.
 '  5. Click OK to close the PropertyManager page.
 '  6. Exit SOLIDWORKS Design.
 '  7. Change the size of the text and other items on your computer.
 '     For example, in Windows 7:
 '     a. Click Start > Control Panel > Appearance and
 '        Personalization > Display.
 '     b. Select a different size.
 '     c. Click Apply.
 '     d. Click Log off now.
 '     e. Log back in.
 '  8. Start SOLIDWORKS Design.
 '  9. Run this macro again and note the size of the button at
 '     the bottom of the PropertyManager page.
 ' 10. Click OK to close the PropertyManager page.
 '
 ' NOTES:
 ' * After running this macro, select
 '   Tools > Options > System Options > Stop VSTA debugger
 '    on macro exit.
 '  * Because the assembly document is used elsewhere,
 '   do not save any changes.
 '----------------------------------------------------------------------------
  'Main
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
Partial Class SolidWorksMacro
    Public Part As ModelDoc2
     Public WithEvents pm As clsPropMgr

     Sub main()
        Dim openDocErrors As Integer
         Dim OpenDocWarnings As Integer
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)
        Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", openDocErrors, OpenDocWarnings)

        'Create a new instance of the PropertyManager class
         pm = New clsPropMgr(swApp)
         pm.Show()
    End Sub
    Public swApp As SldWorks
End Class
```

[Back to top](#Top)

```vb
  'clsPropMgr
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports System
 Imports System.Runtime.InteropServices
 Imports System.Diagnostics

 <ComVisibleAttribute(True)> _
 Public Class clsPropMgr

    Implements PropertyManagerPage2Handler9
    Dim swApp As SldWorks
     'Control objects required for the PropertyManager page
     Dim pm_Page As PropertyManagerPage2
     Dim pm_Group As PropertyManagerPageGroup
     Dim pm_Selection As PropertyManagerPageSelectionbox
     Dim pm_Selection2 As PropertyManagerPageSelectionbox
     Dim pm_Label As PropertyManagerPageLabel
     Dim pm_Combo As PropertyManagerPageCombobox
     Dim pm_List As PropertyManagerPageListbox
     Dim pm_Number As PropertyManagerPageNumberbox
     Dim pm_Radio As PropertyManagerPageOption
     Dim pm_Slider As PropertyManagerPageSlider
     Dim pm_Tab As PropertyManagerPageTab
     Dim pm_Button As PropertyManagerPageButton
     Dim pm_BMPButton As PropertyManagerPageBitmapButton
     Dim pm_BMPButton2 As PropertyManagerPageBitmapButton
     Dim pm_Bitmap As PropertyManagerPageBitmap
     Dim pm_ActiveX As PropertyManagerPageActiveX

     'Each control in the page needs a unique ID
     Const GroupID As Integer = 1
     Const LabelID As Integer = 2
     Const SelectionID As Integer = 3
     Const ComboID As Integer = 4
     Const ListID As Integer = 5
     Const Selection2ID As Integer = 6
     Const NumberID As Integer = 7
     Const RadioID As Integer = 8
     Const SliderID As Integer = 9
     Const TabID As Integer = 10
     Const ButtonID As Integer = 11
     Const BMPButtonID As Integer = 12
     Const BMPButtonID2 As Integer = 13
     Const BitmapID As Integer = 14
     Const ActiveXID As Integer = 15

     Dim ClickedCancel As Boolean
     Dim retVal As Integer

     Sub Show()
        pm_Page.Show2(0)
    End Sub

    'Run when a new instance
     'of the class is created
     Public Sub New(ByVal swApp As SldWorks)
        Dim PageTitle As String
         Dim caption As String
         Dim tip As String
         Dim options As Integer
         Dim longerrors As Integer
         Dim controlType As Integer
         Dim alignment As Integer
         Dim listItems(3) As String
        'Set the variables for the page
         PageTitle = "Comps"
        options = swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton _
             + swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton _
             + swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage _
             + swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton

        'Create the PropertyManager page
         pm_Page = CType(swApp.CreatePropertyManagerPage(PageTitle, _
             options, Me, longerrors), PropertyManagerPage2)

        'Make sure that the page was created properly
         If longerrors = swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay Then

            'Add the controls to the page
             'Add a tab
             pm_Tab = pm_Page.AddTab(TabID, "Application", "", 0)

             'Add a group box to the tab
             caption = "Controls"
             options = swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + _
                 swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded
             pm_Group = pm_Tab.AddGroupBox(GroupID, caption, options)

            'Add two selection boxes
             controlType = swPropertyManagerPageControlType_e.swControlType_Selectionbox
             caption = ""  ' No caption for selection boxes
             alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
             options = swAddControlOptions_e.swControlOptions_Visible + _
                 swAddControlOptions_e.swControlOptions_Enabled
             tip = "Select an edge, face, vertex, solid body, or a component"
             pm_Selection = pm_Group.AddControl2(SelectionID, _
                 controlType, caption, alignment, options, tip)
             pm_Selection2 = pm_Group.AddControl2(Selection2ID, _
                 controlType, caption, alignment, options, tip)
             Dim filters(6) As swSelectType_e
             filters(0) = swSelectType_e.swSelEDGES
             filters(1) = swSelectType_e.swSelREFEDGES
             filters(2) = swSelectType_e.swSelFACES
             filters(3) = swSelectType_e.swSelVERTICES
             filters(4) = swSelectType_e.swSelSOLIDBODIES
             filters(5) = swSelectType_e.swSelCOMPONENTS
             filters(6) = swSelectType_e.swSelCOMPSDONTOVERRIDE
             Dim filterObj As Object
            filterObj = filters
             pm_Selection.SingleEntityOnly = False
             pm_Selection.AllowMultipleSelectOfSameEntity = True
             pm_Selection.Height = 50
             pm_Selection.SetSelectionFilters(filterObj)
             pm_Selection2.SingleEntityOnly = False
             pm_Selection2.AllowMultipleSelectOfSameEntity = True
             pm_Selection2.Height = 50
             pm_Selection2.SetSelectionFilters(filterObj)
            'Add a combo box
             controlType = swPropertyManagerPageControlType_e.swControlType_Combobox
             caption = ""
             alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
             options = swAddControlOptions_e.swControlOptions_Visible + _
                 swAddControlOptions_e.swControlOptions_Enabled

             tip = "Select a value"
             pm_Combo = pm_Group.AddControl2(ComboID, _
                 controlType, caption, alignment, options, tip)
             If Not pm_Combo Is Nothing Then
                 pm_Combo.Height = 50
                 listItems(0) = "Value 1"
                 listItems(1) = "Value 2"
                 listItems(2) = "Value 3"
                 listItems(3) = "Value 4"
                 pm_Combo.AddItems(listItems)
                 pm_Combo.CurrentSelection = 0
            End If

            'Add a list box
             controlType = swPropertyManagerPageControlType_e.swControlType_Listbox
             caption = ""
             alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
             options = swAddControlOptions_e.swControlOptions_Visible + _
                 swAddControlOptions_e.swControlOptions_Enabled
             tip = "Multi-select values in the list box"
             pm_List = pm_Group.AddControl2(ListID, _
                 controlType, caption, alignment, options, tip)
             pm_List.Style = swPropMgrPageListBoxStyle_e.swPropMgrPageListBoxStyle_MultipleItemSelect
             pm_List.Height = 50
             If Not pm_List Is Nothing Then
                 pm_List.Height = 50
                 listItems(0) = "Value 1"
                 listItems(1) = "Value 2"
                 listItems(2) = "Value 3"
                 listItems(3) = "Value 4"
                 pm_List.AddItems(listItems)
                 pm_List.SetSelectedItem(1, True)
             End If

             'Add a label
             pm_Label = pm_Group.AddControl2(LabelID, swPropertyManagerPageControlType_e.swControlType_Label, "Label", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "")

             'Add a slider
             pm_Slider = pm_Group.AddControl2(SliderID, swPropertyManagerPageControlType_e.swControlType_Slider, "Slider", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Slide")

             'Add a radio button
             pm_Radio = pm_Group.AddControl2(RadioID, swPropertyManagerPageControlType_e.swControlType_Option, "Radio button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Select")

             'Add a number box
             pm_Number = pm_Group.AddControl2(NumberID, swPropertyManagerPageControlType_e.swControlType_Numberbox, "Number box", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Spin")

             'Add a button
             pm_Button = pm_Group.AddControl2(ButtonID, swPropertyManagerPageControlType_e.swControlType_Button, "Button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click")

             'Add a bitmap button
             pm_BMPButton = pm_Group.AddControl2(BMPButtonID, swPropertyManagerPageControlType_e.swControlType_BitmapButton, "Bitmap button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click")
             pm_BMPButton.SetStandardBitmaps(swPropertyManagerPageBitmapButtons_e.swBitmapButtonImage_parallel)
```

```
            ' Add another bitmap button that scales with your computer's resolution
            pm_BMPButton2 = pm_Group.AddControl2(BMPButtonID2, swPropertyManagerPageControlType_e.swControlType_BitmapButton, "Bitmap button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click")
            Dim imageList(2) As String
            Dim imageListMasks(2) As String
            imageList(0) = "Pathname_to_nxn_image"
            imageList(1) = "Pathname_to_nnxnn_image"
            imageList(2) = "Pathname_to_nnnxnnn_image"
            imageListMasks(0) = "Pathname_to_mask_nxn_image"
            imageListMasks(1) = "Pathname_to_mask_nnxnn_image"
            imageListMasks(2) = "Pathname_to_mask_nnnxnnn_image"
            pm_BMPButton2.SetBitmapsByName3(imageList, imageListMasks)

            'Add a bitmap
            pm_Bitmap = pm_Group.AddControl2(BitmapID, swPropertyManagerPageControlType_e.swControlType_Bitmap, "Bitmap", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Bitmap")
            pm_Bitmap.SetStandardBitmap(swBitmapControlStandardTypes_e.swBitmapControl_Volume)

            'Add an ActiveX control
            pm_ActiveX = pm_Group.AddControl2(ActiveXID, swPropertyManagerPageControlType_e.swControlType_ActiveX, "ActiveX", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "ActiveX control tip")
            pm_ActiveX.SetClass("ClassID", "LicenseKey")
```

```vb
        Else
            MsgBox("An error occurred while attempting to create the PropertyManager Page", vbCritical)
        End If
    End Sub

    Public Sub AfterActivation() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterActivation
    End Sub

    Public Sub AfterClose() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterClose
    End Sub

    Public Function OnActiveXControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnActiveXControlCreated
         Debug.Print("ActiveX control created")
    End Function

    Public Sub OnButtonPress(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnButtonPress
         Debug.Print("Button clicked")
    End Sub

    Public Sub OnCheckboxCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnCheckboxCheck
    End Sub

    Public Sub OnClose(ByVal Reason As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnClose
        If Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel Then
            'Cancel button clicked
            ClickedCancel = True
        ElseIf Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
            'OK button clicked
            ClickedCancel = False
        End If
    End Sub

    Public Sub OnComboboxEditChanged(ByVal Id As Integer, ByVal Text As String) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnComboboxEditChanged
    End Sub

    Public Sub OnComboboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnComboboxSelectionChanged
    End Sub

    Public Sub OnGainedFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGainedFocus
        Dim varArray As Object
        Debug.Print("Control box " & Id & " gained focus")
        varArray = pm_List.GetSelectedItems
        pm_Combo.CurrentSelection = varArray(0)
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
        Debug.Print("Control box " & Id & " lost focus")
    End Sub

    Public Function OnNextPage() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNextPage
    End Function

    Public Sub OnNumberboxChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNumberboxChanged
         Debug.Print("Number box changed")
    End Sub

    Public Sub OnOptionCheck(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnOptionCheck
         Debug.Print ("Option selected")
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
        Debug.Print("The focus moved to selection box " & Id)
    End Sub

    Public Sub OnSelectionboxListChanged(ByVal Id As Integer, ByVal Count As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxListChanged
        pm_Page.SetCursor(swPropertyManagerPageCursors_e.swPropertyManagerPageCursors_Advance)
        Debug.Print("The list in selection box " & Id & " changed")
    End Sub

    Public Sub OnSliderPositionChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderPositionChanged
         Debug.Print("Slider position changed")
    End Sub

    Public Sub OnSliderTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderTrackingCompleted
    End Sub

    Public Function OnSubmitSelection(ByVal Id As Integer, ByVal Selection As Object, ByVal SelType As Integer, ByRef ItemText As String) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSubmitSelection
        Return True
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
