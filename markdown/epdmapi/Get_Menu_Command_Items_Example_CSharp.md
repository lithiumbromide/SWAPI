---
title: "Get Menu Command Items Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Menu_Command_Items_Example_CSharp.htm"
---

# Get Menu Command Items Example (C#)

This example shows how to get add-in menu command items.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
 //--------------------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Console > Console App.
 // 3. Type MenuCSharp in Project name.
    // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Replace the code in Program.cs with this code.
 // 9. Add dependencies and safely pass arrays of structures.
 //10. Add System.Windows.Forms as a reference.
 //11. Replace ACME_LAB with the name of a valid vault view.
 //12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the command window.
 // 2. Displays a message box for each add-in menu command item.
 // 3. Click OK to close each message box.
 // 4. Displays the menu in the upper-left corner of the desktop.
 // 5. Click First Command in the menu.
 // 6. Click OK to close the message box.
 // 7. Click the command window and press any key.
 // 8. Closes the command window and exits the application.
 //--------------------------------------------------------------------------------------
 //Program.cs

 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;
 using EPDM.Interop.epdm;

 namespace MenuCSharp
 {
     class Program
     {
         static EdmVault5 vault;

         static Form frmParent;
         static void Main(string[] args)
         {
             try
             {
                 //Create a vault interface
                 vault = new EdmVault5();

                 //Log into vault
                 vault.LoginAuto("ACME_LAB", 0);

                 //Show menu
                 ShowMenu((IEdmVault12)vault);

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }

             Console.WriteLine();
             Console.WriteLine("Press any key to exit.");
             Console.ReadKey();
         }
         private static void ShowMenu(IEdmVault12 vault)
         {
             //Create a context-sensitive menu
             //using Windows InsertMenu function
             System.Windows.Forms.ContextMenu mnu = default(System.Windows.Forms.ContextMenu);
             mnu = new System.Windows.Forms.ContextMenu();

             InsertMenu((IntPtr)mnu.Handle, 0, 0, (IntPtr)100, "First Command");
             InsertMenu((IntPtr)mnu.Handle, 0, 0, (IntPtr)101, "Second Command");
             InsertMenu((IntPtr)mnu.Handle, 0, 0, (IntPtr)102, "Third Command");

             //Create a selection list with all files in the root folder
             IEdmSelectionList5 selList = default(IEdmSelectionList5);
             selList = new EdmSelectionList5();

             IEdmFolder6 folder = default(IEdmFolder6);
             folder = (IEdmFolder6)vault.RootFolder;
             IEdmPos5 pos = default(IEdmPos5);
             pos = folder.GetFirstFilePosition();
             while (!pos.IsNull)
             {
                 IEdmFile8 file = default(IEdmFile8);
                 file = (IEdmFile8)folder.GetNextFile(pos);
                 EdmSelectionObject obj = default(EdmSelectionObject);
                 obj.mbsPath = file.GetLocalPath(folder.ID);
                 obj.meType = file.ObjectType;
                 obj.mlID = file.ID;
                 obj.mlProjectID = folder.ID;
                 ((IEdmSelectionList6)selList).AddTail2(obj);
             }

             //Add menu items for registered add-ins
             int count = 0;
             count = 0;
             int startID = 0;
             startID = 200;
             IEdmMenu7 menuCallback = default(IEdmMenu7);
             EdmCmdInfo[] ppoRetItems = null;
             menuCallback = vault.CreatePluginMenu2(mnu.Handle.ToInt32(), 3, ref startID, (IEdmSelectionList6)selList, (int)CreateMenuFlags.Cmf_ContextMenu, out count);
             menuCallback.GetItems((int)EdmMenuFlags.EdmMenu_Nothing, out ppoRetItems);

             string str = null;
             foreach (EdmCmdInfo item in ppoRetItems)
             {
                 str = "Add-in menu command item: " + "\r\n";
                 str = str + "Command ID: " + item.mlCmdID + "\r\n";
                 str = str + "Command string: " + item.mbsCmdStr + "\r\n";
                 str = str + "Tooltip: " + item.mbsTooltip + "\r\n";
                 str = str + "Status bar help: " + item.mbsStatusBarHelp + "\r\n";
                 str = str + "EdmMenuFlags: " + item.mlEdmMenuFlags;
                 MessageBox.Show(str);
             }

             //Display the menu using Windows TrackPopupMenu function
             int TPM_RETURNCMD = 0;
             TPM_RETURNCMD = 256;
             int cmdID = 0;
             frmParent = new Form();
             cmdID = TrackPopupMenu((IntPtr)mnu.Handle, TPM_RETURNCMD, frmParent.Left, frmParent.Top, 0, (IntPtr)frmParent.Handle, (IntPtr)0);

             //Run the selected command
             switch (cmdID)
             {
                 case 100:
                     MessageBox.Show("First command");
                     break;
                 case 101:
                     MessageBox.Show("Second command");
                     break;
                 case 102:
                     MessageBox.Show("Third command");
                     break;
                 default:
                     MessageBox.Show(cmdID);
                     break;
             }
         }
         [DllImport("user32", EntryPoint = "InsertMenuA", CharSet = CharSet.Ansi, SetLastError = true, ExactSpelling = true)]

         private static extern bool InsertMenu(System.IntPtr hMenu, int uPosition, int uFlags, System.IntPtr uIDNewItem, string lpNewItem);
         [DllImport("user32", EntryPoint = "TrackPopupMenu", CharSet = CharSet.Ansi, SetLastError = true, ExactSpelling = true)]

         private static extern int TrackPopupMenu(IntPtr hMenu, int uFlags, int x, int y, int nReserved, IntPtr hWnd, IntPtr prcRect);
     }
 }
```

[Back to top](#Top)
