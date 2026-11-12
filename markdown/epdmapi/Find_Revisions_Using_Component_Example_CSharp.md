---
title: "Find Revisions Using Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Find_Revisions_Using_Component_Example_CSharp.htm"
---

# Find Revisions Using Component Example (C#)

This example shows how to find the revision numbers using the revision number component named **Alpha Revision Component**.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio.
//  2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
//  3. Type FindRevisionsCSharp in Project name.
//  4. For Location, click ... and navigate to the folder where to
create the project.
//  5. Click Next.
//  6. Select Framework.
//  7. Click Create.
//  8. Click Show All Files in the Solution Explorer toolbar and expand
//     Form1.cs in the Solution Explorer.
//  9. Replace the code in Form1.cs with this code.
// 10. Replace the code in Form1.Designer.cs with this code.
// 11. Add dependencies and safely pass arrays of structures.
// 12. Open the Immediate window.
// 13. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click the Find revisions that use Alpha Revision Component button.
//  4. Prints the names of the revision numbers using the revision number
//     component Alpha Revision Component to the Immediate window.
//  5. Examine the Immediate window.
//  6. Close the dialog.
//----------------------------------------------------------------------------
```

```
//Form1.cs

using EPDM.Interop.epdm;
using System;
using System.Diagnostics;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace FindRevisionsCSharp
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		void FindRevisionsCSharp_Load(System.Object sender, System.EventArgs e)
		{
			try
			{
				//Declare and create an instance of IEdmVault5
				IEdmVault5 vault1 = new EdmVault5();

				//Cast IEdmVault5 to IEdmVault8
				IEdmVault8 vault = (IEdmVault8)vault1;

				EdmViewInfo[] Views = null;

				vault.GetVaultViews(out Views, false);
				VaultsComboBox.Items.Clear();
				foreach (EdmViewInfo View in Views)
				{
					VaultsComboBox.Items.Add(View.mbsVaultName);
				}
				if (VaultsComboBox.Items.Count > 0)
				{
					VaultsComboBox.Text = (string)VaultsComboBox.Items[0];
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

		private void FindRevisionsButton_Click(System.Object sender, System.EventArgs e)
	    {
		    try {
			        //Declare and create an instance of IEdmVault5 object
                                   //and cast to IEdmVault7
			        IEdmVault5 vault = new EdmVault5();
			        IEdmVault7 vault1 = (IEdmVault7)vault;

			        //Log into selected vault as the current user
			        vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

			        Debug.Print("Revision numbers that use revision number component \"Alpha Revision Component\":");
			        Debug.Print("");

			        IEdmRevisionMgr2 RevMgr = default(IEdmRevisionMgr2);
			        RevMgr = (IEdmRevisionMgr2)vault1.CreateUtility(EdmUtility.EdmUtil_RevisionMgr);

			        EdmRevNo[] RevNumbers = null;
			        RevMgr.GetRevisionNumbers(null, out RevNumbers);
			        foreach ( EdmRevNo RevNo in RevNumbers) {
				        EdmRevComponent2[] RevComponents = null;
				        RevMgr.GetRevisionNumberComponents2(-RevNo.mlRevNoID, out RevComponents);
				        foreach ( EdmRevComponent2 RevComponent in RevComponents) {
					        if (RevComponent.mbsComponentName == "Alpha Revision Component") {
						        Debug.Print("  " + RevNo.mbsRevNoName);
					        }
				        }
			        }

		        } catch (System.Runtime.InteropServices.COMException ex) {
			        MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
		        } catch (Exception ex) {
			        MessageBox.Show(ex.Message);
		    }
	    }
	}
}
```

```
Back to top
```

```
//Form1.Designer.cs
```

```
namespace FindRevisionsCSharp
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
        /// <param name="disposing">True if managed resources should be disposed; otherwise false</param>
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
        /// the contents of this method with the code editor
        /// </summary>
        private void InitializeComponent()
        {
            this.VaultsLabel = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.FindRevisionsButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(112, 37);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(94, 77);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // FindRevisionsButton
            //
            this.FindRevisionsButton.Location = new System.Drawing.Point(94, 136);
            this.FindRevisionsButton.Name = "FindRevisionsButton";
            this.FindRevisionsButton.Size = new System.Drawing.Size(121, 50);
            this.FindRevisionsButton.TabIndex = 2;
            this.FindRevisionsButton.Text = "Find revisions that use Alpha Revision Component";
            this.FindRevisionsButton.UseVisualStyleBackColor = true;
            this.FindRevisionsButton.Click += new System.EventHandler(this.FindRevisionsButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(304, 209);
            this.Controls.Add(this.FindRevisionsButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Find revisions using component";
            this.Load += new System.EventHandler(this.FindRevisionsCSharp_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button FindRevisionsButton;
    }
}
```

```
Back to top
```
