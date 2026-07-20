---
title: "Task Add-in Sample (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/TaskSample_CSharp.htm"
---

# Task Add-in Sample (C#)

The following shows the entire source code of a task add-in
written in C#. The add-in:

- Is created using a C# class library (.NET Framework)
  project in Visual Studio.
- Implements

  [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)

  .
- Displays a message box on task launch.
- Creates custom pages in the Task property dialog box.
- Customizes the task details page.

NOTE: To populate the GUID attribute below, click**Tools > Create GUID**in the IDE, select GUID Format 6, click**Copy**, and click**Exit**.
Replace <Guid("")>
with the copied string.

```vb
      using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using EPDM.Interop.epdm;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;  [Guid(""), ComVisible(true)]
     public class Class1 : IEdmAddIn5
     {

         RunPage m_runPage;;           SetupPage SetupPageObj;
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
                 poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskDetails);                  poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskLaunch);                  poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskLaunchButton);
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
    private   void OnTaskLaunchButton(ref  EdmCmd poCmd)           {                 if (poCmd.mbsComment ==   "OK")               {                   poCmd.mbCancel = false;               }                 else               {                   poCmd.mbCancel = 1true;               }           }        private   void OnTaskLaunch(ref  EdmCmd poCmd,  EdmCmdData[] poData)           {              'Display a message box on task launch
            'You can also display a form to collect data to pass back to the task add-in
             IEdmVault7 v11;
            v11 =  (IEdmVault7)poCmd.mpoVault;
             if (v11.MsgBox(poCmd.mlParentWnd, "Hello!" + " Are you sure you want to launch the test task?", EdmMBoxType.EdmMbt_YesNo) <> EdmMBoxResult.EdmMbr_Yes)             {
                poCmd.mbCancel = false;             }
            }     private void OnTaskDetails(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
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
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
                private void OnTaskRun(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
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
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
      'Store the custom set-up page here so it can be accessed from both OnTaskSetup and OnTaskSetupButton
 SetupPage SetupPageObj;     private void OnTaskSetup(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
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
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
      'Called when the user clicks OK or Cancel in the
'task property dialog box
 private void OnTaskSetupButton(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
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
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
      'Main entry point of the add-in; called by SOLIDWORKS
'PDM Professional for all task-related events
  public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
         {

             try
             {
                 switch (poCmd.meCmdType)
                 {

                     //Display a task launch dialog box
                     case EdmCmdType.EdmCmd_TaskLaunch:
                         OnTaskLaunch(ref poCmd, ref ppoData);

                         break;
                     //Sent when the user clicks OK or
                     //Cancel in the task launch dialog box
                     case EdmCmdType.EdmCmd_TaskLaunchButton:
                         OnTaskLaunchButton(ref poCmd, ref ppoData);

                         break;
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
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }

         }
             The following is a resource template of the custom set-up page that is displayed in the Task property dialog box by TaskAddIn::OnTaskSetup. It also appears in the Task Details page    added by TaskAddIn::OnTaskDetails. It is a user control in Visual Studio.

    The code behind the custom set-up page is as follows:
         using System;  using System.Collections;  using System.Collections.Generic;  using System.Data;  using System.Diagnostics;  using System.Windows.Forms;  using EPDM.Interop.epdm;  namespace StateAgeTask_CSharp  {      // Setup page used in the task setup and task details dialogs must be a System.Windows.Forms.UserControl      public   partial   class   SetupPage       {               private IEdmVault7 mVault;            private IEdmTaskProperties mTaskProps;            private IEdmTaskInstance mTaskInst;          // Constructor called from task setup          public   SetupPage(IEdmVault7 Vault, IEdmTaskProperties Props)           {                try               {                   InitializeComponent();                   mVault = Vault;                   mTaskProps = Props;                   mTaskInst =   null;                  }                catch (System.Runtime.InteropServices.COMException ex)               {                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);               }                catch (Exception ex)               {                   MessageBox.Show(ex.Message);               }           }          // Constructor called from task details          public   SetupPage(IEdmVault7 Vault, IEdmTaskInstance Props)           {                try               {                   InitializeComponent();                   mVault = Vault;                   mTaskProps =   null;                   mTaskInst = Props;                  }                catch (System.Runtime.InteropServices.COMException ex)               {                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);               }                catch (Exception ex)               {                   MessageBox.Show(ex.Message);               }           }               public  void LoadData(EdmCmd poCmd)           {                try               {                  //Add the names of the available workflows                  //to WorkflowsComboBox                   WorkflowsComboBox.Items.Clear();                   IEdmWorkflowMgr6 WorkflowMgr =   default(IEdmWorkflowMgr6);                   WorkflowMgr = (IEdmWorkflowMgr6)mVault.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr);                   IEdmPos5 WorkflowPos = WorkflowMgr.GetFirstWorkflowPosition();                    while (!WorkflowPos.IsNull)                   {                       IEdmWorkflow6 Workflow =   default(IEdmWorkflow6);                       Workflow = WorkflowMgr.GetNextWorkflow(WorkflowPos);                       WorkflowsComboBox.Items.Add(Workflow.Name);                   }                       string SelectedWorkflow =  "";                    string NoDays =   "";                    if ((mTaskProps !=   null))                   {                      //Retrieve the name of the workflow that was                      //selected by the user                       SelectedWorkflow = (string)mTaskProps.GetValEx("SelectedWorkflowVar");                      //Retrieve the number of days in a state                      //before sending a message                       NoDays = (string)mTaskProps.GetValEx("NoDaysVar");                   }                    else  if ((mTaskInst !=   null))                   {                      //Retrieve the name of the workflow that                      //was selected by the user                       SelectedWorkflow = (string)mTaskInst.GetValEx("SelectedWorkflowVar");                      //Retrieve the number of days in a state                      //before sending a message                       NoDays = (string)mTaskInst.GetValEx("NoDaysVar");                   }                        //Select the workflow to display in                     //WorkflowsComboBox; setting this also                     //causes SetupPage::WorkflowsComboBox_SelectedIndexChanged                    //to be called to fill StatesListBox                      //with the available states for this workflow                    if (string.IsNullOrEmpty(SelectedWorkflow))                   {                       WorkflowsComboBox.SelectedIndex = 0;                   }                    else                   {                       WorkflowsComboBox.Text = SelectedWorkflow;                   }                        }                catch (System.Runtime.InteropServices.COMException ex)               {                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);               }                catch (Exception ex)               {                   MessageBox.Show(ex.Message);               }           }               public  void StoreData()           {                try               {                  //Add the selected states to StatesList                  string StatesList =   "";                    foreach (int SelectedStateIndex  in StatesListBox.SelectedIndices)                   {                       StatesList += StatesListBox.Items[SelectedStateIndex] +  "";                   }                  //Save the states selected by the user                   mTaskProps.SetValEx("SelectedStatesVar", StatesList);                  //Save the workflow selected by the user                   mTaskProps.SetValEx("SelectedWorkflowVar", WorkflowsComboBox.Text);                  //Save the number of days selected by the user                   mTaskProps.SetValEx("NoDaysVar", DaysNumericUpDown.Value.ToString());                  }                catch (System.Runtime.InteropServices.COMException ex)               {                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);               }                catch (Exception ex)               {                   MessageBox.Show(ex.Message);               }           }                  private  void WorkflowsComboBox_SelectedIndexChanged(System.Object sender, System.EventArgs e)           {                try               {                  //Find the IEdmWorkflow corresponding to the                  //selected workflow name                   IEdmWorkflowMgr6 WorkflowMgr =  default(IEdmWorkflowMgr6);                   WorkflowMgr = (IEdmWorkflowMgr6)mVault.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr);                   IEdmPos5 WorkflowPos = WorkflowMgr.GetFirstWorkflowPosition();                   IEdmWorkflow6 Workflow =   null;                   IEdmWorkflow6 SelectedWorkflow =   null;                    while (!WorkflowPos.IsNull)                   {                       Workflow = WorkflowMgr.GetNextWorkflow(WorkflowPos);                         if (Workflow.Name == WorkflowsComboBox.Text)                       {                           SelectedWorkflow = Workflow;                             break;                       }                   }                        //Add the names of the available states for the                     //selected workflow to StatesListBox                   StatesListBox.Items.Clear();                    if (SelectedWorkflow !=   null)                   {                       IEdmPos5 StatePos = SelectedWorkflow.GetFirstStatePosition();                         while (!(StatePos.IsNull))                       {                           IEdmState6 State =   default(IEdmState6);                           State = SelectedWorkflow.GetNextState(StatePos);                           StatesListBox.Items.Add(State.Name);                          }                      }                       string SelectedStates =   "";                    if ((mTaskProps !=   null))                   {                       SelectedStates = (string)mTaskProps.GetValEx("SelectedStatesVar");                   }                    else  if ((mTaskInst !=   null))                   {                       SelectedStates = (string)mTaskInst.GetValEx("SelectedStatesVar");                   }                       string[] States = SelectedStates.Split(new  string[] {  "\\n" }, StringSplitOptions.None);                    foreach (string State   in States)                   {                         if (!string.IsNullOrEmpty(State.Trim()))                       {                           StatesListBox.SelectedItems.Add(State);                       }                   }                  }                catch (System.Runtime.InteropServices.COMException ex)               {                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);               }                catch (Exception ex)               {                   MessageBox.Show(ex.Message);               }           }               public  void DisableControls()           {                try               {                   WorkflowsComboBox.Enabled =   false;                   StatesListBox.Enabled =   false;                   DaysNumericUpDown.Enabled =   false;               }                catch (System.Runtime.InteropServices.COMException ex)               {                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);               }                catch (Exception ex)               {                   MessageBox.Show(ex.Message);               }           }          }  }      See Also Programming Tasks  Standard Task Add-in  TaskSample (VB.NET)

 Back to top
```
