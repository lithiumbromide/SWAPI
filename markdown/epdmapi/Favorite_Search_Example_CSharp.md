---
title: "Favorite Search Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Favorite_Search_Example_CSharp.htm"
---

# Favorite Search Example (C#)

This example shows how to perform a favorite search.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio.
//  2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
//  3. Type FavoriteSearch_CSharp in Project name.
//  4. For Location, click ... and navigate to the folder where to
create the project.
//  5. Click Next.
//  6. Select Framework.
//  7. Click Create.
//  8. Click Show All Files in the Solution Explorer toolbar and expand
//     Form1.cs in the Solution Explorer.
//  9. Replace the code in Form1.cs with this code.
// 10. To create the form, replace the code in Form1.Designer.cs with this code.
// 11. Add dependencies and safely pass arrays of structures.
// 12. Ensure that you know the name of a saved favorite search, and that search
//     finds at least one vault file whose extension (e.g., sldprt)
//     has a file data card (e.g. Quick Start Data Card) with a Description field.
// 13. Check out the vault file and add a description. Check it back in.
// 14. Use the Admin Tool to create a new column set for complete search results.
//     (Right-click on Admin Tool > vault_name > Columns > Search Result Columns and select New Column Set.
// 15. Click Add and select Description from the Variable dropdown
// 16. Save the new column set with name, MyFavoriteSearchResults.
// 17. Double-click Admin Tool > vault_name > Cards > Search Cards > Complete Search.
// 18. In the Card Properties panel, select the View and Preferred checkboxes next to MyFavoriteSearchResults.
// 19. Save and close the Card Editor dialog.
// 20. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Type in a favorite search name.
//  4. Click Perform Search.
//  5. Displays search results, including the custom search column, Description.
//  6. Close the dialog.
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
 using EPDM.Interop.epdm;

 namespace FavoriteSearch_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
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

         public void PerformSearch_Click(System.Object sender, System.EventArgs e)
         {

             try
             {

                 IEdmVault9 vault2 =   null;
                   if (vault1 ==   null)
                      vault1 =   new EdmVault5();
                  vault2 = (IEdmVault9)vault1;
                   if (!vault1.IsLoggedIn)
                      vault1.LoginAuto(VaultsComboBox.Text,  this.Handle.ToInt32());

                  IEdmSearch10 oSearch = (IEdmSearch10)vault1.CreateSearch();
                  IEdmSearchResult6 oSearchResult = (IEdmSearchResult6)oSearch.GetFirstFavoriteResult(TextBox1.Text,   true);   // get custom search result columns, if present

                   do
                  {
                        // oSearchResult will have default values like path or ID, even if custom columns do not exist
                      ListBox1.Items.Add("ID: " + oSearchResult.ID);
                      ListBox1.Items.Add("Name: " + oSearchResult.Name);
                      ListBox1.Items.Add("Path: " + oSearchResult.Path);
                      ListBox1.Items.Add("Version: " + oSearchResult.Version);
                      EdmListCol[] oColsInfo =   null;
                        string[] oStrValues =   null;
                        oSearchResult.GetCustomColumnsInfo(out oColsInfo);
                      oSearchResult.GetCustomColumnValues(out oStrValues);
                       if (oColsInfo !=   null)
                      {
                            for (int i = 0; i <= oColsInfo.Length - 1; i++)
                              ListBox1.Items.Add(oColsInfo[i].mbsCaption +   ": " + oStrValues[i]);
                      }

                      oSearchResult = (IEdmSearchResult6)oSearch.GetNextResult();
                  }
                  while (oSearchResult !=   null);

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
 namespace FavoriteSearch_CSharp
 {
       partial  class   Form1
      {
           ///  <summary>
          /// Required designer variable.
           ///  </summary>
           private System.ComponentModel.IContainer components =  null;

           ///  <summary>
           /// Clean up any resources being used.
           ///  </summary>
           ///  <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
           protected  override   void Dispose(bool disposing)
          {
               if (disposing && (components !=   null))
              {
                  components.Dispose();
              }
               base.Dispose(disposing);
          }

           #region Windows Form Designer generated code

           ///  <summary>
           /// Required method for Designer support - do not modify
           /// the contents of this method with the code editor.
          ///   </summary>
           private  void InitializeComponent()
          {
               this.VaultsLabel =   new System.Windows.Forms.Label();
               this.VaultsComboBox =   new System.Windows.Forms.ComboBox();
               this.PerformSearch =   new System.Windows.Forms.Button();
               this.TextBox1 =   new System.Windows.Forms.TextBox();
               this.Label1 =  new System.Windows.Forms.Label();
               this.Label2 =  new System.Windows.Forms.Label();
               this.ListBox1 =   new System.Windows.Forms.ListBox();
               this.SuspendLayout();
               //
               // VaultsLabel
               //
               this.VaultsLabel.AutoSize =   true;
               this.VaultsLabel.Location =   new System.Drawing.Point(36, 24);
               this.VaultsLabel.Name =   "VaultsLabel";
               this.VaultsLabel.Size =   new System.Drawing.Size(91, 13);
               this.VaultsLabel.TabIndex = 0;
               this.VaultsLabel.Text =   "Select vault view:";
               //
               // VaultsComboBox
               //
               this.VaultsComboBox.FormattingEnabled =   true;
               this.VaultsComboBox.Location =   new System.Drawing.Point(39, 40);
               this.VaultsComboBox.Name =   "VaultsComboBox";
               this.VaultsComboBox.Size =   new System.Drawing.Size(157, 21);
               this.VaultsComboBox.TabIndex = 1;
               //
               // PerformSearch
               //
               this.PerformSearch.Location =   new System.Drawing.Point(215, 101);
               this.PerformSearch.Name =   "PerformSearch";
               this.PerformSearch.Size =   new System.Drawing.Size(96, 23);
               this.PerformSearch.TabIndex = 6;
               this.PerformSearch.Text =   "Perform Search";
               this.PerformSearch.UseVisualStyleBackColor =   true;
               this.PerformSearch.Click +=   new System.EventHandler(this.PerformSearch_Click);
               //
               // TextBox1
               //
               this.TextBox1.Location =   new System.Drawing.Point(39, 103);
               this.TextBox1.Name =   "TextBox1";
              this.TextBox1.Size =   new System.Drawing.Size(157, 20);
               this.TextBox1.TabIndex = 7;
               //
               // Label1
               //
               this.Label1.AutoSize =   true;
               this.Label1.Location =   new System.Drawing.Point(39, 84);
               this.Label1.Name =   "Label1";
               this.Label1.Size =   new System.Drawing.Size(136, 13);
               this.Label1.TabIndex = 8;
               this.Label1.Text =   "Type favorite search name:";
               //
              // Label2
               //
               this.Label2.AutoSize =   true;
               this.Label2.Location =   new System.Drawing.Point(39, 164);
               this.Label2.Name =   "Label2";
               this.Label2.Size =   new System.Drawing.Size(45, 13);
               this.Label2.TabIndex = 10;
               this.Label2.Text =   "Results:";
               //
               // ListBox1
               //
               this.ListBox1.FormattingEnabled =   true;
               this.ListBox1.HorizontalScrollbar =   true;
               this.ListBox1.Location =   new System.Drawing.Point(39, 181);
               this.ListBox1.Name =   "ListBox1";
               this.ListBox1.ScrollAlwaysVisible =   true;
               this.ListBox1.Size =   new System.Drawing.Size(340, 264);
               this.ListBox1.TabIndex = 11;
               //
               // Form1
               //
               this.AutoScaleDimensions =   new System.Drawing.SizeF(6F, 13F);
               this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
               this.ClientSize =   new System.Drawing.Size(407, 472);
               this.Controls.Add(this.ListBox1);
               this.Controls.Add(this.Label2);
               this.Controls.Add(this.Label1);
               this.Controls.Add(this.TextBox1);
               this.Controls.Add(this.PerformSearch);
               this.Controls.Add(this.VaultsComboBox);
               this.Controls.Add(this.VaultsLabel);
               this.Name =  "Form1";
               this.Text =  "Favorite Search";
               this.Load +=  new System.EventHandler(this.Form1_Load);
               this.ResumeLayout(false);
               this.PerformLayout();

          }
           internal System.Windows.Forms.Label VaultsLabel;
           internal System.Windows.Forms.ComboBox VaultsComboBox;
           internal System.Windows.Forms.Button PerformSearch;
           internal System.Windows.Forms.TextBox TextBox1;
           internal System.Windows.Forms.Label Label1;
           internal System.Windows.Forms.Label Label2;
           internal System.Windows.Forms.ListBox ListBox1;

           #endregion
      }
 }
```

```
Back to top
```
