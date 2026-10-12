---
title: "Favorite Search Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Favorite_Search_Example_VBNET.htm"
---

# Favorite Search Example (VB.NET)

This example shows how to perform a favorite search.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio.
 '  2. Click File > New > Project > Visual Basic > Windows Forms Application.
 '  3. Type FavoriteSearch in Name.
 '  4. Click Browse to navigate to the folder where to create the project.
 '  5. Click OK.
  '  6. Click Show All Files in the Solution Explorer toolbar and expand
 '     Form1.vb in the Solution Explorer.
 '  7. Replace the code in Form1.vb with this code.
 '  8. To create the form, replace the code in Form1.Designer.vb with this code.
 '  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add Reference, click
 '     Assembly > Framework in the left-side panel, browse to the top folder of your
 '     SOLIDWORKS PDM Professional installation, locate and click
 '     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 10. Right-click EPDM.Interop.epdm in References, select Properties, and set
 '     Embed Interop Types to False to handle methods that pass arrays of
 '     structures.
' 11. Ensure that you know the name of a saved favorite search, and that search
 '     finds at least one vault file whose extension  (e.g., sldprt)
'     has a file data card (e.g. Quick Start Data Card) with a Description field.
' 12. Check out the vault file and add a description. Check it back in.
 ' 13. Use the Admin Tool to create a new column set for complete search results.
 '     (Right-click on Admin Tool > vault_name > Columns > Search Result Columns and select New Column Set.
 ' 14. Click Add and select Description from the Variable dropdown
' 15. Save the new column set with name, MyFavoriteSearchResults.
 ' 16. Double-click Admin Tool > vault_name > Cards > Search Cards > Complete Search.
 ' 17. In the Card Properties panel, select the View and Preferred checkboxes next to MyFavoriteSearchResults.
 ' 18. Save and close the Card Editor dialog.
 ' 19. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. Displays a dialog.
 '  2. Select a vault.
'  3. Type in a favorite search name.
 '  4. Click Perform Search.
 '  5. Displays search results, including the custom search column, Description.
 '  6. Close the dialog.
 '----------------------------------------------------------------------------
```

```
'Form1.vb
```

```vb
 Imports System.IO
 Imports System.Xml.Serialization
 Imports System.Collections
 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public   Class   Form1

       Private vault1  As IEdmVault5 =   Nothing

       Public  Sub Form1_Load(ByVal sender  As System.Object,   ByVal e  As System.EventArgs)  Handles  MyBase.Load

            Try
              vault1 =   New EdmVault5()
               Dim vault  As IEdmVault8 =   DirectCast(vault1, IEdmVault8)
               Dim Views  As EdmViewInfo() =   Nothing

              vault.GetVaultViews(Views,   False)
              VaultsComboBox.Items.Clear()
               For  Each View  As EdmViewInfo  In Views
                  VaultsComboBox.Items.Add(View.mbsVaultName)
               Next
               If VaultsComboBox.Items.Count > 0   Then
                  VaultsComboBox.Text =   DirectCast(VaultsComboBox.Items(0),   String)
               End  If
            Catch ex  As System.Runtime.InteropServices.COMException
              MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") +  " " + ex.Message)
            Catch ex  As Exception
              MessageBox.Show(ex.Message)
            End  Try
       End  Sub

       Public  Sub PerformSearch_Click(ByVal sender  As System.Object,   ByVal e  As System.EventArgs)  Handles PerformSearch.Click
            Try

               Dim vault2  As IEdmVault7 =   Nothing
               If vault1  Is  Nothing   Then
                  vault1 =   New EdmVault5()
               End  If
              vault2 =   DirectCast(vault1, IEdmVault9)
               If  Not vault1.IsLoggedIn   Then
                  vault1.LoginAuto(VaultsComboBox.Text,  Me.Handle.ToInt32())
               End  If

               Dim oSearch  As IEdmSearch10 = vault1.CreateSearch()
               Dim oSearchResult  As IEdmSearchResult6 = oSearch.GetFirstFavoriteResult(TextBox1.Text,   True)   'get custom search result columns, if present

               Do
                   'oSearchResult will have default values like path or ID, even if custom columns do not exist
                  ListBox1.Items.Add("ID: " & oSearchResult.ID)
                  ListBox1.Items.Add("Name: " & oSearchResult.Name)
                  ListBox1.Items.Add("Path: " & oSearchResult.Path)
                  ListBox1.Items.Add("Version: " & oSearchResult.Version)

                   Dim oColsInfo()  As EdmListCol =   Nothing
                   Dim oStrValues()  As   String =   Nothing

                      oSearchResult.GetCustomColumnsInfo(oColsInfo)
                  oSearchResult.GetCustomColumnValues(oStrValues)

                   If oColsInfo   IsNot   Nothing   Then
                        For i  As   Integer = 0  To oColsInfo.Length - 1

                          ListBox1.Items.Add(oColsInfo(i).mbsCaption    ": " & oStrValues(i))

                        Next i

                   End  If

                  oSearchResult = oSearch.GetNextResult()  'Get next result

               Loop  Until oSearchResult  Is   Nothing

            Catch ex  As System.Runtime.InteropServices.COMException
              MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") +  " " + ex.Message)
            Catch ex  As Exception
              MessageBox.Show(ex.Message)
            End  Try

       End  Sub

 End  Class
```

```
Back to top
```

```
'Form1.Designer.vb
```

```vb
 <Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
 Partial   Class   Form1
       Inherits System.Windows.Forms.Form

        'Form overrides dispose to clean up the component list.
       <System.Diagnostics.DebuggerNonUserCode()>
       Protected  Overrides   Sub Dispose(ByVal disposing   As   Boolean)
           Try
               If disposing   AndAlso components   IsNot   Nothing   Then
                  components.Dispose()
               End  If
           Finally
               MyBase.Dispose(disposing)
           End  Try
       End  Sub

        'Required by the Windows Form Designer
       Private components   As System.ComponentModel.IContainer

        'NOTE: The following procedure is required by the Windows Form Designer
        'It can be modified using the Windows Form Designer.
        'Do not modify it using the code editor.
       <System.Diagnostics.DebuggerStepThrough()>
       Private  Sub InitializeComponent()
           Me.VaultsLabel =   New System.Windows.Forms.Label()
           Me.VaultsComboBox =   New System.Windows.Forms.ComboBox()
           Me.PerformSearch =   New System.Windows.Forms.Button()
           Me.TextBox1 =   New System.Windows.Forms.TextBox()
           Me.Label1 =  New System.Windows.Forms.Label()
           Me.Label2 =  New System.Windows.Forms.Label()
           Me.ListBox1 =   New System.Windows.Forms.ListBox()
           Me.SuspendLayout()
           '
           'VaultsLabel
           '
           Me.VaultsLabel.AutoSize =   True
           Me.VaultsLabel.Location =   New System.Drawing.Point(36, 24)
           Me.VaultsLabel.Name =   "VaultsLabel"
           Me.VaultsLabel.Size =   New System.Drawing.Size(91, 13)
           Me.VaultsLabel.TabIndex = 0
           Me.VaultsLabel.Text =   "Select vault view:"
           '
           'VaultsComboBox
           '
           Me.VaultsComboBox.FormattingEnabled =   True
           Me.VaultsComboBox.Location =   New System.Drawing.Point(39, 40)
           Me.VaultsComboBox.Name =   "VaultsComboBox"
           Me.VaultsComboBox.Size =   New System.Drawing.Size(157, 21)
           Me.VaultsComboBox.TabIndex = 1
           '
           'PerformSearch
           '
           Me.PerformSearch.Location =   New System.Drawing.Point(215, 101)
           Me.PerformSearch.Name =   "PerformSearch"
           Me.PerformSearch.Size =   New System.Drawing.Size(96, 23)
           Me.PerformSearch.TabIndex = 6
           Me.PerformSearch.Text =   "Perform Search"
           Me.PerformSearch.UseVisualStyleBackColor =   True
           '
           'TextBox1
           '
           Me.TextBox1.Location =   New System.Drawing.Point(39, 103)
           Me.TextBox1.Name =   "TextBox1"
           Me.TextBox1.Size =   New System.Drawing.Size(157, 20)
           Me.TextBox1.TabIndex = 7
           '
           'Label1
           '
           Me.Label1.AutoSize =   True
           Me.Label1.Location =   New System.Drawing.Point(39, 84)
           Me.Label1.Name =   "Label1"
           Me.Label1.Size =   New System.Drawing.Size(136, 13)
           Me.Label1.TabIndex = 8
           Me.Label1.Text =   "Type favorite search name:"
           '
           'Label2
             '
           Me.Label2.AutoSize =   True
           Me.Label2.Location =   New System.Drawing.Point(39, 164)
           Me.Label2.Name =   "Label2"
           Me.Label2.Size =   New System.Drawing.Size(45, 13)
           Me.Label2.TabIndex = 10
           Me.Label2.Text =   "Results:"
           '
           'ListBox1
           '
           Me.ListBox1.FormattingEnabled =   True
           Me.ListBox1.HorizontalScrollbar =   True
           Me.ListBox1.Location =   New System.Drawing.Point(39, 181)
           Me.ListBox1.Name =   "ListBox1"
           Me.ListBox1.ScrollAlwaysVisible =   True
           Me.ListBox1.Size =   New System.Drawing.Size(340, 264)
           Me.ListBox1.TabIndex = 11
           '
           'Form1
           '
           Me.AutoScaleDimensions =   New System.Drawing.SizeF(6.0!, 13.0!)
           Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
           Me.ClientSize =   New System.Drawing.Size(407, 472)
           Me.Controls.Add(Me.ListBox1)
           Me.Controls.Add(Me.Label2)
           Me.Controls.Add(Me.Label1)
           Me.Controls.Add(Me.TextBox1)
          Me.Controls.Add(Me.PerformSearch)
           Me.Controls.Add(Me.VaultsComboBox)
           Me.Controls.Add(Me.VaultsLabel)
           Me.Name =  "Form1"
           Me.Text =  "Favorite Search"
           Me.ResumeLayout(False)
           Me.PerformLayout()

       End  Sub
       Friend  WithEvents VaultsLabel   As System.Windows.Forms.Label
       Friend  WithEvents VaultsComboBox   As System.Windows.Forms.ComboBox
       Friend  WithEvents PerformSearch   As System.Windows.Forms.Button
       Friend  WithEvents TextBox1   As TextBox
       Friend  WithEvents Label1   As Label
       Friend  WithEvents Label2   As Label
       Friend  WithEvents ListBox1   As ListBox

 End  Class
```

```
Back to top
```
