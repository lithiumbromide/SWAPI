---
title: "Get and Run a Task Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_and_Run_a_Task_Add-in_Example_CSharp.htm"
---

# Get and Run a Task Add-in Example (C#)

This example shows how to get a task add-in that is registered in the Admin tool and run it.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type TasksDemo in Project name.
 // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9. Replace the code in Form1.cs with this code.
 //10. To create the form, replace the code in Form1.Designer.cs with
 //    this code.
 //11.     Add dependencies and safely pass arrays of structures.
 //12. Ensure that a task add-in has been registered with the Administration tool.
 //13. Ensure that a task to run the task add-in has been created in the
 //    Administration tool.
 //14. Ensure that your vault has permission to run the task add-in by selecting
 //    Permit in Task Host Configuration dialog. (Right-click the SOLIDWORKS PDM
 //    icon on the notification tool bar and select Task Host Configuration.)
 //15. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. In the Vaults dropdown, select the vault permitted to run the task add-in.
 // 2. Click Log In.
 // 3. In the Tasks dropdown, select the task to run.
 // 4. Click Select Files to select any files that are required for the task.
 // 5. Click Run Task.
 //----------------------------------------------------------------------------
  //Form1.cs
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace TasksDemo
 {
     public partial class Form1 : Form
     {
         IEdmVault5 vault5;
         IEdmVault20 vault20;
         IEdmTaskMgr TaskMgr;
         EdmStrLst5 files;
         class CustomComboType
         {
             public EdmTaskInfo TaskInfo;
             public override string ToString()
             {
                 return TaskInfo.mbsTaskName;
             }
         }
         public Form1()
         {
             InitializeComponent();
             vault5 = new EdmVault5();
             vault20 = (IEdmVault20)vault5;
             EdmViewInfo[] Views = new EdmViewInfo[1];
             vault20.GetVaultViews(out Views, false);
             foreach (EdmViewInfo view in Views)
                 comboBox1.Items.Add(view.mbsVaultName);
             if (comboBox1.Items.Count > 0)
                 comboBox1.Text = comboBox1.Items[0].ToString();
         }

         private void button1_Click(object sender, EventArgs e)
         {
             //Create a file vault interface and log into a vault
             if (comboBox1.Text != string.Empty)
             {
                 vault20.LoginAuto(comboBox1.Text, this.Handle.ToInt32());
                 TaskMgr = (IEdmTaskMgr)vault20.CreateUtility(EdmUtility.EdmUtil_TaskMgr);
                 System.Array Tasks = TaskMgr.GetTasks();

                 foreach (EdmTaskInfo task in Tasks)
                     comboBox2.Items.Add( new CustomComboType { TaskInfo = task });
                 if (comboBox2.Items.Count > 0)
                     comboBox2.SelectedItem = comboBox2.Items[0];
             }
         }

         private void button2_Click(object sender, EventArgs e)
         {
             files  = vault20.BrowseForFile(this.Handle.ToInt32(),
                 (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitMultipleSel + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles,
                 "SOLIDWORKS files " + "(*.sldprt; *.sldasm; *.slddrw)|" + "*.sldprt;*.sldasm;*.slddrw|" + "All Files (*.*)|*.*||", "", "",
                 vault20.RootFolderPath, "Select Files");

         }

         private void button3_Click(object sender, EventArgs e)
         {
             EdmSelItem2[] selection = new EdmSelItem2[files.Count];
             IEdmPos5 pos = files.GetHeadPosition();
             int counter = 0;
             while(!pos.IsNull)
             {
                 IEdmFolder5 parentFolder = null;
                 IEdmFile5 file = vault20.GetFileFromPath(files.GetNext(pos), out parentFolder);
                 selection[counter].mlID = file.ID;
                 selection[counter].mlParentID = parentFolder.ID;
                 selection[counter].mlVersion = file.CurrentVersion;
                 selection[counter].meType = EdmObjectType.EdmObject_File;
             }
             TaskMgr.RunTask(((CustomComboType)comboBox2.SelectedItem).TaskInfo, selection, this.Handle.ToInt32());
         }
     }
 }

 Back to top

  //Form1.Designer
 namespace TasksDemo
 {
     partial class Form1
     {
         /// <summary>
         /// Required designer variable.
         /// </summary>
         private System.ComponentModel.IContainer components = null;

         /// <summary>
         /// Clean up any resources being used.
         /// </summary>
         /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
         protected override void Dispose(bool disposing)
         {
             if (disposing && (components != null))
             {
                 components.Dispose();
             }
             base.Dispose(disposing);
         }

         #region Windows Form Designer generated code

         /// <summary>
         /// Required method for Designer support - do not modify
         /// the contents of this method with the code editor.
         /// </summary>
         private void InitializeComponent()
         {
             this.comboBox1 = new System.Windows.Forms.ComboBox();
             this.comboBox2 = new System.Windows.Forms.ComboBox();
             this.button1 = new System.Windows.Forms.Button();
             this.button2 = new System.Windows.Forms.Button();
             this.button3 = new System.Windows.Forms.Button();
             this.label1 = new System.Windows.Forms.Label();
             this.label2 = new System.Windows.Forms.Label();
             this.SuspendLayout();
             //
             // comboBox1
             //
             this.comboBox1.DisplayMember = "mbsVaultName";
             this.comboBox1.FormattingEnabled = true;
             this.comboBox1.Location = new System.Drawing.Point(50, 12);
             this.comboBox1.Name = "comboBox1";
             this.comboBox1.Size = new System.Drawing.Size(121, 21);
             this.comboBox1.TabIndex = 0;
             //
             // comboBox2
             //
             this.comboBox2.FormattingEnabled = true;
             this.comboBox2.Location = new System.Drawing.Point(50, 66);
             this.comboBox2.Name = "comboBox2";
             this.comboBox2.Size = new System.Drawing.Size(121, 21);
             this.comboBox2.TabIndex = 1;
             //
             // button1
             //
             this.button1.Location = new System.Drawing.Point(50, 37);
             this.button1.Name = "button1";
             this.button1.Size = new System.Drawing.Size(121, 23);
             this.button1.TabIndex = 2;
             this.button1.Text = "Log In";
             this.button1.UseVisualStyleBackColor = true;
             this.button1.Click += new System.EventHandler(this.button1_Click);
             //
             // button2
             //
             this.button2.Location = new System.Drawing.Point(50, 93);
             this.button2.Name = "button2";
             this.button2.Size = new System.Drawing.Size(121, 23);
             this.button2.TabIndex = 3;
             this.button2.Text = "Select Files";
             this.button2.UseVisualStyleBackColor = true;
             this.button2.Click += new System.EventHandler(this.button2_Click);
             //
             // button3
             //
             this.button3.Location = new System.Drawing.Point(50, 123);
             this.button3.Name = "button3";
             this.button3.Size = new System.Drawing.Size(121, 23);
             this.button3.TabIndex = 4;
             this.button3.Text = "Run Task";
             this.button3.UseVisualStyleBackColor = true;
             this.button3.Click += new System.EventHandler(this.button3_Click);
             //
             // label1
             //
             this.label1.AutoSize = true;
             this.label1.Location = new System.Drawing.Point(2, 19);
             this.label1.Name = "label1";
             this.label1.Size = new System.Drawing.Size(39, 13);
             this.label1.TabIndex = 5;
             this.label1.Text = "Vaults:";
             //
             // label2
             //
             this.label2.AutoSize = true;
             this.label2.Location = new System.Drawing.Point(5, 74);
             this.label2.Name = "label2";
             this.label2.Size = new System.Drawing.Size(39, 13);
             this.label2.TabIndex = 6;
             this.label2.Text = "Tasks:";
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(178, 150);
             this.Controls.Add(this.label2);
             this.Controls.Add(this.label1);
             this.Controls.Add(this.button3);
             this.Controls.Add(this.button2);
             this.Controls.Add(this.button1);
             this.Controls.Add(this.comboBox2);
             this.Controls.Add(this.comboBox1);
             this.Name = "Form1";
             this.Text = "Tasks API Demo";
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.ComboBox comboBox1;
         private System.Windows.Forms.ComboBox comboBox2;
         private System.Windows.Forms.Button button1;
         private System.Windows.Forms.Button button2;
         private System.Windows.Forms.Button button3;
         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.Label label2;
     }
 }

 Back to top
```
