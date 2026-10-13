---
title: "Change Card Variables Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Change_Card_Variables_Addin_Example_CSharp.htm"
---

# Change Card Variables Add-in Example (C#)

This example shows how to create an add-in that modifies a data card variable when another data card variable changes.

```vb
 //--------------------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Library > Class Library (.NET Framework).
 // 3. Select .NET Framework 4.5 or later in the dropdown.
 // 4. Type CardVariables_CSharp in Project name.
 // 5.      For Location, click ... and navigate to the folder where to create the project.
 // 6. Click Create.
 // 7. Right-click the project name in the Solution Explorer and click Add > Reference....
 // 8. In the Reference Manager dialog:
 //    a. Add dependencies and safely pass arrays of structures.
//    b. Add Microsoft.VisualBasic  and System.Windows.Forms as a references (click Assemblies > Framework in the
 //       left-side panel, click System.Windows.Forms  and Microsoft.VisualBasic, and click OK).
 // 9. Right-click the project name in the Solution Explorer and click Properties.
 //10. In the Properties window:
 //    a. On the Application tab, click Assembly Information....
 //    b. De-select Make assembly COM-Visible.
 //    c. On the Build tab, select Any CPU, de-select Prefer 32-bit, and select Register for COM interop.
 //11. Save the project.
 //12. Copy the code below to Class1.cs.
 //13. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 //    select GUID Format 5, click Copy, and click Exit. Populate [Guid(""),...] with
 //    the copied string.
 //14. Click Build > Build Solution.
 //
// Postconditions:
 // 1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 //    and log in as Admin.
 // 2. Under vault_name, right-click Add-ins, and click New Add-in.
 //    a. Navigate to the bin\Debug directory of your built project.
 //    b. Click EPDM.Interop.epdm.dll and CardVariables.dll.
 //    c. Click Open.
 //    d. Click OK.
 // 3. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 // 4. In the taskbar, click the Administration tool blueberry and click Log off > vault_name.
 // 5. Open File Explorer on a view of vault_name to:
 //    a. Log in as Admin.
 //    b. Create, check in, and check out a file whose data card contains Project Name
 //       and Project Number.
 //    c. Click the Data Card tab.
 //    d. In Project Name, type Mercury, Venus, Earth, Mars, Jupiter, or Saturn.
 //    e. Observe the change in Project Number.
//    f. In Project Number, type a number between 1000 and 1005.
 //    g. Observe the change in Project Name.
 //---------------------------------------------------------------------------------------

 using Microsoft.VisualBasic
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using EPDM.Interop.epdm;
 using System.Runtime.InteropServices;

 [Guid(""), ComVisible(true)]
 public class CardVariables : IEdmAddIn5
 {

     public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
     {
         try
         {
             poInfo.mbsAddInName = "C# Card Variable Add-In";
             poInfo.mbsCompany = "Dassault Systemes";
             poInfo.mbsDescription = "Example demonstrating updating a card variable based on another card variable";
             poInfo.mlAddInVersion = 1;
             //Minimum SOLIDWORKS PDM Professional version
             //needed for C# Add-Ins is 6.4
             poInfo.mlRequiredVersionMajor = 6;
             poInfo.mlRequiredVersionMinor = 4;

             //Register to receive a notification when
             //a data card variable value changes
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_CardInput);

             IEdmDictionary5 ProjectDictionary = default(IEdmDictionary5);
             ProjectDictionary = poVault.GetDictionary("Projects", true);

             bool SuccessSet = false;
             SuccessSet = ProjectDictionary.StringTestAndSetAt("1000", "Mercury");
             SuccessSet = ProjectDictionary.StringTestAndSetAt("1001", "Venus");
             SuccessSet = ProjectDictionary.StringTestAndSetAt("1002", "Earth");
             SuccessSet = ProjectDictionary.StringTestAndSetAt("1003", "Mars");
             SuccessSet = ProjectDictionary.StringTestAndSetAt("1004", "Jupiter");
             SuccessSet = ProjectDictionary.StringTestAndSetAt("1005", "Saturn");

         }
         catch (System.Runtime.InteropServices.COMException ex)
         {
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\r\n" + ex.Message);
         }
         catch (Exception ex)
         {
             MessageBox.Show(ex.Message);
         }
     }

     readonly Microsoft.VisualBasic.CompilerServices.StaticLocalInitFlag static_OnCmd_VariableChangeInProgress_Init = new Microsoft.VisualBasic.CompilerServices.StaticLocalInitFlag();

     //A data card variable value has changed
     bool static_OnCmd_VariableChangeInProgress;
     public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
     {
         try
         {
             switch (poCmd.meCmdType)
             {
                 case EdmCmdType.EdmCmd_CardInput:

                     lock (static_OnCmd_VariableChangeInProgress_Init)
                     {
                         try
                         {
                             if (InitStaticVariableHelper(static_OnCmd_VariableChangeInProgress_Init))
                             {
                                 static_OnCmd_VariableChangeInProgress = false;
                             }
                         }
                         finally
                         {
                             static_OnCmd_VariableChangeInProgress_Init.State = 1;
                         }
                     }

                     IEdmEnumeratorVariable5 vars = (IEdmEnumeratorVariable5)poCmd.mpoExtra;
                     IEdmStrLst5 ConfigNames = (IEdmStrLst5)((EdmCmdData)ppoData.GetValue(0)).mpoExtra;
                     string Config = null;
                     if (IsConfigInList(ConfigNames, "@"))
                     {
                         Config = "@";
                     }
                     else
                     {
                         Config = "";
                     }

                     //Take appropriate action based on the data card variable that has changed
                     switch (poCmd.mbsComment)
                     {

                         //The Project Name variable has changed
                         case "Project Name":
                             if (static_OnCmd_VariableChangeInProgress == true)
                             {
                                 static_OnCmd_VariableChangeInProgress = false;
                                 break;
                             }
                             object ProjectName = "";
                             vars.GetVar("Project Name", Config, out ProjectName);

                             //Get the old Project Number
                             object ProjectNumber = "";
                             vars.GetVar("Project number", Config, out ProjectNumber);

                             //Get the existing Projects dictionary
                             IEdmDictionary5 ProjectDictionary = default(IEdmDictionary5);
                             ProjectDictionary = ((IEdmVault5)(poCmd.mpoVault)).GetDictionary("Projects", false);

                             //Look up the new project number
                             string NewProjectNumber = "";
                             //Find all values containing the substring
                             //stored in ProjectName
                             string key = "";
                             string value = "";
                             IEdmPos5 pos = default(IEdmPos5);
                             pos = ProjectDictionary.StringFindValues((string)ProjectName);
                             while (!pos.IsNull)
                             {
                                 ProjectDictionary.StringGetNextAssoc(pos, out key, out value);
                                 //Traverse the values until a match
                                 //is found
                                 if (value == (string)ProjectName)
                                 {
                                     NewProjectNumber = key;
                                     break;
                                 }
                             }

                             //Only update the variable if it changed
                             if (!(NewProjectNumber == (string)ProjectNumber))
                             {
                                 static_OnCmd_VariableChangeInProgress = true;
                                 vars.SetVar("Project number", Config, NewProjectNumber);

                             }
                             break;

                         //The Project Number variable has changed
                         case "Project number":
                             if (static_OnCmd_VariableChangeInProgress == true)
                             {
                                 static_OnCmd_VariableChangeInProgress = false;
                                 break;
                             }

                             ProjectNumber = "";
                             vars.GetVar("Project number", Config, out ProjectNumber);

                             //Get the old Project Name
                             ProjectName = "";
                             vars.GetVar("Project Name", Config, out ProjectName);

                             //Get the existing Projects dictionary
                             ProjectDictionary = ((IEdmVault5)(poCmd.mpoVault)).GetDictionary("Projects", false);

                             //Look up the project name
                             string NewProjectName = "";
                             ProjectDictionary.StringGetAt((string)ProjectNumber, out NewProjectName);

                             //Only update the variable if it's changed
                             if (!(NewProjectName == ((string)ProjectName)))
                             {
                                 static_OnCmd_VariableChangeInProgress = true;
                                 vars.SetVar("Project Name", Config, NewProjectName);
                             }
                             break;
                     }
                     break;
             }
         }
         catch (System.Runtime.InteropServices.COMException ex)
         {
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\r\n" + ex.Message);
         }
         catch (Exception ex)
         {
             MessageBox.Show(ex.Message);
         }
     }

     private bool IsConfigInList(IEdmStrLst5 ConfigNames, string ConfigName)
     {
         bool functionReturnValue = false;
         functionReturnValue = false;
         try
         {
             string CurConfig = null;
             IEdmPos5 Pos = ConfigNames.GetHeadPosition();
             while (!Pos.IsNull)
             {
                 CurConfig = ConfigNames.GetNext(Pos);
                 if (CurConfig == ConfigName)
                 {
                     functionReturnValue = true;
                     break;
                 }
             }
             return functionReturnValue;
         }
         catch (System.Runtime.InteropServices.COMException ex)
         {
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\r\n" + ex.Message);
         }
         catch (Exception ex)
         {
             MessageBox.Show(ex.Message);
         }
         return functionReturnValue;
     }

     static bool InitStaticVariableHelper(Microsoft.VisualBasic.CompilerServices.StaticLocalInitFlag flag)
     {
         if (flag.State == 0)
         {
             flag.State = 2;
             return true;
         }
         else if (flag.State == 2)
         {
             throw new Microsoft.VisualBasic.CompilerServices.IncompleteInitialization();
         }
         else
         {
             return false;
         }
     }

 }
```

[Back to top](#top)
