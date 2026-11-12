---
title: "Create PropertyManager Page Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Create_PropertyManager_Page_Example_CSharp.htm"
---

# Create PropertyManager Page Example (C#)

This example shows how to create a PropertyManager page that contains the following controls:

- ActiveX
- Bitmap
- Bitmap button
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

NOTE: If the model is an assembly that contains multiple components, and you want to allow the user to select edges, faces, or vertices, then you must specify swSelCOMPSDONTOVERRIDE for parameter SelType of IPropertyManagerPageSelectionbox::SetSelectionFilters. Otherwise, if the user attempts to select an edge, face, or vertex, then the entire component might get selected and not the edge, face, or vertex. This example demonstrates how to specify SelType.

```vb
//-------------------------------------------------------------------------
 // Preconditions:
 // 1  Copy  Modules - Main to your project.
 // 2. Copy  Class Modules - clsPropMgr to a class in your project.
 // 3. Right-click the name of your project, select
 //    Add Reference, browse install_dir\api\redist\, select
 //    SolidWorks.Interop.swpublished.dll, and click OK.
 // 4. Ensure that the namespace and class names in the sample code
 //    match that of your C# project.
  // 5. Ensure that the specified assembly document exists.
 // 6. Modify ClassID and LicenseKey parameters in
 //    IPropertyManagerPageActiveX::SetClass to add your ActiveX control
 //    to the PropertyManager page.
 // 7. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a PropertyManager page called Comps.
 // 2. Creates the specified controls.
 // 3. Inspect the contents of Comps and the Immediate Window as
 //    you use the controls.
 // 4. Click the green check mark to close the PropertyManager page.
 //
 // NOTES:
 // * After running this macro, select
 //   Tools > Options > System Options > Stop VSTA debugger
 //   on macro exit.
 // * Because the assembly document is used elsewhere,
 //   do not save any changes when closing the document.
 //---------------------------------------------------------------------------
//  Modules - Main
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace CreatePropertyManagerPageExample_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public ModelDoc2 Part;
        public clsPropMgr pm;
        public void Main()
        {
            int openDocErrors = 0;
            int openDocWarnings = 0;

            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);
            Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bladed shaft.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref openDocErrors, ref openDocWarnings);

            //Create a new instance of the PropertyManager class
            pm = new clsPropMgr(swApp);
            pm.Show();
        }
        public SldWorks swApp;
    }
```

}

[Back to top](#Top)

```vb
//  Class Modules - clsPropMgr
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
namespace CreatePropertyManagerPageExample_CSharp.csproj
{
    [ComVisibleAttribute(true)]
    public class clsPropMgr : PropertyManagerPage2Handler9
    {

          //Control objects required for the PropertyManager page
         PropertyManagerPage2 pm_Page;
         PropertyManagerPageGroup pm_Group;
         PropertyManagerPageSelectionbox pm_Selection;
         PropertyManagerPageSelectionbox pm_Selection2;
         PropertyManagerPageLabel pm_Label;
         PropertyManagerPageCombobox pm_Combo;
         PropertyManagerPageListbox pm_List;
         PropertyManagerPageNumberbox pm_Number;
         PropertyManagerPageOption pm_Radio;
         PropertyManagerPageSlider pm_Slider;
         PropertyManagerPageTab pm_Tab;
         PropertyManagerPageButton pm_Button;
         PropertyManagerPageBitmapButton pm_BMPButton;
         PropertyManagerPageBitmap pm_Bitmap;
         PropertyManagerPageActiveX pm_ActiveX;

         //Each control in the page needs a unique ID
         const int GroupID = 1;
         const int LabelID = 2;
         const int SelectionID = 3;
         const int ComboID = 4;
         const int ListID = 5;
         const int Selection2ID = 6;
         const int NumberID = 7;
         const int RadioID = 8;
         const int SliderID = 9;
         const int TabID = 10;
         const int ButtonID = 11;
         const int BMPButtonID = 12;
         const int BitmapID = 13;
         const int ActiveXID = 14;

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
            string[] listItems = new string[4];

            //Set the variables for the page
            PageTitle = "Comps";
            options = (int)swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton + (int)swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton;

            //Create the PropertyManager page
            pm_Page = (PropertyManagerPage2)swApp.CreatePropertyManagerPage(PageTitle, (int)options, this, ref longerrors);

            //Make sure that the page was created properly
            if (longerrors == (int)swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay)
            {
                //Add the controls to the page

                  //Add a tab
          pm_Tab = pm_Page.AddTab(TabID, "Application", "", 0);

          //Add a group box to the tab
          caption = "Controls";
          options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded;
          pm_Group = (PropertyManagerPageGroup)pm_Tab.AddGroupBox(GroupID, caption, options);

 //Add two selection boxes
                controlType = (int)swPropertyManagerPageControlType_e.swControlType_Selectionbox;
                caption = "";

                alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
                options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
                tip = "Select an edge, face, vertex, solid body, or a component";
                pm_Selection = (PropertyManagerPageSelectionbox)pm_Group.AddControl2(SelectionID, (short)controlType, caption, (short)alignment, (int)options, tip);
                pm_Selection2 = (PropertyManagerPageSelectionbox)pm_Group.AddControl2(Selection2ID, (short)controlType, caption, (short)alignment, (int)options, tip);

                swSelectType_e[] filters = new swSelectType_e[7];
                filters[0] = swSelectType_e.swSelEDGES;
                filters[1] = swSelectType_e.swSelREFEDGES;
                filters[2] = swSelectType_e.swSelFACES;
                filters[3] = swSelectType_e.swSelVERTICES;
                filters[4] = swSelectType_e.swSelSOLIDBODIES;
                filters[5] = swSelectType_e.swSelCOMPONENTS;
                filters[6] = swSelectType_e.swSelCOMPSDONTOVERRIDE;

                object filterObj = null;
                filterObj = filters;

                pm_Selection.SingleEntityOnly = false;
                pm_Selection.AllowMultipleSelectOfSameEntity = true;
                pm_Selection.Height = 50;
                pm_Selection.SetSelectionFilters(filterObj);

                pm_Selection2.SingleEntityOnly = false;
                pm_Selection2.AllowMultipleSelectOfSameEntity = true;
                pm_Selection2.Height = 50;
                pm_Selection2.SetSelectionFilters(filterObj);

                //Add a combo box
                controlType = (int)swPropertyManagerPageControlType_e.swControlType_Combobox;
                caption = "";
                alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
                options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
                tip = "Select a value";
                pm_Combo = (PropertyManagerPageCombobox)pm_Group.AddControl2(ComboID, (short)controlType, caption, (short)alignment, (int)options, tip);
                if ((pm_Combo != null))
                {
                    pm_Combo.Height = 50;
                    listItems[0] = "Value 1";
                    listItems[1] = "Value 2";
                    listItems[2] = "Value 3";
                    listItems[3] = "Value 4";
                    pm_Combo.AddItems(listItems);
                    pm_Combo.CurrentSelection = 0;
                }

                //Add a list box
                controlType = (int)swPropertyManagerPageControlType_e.swControlType_Listbox;
                caption = "";
                alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
                options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
                tip = "Multi-select values in the list box";
                pm_List = (PropertyManagerPageListbox)pm_Group.AddControl2(ListID, (short)controlType, caption, (short)alignment, (int)options, tip);

                if ((pm_List != null))
                {
                    pm_List.Style = (int)swPropMgrPageListBoxStyle_e.swPropMgrPageListBoxStyle_MultipleItemSelect;
                    pm_List.Height = 50;
                    listItems[0] = "Value 1";
                    listItems[1] = "Value 2";
                    listItems[2] = "Value 3";
                    listItems[3] = "Value 4";
                    pm_List.AddItems(listItems);
                    pm_List.SetSelectedItem(1, true);
                }
                 //Add a label
         pm_Label = (PropertyManagerPageLabel)pm_Group.AddControl2(LabelID, (int)swPropertyManagerPageControlType_e.swControlType_Label, "Label", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "");

         //Add a slider
         pm_Slider = (PropertyManagerPageSlider)pm_Group.AddControl2(SliderID, (int)swPropertyManagerPageControlType_e.swControlType_Slider, "Slider", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Slide");

         //Add a radio button
         pm_Radio = (PropertyManagerPageOption)pm_Group.AddControl2(RadioID, (int)swPropertyManagerPageControlType_e.swControlType_Option, "Radio button", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Select");

         //Add a number box
         pm_Number = (PropertyManagerPageNumberbox)pm_Group.AddControl2(NumberID, (int)swPropertyManagerPageControlType_e.swControlType_Numberbox, "Number box", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Spin");

         //Add a button
         pm_Button = (PropertyManagerPageButton)pm_Group.AddControl2(ButtonID, (int)swPropertyManagerPageControlType_e.swControlType_Button, "Button", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click");

         //Add a bitmap button
         pm_BMPButton = (PropertyManagerPageBitmapButton)pm_Group.AddControl2(BMPButtonID, (int)swPropertyManagerPageControlType_e.swControlType_BitmapButton, "Bitmap button", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click");
         pm_BMPButton.SetStandardBitmaps((int)swPropertyManagerPageBitmapButtons_e.swBitmapButtonImage_parallel);

         //Add a bitmap
         pm_Bitmap = (PropertyManagerPageBitmap)pm_Group.AddControl2(BitmapID, (int)swPropertyManagerPageControlType_e.swControlType_Bitmap, "Bitmap", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Bitmap");
         pm_Bitmap.SetStandardBitmap((int)swBitmapControlStandardTypes_e.swBitmapControl_Volume);

         //Add an ActiveX control
         pm_ActiveX = (PropertyManagerPageActiveX)pm_Group.AddControl2(ActiveXID, (int)swPropertyManagerPageControlType_e.swControlType_ActiveX, "ActiveX", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "ActiveX control tip");
         pm_ActiveX.SetClass("ClassID", "LicenseKey");
            }
            else
            {
                //If the page is not created
                System.Windows.Forms.MessageBox.Show("An error occurred while attempting to create the " + "PropertyManager Page");
            }
        }

#region  IPropertyManagerPage2Handler9 Members
        void IPropertyManagerPage2Handler9.AfterActivation()
        {
        }
        void IPropertyManagerPage2Handler9.AfterClose()
        {
        }
        int IPropertyManagerPage2Handler9.OnActiveXControlCreated(int Id, bool Status)
        {
            Debug.Print("ActiveX control created");
        }
        void IPropertyManagerPage2Handler9.OnButtonPress(int Id)
        {
             Debug.Print("Button clicked");
        }
        void IPropertyManagerPage2Handler9.OnCheckboxCheck(int Id, bool Checked)
        {
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
        }
        void IPropertyManagerPage2Handler9.OnComboboxSelectionChanged(int Id, int Item)
        {
        }
        void IPropertyManagerPage2Handler9.OnGainedFocus(int Id)
        {
            short[] varArray = null;
            Debug.Print("Control box " + Id + " gained focus");
            varArray = (short[])pm_List.GetSelectedItems();
            pm_Combo.CurrentSelection = varArray[0];
        }
        void IPropertyManagerPage2Handler9.OnGroupCheck(int Id, bool Checked)
        {
        }
        void IPropertyManagerPage2Handler9.OnGroupExpand(int Id, bool Expanded)
        {
        }
        bool IPropertyManagerPage2Handler9.OnHelp()
        {
        }
        bool IPropertyManagerPage2Handler9.OnKeystroke(int Wparam, int Message, int Lparam, int Id)
        {
        }
        void IPropertyManagerPage2Handler9.OnListboxSelectionChanged(int Id, int Item)
        {
        }
        void IPropertyManagerPage2Handler9.OnLostFocus(int Id)
        {
            Debug.Print("Control box " + Id + " lost focus");
        }
        bool IPropertyManagerPage2Handler9.OnNextPage()
        {
        }
        void IPropertyManagerPage2Handler9.OnNumberboxChanged(int Id, double Value)
        {
            Debug.Print("Number box changed");
        }
        void IPropertyManagerPage2Handler9.OnOptionCheck(int Id)
        {
            Debug.Print("Option selected");
        }
        void IPropertyManagerPage2Handler9.OnPopupMenuItem(int Id)
        {
        }
        void IPropertyManagerPage2Handler9.OnPopupMenuItemUpdate(int Id, ref int retval)
        {
        }
        bool IPropertyManagerPage2Handler9.OnPreview()
        {
        }
        bool IPropertyManagerPage2Handler9.OnPreviousPage()
        {
        }
        void IPropertyManagerPage2Handler9.OnRedo()
        {
        }
        void IPropertyManagerPage2Handler9.OnSelectionboxCalloutCreated(int Id)
        {
        }
        void IPropertyManagerPage2Handler9.OnSelectionboxCalloutDestroyed(int Id)
        {
        }
        void IPropertyManagerPage2Handler9.OnSelectionboxFocusChanged(int Id)
        {
            Debug.Print("The focus moved to selection box " + Id);
        }
        void IPropertyManagerPage2Handler9.OnSelectionboxListChanged(int Id, int Count)
        {
            pm_Page.SetCursor((int)swPropertyManagerPageCursors_e.swPropertyManagerPageCursors_Advance);
            Debug.Print("The list in selection box " + Id + " changed");
        }
        void IPropertyManagerPage2Handler9.OnSliderPositionChanged(int Id, double Value)
        {
            Debug.Print("Slider position changed");
        }
        void IPropertyManagerPage2Handler9.OnSliderTrackingCompleted(int Id, double Value)
        {
        }
        bool IPropertyManagerPage2Handler9.OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
        {
// This method must return true for selections to occur
            return true;
        }
        bool IPropertyManagerPage2Handler9.OnTabClicked(int Id)
        {
        }
        void IPropertyManagerPage2Handler9.OnTextboxChanged(int Id, string Text)
        {
        }
        void IPropertyManagerPage2Handler9.OnUndo()
        {
        }
        void IPropertyManagerPage2Handler9.OnWhatsNew()
        {
        }
         void IPropertyManagerPage2Handler9.OnListboxRMBUp(int Id, int PosX, int PosY)
         {

         }
```

```vb
   int IPropertyManagerPage2Handler9.OnWindowFromHandleControlCreated(int Id, bool Status)
    {

    }
   void IPropertyManagerPage2Handler9.OnNumberBoxTrackingCompleted(int Id, double Value)
    {

    }
```

```vb
        #endregion
    }
}
```

[Back to top](#Top)
