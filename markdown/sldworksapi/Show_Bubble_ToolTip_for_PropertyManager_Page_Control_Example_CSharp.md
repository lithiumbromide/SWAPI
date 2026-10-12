---
title: "Show Bubble ToolTip for PropertyManager Page Control Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Bubble_ToolTip_for_PropertyManager_Page_Control_Example_CSharp.htm"
---

# Show Bubble ToolTip for PropertyManager Page Control Example (C#)

This example shows how to create a PropertyManager page. When the check box on the PropertyManager page is selected, a bubble ToolTip is displayed. This type of ToolTip is useful for validating data typed or selected by users in controls on a PropertyManager page.

```
//--------------------------------------
// Preconditions:
// 1. Copy SolidWorksMacro.cs to your project.
// 2. Add a class module called PropMgrHdlr.cs and copy
//    PropMgrHdlr.cs to that module.
// 3. Click Project > Add Reference, browse to install_dir\api\redist,
//    select SolidWorks.Interop.swpublished.dll > OK.
// 4. Verify that the Tools > Options > System Options > Stop VSTA debugger
//    on macro exit checkbox is clear.
// 5. Open a part.
//
// Postconditions:
// 1. Creates and displays a PropertyManager page.
// 2. Select Sample check box to display a bubble ToolTip.
// 3. Click outside the bubble ToolTip to close it.
//    NOTE: Clearing Sample check box does not display
//    the bubble ToolTip.
//---------------------------------------
//SolidWorksMacro.cs
```

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
namespace CreatePropertyManagerPage_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public ModelDoc2 swModel;
         public SelectionMgr swSelMgr;
         public PropMgrHdlr pm;
         public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             //Create a new instance of the PropertyManager class
             pm = new PropMgrHdlr(swApp);
             pm.Show();
        }
        public SldWorks swApp;
    }
}

//PropMgrHdlr.cs
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
using System;
using System.Runtime.InteropServices;
[ComVisibleAttribute(true)]
public class PropMgrHdlr : IPropertyManagerPage2Handler6
{
    //Required for PropertyManager page controls
    //Objects required for the PropertyManager page
    PropertyManagerPage2 pm_Page;
    PropertyManagerPageGroup pm_Group;
    PropertyManagerPageSelectionbox pm_Selection;
    PropertyManagerPageControl pm_Control;

    //Each object in the page needs a unique ID
    const int GroupID = 1;
    const int SelectionID = 3;
    const int ControlID = 4;
    string bubbleToolTipTitle;
    string bubbleToolTipMessage;
    string bubbleToolTipBmpFile;
    public void Show()
    {
        pm_Page.Show();
    }
    public PropMgrHdlr(SolidWorks.Interop.sldworks.SldWorks swApp)
    {
        string PageTitle = null;
        string caption = null;
        string tip = null;
        int options = 0;
        int longerrors = 0;
        int controlType = 0;
        int alignment = 0;
```

```
        //Set the variables for the page
        PageTitle = "Sample PropertyManager page";
        options = (int)swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton + (int)swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton;

        //Create the PropertyManager page
        pm_Page = (PropertyManagerPage2)swApp.CreatePropertyManagerPage(PageTitle, options, this, ref longerrors);
        //Make sure that the page was created properly
        if (longerrors == (int)swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay)
        {
            //Begin adding the controls to the page
            //Create the group box
            caption = "Sample Group Box";
            options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded;
            pm_Group = (PropertyManagerPageGroup)pm_Page.AddGroupBox(GroupID, caption, options);
            //Create selection box
            controlType = (int)swPropertyManagerPageControlType_e.swControlType_Selectionbox;
            caption = "";
            // No caption for selection boxes
            alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
            options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
            tip = "Select an edge, face, vertex, solid body, or a component";
            pm_Selection = (PropertyManagerPageSelectionbox)pm_Group.AddControl(SelectionID, (short)controlType, caption, (short)alignment, options, tip);
            int[] filters = new int[7];
            filters[0] = (int)swSelectType_e.swSelEDGES;
            filters[1] = (int)swSelectType_e.swSelREFEDGES;
            filters[2] = (int)swSelectType_e.swSelFACES;
            filters[3] = (int)swSelectType_e.swSelVERTICES;
            filters[4] = (int)swSelectType_e.swSelSOLIDBODIES;
            filters[5] = (int)swSelectType_e.swSelCOMPONENTS;
            filters[6] = (int)swSelectType_e.swSelCOMPSDONTOVERRIDE;
            pm_Selection.SingleEntityOnly = false;
            pm_Selection.AllowMultipleSelectOfSameEntity = true;
            pm_Selection.Height = 50;
            pm_Selection.SetSelectionFilters(filters);
            // Create check box
            controlType = (int)swPropertyManagerPageControlType_e.swControlType_Checkbox;
            caption = "Sample check box";
            alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
            options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
            tip = "Check box";
            pm_Control = (PropertyManagerPageControl)pm_Group.AddControl(ControlID, (short)controlType, caption, (short)alignment, options, tip);
```

```
            bubbleToolTipTitle = "Sample bubble ToolTip Title";
            bubbleToolTipMessage = "Sample bubble ToolTip message";
            bubbleToolTipBmpFile = "";
        }
        else
        {
            //If the page is not created
            System.Windows.Forms.MessageBox.Show("An error occurred while attempting to create the " + "PropertyManager Page");
        }
    }
    private void PropertyManagerPage2Handler6_OnCheckboxCheck(int Id, bool isChecked)
    {
        if (isChecked)
        {
            pm_Control.ShowBubbleTooltip(bubbleToolTipTitle, bubbleToolTipMessage, bubbleToolTipBmpFile);
        }
        else
        {
        }
    }
    void IPropertyManagerPage2Handler6.OnCheckboxCheck(int Id, bool isChecked)
    {
        PropertyManagerPage2Handler6_OnCheckboxCheck(Id, isChecked);
    }
    private void PropertyManagerPage2Handler6_AfterClose()
    {
    }
    void IPropertyManagerPage2Handler6.AfterClose()
    {
        PropertyManagerPage2Handler6_AfterClose();
    }
    private void PropertyManagerPage2Handler6_OnButtonPress(int Id)
    {
    }
    void IPropertyManagerPage2Handler6.OnButtonPress(int Id)
    {
        PropertyManagerPage2Handler6_OnButtonPress(Id);
    }
    private void PropertyManagerPage2Handler6_OnClose(int Reason)
    {
    }
    void IPropertyManagerPage2Handler6.OnClose(int Reason)
    {
        PropertyManagerPage2Handler6_OnClose(Reason);
    }
    private void PropertyManagerPage2Handler6_OnSelectionboxCalloutCreated(int Id)
    {
    }
    void IPropertyManagerPage2Handler6.OnSelectionboxCalloutCreated(int Id)
    {
        PropertyManagerPage2Handler6_OnSelectionboxCalloutCreated(Id);
    }
    private void PropertyManagerPage2Handler6_OnComboboxEditChanged(int Id, string Text)
    {
    }
    void IPropertyManagerPage2Handler6.OnComboboxEditChanged(int Id, string Text)
    {
        PropertyManagerPage2Handler6_OnComboboxEditChanged(Id, Text);
    }
    private void PropertyManagerPage2Handler6_OnComboboxSelectionChanged(int Id, int Item)
    {
    }
    void IPropertyManagerPage2Handler6.OnComboboxSelectionChanged(int Id, int Item)
    {
        PropertyManagerPage2Handler6_OnComboboxSelectionChanged(Id, Item);
    }
    private void PropertyManagerPage2Handler6_OnGroupCheck(int Id, bool Checked)
    {
    }
    void IPropertyManagerPage2Handler6.OnGroupCheck(int Id, bool Checked)
    {
        PropertyManagerPage2Handler6_OnGroupCheck(Id, Checked);
    }
    private void PropertyManagerPage2Handler6_OnGroupExpand(int Id, bool Expanded)
    {
    }
    void IPropertyManagerPage2Handler6.OnGroupExpand(int Id, bool Expanded)
    {
        PropertyManagerPage2Handler6_OnGroupExpand(Id, Expanded);
    }
    private bool PropertyManagerPage2Handler6_OnHelp()
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnHelp()
    {
        return PropertyManagerPage2Handler6_OnHelp();
    }
    private bool PropertyManagerPage2Handler6_OnKeystroke(int Wparam, int Message, int Lparam, int Id)
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnKeystroke(int Wparam, int Message, int Lparam, int Id)
    {
        return PropertyManagerPage2Handler6_OnKeystroke(Wparam, Message, Lparam, Id);
    }
    private void PropertyManagerPage2Handler6_OnListboxSelectionChanged(int Id, int Item)
    {
    }
    void IPropertyManagerPage2Handler6.OnListboxSelectionChanged(int Id, int Item)
    {
        PropertyManagerPage2Handler6_OnListboxSelectionChanged(Id, Item);
    }
    private bool PropertyManagerPage2Handler6_OnNextPage()
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnNextPage()
    {
        return PropertyManagerPage2Handler6_OnNextPage();
    }
    private void PropertyManagerPage2Handler6_OnNumberboxChanged(int Id, double Value)
    {
    }
    void IPropertyManagerPage2Handler6.OnNumberboxChanged(int Id, double Value)
    {
        PropertyManagerPage2Handler6_OnNumberboxChanged(Id, Value);
    }
    private void PropertyManagerPage2Handler6_OnOptionCheck(int Id)
    {
    }
    void IPropertyManagerPage2Handler6.OnOptionCheck(int Id)
    {
        PropertyManagerPage2Handler6_OnOptionCheck(Id);
    }
    private void PropertyManagerPage2Handler6_OnPopupMenuItem(int Id)
    {
    }
    void IPropertyManagerPage2Handler6.OnPopupMenuItem(int Id)
    {
        PropertyManagerPage2Handler6_OnPopupMenuItem(Id);
    }
    private void PropertyManagerPage2Handler6_OnPopupMenuItemUpdate(int Id, ref int retval)
    {
    }
    void IPropertyManagerPage2Handler6.OnPopupMenuItemUpdate(int Id, ref int retval)
    {
        PropertyManagerPage2Handler6_OnPopupMenuItemUpdate(Id, ref retval);
    }
    private bool PropertyManagerPage2Handler6_OnPreview()
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnPreview()
    {
        return PropertyManagerPage2Handler6_OnPreview();
    }
    private bool PropertyManagerPage2Handler6_OnPreviousPage()
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnPreviousPage()
    {
        return PropertyManagerPage2Handler6_OnPreviousPage();
    }
    private void PropertyManagerPage2Handler6_OnRedo()
    {
    }
    void IPropertyManagerPage2Handler6.OnRedo()
    {
        PropertyManagerPage2Handler6_OnRedo();
    }
    private void PropertyManagerPage2Handler6_OnSelectionboxCalloutDestroyed(int Id)
    {
    }
    void IPropertyManagerPage2Handler6.OnSelectionboxCalloutDestroyed(int Id)
    {
        PropertyManagerPage2Handler6_OnSelectionboxCalloutDestroyed(Id);
    }
    private void PropertyManagerPage2Handler6_OnSelectionboxFocusChanged(int Id)
    {
    }
    void IPropertyManagerPage2Handler6.OnSelectionboxFocusChanged(int Id)
    {
        PropertyManagerPage2Handler6_OnSelectionboxFocusChanged(Id);
    }
    private void PropertyManagerPage2Handler6_OnSelectionboxListChanged(int Id, int Count)
    {
    }
    void IPropertyManagerPage2Handler6.OnSelectionboxListChanged(int Id, int Count)
    {
        PropertyManagerPage2Handler6_OnSelectionboxListChanged(Id, Count);
    }
    private void PropertyManagerPage2Handler6_OnSliderPositionChanged(int Id, double Value)
    {
    }
    void IPropertyManagerPage2Handler6.OnSliderPositionChanged(int Id, double Value)
    {
        PropertyManagerPage2Handler6_OnSliderPositionChanged(Id, Value);
    }
    private void PropertyManagerPage2Handler6_OnSliderTrackingCompleted(int Id, double Value)
    {
    }
    void IPropertyManagerPage2Handler6.OnSliderTrackingCompleted(int Id, double Value)
    {
        PropertyManagerPage2Handler6_OnSliderTrackingCompleted(Id, Value);
    }
    private bool PropertyManagerPage2Handler6_OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
    {
        return PropertyManagerPage2Handler6_OnSubmitSelection(Id, Selection, SelType, ref ItemText);
    }
    private bool PropertyManagerPage2Handler6_OnTabClicked(int Id)
    {
        return true;
    }
    bool IPropertyManagerPage2Handler6.OnTabClicked(int Id)
    {
        return PropertyManagerPage2Handler6_OnTabClicked(Id);
    }
    private void PropertyManagerPage2Handler6_OnTextboxChanged(int Id, string Text)
    {
    }
    void IPropertyManagerPage2Handler6.OnTextboxChanged(int Id, string Text)
    {
        PropertyManagerPage2Handler6_OnTextboxChanged(Id, Text);
    }
    private void PropertyManagerPage2Handler6_OnUndo()
    {
    }
    void IPropertyManagerPage2Handler6.OnUndo()
    {
        PropertyManagerPage2Handler6_OnUndo();
    }
    private void PropertyManagerPage2Handler6_OnWhatsNew()
    {
    }
    void IPropertyManagerPage2Handler6.OnWhatsNew()
    {
        PropertyManagerPage2Handler6_OnWhatsNew();
    }
    private int PropertyManagerPage2Handler6_OnActiveXControlCreated(int Id, bool Status)
    {
        return 0;
    }
    int IPropertyManagerPage2Handler6.OnActiveXControlCreated(int Id, bool Status)
    {
        return PropertyManagerPage2Handler6_OnActiveXControlCreated(Id, Status);
    }
    private void PropertyManagerPage2Handler6_AfterActivation()
    {
    }
    void IPropertyManagerPage2Handler6.AfterActivation()
    {
        PropertyManagerPage2Handler6_AfterActivation();
    }
}
```
