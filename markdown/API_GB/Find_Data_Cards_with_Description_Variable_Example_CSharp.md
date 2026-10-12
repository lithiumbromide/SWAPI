---
title: "Find Data Cards with Description Variable Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Find_Data_Cards_with_Description_Variable_Example_CSharp.htm"
---

# Find Data Cards with Description Variable Example (C#)

This example shows how to find the data cards in your vault that have a Description variable.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio 2010.
//  2. Click File > New > Project > C# > Windows Forms Application.
//  3. Type CardsVariableCSharp in Name.
//  4. Click the Browse button and browse to the folder where to create the project.
//  5. Click OK.
//  6. Create a form similar to the form shown above and change:
//     a. Label to VaultsLabel.
//     b. Combo box to VaultsComboBox.
//     c. Button to FindCardsButton.
//  7. Replace the code in Form1.cs with this code.
//  8. Replace the code in Form1.Designer.cs with this code.
//  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
//     name in the Solution Explorer, click Add Reference, click
//     Framework in the left-side panel, browse to the top folder of your
//     SOLIDWORKS PDM Professional installation, locate and select
//     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
// 10. Right-click EPDM.Interop.epdm in References, click Properties, and set
//     Embed Interop Types to False to handle methods that pass arrays of
//     structures.
// 11. Open the Immediate window.
// 12. Switch back to the Form1.cs code window.
// 13. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click the Find cards with Description variable button.
//     The cards in your vault with a Description variable are
//     printed to the Immediate window.
//  4. Examine the Immediate window.
//  5. Close the dialog.
//----------------------------------------------------------------------------
```

```
//Form1.cs
```

```
using System;
using System.Diagnostics;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using EPDM.Interop.epdm;
using System.Collections;

namespace CardsVariableCSharp
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		void CardsVariableCSharp_Load(System.Object sender, System.EventArgs e)
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

		private void FindCardsButton_Click(System.Object sender, System.EventArgs e)
		{

			try
			{
				//Declare and create an instance of IEdmVault5 object
				IEdmVault5 vault = new EdmVault5();

				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

				ArrayList Cards = new ArrayList();
				Cards.Clear();

				IEdmFolder5 Folder = default(IEdmFolder5);
				Folder = vault.RootFolder;

				IEdmVariableMgr5 VarMgr = default(IEdmVariableMgr5);
				VarMgr = (IEdmVariableMgr5)vault;

				//You could get the "Description" variable directly,
				//but get it by enumerating through all
				//the variables until it's found -
				//Dim DescVar As IEdmVariable5
				//DescVar = VarMgr.GetVariable("Description")

				IEdmPos5 VarPos = default(IEdmPos5);
				VarPos = VarMgr.GetFirstVariablePosition();
				while (!VarPos.IsNull)
				{
					IEdmVariable5 Var = default(IEdmVariable5);
					Var = VarMgr.GetNextVariable(VarPos);
					if (!(Var.Name == "Description"))
						continue;
					IEdmPos5 AttPos = default(IEdmPos5);
					AttPos = Var.GetFirstAttributePosition("");
					while (!AttPos.IsNull)
					{
						IEdmAttribute5 Att = default(IEdmAttribute5);
						Att = Var.GetNextAttribute(AttPos);
						string[] Extensions = null;
						Extensions = Att.Extensions.Split(',');
						string Extension = null;
						foreach (string Extension_loopVariable in Extensions)
						{
							Extension = Extension_loopVariable;
							IEdmCard5 Card = default(IEdmCard5);
							IEdmCard6 Card1 = default(IEdmCard6);
							try
							{
								Card = Folder.GetCard(Extension);
								Card1 = (IEdmCard6)Card;
								if (Card1.CardType == EdmCardType.EdmCard_File)
								{
									if (!Cards.Contains(Card.Name))
									{
										Cards.Add(Card.Name);
									}
								}
							} catch (System.Runtime.InteropServices.COMException ex)
							{
								//E_EDM_INVALID_NAME
								if (!(ex.ErrorCode == unchecked((int)0x8004021d)))
								{
									throw new System.Runtime.InteropServices.COMException(ex.Message, ex.ErrorCode);
								}
							}
						}
					}
				}

				string CardName = null;
				foreach (string CardName_loopVariable in Cards)
				{
					CardName = CardName_loopVariable;
					Debug.Print(CardName);
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
namespace CardsVariableCSharp
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used
        /// </summary>
        /// <param name="disposing">True if managed resources should be disposed; otherwise false.</param>
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
            this.FindCardsButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(86, 23);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(70, 55);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // FindCardsButton
            //
            this.FindCardsButton.Location = new System.Drawing.Point(70, 95);
            this.FindCardsButton.Name = "FindCardsButton";
            this.FindCardsButton.Size = new System.Drawing.Size(121, 50);
            this.FindCardsButton.TabIndex = 2;
            this.FindCardsButton.Text = "Find cards with Description variable";
            this.FindCardsButton.UseVisualStyleBackColor = true;
            this.FindCardsButton.Click += new System.EventHandler(this.FindCardsButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(272, 173);
            this.Controls.Add(this.FindCardsButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Find cards with Description";
            this.Load += new System.EventHandler(this.CardsVariableCSharp_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button FindCardsButton;
    }
}
```

```
Back to top
```
