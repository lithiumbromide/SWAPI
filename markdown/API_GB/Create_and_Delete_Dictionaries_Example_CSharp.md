---
title: "Create and Delete Dictionaries Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_and_Delete_Dictionaries_Example_CSharp.htm"
---

# Create and Delete Dictionaries Example (C#)

This example shows how to cerate and delete dictionaries and their keys and values.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio 2010.
//    a. Click File > New > Project > Visual C# > Windows Forms Application.
//    b. Type AddDictionaryCSharp in Name.
//    c. Click Browse and navigate to the folder where to create
//       the project.
//    d. Click OK.
//    e. Click Show All Files in the Solution Explorer toolbar and expand
//       Form1.cs in the Solution Explorer.
//    f. Replace the code in Form1.cs with this code.
//    g. To create the form, replace the code in Form1.Designer.cs with this code.
// 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
//    name in the Solution Explorer, click Add Reference, click
//    Assemblies > Framework in the left-side panel, browse to the top folder of
//    your SOLIDWORKS PDM Professional installation, locate and click
//    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
// 3. Right-click EPDM.Interop.epdm in References, cick Properties, and set
//    Embed Interop Types to False to handle methods that pass arrays of
//    structures.
// 4. Click Debug > Start Debugging or press F5.
//
// Postconditions:
// 1. Displays a dialog.
// 2. Select a vault.
// 3. Select the MyProjects dictionary.
//    a. Click Create.
//    b. Click Add project items.
//       The Key/Value list is populated with the
//       MyProjects dictionary's keys and values.
//    c. Type a unique value in Key and any value in Value.
//    d. Click Add Key/Value.
//       The key and value are added to the Key/Value list.
//    e. Select a key and value in the Key/Value list and
//       click Remove selected Key/Value.
//       The selected key and value are deleted from the
//       dictionary.
//    f. Type an existing key in Key and any value in Value.
//    g. Click Add Key/Value.
//       A message box is displayed informing you that the
//       duplicate keys are prohibited. Neither the key
//       nor value was added to the dictionary.
//    h. Click OK to close the message box.
// 4. Select the MyCounters dictionary.
//    a. Click Create.
//    b. Click Add counter items.
//       The Key/Value list is populated with the MyCounters
//       dictionary's keys and values.
// 5. Experiment with creating your own dictionary and adding
//    and removing keys and values to and from that dictionary.
// 6. Close the dialog.
//----------------------------------------------------------------------------
```

```
//Form1.cs
using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;
using System.Runtime.InteropServices;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Diagnostics;

namespace AddDictionaryCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        IEdmVault5 vault;
        IEdmVault8 vault1;

        void AddDictionary_Load(System.Object sender, System.EventArgs e)
        {
            try
            {
                vault = new EdmVault5();
                vault1 = (IEdmVault8)vault;
                EdmViewInfo[] Views = null;

                vault1.GetVaultViews(out Views, false);
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

        private void AddProjectItemsButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }
                IEdmDictionary5 ProjectDictionary = default(IEdmDictionary5);
                ProjectDictionary = vault.GetDictionary("MyProjects", true);
                //Create it if it doesn't exist

                //Add the new dictionary name to the combo box
                //if it doesn't exist
                if (!DictionaryComboBox.Items.Contains("MyProjects"))
                {
                    DictionaryComboBox.Items.Add("MyProjects");
                }

                bool SuccessSet = false;
                SuccessSet = ProjectDictionary.StringTestAndSetAt("1000", "Mercedes Benz");
                SuccessSet = ProjectDictionary.StringTestAndSetAt("1001", "Lexus");
                SuccessSet = ProjectDictionary.StringTestAndSetAt("1002", "Porche");
                SuccessSet = ProjectDictionary.StringTestAndSetAt("1003", "Audi");
                SuccessSet = ProjectDictionary.StringTestAndSetAt("1004", "BMW");
                SuccessSet = ProjectDictionary.StringTestAndSetAt("1005", "Jaguar");

                if (DictionaryComboBox.Text == "MyProjects")
                {
                    DisplayDictionaryItems("MyProjects", ProjectDictionary, KeyValueListBox);
                }
                else
                {
                    DictionaryComboBox.Text = "MyProjects";
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

        private void DictionaryComboBox_SelectedIndexChanged(System.Object sender, System.EventArgs e)
        {
            try
            {
                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                //Get the selected dictionary, if it exists
                IEdmDictionary5 Dictionary = default(IEdmDictionary5);
                Dictionary = vault.GetDictionary(DictionaryComboBox.Text, false);
                //Display the dictionary contents
                DisplayDictionaryItems(DictionaryComboBox.Text, Dictionary, KeyValueListBox);
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

        private void CreateButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                KeyValueListBox.Items.Clear();

                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                //Get the selected dictionary, if it exists
                IEdmDictionary5 Dictionary = default(IEdmDictionary5);
                Dictionary = vault.GetDictionary(DictionaryComboBox.Text, false);
                //If it doesn't exist, create it
                if (Dictionary == null)
                {
                    //Create it, because it doesn't exist
                    Dictionary = vault.GetDictionary(DictionaryComboBox.Text, true);
                    KeyValueListBox.Items.Add(DictionaryComboBox.Text + " dictionary created.");
                }
                else
                {
                    //If it does exist, inform the user
                    KeyValueListBox.Items.Add(DictionaryComboBox.Text + " dictionary already exists.");
                }

                //Add the new dictionary name to the combo box,
                //if it doesn't exist
                if (!DictionaryComboBox.Items.Contains(DictionaryComboBox.Text))
                {
                    DictionaryComboBox.Items.Add(DictionaryComboBox.Text);
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

        private void DeleteButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                KeyValueListBox.Items.Clear();
                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                //Get the selected dictionary, if it exists
                IEdmDictionary5 Dictionary = default(IEdmDictionary5);
                Dictionary = vault.GetDictionary(DictionaryComboBox.Text, false);
                //If it doesn't exist, inform the user
                if (Dictionary == null)
                {
                    KeyValueListBox.Items.Add(DictionaryComboBox.Text + " dictionary doesn't exist.");
                    //If it does exist, delete it and inform the user
                }
                else
                {
                    Dictionary.RemoveDictionary();
                    KeyValueListBox.Items.Add(DictionaryComboBox.Text + " dictionary deleted.");
                }
                //Remove the dictionary name from the list box
                DictionaryComboBox.Items.Remove(DictionaryComboBox.Text);
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

        private void AddKeyValueButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                IEdmDictionary5 Dictionary = default(IEdmDictionary5);
                Dictionary = vault.GetDictionary(DictionaryComboBox.Text, false);

                //Make sure that the user has typed valid data
                if (string.IsNullOrEmpty(KeyTextBox.Text) | string.IsNullOrEmpty(ValueTextBox.Text))
                {
                    MessageBox.Show("Please type a key and a value.");
                    return;
                }

                //Add the data if it doesn't exist in the dictionary
                bool SuccessSet = false;
                SuccessSet = Dictionary.StringTestAndSetAt(KeyTextBox.Text, ValueTextBox.Text);
                if (!SuccessSet)
                {
                    MessageBox.Show("The value you typed for Key already exists; duplicate keys are prohibited. Neither the key nor value was added to this dictionary. Try again.");
                }
                else
                {
                    DisplayDictionaryItems(DictionaryComboBox.Text, Dictionary, KeyValueListBox);
                    KeyTextBox.Text = "";
                    ValueTextBox.Text = "";
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

        private void RemoveButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                if (KeyValueListBox.SelectedIndex == -1)
                {
                    MessageBox.Show("No Key/Value selected.");
                    return;
                }

                string KeyValue = null;
                KeyValue = (string)KeyValueListBox.Items[KeyValueListBox.SelectedIndex];
                string key = null;
                string spaceSeparator = " ";
                string[] splitValue = KeyValue.Split(spaceSeparator.ToCharArray());
                key = (string)splitValue[0];

                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                IEdmDictionary5 Dictionary = default(IEdmDictionary5);
                Dictionary = vault.GetDictionary(DictionaryComboBox.Text, false);

                Dictionary.StringRemoveAt(key);
                KeyValueListBox.Items.Remove(KeyValue);
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

        private void AddCounterItemsButton_Click(System.Object sender, System.EventArgs e)
        {

            try
            {
                if (!vault.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                IEdmDictionary5 CounterDictionary = default(IEdmDictionary5);
                CounterDictionary = vault.GetDictionary("MyCounters", true);
                //Create it, if it doesn't exist

                //Add the new dictionary name to the list box,
                //if it doesn't exist
                if (!DictionaryComboBox.Items.Contains("MyCounters"))
                {
                    DictionaryComboBox.Items.Add("MyCounters");
                }

                bool SuccessSet = false;
                SuccessSet = CounterDictionary.StringTestAndSetAt("Electric", "5");
                SuccessSet = CounterDictionary.StringTestAndSetAt("Hybrid", "10");
                SuccessSet = CounterDictionary.StringTestAndSetAt("Gasoline", "15");
                SuccessSet = CounterDictionary.StringTestAndSetAt("Diesel", "20");

                if (DictionaryComboBox.Text == "MyCounters")
                {
                    DisplayDictionaryItems("MyCounters", CounterDictionary, KeyValueListBox);
                }
                else
                {
                    DictionaryComboBox.Text = "MyCounters";
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

        private void DisplayDictionaryItems(string DictionaryName, IEdmDictionary5 Dictionary, ListBox ListObject)
        {
            try
            {

                ListObject.Items.Clear();

                if (Dictionary == null)
                {
                    ListObject.Items.Add(DictionaryComboBox.Text + " dictionary doesn't exist.");
                }
                else
                {
                    //Traverse and display the Key/Value pairs
                    //in the dictionary
                    string Key = "";
                    string Value = "";
                    IEdmPos5 Pos = default(IEdmPos5);
                    Pos = Dictionary.StringGetFirstPosition();
                    while (!Pos.IsNull)
                    {
                        Dictionary.StringGetNextAssoc(Pos, out Key, out Value);
                        ListObject.Items.Add(Key + " " + Value);
                    }
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
namespace AddDictionaryCSharp
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
            this.VaultsLabel = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.DictionaryLabel = new System.Windows.Forms.Label();
            this.DictionaryComboBox = new System.Windows.Forms.ComboBox();
            this.CreateButton = new System.Windows.Forms.Button();
            this.DeleteButton = new System.Windows.Forms.Button();
            this.KeyValueLabel = new System.Windows.Forms.Label();
            this.KeyValueListBox = new System.Windows.Forms.ListBox();
            this.RemoveButton = new System.Windows.Forms.Button();
            this.KeyLabel = new System.Windows.Forms.Label();
            this.KeyTextBox = new System.Windows.Forms.TextBox();
            this.ValueLabel = new System.Windows.Forms.Label();
            this.ValueTextBox = new System.Windows.Forms.TextBox();
            this.AddKeyValueButton = new System.Windows.Forms.Button();
            this.AddProjectItemsButton = new System.Windows.Forms.Button();
            this.AddCounterItemsButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(13, 27);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(15, 43);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(213, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // DictionaryLabel
            //
            this.DictionaryLabel.AutoSize = true;
            this.DictionaryLabel.Location = new System.Drawing.Point(16, 78);
            this.DictionaryLabel.Name = "DictionaryLabel";
            this.DictionaryLabel.Size = new System.Drawing.Size(88, 13);
            this.DictionaryLabel.TabIndex = 2;
            this.DictionaryLabel.Text = "Select dictionary:";
            //
            // DictionaryComboBox
            //
            this.DictionaryComboBox.FormattingEnabled = true;
            this.DictionaryComboBox.Items.AddRange(new object[] { "MyProjects", "MyCounters" });
            this.DictionaryComboBox.Location = new System.Drawing.Point(15, 94);
            this.DictionaryComboBox.Name = "DictionaryComboBox";
            this.DictionaryComboBox.Size = new System.Drawing.Size(210, 21);
            this.DictionaryComboBox.TabIndex = 3;
            //
            // CreateButton
            //
            this.CreateButton.Location = new System.Drawing.Point(16, 121);
            this.CreateButton.Name = "CreateButton";
            this.CreateButton.Size = new System.Drawing.Size(75, 23);
            this.CreateButton.TabIndex = 4;
            this.CreateButton.Text = "Create";
            this.CreateButton.UseVisualStyleBackColor = true;
            this.CreateButton.Click += new System.EventHandler(this.CreateButton_Click);
            //
            // DeleteButton
            //
            this.DeleteButton.Location = new System.Drawing.Point(150, 121);
            this.DeleteButton.Name = "DeleteButton";
            this.DeleteButton.Size = new System.Drawing.Size(75, 23);
            this.DeleteButton.TabIndex = 5;
            this.DeleteButton.Text = "Delete";
            this.DeleteButton.UseVisualStyleBackColor = true;
            this.DeleteButton.Click += new System.EventHandler(this.DeleteButton_Click);
            //
            // KeyValueLabel
            //
            this.KeyValueLabel.AutoSize = true;
            this.KeyValueLabel.Location = new System.Drawing.Point(19, 163);
            this.KeyValueLabel.Name = "KeyValueLabel";
            this.KeyValueLabel.Size = new System.Drawing.Size(57, 13);
            this.KeyValueLabel.TabIndex = 6;
            this.KeyValueLabel.Text = "Key/Value";
            //
            // KeyValueListBox
            //
            this.KeyValueListBox.FormattingEnabled = true;
            this.KeyValueListBox.Location = new System.Drawing.Point(15, 190);
            this.KeyValueListBox.Name = "KeyValueListBox";
            this.KeyValueListBox.Size = new System.Drawing.Size(210, 95);
            this.KeyValueListBox.TabIndex = 7;
            //
            // RemoveButton
            //
            this.RemoveButton.Location = new System.Drawing.Point(16, 301);
            this.RemoveButton.Name = "RemoveButton";
            this.RemoveButton.Size = new System.Drawing.Size(210, 23);
            this.RemoveButton.TabIndex = 8;
            this.RemoveButton.Text = "Remove selected Key/Value";
            this.RemoveButton.UseVisualStyleBackColor = true;
            this.RemoveButton.Click += new System.EventHandler(this.RemoveButton_Click);
            //
            // KeyLabel
            //
            this.KeyLabel.AutoSize = true;
            this.KeyLabel.Location = new System.Drawing.Point(19, 340);
            this.KeyLabel.Name = "KeyLabel";
            this.KeyLabel.Size = new System.Drawing.Size(25, 13);
            this.KeyLabel.TabIndex = 9;
            this.KeyLabel.Text = "Key";
            //
            // KeyTextBox
            //
            this.KeyTextBox.Location = new System.Drawing.Point(19, 356);
            this.KeyTextBox.Name = "KeyTextBox";
            this.KeyTextBox.Size = new System.Drawing.Size(100, 20);
            this.KeyTextBox.TabIndex = 10;
            //
            // ValueLabel
            //
            this.ValueLabel.AutoSize = true;
            this.ValueLabel.Location = new System.Drawing.Point(144, 340);
            this.ValueLabel.Name = "ValueLabel";
            this.ValueLabel.Size = new System.Drawing.Size(34, 13);
            this.ValueLabel.TabIndex = 11;
            this.ValueLabel.Text = "Value";
            //
            // ValueTextBox
            //
            this.ValueTextBox.Location = new System.Drawing.Point(147, 356);
            this.ValueTextBox.Name = "ValueTextBox";
            this.ValueTextBox.Size = new System.Drawing.Size(100, 20);
            this.ValueTextBox.TabIndex = 12;
            //
            // AddKeyValueButton
            //
            this.AddKeyValueButton.Location = new System.Drawing.Point(19, 397);
            this.AddKeyValueButton.Name = "AddKeyValueButton";
            this.AddKeyValueButton.Size = new System.Drawing.Size(228, 23);
            this.AddKeyValueButton.TabIndex = 13;
            this.AddKeyValueButton.Text = "Add Key/Value";
            this.AddKeyValueButton.UseVisualStyleBackColor = true;
            this.AddKeyValueButton.Click += new System.EventHandler(this.AddKeyValueButton_Click);
            //
            // AddProjectItemsButton
            //
            this.AddProjectItemsButton.Location = new System.Drawing.Point(19, 438);
            this.AddProjectItemsButton.Name = "AddProjectItemsButton";
            this.AddProjectItemsButton.Size = new System.Drawing.Size(100, 23);
            this.AddProjectItemsButton.TabIndex = 14;
            this.AddProjectItemsButton.Text = "Add project items";
            this.AddProjectItemsButton.UseVisualStyleBackColor = true;
            this.AddProjectItemsButton.Click += new System.EventHandler(this.AddProjectItemsButton_Click);
            //
            // AddCounterItemsButton
            //
            this.AddCounterItemsButton.Location = new System.Drawing.Point(136, 438);
            this.AddCounterItemsButton.Name = "AddCounterItemsButton";
            this.AddCounterItemsButton.Size = new System.Drawing.Size(110, 23);
            this.AddCounterItemsButton.TabIndex = 15;
            this.AddCounterItemsButton.Text = "Add counter items";
            this.AddCounterItemsButton.UseVisualStyleBackColor = true;
            this.AddCounterItemsButton.Click += new System.EventHandler(this.AddCounterItemsButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 482);
            this.Controls.Add(this.AddCounterItemsButton);
            this.Controls.Add(this.AddProjectItemsButton);
            this.Controls.Add(this.AddKeyValueButton);
            this.Controls.Add(this.ValueTextBox);
            this.Controls.Add(this.ValueLabel);
            this.Controls.Add(this.KeyTextBox);
            this.Controls.Add(this.KeyLabel);
            this.Controls.Add(this.RemoveButton);
            this.Controls.Add(this.KeyValueListBox);
            this.Controls.Add(this.KeyValueLabel);
            this.Controls.Add(this.DeleteButton);
            this.Controls.Add(this.CreateButton);
            this.Controls.Add(this.DictionaryComboBox);
            this.Controls.Add(this.DictionaryLabel);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Create a dictionary";
            this.Load += new System.EventHandler(this.AddDictionary_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Label DictionaryLabel;
        private System.Windows.Forms.ComboBox DictionaryComboBox;
        private System.Windows.Forms.Button CreateButton;
        private System.Windows.Forms.Button DeleteButton;
        private System.Windows.Forms.Label KeyValueLabel;
        private System.Windows.Forms.ListBox KeyValueListBox;
        private System.Windows.Forms.Button RemoveButton;
        private System.Windows.Forms.Label KeyLabel;
        private System.Windows.Forms.TextBox KeyTextBox;
        private System.Windows.Forms.Label ValueLabel;
        private System.Windows.Forms.TextBox ValueTextBox;
        private System.Windows.Forms.Button AddKeyValueButton;
        private System.Windows.Forms.Button AddProjectItemsButton;
        private System.Windows.Forms.Button AddCounterItemsButton;
    }
}
```

```
Back to top
```
