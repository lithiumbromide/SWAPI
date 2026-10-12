---
title: "Start, Update, and Stop Progress Indicator Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Start,_Update,_and_Stop_User_Progress_Bar_Example_CSharp.htm"
---

# Start, Update, and Stop Progress Indicator Example (C#)

This example shows how to create, start, update, and stop a progress indicator on the system task bar.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# macro in SOLIDWORKS Design called ManipulatePB_CSharp.
 // 2. Right-click the macro project name in the Project Explorer and click
 //    Add > Windows Form.
 // 3. Click Add.
 // 4. Modify Form1.cs [Design] to look like this:

// 5. Copy  Forms - Form1  into Form1.cs.
 // 6. Modify control_name in each control_name_Click subroutine to
 //    match your form.
 // 7. Copy SolidWorksMacro into SolidWorksMacro.cs.
 // 8. Open the Immediate window.
 //
 // Postconditions:
 // 1. Shows a dialog box.
 // 2. Click Start.
 //    * Displays a progress indicator on the SOLIDWORKS Design icon on the
 //      system taskbar.
 //    * Increments the progress indicator to 100% completion.
 // 3. Click Update repeatedly to increment the progress indicator in steps of
 //    10.
 // 4. Inspect the Immediate window to see the return code after each update.
 // 5. Type a new title and click Update Title to change the progress indicator
 //    title.
 // 6. Click Stop to remove the progress indicator from SOLIDWORKS Design.
 // 7. Click Exit to close the dialog box.
 // ---------------------------------------------------------------------------
```

#### Forms - Form1

```vb
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Text;
 using System.Windows.Forms;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using Microsoft.VisualBasic;

 namespace ManipulateUserPB_CSharp.csproj
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         UserProgressBar pb;
         int Position;
         int lRet;
         bool retVal;
         bool boolstatus;
         public SldWorks swApp;

         public void cmdExit_Click(System.Object sender, System.EventArgs e)
         {
             this.Close();
         }

         public void cmdPBTitle_Click(System.Object sender, System.EventArgs e)
         {
             retVal = pb.UpdateTitle(textBox1.Text);
         }

         public void cmdStartPB_Click(System.Object sender, System.EventArgs e)
         {
             boolstatus = pb.Start(0, 160, "Status");
             while (!(Position == 160)) {
                 Position = Position + 10;
                 lRet = pb.UpdateProgress(Position);
             }
             Position = 0;
         }

         public void cmdStopPB_Click(System.Object sender, System.EventArgs e)
         {
             pb.End();
         }

         public void Form1_Initialize(System.Object sender, System.EventArgs e)
         {
             swApp = (SldWorks)System.Runtime.InteropServices.Marshal.GetActiveObject("SldWorks.Application");
             retVal = swApp.GetUserProgressBar(out pb);
         }

         public void cmdUpdatePB_Click(System.Object sender, System.EventArgs e)
         {
             Position = Position + 10;
             if ((Position == 160))
                 Position = 0;
             lRet = pb.UpdateProgress(Position);
             if (lRet != 2) {
                 Debug.Print(" Result " + lRet);
             } else {
                 MessageBox.Show(" User pressed Esc to cancel ", " API");
                 pb.End();
             }
         }

         private void TextBox1_TextChanged(System.Object sender, System.EventArgs e)
         {
         }

     }
 }
```

[Back to top](#Top)

#### SolidWorksMacro

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace ManipulateUserPB_CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         System.Windows.Forms.Form aForm;
         public void Main()
         {
             aForm = new Form1();
             aForm.ShowDialog();
         }

         /// <summary>
         ///  The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

[Back to top](#Top)
