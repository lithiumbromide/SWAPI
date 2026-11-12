---
title: "Activate PropertyManager Page Tab Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Property_Manager_Page_Tab_Example_CSharp.htm"
---

# Activate PropertyManager Page Tab Example (C#)

The following code example demonstrates how SOLIDWORKS add-ins can use IPropertyManagerPageTab.Activate to programmatically select a tab on a SOLIDWORKS PropertyManager page.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Copy Main to the main module.
// 2. Click Project > Add Class > Add and copy Class1 to Class1.cs.
// 3. Click Project > Add Reference, browse to install_dir\api\redist\, select
//    SolidWorks.Interop.swpublished.dll > OK.
// 4. Open an assembly that has multiple components.
//
// Postconditions:
// 1. Creates a PropertyManager page called Materials and Dimensions
//    with two tabs:
//    * Materials
//    * Dimensions
// 2. Selects the Materials tab.
// 3. Examine the PropertyManager page.
//----------------------------------------------------------------------------
//Main
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        public SldWorks swApp;
        public ModelDoc2 Part;
        public SelectionMgr SelMgr;
        public Class1 pm;

        public void Main()
        {
            Part = (ModelDoc2)swApp.ActiveDoc;
            SelMgr = (SelectionMgr)Part.SelectionManager;

            //Create a new instance of the PropertyManager class
            pm = new Class1(swApp);
            pm.Show();
        }
    }
}
```

```
Back to top
```

```
//Class1
using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.InteropServices;
using SolidWorks.Interop.swpublished;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

namespace Macro1CSharp.csproj
{
    [ComVisibleAttribute(true)]

    public class Class1 : PropertyManagerPage2Handler6
    {
        PropertyManagerPage2 pm_Page;
        bool ClickedCancel;
        public void Show()
        {
            pm_Page.Show();

        }

        public Class1(SolidWorks.Interop.sldworks.SldWorks swApp)
        {
            //General objects required for the PropertyManager page
            PropertyManagerPageTab pm_Page_Tab = default(PropertyManagerPageTab);
            PropertyManagerPageTab pm_Page_Tab_2 = default(PropertyManagerPageTab);
            PropertyManagerPageGroup pm_Group = default(PropertyManagerPageGroup);
            PropertyManagerPageSelectionbox pm_Selection = default(PropertyManagerPageSelectionbox);

            //Each object in the page needs a unique ID
            const int GroupID = 1;
            const int SelectionID = 3;
            const int Tab1ID = 1;
            const int Tab2ID = 2;
            string PageTitle = null;
            string caption = null;
            string tip = null;
            int options = 0;
            int longerrors = 0;
            short controlType = 0;
            short alignment = 0;

            //Set the variables for the page
            PageTitle = "Materials and Dimensions";
            options = (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_OkayButton + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_CancelButton + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton;
            pm_Page = (PropertyManagerPage2)swApp.CreatePropertyManagerPage(PageTitle, options, this, ref longerrors);

            // Create page tabs
            pm_Page_Tab = (PropertyManagerPageTab)pm_Page.AddTab(Tab1ID, "Materials", "", 0);
            pm_Page_Tab_2 = (PropertyManagerPageTab)pm_Page.AddTab(Tab2ID, "Dimensions", "", 0);

            // Activate the first tab
            pm_Page_Tab.Activate();

            //Begin adding the controls to the page tab

            //Create the group box
            caption = "Materials";
            options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded;
            pm_Group = (PropertyManagerPageGroup)pm_Page_Tab.AddGroupBox(GroupID, caption, options);

            //Create selection box
            controlType = (short)swPropertyManagerPageControlType_e.swControlType_Selectionbox;
            caption = "";

            // No caption for selection boxes
            alignment = (short)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
            options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
            tip = "Select an edge, face, vertex, solid body, or a component";
            pm_Selection = (PropertyManagerPageSelectionbox)pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip);
            long[] filters = new long[7];
            filters[0] = (long)swSelectType_e.swSelEDGES;
            filters[1] = (long)swSelectType_e.swSelREFEDGES;
            filters[2] = (long)swSelectType_e.swSelFACES;
            filters[3] = (long)swSelectType_e.swSelVERTICES;
            filters[4] = (long)swSelectType_e.swSelSOLIDBODIES;
            filters[5] = (long)swSelectType_e.swSelCOMPONENTS;
            filters[6] = (long)swSelectType_e.swSelCOMPSDONTOVERRIDE;

            pm_Selection.SingleEntityOnly = false;
            pm_Selection.AllowMultipleSelectOfSameEntity = true;
            pm_Selection.Height = 50;
            pm_Selection.SetSelectionFilters(filters);
        }

        private void PropertyManagerPage2Handler6_AfterActivation()
        {
        }

        private void PropertyManagerPage2Handler6_AfterClose()
        {
        }

        private void PropertyManagerPage2Handler6_OnClose(int Reason)
        {
            if (Reason == (int)swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel)
            {
                //Cancel button was clicked
                ClickedCancel = true;
            }
            else if (Reason == (int)swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay)
            {
                //OK button was clicked
                ClickedCancel = false;
            }

            //Store the density and material name values based
            //on the combo-box selection
        }

        private bool PropertyManagerPage2Handler6_OnHelp()
        {
            return false;
        }

        private bool PropertyManagerPage2Handler6_OnNextPage()
        {
            return false;
        }

        private bool PropertyManagerPage2Handler6_OnPreview()
        {
            return false;
        }

        private bool PropertyManagerPage2Handler6_OnPreviousPage()
        {
            return false;
        }

        private void PropertyManagerPage2Handler6_OnRedo()
        {
        }

        private void PropertyManagerPage2Handler6_OnUndo()
        {
        }

        private void PropertyManagerPage2Handler6_OnWhatsNew()
        {
        }

        public void AfterActivation()
        {
        }

        public void AfterClose()
        {
        }

        public int OnActiveXControlCreated(int Id, bool Status)
        {
            return 0;
        }

        public void OnButtonPress(int Id)
        {
        }

        public void OnCheckboxCheck(int Id, bool Checked)
        {
        }

        public void OnClose(int Reason)
        {
        }

        public void OnComboboxEditChanged(int Id, string Text)
        {
        }

        public void OnComboboxSelectionChanged(int Id, int Item)
        {
        }

        public void OnGroupCheck(int Id, bool Checked)
        {
        }

        public void OnGroupExpand(int Id, bool Expanded)
        {
        }

        public bool OnHelp()
        {
            return false;
        }

        public bool OnKeystroke(int Wparam, int Message, int Lparam, int Id)
        {
            return false;
        }

        public void OnListboxSelectionChanged(int Id, int Item)
        {
        }

        public bool OnNextPage()
        {
            return false;
        }

        public void OnNumberboxChanged(int Id, double Value)
        {
        }

        public void OnOptionCheck(int Id)
        {
        }

        public void OnPopupMenuItem(int Id)
        {
        }

        public void OnPopupMenuItemUpdate(int Id, ref int retval)
        {
        }

        public bool OnPreview()
        {
            return false;
        }

        public bool OnPreviousPage()
        {
            return false;
        }

        public void OnRedo()
        {
        }

        public void OnSelectionboxCalloutCreated(int Id)
        {
        }

        public void OnSelectionboxCalloutDestroyed(int Id)
        {
        }

        public void OnSelectionboxFocusChanged(int Id)
        {
        }

        public void OnSelectionboxListChanged(int Id, int Count)
        {
        }

        public void OnSliderPositionChanged(int Id, double Value)
        {
        }

        public void OnSliderTrackingCompleted(int Id, double Value)
        {
        }

        public bool OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
        {
            return false;
        }

        public bool OnTabClicked(int Id)
        {
            return false;
        }

        public void OnTextboxChanged(int Id, string Text)
        {
        }

        public void OnUndo()
        {
        }

        public void OnWhatsNew()
        {
        }
    }
}
```

```
Back to top
```
