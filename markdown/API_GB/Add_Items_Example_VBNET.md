---
title: "Add Items Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Add_Items_Example_VBNET.htm"
---

# Add Items Example (VB.NET)

This example shows how to add items to a vault. The data for the items is imported from an XML file, which is read by the .NET XmlReader.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Create an XML file for this example.
'     a. Open a text editor like Notepad and copy and paste this code
'        into the editor.
'     b. Save the file as Items.xml and remember where you save the file.
'  2. Open the SOLIDWORKS PDM Professional Administration tool.
'  3. Log into the vault where to add a new serial number.
'     a. Right-click Serial Numbers and click New Serial Number.
'        1. Type AddItems in Name.
'        2. For Format string, click the right-arrow button and select Counter value > 00001.
'        3. Click OK.
'     b. Right-click Items and select Open.
'        1. Click AddItems in Item Serial Number.
'        2. Click OK.
'  4. Start Microsoft Visual Studio.
'     a. Click File > New > Project > Visual Basic > Windows Forms Application.
'     b. Type AddItems in Name.
'     c. Click the Browse button and browse to the folder where to create the project.
'     d. Click OK.
'     e. Click Show All Files in the Solution Explorer toolbar.
'     f. Create a form similar to the form shown above and change:
'        1. Top label to VaultsLabel.
'        2. Combo box to VaultsComboBox.
'        3. Second label to XmlLabel.
'        4. Text box to XmlTextBox.
'        5. Browse button to BrowseButton.
'        6. Add items button to AddItemsButton.
'        7. List box to ItemsListBox.
'     g. Replace the code in Form1.vb with this code.
'     h. Replace the code in Form1.Designer.vb with this code.
'     i. Right-click the AddItems project name in the Solution Explorer.
'        1. Click Add > Class > Class.
'        2. Type EdmVaultSingleton.vb in Name.
'        3. Click Add.
'        4. Replace the code in EdmVaultSingleton.vb with this code.
'     j. Right-click the AddItems project name in the Solution Explorer.
'        1. Click Add > Class > Class.
'        2. Type NewItem.vb in Name.
'        3. Click Add.
'        4. Replace the code in NewItem.vb with this code.
'  5. Add EPDM.Interop.epdm.dll as a reference (right-click the project
'     name in the Solution Explorer, click Add Reference, click
'     Assemblies > Framework in the left-side panel, browse to the top folder of your
'     SOLIDWORKS PDM Professional installation, locate and click
'     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
'  6. Right-click EPDM.Interop.epdm in References, click Properties, and set
'     Embed Interop Types to False to handle methods that pass arrays of
'     structures.
'  7. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click the Browse button, locate and click Items.xml, and click Open.
'  4. Click the Add items button.
'     The new items are printed in the dialog's list.
'  5. Close the dialog.
'  6. Open the SOLIDWORKS PDM Professional Item Explorer tool.
'     (In Windows 7, click Start > All Programs > SOLIDWORKS PDM Professional >
'     Item Explorer.)
'  7. Expand the vault where the new items were added.
'     The new items are listed below the name of the expanded vault.
'----------------------------------------------------------------------------
```

```
<?xml version="1.0" encoding="utf-8"?>
<ArrayOfAnyType xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <anyType xsi:type="Item">
    <Description>First Item</Description>
    <ProjectName>Project 1</ProjectName>
    <ProjectNumber>1</ProjectNumber>
    <PartType>Purchased</PartType>
    <ItemName>Item 1</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Second Item</Description>
    <ProjectName>Project 2</ProjectName>
    <ProjectNumber>2</ProjectNumber>
    <PartType>Built</PartType>
    <ItemName>Item 2</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Third Item</Description>
    <ProjectName>Project 3</ProjectName>
    <ProjectNumber>3</ProjectNumber>
    <PartType>Purchased</PartType>
    <ItemName>Item 3</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Fourth Item</Description>
    <ProjectName>Project 4</ProjectName>
    <ProjectNumber>4</ProjectNumber>
    <PartType>Built</PartType>
    <ItemName>Item 4</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Fifth Item</Description>
    <ProjectName>Project 5</ProjectName>
    <ProjectNumber>5</ProjectNumber>
    <PartType>Purchased</PartType>
    <ItemName>Item 5</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Sixth Item</Description>
    <ProjectName>Project 6</ProjectName>
    <ProjectNumber>6</ProjectNumber>
    <PartType>Built</PartType>
    <ItemName>Item 6</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Seventh Item</Description>
    <ProjectName>Project 7</ProjectName>
    <ProjectNumber>7</ProjectNumber>
    <PartType>Purchased</PartType>
    <ItemName>Item 7</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Eighth Item</Description>
    <ProjectName>Project 8</ProjectName>
    <ProjectNumber>8</ProjectNumber>
    <PartType>Built</PartType>
    <ItemName>Item 8</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Ninth Item</Description>
    <ProjectName>Project 9</ProjectName>
    <ProjectNumber>9</ProjectNumber>
    <PartType>Purchased</PartType>
    <ItemName>Item 9</ItemName>
  </anyType>
  <anyType xsi:type="Item">
    <Description>Tenth Item</Description>
    <ProjectName>Project 10</ProjectName>
    <ProjectNumber>10</ProjectNumber>
    <PartType>Built</PartType>
    <ItemName>Item 10</ItemName>
  </anyType>
</ArrayOfAnyType>
```

```
Back to top
```

```
'Form1.vb
```

```
Imports System.IO
Imports EPDM.Interop.epdm
Imports System.Xml
Imports System.Windows.Forms

Public Class AddItems

  Private Sub BrowseButton_Click( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles BrowseButton.Click

    Try
      Dim dlgResult As DialogResult = XmlOpenFileDialog.ShowDialog()
      If dlgResult = Windows.Forms.DialogResult.Cancel Then
        Exit Sub
      End If
      XmlTextBox.Text = XmlOpenFileDialog.FileName
    Catch ex As Runtime.InteropServices.COMException
      MessageBox.Show("HRESULT = 0x" + _
        ex.ErrorCode.ToString("X") + vbCrLf + _
        ex.Message)
    Catch ex As Exception
      MessageBox.Show(ex.Message)
    End Try
  End Sub

  Private Sub AddItemsButton_Click( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles AddItemsButton.Click

    Try
      ItemsListBox.Items.Clear()
      Dim NewItems As ArrayList = New ArrayList

      Using XmlReader As Xml.XmlReader = _
        Xml.XmlReader.Create(XmlTextBox.Text)

        XmlReader.Read()
        XmlReader.ReadToNextSibling("ArrayOfAnyType")
        XmlReader.ReadToDescendant("anyType")
        Do
          Dim CurItem As New NewItem
          XmlReader.ReadToDescendant("Description")
          CurItem.Description = XmlReader.ReadString()
          XmlReader.ReadToNextSibling("ProjectName")
          CurItem.ProjectName = XmlReader.ReadString()
          XmlReader.ReadToNextSibling("ProjectNumber")
          CurItem.ProjectNumber = XmlReader.ReadString()
          XmlReader.ReadToNextSibling("PartType")
          CurItem.PartType = XmlReader.ReadString()
          XmlReader.ReadToNextSibling("ItemName")
          CurItem.ItemName = XmlReader.ReadString()
          NewItems.Add(CurItem)
        Loop While XmlReader.ReadToFollowing("anyType")
      End Using

      'Obtain the only instance of the IEdmVault5 object
      Dim vault As IEdmVault5 = EdmVaultSingleton.Instance

      If Not vault.IsLoggedIn Then
        'Log into selected vault as the current user
        vault.LoginAuto(VaultsComboBox.Text, _
          Me.Handle.ToInt32())
      End If

      'Create the batch interface
      Dim BatchItemGen As IEdmBatchItemGeneration2
      BatchItemGen = vault.CreateUtility( _
        EdmUtility.EdmUtil_BatchItemGeneration)
      Dim VarVals(3) As EdmVarVal
      VarVals(0).mlEdmVarValFlags = 0
      VarVals(0).moVarIDorName = "Description"
      VarVals(1).mlEdmVarValFlags = 0
      VarVals(1).moVarIDorName = "Project Name"
      VarVals(2).mlEdmVarValFlags = 0
      VarVals(2).moVarIDorName = "Project number"
      VarVals(3).mlEdmVarValFlags = 0
      VarVals(3).moVarIDorName = "Part Type"
      For i As Integer = 0 To NewItems.Count - 1
        VarVals(0).moValue = NewItems(i).Description
        VarVals(1).moValue = NewItems(i).ProjectName
        VarVals(2).moValue = NewItems(i).ProjectNumber
        VarVals(3).moValue = NewItems(i).PartType
        BatchItemGen.AddSelection2(vault, VarVals, _
          NewItems(i).ItemName)
      Next i

      'Build the item tree
      Dim CreateSuccess As Boolean
      CreateSuccess = BatchItemGen.CreateTree( _
        Me.Handle.ToInt32, _
        EdmItemGenerationFlags.Eigcf_Nothing)
            If (CreateSuccess = False) Then Exit Sub

      'Generate the items
      Dim ReturnedItems() As EdmGenItemInfo = Nothing
      Dim bOpenExplorer As Boolean = False
      BatchItemGen.GenerateItems(Me.Handle.ToInt32, _
        ReturnedItems, bOpenExplorer, Nothing)

      'Display the new item information in the list box
      Dim msg As String = ""
      If ReturnedItems.Length = 0 Then
        msg = "No items were added."
        ItemsListBox.Items.Add("No items were added.")
      Else
        For Each ItemInfo As EdmGenItemInfo _
          In ReturnedItems

          ItemsListBox.Items.Add("Item name: " + _
            ItemInfo.mbsItemName)
          ItemsListBox.Items.Add("Alternate name: " + _
            ItemInfo.mbsItemAlternativeName)
          ItemsListBox.Items.Add("Status: " + _
            vault.GetErrorMessage(ItemInfo.mhResult))
          ItemsListBox.Items.Add("")
        Next ItemInfo
      End If
    Catch ex As Runtime.InteropServices.COMException
      MessageBox.Show("HRESULT = 0x" + _
        ex.ErrorCode.ToString("X") + vbCrLf + _
        ex.Message)
    Catch ex As Exception
      MessageBox.Show(ex.Message)
    End Try
  End Sub

  Private Sub AddItems_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Try
      'Obtain the only instance of the IEdmVault object
      Dim vault As IEdmVault8 = EdmVaultSingleton.Instance
      Dim Views() As EdmViewInfo = Nothing

      vault.GetVaultViews(Views, False)
      VaultsComboBox.Items.Clear()
      For Each View As EdmViewInfo In Views
        VaultsComboBox.Items.Add(View.mbsVaultName)
      Next
      If VaultsComboBox.Items.Count > 0 Then
        VaultsComboBox.Text = VaultsComboBox.Items(0)
      End If
    Catch ex As Runtime.InteropServices.COMException
      MessageBox.Show("HRESULT = 0x" + _
        ex.ErrorCode.ToString("X") + vbCrLf + _
        ex.Message)
    Catch ex As Exception
      MessageBox.Show(ex.Message)
    End Try
  End Sub
End Class
```

```
Back to top
```

```
'Form1.Designer.vb
```

```
<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class AddItems
   Inherits System.Windows.Forms.Form

   'Form overrides dispose to clean up the component list.
   <System.Diagnostics.DebuggerNonUserCode()> _
   Protected Overrides Sub Dispose(ByVal disposing As Boolean)
      Try
         If disposing AndAlso components IsNot Nothing Then
            components.Dispose()
         End If
      Finally
         MyBase.Dispose(disposing)
      End Try
   End Sub

   'Required by the Windows Form Designer
   Private components As System.ComponentModel.IContainer

   'NOTE: The following procedure is required by the Windows Form Designer
   'It can be modified using the Windows Form Designer.
   'Do not modify it using the code editor.
   <System.Diagnostics.DebuggerStepThrough()> _
   Private Sub InitializeComponent()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.XmlTextBox = New System.Windows.Forms.TextBox()
        Me.XmlLabel = New System.Windows.Forms.Label()
        Me.XmlOpenFileDialog = New System.Windows.Forms.OpenFileDialog()
        Me.AddItemsButton = New System.Windows.Forms.Button()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.ItemsListBox = New System.Windows.Forms.ListBox()
        Me.SuspendLayout()
        '
        'BrowseButton
        '
        Me.BrowseButton.Location = New System.Drawing.Point(222, 94)
        Me.BrowseButton.Margin = New System.Windows.Forms.Padding(2)
        Me.BrowseButton.Name = "BrowseButton"
        Me.BrowseButton.Size = New System.Drawing.Size(59, 26)
        Me.BrowseButton.TabIndex = 0
        Me.BrowseButton.Text = "Browse..."
        Me.BrowseButton.UseVisualStyleBackColor = True
        '
        'XmlTextBox
        '
        Me.XmlTextBox.Location = New System.Drawing.Point(24, 94)
        Me.XmlTextBox.Margin = New System.Windows.Forms.Padding(2)
        Me.XmlTextBox.Name = "XmlTextBox"
        Me.XmlTextBox.Size = New System.Drawing.Size(182, 20)
        Me.XmlTextBox.TabIndex = 1
        '
        'XmlLabel
        '
        Me.XmlLabel.AutoSize = True
        Me.XmlLabel.Location = New System.Drawing.Point(22, 78)
        Me.XmlLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.XmlLabel.Name = "XmlLabel"
        Me.XmlLabel.Size = New System.Drawing.Size(172, 13)
        Me.XmlLabel.TabIndex = 2
        Me.XmlLabel.Text = "XML file from which to import items:"
        '
        'XmlOpenFileDialog
        '
        Me.XmlOpenFileDialog.Filter = "XML files|*.xml"
        '
        'AddItemsButton
        '
        Me.AddItemsButton.Location = New System.Drawing.Point(29, 139)
        Me.AddItemsButton.Margin = New System.Windows.Forms.Padding(2)
        Me.AddItemsButton.Name = "AddItemsButton"
        Me.AddItemsButton.Size = New System.Drawing.Size(87, 24)
        Me.AddItemsButton.TabIndex = 3
        Me.AddItemsButton.Text = "Add items"
        Me.AddItemsButton.UseVisualStyleBackColor = True
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(22, 40)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(184, 21)
        Me.VaultsComboBox.TabIndex = 12
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(22, 24)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(94, 13)
        Me.VaultsLabel.TabIndex = 13
        Me.VaultsLabel.Text = "Select vault  view:"
        '
        'ItemsListBox
        '
        Me.ItemsListBox.FormattingEnabled = True
        Me.ItemsListBox.Location = New System.Drawing.Point(29, 175)
        Me.ItemsListBox.Margin = New System.Windows.Forms.Padding(2)
        Me.ItemsListBox.Name = "ItemsListBox"
        Me.ItemsListBox.Size = New System.Drawing.Size(253, 121)
        Me.ItemsListBox.TabIndex = 14
        '
        'AddItems
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(299, 320)
        Me.Controls.Add(Me.ItemsListBox)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Controls.Add(Me.AddItemsButton)
        Me.Controls.Add(Me.XmlLabel)
        Me.Controls.Add(Me.XmlTextBox)
        Me.Controls.Add(Me.BrowseButton)
        Me.Margin = New System.Windows.Forms.Padding(2)
        Me.Name = "AddItems"
        Me.Text = "Add New Items"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
   Friend WithEvents BrowseButton As System.Windows.Forms.Button
   Friend WithEvents XmlTextBox As System.Windows.Forms.TextBox
   Friend WithEvents XmlLabel As System.Windows.Forms.Label
   Friend WithEvents XmlOpenFileDialog As System.Windows.Forms.OpenFileDialog
   Friend WithEvents AddItemsButton As System.Windows.Forms.Button
   Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
   Friend WithEvents VaultsLabel As System.Windows.Forms.Label
   Friend WithEvents ItemsListBox As System.Windows.Forms.ListBox

End Class
```

```
Back to top
```

```
'EdmVaultSingleton.vb
```

```
Imports System.Threading
Imports EPDM.Interop.epdm

Public NotInheritable Class EdmVaultSingleton
  Private Shared mInstance As EdmVault5 = Nothing
  Private Shared mLockObj As New Object()

  Private Sub New()

  End Sub

  Public Shared ReadOnly Property Instance() As EdmVault5
    Get
      Try
        If mInstance Is Nothing Then
          Monitor.Enter(mLockObj)
          If mInstance Is Nothing Then
            mInstance = New EdmVault5()
          End If
          Monitor.Exit(mLockObj)
        End If
      Catch ex As Exception
        Monitor.Exit(mLockObj)
      End Try

      Return mInstance

    End Get
  End Property

End Class
```

```
Back to top
```

```
'NewItem.vb
```

```
Public Class NewItem
    'Value of "Description" variable
    Private mDescription As String
    'Value of "Project Name" variable
    Private mProjectName As String
    'Value of "Project number" variable
    Private mProjectNumber As String
    'Value of "Part Type" variable
    Private mPartType As String
    'Item name
    Private mItemName As String

    Public Sub New()

    End Sub

    Public Property Description() As String
        Get
            Description = mDescription
        End Get
        Set(ByVal Value As String)
            mDescription = Value
        End Set
    End Property

    Public Property ProjectName() As String
        Get
            ProjectName = mProjectName
        End Get
        Set(ByVal Value As String)
            mProjectName = Value
        End Set
    End Property

    Public Property ProjectNumber() As String
        Get
            ProjectNumber = mProjectNumber
        End Get
        Set(ByVal Value As String)
            mProjectNumber = Value
        End Set
    End Property

    Public Property PartType() As String
        Get
            PartType = mPartType
        End Get
        Set(ByVal Value As String)
            mPartType = Value
        End Set
    End Property

    Public Property ItemName() As String
        Get
            ItemName = mItemName
        End Get
        Set(ByVal Value As String)
            mItemName = Value
        End Set
    End Property

End Class
```

```
Back to top
```
