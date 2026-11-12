---
title: "Create a Task that Finds Files in Workflow States Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm"
---

# Create a Task that Finds Files in Workflow States Example (C#)

This example shows how to create a task add-in that finds files that have been in specified workflow states a specified number of days.

```vb
  //--------------------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //  2. Click File > New > Project > Visual C# > Class Library (.NET Framework).
 //  3. Select .NET Framework 4.5 or later in the dropdown.
 //  4. Click Browse and navigate to the folder where to create the project.
 //  5. Type StateAgeTask_CSharp in Name.
 //  6. Click OK.
 //  7. Right-click the project in the Solution Explorer and click Add > User Control.
 //  8. In the Add New Item dialog, keep the default name and click Add.
 //  9. Create a user control similar to the one shown above and change:
 //     a. Top label to WorkflowLabel.
 //     b. Combo box to WorkflowsComboBox.
 //     c. Second label to StatesLabel.
 //     d. List box to StatesListBox.
 //     e. Third label to DaysLabel.
 //     f. Numeric spin box to DaysNumericUpDown.
 // 10. Click Show all Files in the Solution Explorer toolbar and expand UserControl1.vb.
 // 11. Replace the code in Class1.cs with this code.
 // 12. Replace the code in UserControl1.Designer.cs with this code.
 // 13. Replace the code in UserControl1.cs with this code.
 // 14. Right-click the project name in the Solution Explorer and click Add Reference.
 // 15. In the Add Reference dialog:
 //     a. Add the SOLIDWORKS PDM Professional  interop assembly as a reference (click Browse in the
 //       left-side panel, click EPDM.Interop.epdm.dll,
 //       and click OK).
   //     b. Click Assemblies > Framework in the left-side panel, click
 //        Microsoft.VisualBasic, and click Add.
 //     c. Click Close.
 // 16. Right-click the project name in the Solution Explorer and click  Properties.
 // 17. In the Properties window:
 //     a. On the Application tab, click Assembly Information.
 //     b. De-select Make assembly COM-Visible.
 //     c. On the Build tab,  select Any CPU, de-select Prefer 32-bit, and select Register for COM interop.
 // 18. Save the project.
 // 19. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 //     select GUID Format 5, click Copy, and click Exit. Replace [Guid(""), ...]
 //     with the copied string.
 // 20. Click Build > Build Solution.
 //
 // Postconditions:
 //  1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 //     and log in as Admin.
 //  2. Under vault_name, right-click Add-ins and click New Add-in.
  //     a. Navigate to the bin\Debug  directory of your built project.
 //     b. Click EPDM.Interop.epdm.dll and StateAgeTask_CSharp.dll.
 //     c. Click Open.
 //     d. Click OK.
 //  3. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 //  4. In the taskbar notification area:
 //     a. Click the SOLIDWORKS PDM icon.
 //     b. Click Task Host Configuration.
 //     c. Select vault_name in the File Vault dropdown.
 //     d. Select Permit next to the add-in you just installed.
 //     e. Click OK.
 //  5. In the Administration tool under vault_name, right-click Tasks and click New Task.
 //  6. In the New Task dialog:
 //     a. Type State Age Task in the upper-left text box.
 //     b. Select the C# Workflow State Age Task Add-in from the Add-in dropdown.
 //     c. Click Next.
  //     d. On the Execution Method properties page, select the local computer.
 //     e. Click Next.
 //     f. On the Scheduling properties page, select This task is not scheduled.
 //     g. Click Next.
 //     h. On the Choose states to check page, select the file search criteria in:
 //        1. Choose Workflow.
 //        2. Select States.
 //        3. Number of Days in State.
 //     i. Click Next.
 //     j. On the Permissions property page, select Admin.
 //     k. Click Next.
 //     l. On the Success Notification property page:
 //        1. Select Notify the user who launched the task.
 //        2. In the Subject field, type Success.
 //        3. In the Text field, type The task successfully completed at, type a space,
 //           click >, and click Current Time.
 //     m. Click OK to close the New Task dialog.
 //  7. Expand vault_name > Tasks and double-click Task List.
 //  8. Click Add Task.
 //  9. In the Add Task dialog:
 //     a. Select State Age Task from the dropdown.
 //     b. Click OK.
 // 10. The task appears in the Pending tasks list. Observe the task status.
  // 11. When the task completes, the task moves to the Completed tasks
  //     list. After a minute or so, the logged-in user receives a notification with the
 //     list of files that have  been in the specified workflow states a specified
 //     number of days.
  //---------------------------------------------------------------------------------------
```

[Back to top](#top)

```vb
 //Class1.cs
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using EPDM.Interop.epdm;
 using System.Runtime.InteropServices;

 namespace StateAgeTask_CSharp
 {
     [Guid(""), ComVisible(true)]
     public class Class1 : IEdmAddIn5
     {

         SetupPage SetupPageObj;
         public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
         {

             try
             {
                 poInfo.mbsAddInName = "C# Workflow State Age Task Add-In";
                 poInfo.mbsCompany = "Dassault Systemes";
                 poInfo.mbsDescription = "Example demonstrates a task that finds files that have been in selected workflow states a selected number of days";
                 poInfo.mlAddInVersion = 1;
                 //Minimum SOLIDWORKS PDM Professional version
                 //needed for Tasks is 10.0
                 poInfo.mlRequiredVersionMajor = 10;
                 poInfo.mlRequiredVersionMinor = 0;

                 //Register to call OnCmd on task-related events
                 poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetup);
                 poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetupButton);
                 poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskRun);
                 poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskDetails);
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         public void OnCmd(ref EdmCmd poCmd, ref System.Array ppoData)
         {

             try
             {
                 switch (poCmd.meCmdType)
                 {

                     //Called from the Administration tool when
                     //the user selects this task add-in from the
                     //drop-down list and whenever this task is
                     //subsequently edited in the Administration tool
                     case EdmCmdType.EdmCmd_TaskSetup:
                         OnTaskSetup(ref poCmd, ref ppoData);

                         break;
                     //Sent when the user clicks OK or
                     //Cancel in the task property dialog box
                     case EdmCmdType.EdmCmd_TaskSetupButton:
                         OnTaskSetupButton(ref poCmd, ref ppoData);

                         break;
                     //Called when an instance of the
                     //task is run
                     case EdmCmdType.EdmCmd_TaskRun:
                         OnTaskRun(ref poCmd, ref ppoData);

                         break;
                     //Called from the Task List in the
                     //Administration tool when the task details
                     //dialog is displayed
                     case EdmCmdType.EdmCmd_TaskDetails:
                         OnTaskDetails(ref poCmd, ref ppoData);
                         break;
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }

         }

         private void OnTaskSetup(ref EdmCmd poCmd, ref System.Array ppoData)
         {
             try
             {
                 IEdmTaskProperties props = (IEdmTaskProperties)poCmd.mpoExtra;
                 if ((props != null))
                 {
                     //Set the task properties
                     props.TaskFlags = (int)EdmTaskFlag.EdmTask_SupportsScheduling + (int)EdmTaskFlag.EdmTask_SupportsDetails;

                     SetupPageObj = new SetupPage((IEdmVault7)poCmd.mpoVault, props);
                     //Force immediate creation of the control
                     //and its handle
                     SetupPageObj.CreateControl();
                     SetupPageObj.LoadData(poCmd);

                     EdmTaskSetupPage[] pages = new EdmTaskSetupPage[1];
                     //Page name that appears in the
                     //navigation pane of the Add Task dialog
                     //in the Administration tool
                     pages[0].mbsPageName = "Choose states to check";
                     pages[0].mlPageHwnd = SetupPageObj.Handle.ToInt32();
                     pages[0].mpoPageImpl = SetupPageObj;

                     props.SetSetupPages(pages);

                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         private void OnTaskSetupButton(ref EdmCmd poCmd, ref System.Array ppoData)
         {
             try
             {
                 //Custom setup page, SetupPageObj, is created
                 //in method Class1::OnTaskSetup; SetupPage::StoreData
                 //saves the contents of the list box to poCmd.mpoExtra
                 //in the IEdmTaskProperties interface
                 if (poCmd.mbsComment == "OK" & (SetupPageObj != null))
                 {
                     SetupPageObj.StoreData();
                 }
                 SetupPageObj = null;

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         private void OnTaskRun(ref EdmCmd poCmd, ref System.Array ppoData)
         {
             try
             {
                 IEdmTaskInstance TaskInstance = default(IEdmTaskInstance);
                 TaskInstance = (IEdmTaskInstance)poCmd.mpoExtra;
                 if ((TaskInstance != null))
                 {
                     TaskInstance.SetStatus(EdmTaskStatus.EdmTaskStat_Running);
                     TaskInstance.SetProgressRange(100, 0, "Task is running.");

                     string NoDays = null;
                     NoDays = (string)TaskInstance.GetValEx("NoDaysVar");

                     string States = "";
                     States = (string)TaskInstance.GetValEx("SelectedStatesVar");

                     List<EdmSelItem2> Items = new List<EdmSelItem2>();

                     DoSearch((IEdmVault11)poCmd.mpoVault, States, NoDays, Items);

                     EdmSelItem2[] NotificationArray = new EdmSelItem2[Items.Count];

                     Items.CopyTo(NotificationArray);

                     string ProgresssMsg = null;
                     if ((Items.Count > 0))
                     {
                         ProgresssMsg = "Found " + Items.Count.ToString() + " files.";
                     }
                     else
                     {
                         ProgresssMsg = ("No files found.");
                     }

                     TaskInstance.SetProgressPos(100, ProgresssMsg);
                     TaskInstance.SetStatus(EdmTaskStatus.EdmTaskStat_DoneOK, 0, "", NotificationArray, ProgresssMsg);
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         public void DoSearch(IEdmVault11 Vault, string States, string Days, List<EdmSelItem2> Items)
         {
             try
             {
                 //Calculate age to use for search
                 DateTime dt = DateTime.Today;
                 int DaysInt = Convert.ToInt32(Days) - 1;
                 TimeSpan ts = new TimeSpan(DaysInt, 0, 0, 0);
                 dt = dt.Subtract(ts);

                 //Split States into an array of
                 //State strings
                 string[] StatesObj = Strings.Split(States, Constants.vbCrLf);
                 //Search each selected state for aged files
                 foreach (string State in StatesObj)
                 {
                     //Skip empty strings
                     if (string.IsNullOrEmpty(Strings.Trim(State)))
                     {
                         continue;
                     }

                     IEdmSearch6 Search = (IEdmSearch6)Vault.CreateSearch();
                     if (Search == null)
                         return;

                     Search.FindFiles = true;
                     Search.SetToken(EdmSearchToken.Edmstok_StateBefore, dt);
                     Search.SetToken(EdmSearchToken.Edmstok_StateName, State);

                     IEdmSearchResult5 SearchResult = Search.GetFirstResult();
                     while ((SearchResult != null))
                     {
                         EdmSelItem2 SelItem = new EdmSelItem2();
                         SelItem.mlID = SearchResult.ID;
                         SelItem.mlParentID = SearchResult.ParentFolderID;
                         SelItem.meType = SearchResult.ObjectType;
                         SelItem.mlVersion = SearchResult.Version;

                         Items.Add(SelItem);
                         SearchResult = Search.GetNextResult();
                     }
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         private void OnTaskDetails(ref EdmCmd poCmd, ref System.Array ppoData)
         {
             try
             {
                 IEdmTaskInstance TaskInstance = (IEdmTaskInstance)poCmd.mpoExtra;
                 if ((TaskInstance != null))
                 {
                     SetupPageObj = new SetupPage((IEdmVault7)poCmd.mpoVault, TaskInstance);
                     //Force immediate creation of the control
                     //and its handle
                     SetupPageObj.CreateControl();
                     SetupPageObj.LoadData(poCmd);
                     SetupPageObj.DisableControls();
                     poCmd.mbsComment = "State Age Details";
                     poCmd.mlParentWnd = SetupPageObj.Handle.ToInt32();
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

     }
 }
 Back to top
 //UserControl1.cs
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;
 namespace StateAgeTask_CSharp
 {
     // Setup page used in the task setup and task details dialogs must be a System.Windows.Forms.UserControl
     public partial class SetupPage
     {

         private IEdmVault7 mVault;
         private IEdmTaskProperties mTaskProps;
         private IEdmTaskInstance mTaskInst;
         // Constructor called from task setup
         public SetupPage(IEdmVault7 Vault, IEdmTaskProperties Props)
         {
             try
             {
                 InitializeComponent();
                 mVault = Vault;
                 mTaskProps = Props;
                 mTaskInst = null;

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }
         // Constructor called from task details
         public SetupPage(IEdmVault7 Vault, IEdmTaskInstance Props)
         {
             try
             {
                 InitializeComponent();
                 mVault = Vault;
                 mTaskProps = null;
                 mTaskInst = Props;

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         public void LoadData(EdmCmd poCmd)
         {
             try
             {
                 //Add the names of the available workflows
                 //to WorkflowsComboBox
                 WorkflowsComboBox.Items.Clear();
                 IEdmWorkflowMgr6 WorkflowMgr = default(IEdmWorkflowMgr6);
                 WorkflowMgr = (IEdmWorkflowMgr6)mVault.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr);
                 IEdmPos5 WorkflowPos = WorkflowMgr.GetFirstWorkflowPosition();
                 while (!WorkflowPos.IsNull)
                 {
                     IEdmWorkflow6 Workflow = default(IEdmWorkflow6);
                     Workflow = WorkflowMgr.GetNextWorkflow(WorkflowPos);
                     WorkflowsComboBox.Items.Add(Workflow.Name);
                 }

                 string SelectedWorkflow = "";
                 string NoDays = "";
                 if ((mTaskProps != null))
                 {
                     //Retrieve the name of the workflow that was
                     //selected by the user
                     SelectedWorkflow = (string)mTaskProps.GetValEx("SelectedWorkflowVar");
                     //Retrieve the number of days in a state
                     //before sending a message
                     NoDays = (string)mTaskProps.GetValEx("NoDaysVar");
                 }
                 else if ((mTaskInst != null))
                 {
                     //Retrieve the name of the workflow that
                     //was selected by the user
                     SelectedWorkflow = (string)mTaskInst.GetValEx("SelectedWorkflowVar");
                     //Retrieve the number of days in a state
                     //before sending a message
                     NoDays = (string)mTaskInst.GetValEx("NoDaysVar");
                 }

                 //Select the workflow to display in
                 //WorkflowsComboBox; setting this also
                 //causes SetupPage::WorkflowsComboBox_SelectedIndexChanged
                 //to be called to fill StatesListBox
                 //with the available states for this workflow
                 if (string.IsNullOrEmpty(SelectedWorkflow))
                 {
                     WorkflowsComboBox.SelectedIndex = 0;
                 }
                 else
                 {
                     WorkflowsComboBox.Text = SelectedWorkflow;
                 }

                 //Retrieve the number of days in a state
                 //before sending a message
                 if (Information.IsNumeric(NoDays))
                 {
                     DaysNumericUpDown.Value = Convert.ToDecimal(NoDays);
                 }
                 else
                 {
                     DaysNumericUpDown.Value = 0;
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         public void StoreData()
         {
             try
             {
                 //Add the selected states to StatesList
                 string StatesList = "";
                 foreach (int SelectedStateIndex in StatesListBox.SelectedIndices)
                 {
                     StatesList += StatesListBox.Items[SelectedStateIndex] + Constants.vbCrLf;
                 }
                 //Save the states selected by the user
                 mTaskProps.SetValEx("SelectedStatesVar", StatesList);
                 //Save the workflow selected by the user
                 mTaskProps.SetValEx("SelectedWorkflowVar", WorkflowsComboBox.Text);
                 //Save the number of days selected by the user
                 mTaskProps.SetValEx("NoDaysVar", DaysNumericUpDown.Value.ToString());

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

         private void WorkflowsComboBox_SelectedIndexChanged(System.Object sender, System.EventArgs e)
         {
             try
             {
                 //Find the IEdmWorkflow corresponding to the
                 //selected workflow name
                 IEdmWorkflowMgr6 WorkflowMgr = default(IEdmWorkflowMgr6);
                 WorkflowMgr = (IEdmWorkflowMgr6)mVault.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr);
                 IEdmPos5 WorkflowPos = WorkflowMgr.GetFirstWorkflowPosition();
                 IEdmWorkflow6 Workflow = null;
                 IEdmWorkflow6 SelectedWorkflow = null;
                 while (!WorkflowPos.IsNull)
                 {
                     Workflow = WorkflowMgr.GetNextWorkflow(WorkflowPos);
                     if (Workflow.Name == WorkflowsComboBox.Text)
                     {
                         SelectedWorkflow = Workflow;
                         break;
                     }
                 }

                 //Add the names of the available states for the
                 //selected workflow to StatesListBox
                 StatesListBox.Items.Clear();
                 if (SelectedWorkflow != null)
                 {
                     IEdmPos5 StatePos = SelectedWorkflow.GetFirstStatePosition();
                     while (!(StatePos.IsNull))
                     {
                         IEdmState6 State = default(IEdmState6);
                         State = SelectedWorkflow.GetNextState(StatePos);
                         StatesListBox.Items.Add(State.Name);

                     }

                 }

                 string SelectedStates = "";
                 if ((mTaskProps != null))
                 {
                     SelectedStates = (string)mTaskProps.GetValEx("SelectedStatesVar");
                 }
                 else if ((mTaskInst != null))
                 {
                     SelectedStates = (string)mTaskInst.GetValEx("SelectedStatesVar");
                 }

                 string[] States = Strings.Split(SelectedStates, Constants.vbCrLf);
                 foreach (string State in States)
                 {
                     if (!string.IsNullOrEmpty(Strings.Trim(State)))
                     {
                         StatesListBox.SelectedItems.Add(State);
                     }
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 System.Windows.Forms.MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 System.Windows.Forms.MessageBox.Show(ex.Message);
             }
         }

         public void DisableControls()
         {
             try
             {
                 WorkflowsComboBox.Enabled = false;
                 StatesListBox.Enabled = false;
                 DaysNumericUpDown.Enabled = false;
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 Interaction.MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + Constants.vbCrLf + ex.Message);
             }
             catch (Exception ex)
             {
                 Interaction.MsgBox(ex.Message);
             }
         }

     }
 }
 Back to top
 //UserControl1.Designer.cs
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 namespace StateAgeTask_CSharp
 {
     [Microsoft.VisualBasic.CompilerServices.DesignerGenerated()]
     partial class SetupPage : System.Windows.Forms.UserControl
     {

         //UserControl overrides dispose to clean up the component list.
         [System.Diagnostics.DebuggerNonUserCode()]
         protected override void Dispose(bool disposing)
         {
             try
             {
                 if (disposing && components != null)
                 {
                     components.Dispose();
                 }
             }
             finally
             {
                 base.Dispose(disposing);
             }
         }

         //Required by the Windows Form Designer

         private System.ComponentModel.IContainer components;
         //NOTE: The following procedure is required by the Windows Form Designer
         //It can be modified using the Windows Form Designer.
         //Do not modify it using the code editor.
         [System.Diagnostics.DebuggerStepThrough()]
         private void InitializeComponent()
         {
             this.StatesListBox = new System.Windows.Forms.ListBox();
             this.WorkflowsComboBox = new System.Windows.Forms.ComboBox();
             this.WorkflowLabel = new System.Windows.Forms.Label();
             this.StatesLabel = new System.Windows.Forms.Label();
             this.DaysLabel = new System.Windows.Forms.Label();
             this.DaysNumericUpDown = new System.Windows.Forms.NumericUpDown();
             ((System.ComponentModel.ISupportInitialize)(this.DaysNumericUpDown)).BeginInit();
             this.SuspendLayout();
             //
             // StatesListBox
             //
             this.StatesListBox.FormattingEnabled = true;
             this.StatesListBox.Location = new System.Drawing.Point(19, 97);
             this.StatesListBox.Margin = new System.Windows.Forms.Padding(2);
             this.StatesListBox.Name = "StatesListBox";
             this.StatesListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
             this.StatesListBox.Size = new System.Drawing.Size(124, 108);
             this.StatesListBox.TabIndex = 0;

             //
             // WorkflowsComboBox
             //
             this.WorkflowsComboBox.FormattingEnabled = true;
             this.WorkflowsComboBox.Location = new System.Drawing.Point(19, 35);
             this.WorkflowsComboBox.Margin = new System.Windows.Forms.Padding(2);
             this.WorkflowsComboBox.Name = "WorkflowsComboBox";
             this.WorkflowsComboBox.Size = new System.Drawing.Size(124, 21);
             this.WorkflowsComboBox.TabIndex = 1;
             this.WorkflowsComboBox.SelectedIndexChanged += new System.EventHandler(this.WorkflowsComboBox_SelectedIndexChanged);
             //
             // WorkflowLabel
             //
             this.WorkflowLabel.AutoSize = true;
             this.WorkflowLabel.Location = new System.Drawing.Point(20, 12);
             this.WorkflowLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
             this.WorkflowLabel.Name = "WorkflowLabel";
             this.WorkflowLabel.Size = new System.Drawing.Size(91, 13);
             this.WorkflowLabel.TabIndex = 2;
             this.WorkflowLabel.Text = "Choose Workflow";
             //
             // StatesLabel
             //
             this.StatesLabel.AutoSize = true;
             this.StatesLabel.Location = new System.Drawing.Point(20, 72);
             this.StatesLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
             this.StatesLabel.Name = "StatesLabel";
             this.StatesLabel.Size = new System.Drawing.Size(76, 13);
             this.StatesLabel.TabIndex = 3;
             this.StatesLabel.Text = "Select State(s)";
             //
             // DaysLabel
             //
             this.DaysLabel.AutoSize = true;
             this.DaysLabel.Location = new System.Drawing.Point(20, 223);
             this.DaysLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
             this.DaysLabel.Name = "DaysLabel";
             this.DaysLabel.Size = new System.Drawing.Size(122, 13);
             this.DaysLabel.TabIndex = 4;
             this.DaysLabel.Text = "Number of Days in State";
             //
             // DaysNumericUpDown
             //
             this.DaysNumericUpDown.Location = new System.Drawing.Point(22, 247);
             this.DaysNumericUpDown.Margin = new System.Windows.Forms.Padding(2);
             this.DaysNumericUpDown.Name = "DaysNumericUpDown";
             this.DaysNumericUpDown.Size = new System.Drawing.Size(119, 20);
             this.DaysNumericUpDown.TabIndex = 5;
             //
             // SetupPage
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.Controls.Add(this.DaysNumericUpDown);
             this.Controls.Add(this.DaysLabel);
             this.Controls.Add(this.StatesLabel);
             this.Controls.Add(this.WorkflowLabel);
             this.Controls.Add(this.WorkflowsComboBox);
             this.Controls.Add(this.StatesListBox);
             this.Margin = new System.Windows.Forms.Padding(2);
             this.Name = "SetupPage";
             this.Size = new System.Drawing.Size(162, 278);
             ((System.ComponentModel.ISupportInitialize)(this.DaysNumericUpDown)).EndInit();
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         private System.Windows.Forms.ListBox StatesListBox;
         private System.Windows.Forms.ComboBox WorkflowsComboBox;
         private System.Windows.Forms.Label WorkflowLabel;
         private System.Windows.Forms.Label StatesLabel;
         private System.Windows.Forms.Label DaysLabel;

         private System.Windows.Forms.NumericUpDown DaysNumericUpDown;
     }
 }
 Back to top
```
