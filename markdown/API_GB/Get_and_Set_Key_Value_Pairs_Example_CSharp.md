---
title: "Get and Set Dictionary Key-Value Pairs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_and_Set_Key_Value_Pairs_Example_CSharp.htm"
---

# Get and Set Dictionary Key-Value Pairs Example (C#)

This example shows how to access key-value pairs in a vault dictionary.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio 2010.
//    a. Click File > New > Project > Visual C# > Windows Forms Application.
//    b. Type TestDictionary_CSharp in Name.
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
//    EPDM.Interop.epdm.dll, click Open, and click Add).
// 3. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
//    click Microsoft.VisualBasic, click Add, and click Close).
// 4. Right-click EPDM.Interop.epdm in References, cick Properties, and set
//    Embed Interop Types to False to handle methods that pass arrays of
//    structures.
// 5. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault view.
//  3. Click Substring in key.
//  4. Click Get key-value pairs.
//     a. Displays a message box with all key-value pairs in the dictionary where
//        string key contains "at".
//     b. Click OK.
//  5. Click Integer key range.
//  6. Click Get key-value pairs.
//     a. Displays a message box with all key-value pairs in the dictionary where
//        integer keys are in the range, 13-88.
//     b. Click OK.
//  7. Click Substring in values of all integer keys.
//  8. Click Get key-value pairs.
//     a. Displays a message box with all key-value pairs in the dictionary where
//        value contains "three".
//     b. Click OK.
//  9. Click Specific integer key.
// 10. Click Get key-value pairs.
//     a. Displays a message box with the value for key, 77.
//     b. Click OK.
// 11. Click Enumeration of all integer keys.
// 12. Click Get key-value pairs.
//     a. Displays a message box with all integer key-value pairs in the dictionary.
//     b. Click OK.
// 13. Click Delete a key-value pair.
//     a. Displays a message box notifying that key, 2, is removed.
//     b. Click OK.
// 14. Click Create a key-value pair.
//     a. Displays a message box notifying that key, 2, is created.
//     b. Click OK.
// 15. Close the dialog.
//----------------------------------------------------------------------------
```

```
//Form1.cs
```

```vb
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using Microsoft.VisualBasic;
 using EPDM.Interop.epdm;

 namespace TestDictionary_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         IEdmVault5 vault1;
         IEdmVault8 vault;

         EdmViewInfo[] Views = null;
         IEdmDictionary5 dic;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
                 vault = (IEdmVault8)vault1;
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

         private void Button5_Click(System.Object sender, System.EventArgs e)
         {
             //Delete key-value pair clicked
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;

                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 dic = vault.GetDictionary("MyDictionary", true);
                 //Add some values
                 dic.LongSetAt(2, "two");
                 dic.LongSetAt(15, "fifteen");
                 dic.LongSetAt(300, "three hundred");
                 dic.LongSetAt(77, "seventy-seven");

                 dic.LongRemoveAt(2);
                 MessageBox.Show("Key <2> removed.");
                 dic.RemoveDictionary();

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

         private void Button1_Click(System.Object sender, System.EventArgs e)
         {
             //Get key-value pairs clicked
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;

                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 if (this.RadioButton1.Checked)
                 {
                     //Get key-value pairs by substring in key

                     dic = vault.GetDictionary("MyDictionary", true);

                     //Add some values
                     dic.StringSetAt("Cat", "Socks");
                     dic.StringSetAt("Dog", "Milou");
                     dic.StringSetAt("Human", "Attila");
                     dic.StringSetAt("At last", "Last value");

                     //Find all keys containing the text, "at"
                     string key = "";
                     string value = "";
                     string message = null;
                     message = "Keys with 'at' in them:" + Constants.vbLf;
                     IEdmPos5 pos = default(IEdmPos5);
                     pos = dic.StringFindKeys("at");
                     while (!pos.IsNull)
                     {
                         dic.StringGetNextAssoc(pos, out key, out value);
                         message = message + "<" + key + "> = <" + value + ">" + Constants.vbLf;
                     }

                     //Show a message and delete the dictionary
                     Interaction.MsgBox(message);
                     dic.RemoveDictionary();

                 }
                 else if (this.RadioButton2.Checked)
                 {
                     //Get key-value pairs by integer key range

                     dic = vault.GetDictionary("MyDictionary", true);

                     //Add some values
                     dic.LongSetAt(2, "two");
                     dic.LongSetAt(15, "fifteen");
                     dic.LongSetAt(300, "three hundred");
                     dic.LongSetAt(77, "seventy-seven");

                     //Find all keys in the range, 13-88
                     int key = 0;
                     string value = "";
                     string message = null;
                     message = "Keys in range, 13-88:" + Constants.vbLf;
                     IEdmPos5 pos = default(IEdmPos5);
                     pos = dic.LongFindKeys(13, 88);
                     while (!pos.IsNull)
                     {
                         dic.LongGetNextAssoc(pos, out key, out value);
                         message = message + "<" + Conversion.Str(key) + "> = <" + value + ">" + Constants.vbLf;
                     }

                     //Show a message and delete the dictionary
                     Interaction.MsgBox(message);
                     dic.RemoveDictionary();

                 }
                 else if (this.RadioButton3.Checked)
                 {
                     //Get key-value pairs by substring in values of integer keys

                     dic = vault.GetDictionary("MyDictionary", true);
                     //Add some values
                     dic.LongSetAt(2, "two");
                     dic.LongSetAt(15, "fifteen");
                     dic.LongSetAt(300, "three hundred");
                     dic.LongSetAt(77, "seventy-seven");

                     string bsValueSubString = "three";
                     IEdmPos5 aPos = default(IEdmPos5);
                     int plRetKey = 0;
                     string pbsRetValue = "";
                     aPos = dic.LongFindValues(bsValueSubString);
                     while (!aPos.IsNull)
                     {
                         dic.LongGetNextAssoc(aPos, out plRetKey, out pbsRetValue);
                         MessageBox.Show("Key-value pair with " + "\"" + bsValueSubString + "\"" + " in value: " + Constants.vbLf + "<" + plRetKey + "> = <" + pbsRetValue + ">");
                     }
                     dic.RemoveDictionary();
                 }
                 else if (this.RadioButton4.Checked)
                 {
                     //Get key-value pairs by specific integer key

                     dic = vault.GetDictionary("MyDictionary", true);
                     //Add some values
                     dic.LongSetAt(2, "two");
                     dic.LongSetAt(15, "fifteen");
                     dic.LongSetAt(300, "three hundred");
                     dic.LongSetAt(77, "seventy-seven");

                     string pbsRetValue = "";
                     dic.LongGetAt(77, out pbsRetValue);
                     MessageBox.Show("Value for key <77>: <" + pbsRetValue + ">");
                     dic.RemoveDictionary();
                 }
                 else if (this.RadioButton5.Checked)
                 {
                     //Get key-value pairs by enumeration of all integer keys

                     dic = vault.GetDictionary("MyDictionary", true);
                     //Add some values
                     dic.LongSetAt(2, "two");
                     dic.LongSetAt(15, "fifteen");
                     dic.LongSetAt(300, "three hundred");
                     dic.LongSetAt(77, "seventy-seven");

                     string msg = null;
                     int key = 0;
                     string value = "";

                     msg = "Integer keys in dictionary:" + Constants.vbLf;

                     IEdmPos5 pos = default(IEdmPos5);
                     pos = dic.LongGetFirstPosition();
                     while (!pos.IsNull)
                     {
                         dic.LongGetNextAssoc(pos, out key, out value);
                         msg = msg + "<" + Conversion.Str(key) + "> = <" + value + ">" + Constants.vbLf;
                     }
                     Interaction.MsgBox(msg);
                     dic.RemoveDictionary();

                 }
                 else
                 {
                     MessageBox.Show("Select how to get key-value pairs");

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

         private void Button7_Click(System.Object sender, System.EventArgs e)
         {
             //Create key-value pair clicked
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;

                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 string pbsRetValue = "";

                 dic = vault.GetDictionary("MyDictionary", true);
                 dic.LongTestAndSetAt(2, "Two");
                 dic.LongGetAt(2, out pbsRetValue);
                 MessageBox.Show("Created:" + Constants.vbLf + "<2> = <" + pbsRetValue + ">");
                 dic.RemoveDictionary();
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

```vb
 namespace TestDictionary_CSharp
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
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.Label1 = new System.Windows.Forms.Label();
             this.Button5 = new System.Windows.Forms.Button();
             this.Button7 = new System.Windows.Forms.Button();
             this.RadioButton1 = new System.Windows.Forms.RadioButton();
             this.RadioButton2 = new System.Windows.Forms.RadioButton();
             this.RadioButton3 = new System.Windows.Forms.RadioButton();
             this.RadioButton4 = new System.Windows.Forms.RadioButton();
             this.RadioButton5 = new System.Windows.Forms.RadioButton();
             this.Button1 = new System.Windows.Forms.Button();
             this.GroupBox1 = new System.Windows.Forms.GroupBox();
             this.GroupBox1.SuspendLayout();
             this.SuspendLayout();
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(20, 39);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(169, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // Label1
             //
             this.Label1.AutoSize = true;
             this.Label1.Location = new System.Drawing.Point(19, 23);
             this.Label1.Name = "Label1";
             this.Label1.Size = new System.Drawing.Size(91, 13);
             this.Label1.TabIndex = 2;
             this.Label1.Text = "Select vault view:";
             //
             // Button5
             //
             this.Button5.Location = new System.Drawing.Point(40, 272);
             this.Button5.Name = "Button5";
             this.Button5.Size = new System.Drawing.Size(132, 23);
             this.Button5.TabIndex = 7;
             this.Button5.Text = "Delete a key-value pair";
             this.Button5.UseVisualStyleBackColor = true;
             this.Button5.Click += new System.EventHandler(this.Button5_Click);
             //
             // Button7
             //
             this.Button7.Location = new System.Drawing.Point(39, 312);
             this.Button7.Name = "Button7";
             this.Button7.Size = new System.Drawing.Size(132, 23);
             this.Button7.TabIndex = 9;
             this.Button7.Text = "Create a key-value pair";
             this.Button7.UseVisualStyleBackColor = true;
             this.Button7.Click += new System.EventHandler(this.Button7_Click);
             //
             // RadioButton1
             //
             this.RadioButton1.AutoSize = true;
             this.RadioButton1.Location = new System.Drawing.Point(30, 19);
             this.RadioButton1.Name = "RadioButton1";
             this.RadioButton1.Size = new System.Drawing.Size(100, 17);
             this.RadioButton1.TabIndex = 11;
             this.RadioButton1.Text = "Substring in key";
             this.RadioButton1.UseVisualStyleBackColor = true;
             //
             // RadioButton2
             //
             this.RadioButton2.AutoSize = true;
             this.RadioButton2.Location = new System.Drawing.Point(30, 42);
             this.RadioButton2.Name = "RadioButton2";
             this.RadioButton2.Size = new System.Drawing.Size(108, 17);
             this.RadioButton2.TabIndex = 12;
             this.RadioButton2.TabStop = true;
             this.RadioButton2.Text = "Integer key range";
             this.RadioButton2.UseVisualStyleBackColor = true;
             //
             // RadioButton3
             //
             this.RadioButton3.AutoSize = true;
             this.RadioButton3.Location = new System.Drawing.Point(29, 65);
             this.RadioButton3.Name = "RadioButton3";
             this.RadioButton3.Size = new System.Drawing.Size(199, 17);
             this.RadioButton3.TabIndex = 13;
             this.RadioButton3.TabStop = true;
             this.RadioButton3.Text = "Substring in values of all integer keys";
             this.RadioButton3.UseVisualStyleBackColor = true;
             //
             // RadioButton4
             //
             this.RadioButton4.AutoSize = true;
             this.RadioButton4.Location = new System.Drawing.Point(30, 88);
             this.RadioButton4.Name = "RadioButton4";
             this.RadioButton4.Size = new System.Drawing.Size(118, 17);
             this.RadioButton4.TabIndex = 14;
             this.RadioButton4.TabStop = true;
             this.RadioButton4.Text = "Specific integer key";
             this.RadioButton4.UseVisualStyleBackColor = true;
             //
             // RadioButton5
             //
             this.RadioButton5.AutoSize = true;
             this.RadioButton5.Location = new System.Drawing.Point(30, 111);
             this.RadioButton5.Name = "RadioButton5";
             this.RadioButton5.Size = new System.Drawing.Size(169, 17);
             this.RadioButton5.TabIndex = 15;
             this.RadioButton5.TabStop = true;
             this.RadioButton5.Text = "Enumeration of all integer keys";
             this.RadioButton5.UseVisualStyleBackColor = true;
             //
             // Button1
             //
             this.Button1.Location = new System.Drawing.Point(30, 143);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(132, 23);
             this.Button1.TabIndex = 16;
             this.Button1.Text = "Get key-value pairs";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click += new System.EventHandler(this.Button1_Click);
             //
             // GroupBox1
             //
             this.GroupBox1.Controls.Add(this.Button1);
             this.GroupBox1.Controls.Add(this.RadioButton5);
             this.GroupBox1.Controls.Add(this.RadioButton4);
             this.GroupBox1.Controls.Add(this.RadioButton3);
             this.GroupBox1.Controls.Add(this.RadioButton2);
             this.GroupBox1.Controls.Add(this.RadioButton1);
             this.GroupBox1.Location = new System.Drawing.Point(10, 69);
             this.GroupBox1.Name = "GroupBox1";
             this.GroupBox1.Size = new System.Drawing.Size(249, 181);
             this.GroupBox1.TabIndex = 17;
             this.GroupBox1.TabStop = false;
             this.GroupBox1.Text = "Get key-value pairs by:";
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(271, 366);
             this.Controls.Add(this.GroupBox1);
             this.Controls.Add(this.Button7);
             this.Controls.Add(this.Button5);
             this.Controls.Add(this.Label1);
             this.Controls.Add(this.VaultsComboBox);
             this.Name = "Form1";
             this.Text = "Dictionary Test";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.GroupBox1.ResumeLayout(false);
             this.GroupBox1.PerformLayout();
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Label Label1;
         internal System.Windows.Forms.Button Button5;
         internal System.Windows.Forms.Button Button7;
         internal System.Windows.Forms.RadioButton RadioButton1;
         internal System.Windows.Forms.RadioButton RadioButton2;
         internal System.Windows.Forms.RadioButton RadioButton3;
         internal System.Windows.Forms.RadioButton RadioButton4;
         internal System.Windows.Forms.RadioButton RadioButton5;
         internal System.Windows.Forms.Button Button1;
         internal System.Windows.Forms.GroupBox GroupBox1;

         #endregion
     }
 }
```

```
Back to top
```
