---
title: "Select Multiple Objects for Selection Boxes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Objects_for_Selection_Boxes_Example_CSharp.htm"
---

# Select Multiple Objects for Selection Boxes Example (C#)

This example shows how to select multiple objects and add the selected objects to different selection boxes on a PropertyManager page.

```vb
 //-------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the assembly to open exists.
 // 2.  Copy  SolidWorksMacro.cs to the project.
 // 3. Add a class module and copy clsPropMgr.cs to that module.
 // 4.  Add the SolidWorks.Interop.swpublished primary interop assembly
 //    reference to your project (click Project > Add Reference,
 //    browse to install_dir\api\redist, select
 //    SolidWorks.Interop.swpublished.dll > OK).
 // 5. Verify that the Tools > Options > System Options > Stop VSTA debugger
 //    on macro exit checkbox is clear.
 //
 // Postconditions:
 // 1. Opens the specified assembly.
 // 2. Creates a PropertyManager page.
 // 3. Examine the PropertyManager page to verify that three selected faces
 //    appear in the top selection box, and two selected faces appear
 //    in the bottom selection box.
 // 4. Close the PropertyManager page.
// NOTE:
 //    *  Reselect the Tools > Options > System Options > Stop VSTA debugger
 //       on macro exit checkbox, if it was selected prior to running the macro.
 //    *  Because the assembly document is used elsewhere,
 //       do not save changes.
 //---------------------------------------------------------------------------
 //   SolidWorksMacro.cs
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace CreatePropertyManagerPageCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public SldWorks swApp;
        public ModelDoc2 swModel;
        public ModelDocExtension swModelDocExt;
        public SelectionMgr swSelectionMgr;
        public const int mark = 1;
        public const int mark2 = 2;
        public clsPropMgr pm;

        public void Main()
        {

            int openDocErrors = 0;
            int openDocWarnings = 0;
            Face2[] selections1 = new Face2[3];
            Face2[] selections2 = new Face2[2];
            int i = 0;
            int j = 0;
            bool status = false;
            int nbrSelections = 0;

            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);
```

```
            string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bladed shaft.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref openDocErrors, ref openDocWarnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Create a new instance of the PropertyManager class
            pm = new clsPropMgr(swApp);
            pm.Show();

            //Selections for top selection box
            status = swModelDocExt.SelectByID2("", "FACE", 0.00369805475952489, 0.0901975482463513, 0.00315907187808762, true, mark, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.00860570843923369, 0.0737431971170679, 0.0039892160950501, true, mark, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0100013029872912, 0.0446884591512742, 0.00996173127262523, true, mark, null, 0);
            nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1);
            nbrSelections = nbrSelections - 1;
            for (i = 0; i <= nbrSelections; i++)
            {
                selections1[i] = (Face2)swSelectionMgr.GetSelectedObject6(i + 1, -1);
            }

            swModel.ClearSelection2(true);

            //Selections for bottom selection box
            status = swModelDocExt.SelectByID2("", "FACE", -0.0264206017159268, -0.00342602957275062, 0.00987615560137556, true, mark2, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.00128130257782288, -0.00354158999988385, 0.0177003152412567, true, mark2, null, 0);
            nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1);
            nbrSelections = nbrSelections - 1;
            for (j = 0; j <= nbrSelections; j++)
            {
                selections2[j] = (Face2)swSelectionMgr.GetSelectedObject6(j + 1, -1);
            }

            swModel.ClearSelection2(true);

            //Populate selection boxes
            SelectBoxFaces1(selections1, mark);
            SelectBoxFaces2(selections2, mark2);

        }
        private void SelectBoxFaces1(Face2[] selections, int selectionBoxMark)
        {
            SelectData swSelectData = default(SelectData);
            swSelectData = (SelectData)swSelectionMgr.CreateSelectData();
            swSelectData.Mark = selectionBoxMark;
            swModelDocExt.MultiSelect2(selections, true, swSelectData);
        }
        private void SelectBoxFaces2(Face2[] selections, int selectionBoxMark)
        {
            SelectData swSelectData = default(SelectData);
            swSelectData = (SelectData)swSelectionMgr.CreateSelectData();
            swSelectData.Mark = selectionBoxMark;
            swModelDocExt.MultiSelect2(selections, true, swSelectData);
        }

    }

}
```

[Back to top](#Top)

```vb
 // clsPropMgr.cs
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace CreatePropertyManagerPageCSharp.csproj
{
    [ComVisibleAttribute(true)]

    public class clsPropMgr : PropertyManagerPage2Handler9
    {
        //General objects required for the PropertyManager page
        PropertyManagerPage2 pm_Page;
        PropertyManagerPageGroup pm_Group;
        PropertyManagerPageSelectionbox pm_Selection;
        PropertyManagerPageSelectionbox pm_Selection2;

        //Each object in the page needs a unique ID
        const int GroupID = 1;
        const int SelectionID = 3;
        const int ComboID = 4;
        const int ListID = 5;
        const int Selection2ID = 6;

        public void Show()
        {
            pm_Page.Show2(0);
        }

        //The following runs when a new instance
        //of the class is created
        public clsPropMgr(SldWorks swApp)
        {

            string PageTitle = null;
            string caption = null;
            string tip = null;
            long options = 0;
            int longerrors = 0;
            int controlType = 0;
            int alignment = 0;

            //Set the variables for the page
            PageTitle = "MultiSelect2 Test";
            options = (int)swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton + (int)swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton;

            //Create the PropertyManager page
            pm_Page = (PropertyManagerPage2)swApp.CreatePropertyManagerPage(PageTitle, (int)options, this, ref longerrors);

            //Make sure that the page was created properly
            if (longerrors == (int)swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay)
            {
                //Begin adding the controls to the page

                //Create the group box
                caption = "";
                options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded;
                pm_Group = (PropertyManagerPageGroup)pm_Page.AddGroupBox(GroupID, caption, (int)options);

                //Create two selection boxes
                controlType = (int)swPropertyManagerPageControlType_e.swControlType_Selectionbox;
                caption = "";
                alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
                options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
                tip = "Select multiple faces.";

                pm_Selection = (PropertyManagerPageSelectionbox)pm_Group.AddControl(SelectionID, (short)controlType, caption, (short)alignment, (int)options, tip);
                pm_Selection2 = (PropertyManagerPageSelectionbox)pm_Group.AddControl(Selection2ID, (short)controlType, caption, (short)alignment, (int)options, tip);

                'Only faces can populate the selection boxes
                swSelectType_e[] filters = new swSelectType_e[1];
                filters[0] = swSelectType_e.swSelFACES;

                object filterObj = null;
                filterObj = filters;

                pm_Selection.SingleEntityOnly = false;
                pm_Selection.AllowMultipleSelectOfSameEntity = true;
                pm_Selection.Height = 50;
                pm_Selection.SetSelectionFilters(filterObj);
                pm_Selection.Mark = SolidWorksMacro.mark;

                pm_Selection2.SingleEntityOnly = false;
                pm_Selection2.AllowMultipleSelectOfSameEntity = true;
                pm_Selection2.Height = 50;
                pm_Selection2.SetSelectionFilters(filterObj);
                pm_Selection2.Mark = SolidWorksMacro.mark2;
            }
            else
            {
                //If the page is not created
                System.Windows.Forms.MessageBox.Show("An error occurred while attempting to create the " + "PropertyManager Page");

            }
        }

        #region IPropertyManagerPage2Handler9 Members

        void IPropertyManagerPage2Handler9.AfterActivation()
        {

            throw new Exception("The method or operation is not implemented.");
        }

        void IPropertyManagerPage2Handler9.AfterClose()
        {

            throw new Exception("The method or operation is not implemented.");
        }

        int IPropertyManagerPage2Handler9.OnActiveXControlCreated(int Id, bool Status)
        {

            throw new Exception("The method or operation is not implemented.");
        }

        void IPropertyManagerPage2Handler9.OnButtonPress(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnCheckboxCheck(int Id, bool Checked)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnClose(int Reason)
        {

            if (Reason == (int)swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel)
            {
                //Do something when the cancel button is clicked
            }
            else if (Reason == (int)swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay)
            {
                //Do something else when the OK button is clicked
            }

        }

        void IPropertyManagerPage2Handler9.OnComboboxEditChanged(int Id, string Text)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnComboboxSelectionChanged(int Id, int Item)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnGainedFocus(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnGroupCheck(int Id, bool Checked)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnGroupExpand(int Id, bool Expanded)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        bool IPropertyManagerPage2Handler9.OnHelp()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        bool IPropertyManagerPage2Handler9.OnKeystroke(int Wparam, int Message, int Lparam, int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnListboxSelectionChanged(int Id, int Item)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnLostFocus(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        bool IPropertyManagerPage2Handler9.OnNextPage()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnNumberboxChanged(int Id, double Value)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnOptionCheck(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnPopupMenuItem(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnPopupMenuItemUpdate(int Id, ref int retval)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        bool IPropertyManagerPage2Handler9.OnPreview()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        bool IPropertyManagerPage2Handler9.OnPreviousPage()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnRedo()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnSelectionboxCalloutCreated(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnSelectionboxCalloutDestroyed(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnSelectionboxFocusChanged(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnSelectionboxListChanged(int Id, int Count)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnSliderPositionChanged(int Id, double Value)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnSliderTrackingCompleted(int Id, double Value)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        bool IPropertyManagerPage2Handler9.OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
        {

            // This method must return true for selections to occur
            Debug.Print("OnSubmitSelection fired.");
            return true;

        }

        bool IPropertyManagerPage2Handler9.OnTabClicked(int Id)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnTextboxChanged(int Id, string Text)
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnUndo()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnWhatsNew()
        {

            throw new Exception("The method or operation is not implemented.");

        }

        void IPropertyManagerPage2Handler9.OnListboxRMBUp(int Id, int PosX, int PosY)
        {
            throw new Exception("The method or operation is not implemented.");
        }

        int IPropertyManagerPage2Handler9.OnWindowFromHandleControlCreated(int Id, bool Status)
        {
            throw new Exception("The method or operation is not implemented.");
        }

        void IPropertyManagerPage2Handler9.OnNumberBoxTrackingCompleted(int Id, double Value)
        {
            throw new Exception("The method or operation is not implemented.");
        }

        #endregion

    }

}
```

[Back to top](#Top)
