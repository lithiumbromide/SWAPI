---
title: "Create a Task that Finds Approved Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Schedule_Task_Addin_Example_CSharp.htm"
---

# Create a Task that Finds Approved Files Example (C#)

This example shows how to create a task add-in that notifies the logged-in user as to which files in the vault are in the Approved state.

```vb
//--------------------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Library > Class Library (.NET Framework), then Next.
 // 3. Select .NET Framework 4.5 or later in the dropdown.
 // 4. Type TaskAddinExample in Project name.
 // 5. For Location, click ... and navigate to the folder where to create the project.
// 6. Click Create.
// 7. Click Show All Files in the Solution Explorer toolbar and expand
//    Class1.cs in the Solution Explorer.
 // 8.    Add dependencies and safely pass arrays of structures.
 // 9. Right-click the project name in the Solution Explorer and click  Properties.
 //10. In the Properties window:
 //    a. On the Application tab, click Assembly Information.
 //    b. De-select Make assembly COM-Visible.
 //    c. On the Build tab, select Any CPU, de-select Prefer 32-bit, and select Register for COM interop.
 //11. Save the project.
 //12. Copy the code below to Class1.cs.
 //13. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 //    select GUID Format 5, click Copy, and click Exit. Populate [Guid(""), ...] with
 //    the copied string.
 //14. Click  Build > Build Solution.
 //
 // Postconditions:
 //  1. Open the SOLIDWORKS PDM Administration tool, expand a vault_name node,
 //     and log in as Admin.
 //  2. Ensure that Default Workflow with an Approved state exists
 //     under vault_name > Workflows.
 //  3. Under vault_name,  right-click Add-ins and click New Add-in.
 //     a. Navigate to the  bin\Debug directory of your built project.
 //     b. Click EPDM.Interop.epdm.dll and TaskAddinExample.dll.
 //     c. Click Open.
 //     d. Click OK.
 //  4. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 //  5. In the taskbar notification area:
 //     a. Click the SOLIDWORKS PDM icon.
 //     b. Click Task Host Configuration.
 //     c. Select vault_name in the File Vault dropdown.
 //     d. Select Permit next to the add-in you installed in step 3.
 //     e. Click OK.
 //  6. In the Administration tool under the vault_name, right-click Tasks and click New Task.
 //     a. Type Approved Files Task in the upper-left text box.
 //     b. Select the C# Task Add-in from the Add-in dropdown.
 //     c. When the attach debugger message box appears:
 //        1. In the IDE, click Debug > Attach to Process > ConisioAdmin.exe.
 //        2. Click Attach.
 //        3. Click OK to close the message box.
 //     d. Click Next.
 //     e. On the Execution Method properties page, select the local computer.
 //     f. Click Next.
 //     g. On the Scheduling properties page, select This task is not scheduled.
 //     h. Click Next.
 //     i. On the Permissions property page, select Admin.
 //     j. Click Next.
 //     k. On the Success Notification property page:
 //        1. Select Notify the user who launched the task.
 //        2. In the Subject field, type Success.
 //        3. In the Text field, type The task successfully completed at, type a space,
 //           click >, and click Current Time.
 //     l. Click OK to close the New Task dialog.
 //  7. Expand vault_name > Tasks and double-click Task List.
 //  8. Click Add Task.
 //  9. In the Add Task dialog:
 //     a. Select Approved Files Task from the dropdown.
 //     b. Click OK.
 // 10. When the attach debugger message box appears:
 //     a. In the IDE, click Debug > Attach to Process > TaskExecutor.exe.
 //     b. Click Attach.
 //     c. Click OK to close the message box.
 // 11. The task appears in the Pending tasks list. Observe the task status.
 // 12. When the task completes, the task moves to the Completed tasks
 //     list. The logged-in user receives a notification with the list of approved files.
 //---------------------------------------------------------------------------------------

 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;
 using System.Runtime.InteropServices;

 [Guid(""), ComVisible(true)]
 public class TaskAddinExample : IEdmAddIn5
 {

     public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
     {
         try
         {
             poInfo.mbsAddInName = "C# Task Add-In";
             poInfo.mbsCompany = "Dassault Systemes";
             poInfo.mbsDescription = "Exercise demonstrating a task that lists files in the Approved state.";
             poInfo.mlAddInVersion = 1;

             //Minimum SOLIDWORKS PDM Professional version
             //needed for C# Task Add-Ins is 10.0
             poInfo.mlRequiredVersionMajor = 10;
             poInfo.mlRequiredVersionMinor = 0;

             //Register this add-in as a task add-in
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskRun);
             //Register this add-in to be called when
             //selected as a task in the Administration tool
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetup);
         }
         catch (System.Runtime.InteropServices.COMException ex)
         {
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") +  ex.Message);
         }
         catch (Exception ex)
         {
             MessageBox.Show(ex.Message);
         }
     }

     public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
     {
         try
         {
             PauseToAttachProcess(poCmd.meCmdType.ToString());

             switch (poCmd.meCmdType)
             {
                 case EdmCmdType.EdmCmd_TaskRun:
                     OnTaskRun(ref poCmd, ref ppoData);
                     break;
                 case EdmCmdType.EdmCmd_TaskSetup:
                     OnTaskSetup(ref poCmd, ref ppoData);
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

     private void OnTaskRun(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
     {
         //Get the task instance interface
         IEdmTaskInstance inst = default(IEdmTaskInstance);
         inst = (IEdmTaskInstance)poCmd.mpoExtra;
         try
         {
             //Keep the Task List status up to date
             inst.SetStatus(EdmTaskStatus.EdmTaskStat_Running);

             //Format a message that will be displayed
             //in the task list
             inst.SetProgressRange(10, 1, "Task is running.");

             List<EdmSelItem2> Items = new List<EdmSelItem2>();
             inst.SetProgressPos(4, "Task is searching.");

             IEdmSearch6 Search = (IEdmSearch6)((IEdmVault5)(poCmd.mpoVault)).CreateSearch();
             if (Search == null)
                 return;
             Search.SetToken(EdmSearchToken.Edmstok_AllVersions, true);
             Search.SetToken(EdmSearchToken.Edmstok_FindFiles, true);
             Search.SetToken(EdmSearchToken.Edmstok_WorkflowName, "Default Workflow");
             Search.SetToken(EdmSearchToken.Edmstok_StateName, "Approved");
```

```vb
             //Uncomment and modify the following lines to look for files
             //that have a card variable with values in a specific range
            //object varName1 = "Card_Variable_ID_or_Name";
             //object varValue1 = "Card_Variable_Value_1";
             //int varOp1 = EdmVarOp_NumberGreaterThan;
             //object varValue2 = "Card_Variable_Value_2";
             //int varOp2 = EdmVarOp_NumberLessThan;
             //Search.BeginAND();
                //Search.AddVariable2(ref varName1, ref varValue1, varOp1);
                //Search.AddVariable2(ref varName1, ref varValue2, varOp2);
             //Search.EndAND();
```

```vb
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
             inst.SetProgressPos(7, "Task finished searching.");

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

             inst.SetProgressPos(10, ProgresssMsg);
             inst.SetStatus(EdmTaskStatus.EdmTaskStat_DoneOK, 0, "", NotificationArray, ProgresssMsg);
         }
         catch (System.Runtime.InteropServices.COMException ex)
         {
             inst.SetStatus(EdmTaskStatus.EdmTaskStat_DoneFailed, ex.ErrorCode, "The test task failed!");
         }
         catch (Exception ex)
         {
             MessageBox.Show(ex.Message);
         }
     }

     private void OnTaskSetup(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
     {
         try
         {
             //Get the property interface used to
             //access the framework
             IEdmTaskProperties props = default(IEdmTaskProperties);
             props = (IEdmTaskProperties)poCmd.mpoExtra;

             //Set the property flag that says you want a
             //menu item for the user to launch the task
             //and a flag to support scheduling
             props.TaskFlags = (int)EdmTaskFlag.EdmTask_SupportsInitExec + (int)EdmTaskFlag.EdmTask_SupportsScheduling;

             //Set up the menu commands to launch this task
             EdmTaskMenuCmd[] cmds = new EdmTaskMenuCmd[1];
             cmds[0].mbsMenuString = "List Approved files task";
             cmds[0].mbsStatusBarHelp = "This command runs the task add-in to get the names of the files in the Approved state.";
             cmds[0].mlCmdID = 1;
             cmds[0].mlEdmMenuFlags = (int)EdmMenuFlags.EdmMenu_Nothing;
             props.SetMenuCmds(cmds);
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

     private void PauseToAttachProcess(string callbackType)
     {
         try
         {
             //If the debugger isn't already attached to a
             //process,
             if (!Debugger.IsAttached)
             {
                 //Launch the debug dialog
                 //Debugger.Launch()
                 //or
                 //use a MsgBox dialog to pause execution
                 //and allow the user time to attach it
                 MessageBox.Show("Attach debugger to process \"" + Process.GetCurrentProcess().ProcessName + "\" for callback \"" + callbackType + "\" before clicking OK.");
             }

         }
         catch (Exception ex)
         {
             MessageBox.Show(ex.Message);
         }
     }

 }
```
