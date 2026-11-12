---
title: "Find Data Cards with Description Variable Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Find_Data_Cards_with_Description_Variable_Example_VBNET.htm"
---

# Find Data Cards with Description Variable Example (VB.NET)

This example shows how to find the data cards in your vault that have a Description variable.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio 2010.
'  2. Click File > New > Project > Visual Basic > Windows Forms Application.
'  3. Type Exercise3 in Name.
'  4. Click the Browse button and browse to the folder where to create the project.
'  5. Click OK.
'  6. Create a form similar to the form shown above and change:
'     a. Label to VaultsLabel.
'     b. Combo box to VaultsComboBox.
'     c. Button to FindCardsButton.
'  7. Replace the code in Form1.vb with this code.
'  8. Replace the code in Form1.Designer.vb with this code.
'  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
'     name in the Solution Explorer, click Add Reference, click
'     Framework in the left-side panel, browse to the top folder of your
'     SOLIDWORKS PDM Professional installation, locate and click
'     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
' 10. Right-click EPDM.Interop.epdm in References, select Properties, and set
'     Embed Interop Types to False to handle methods that pass arrays of
'     structures.
' 11. Open the Immediate window.
' 12. Switch back to the Form1.vb code window.
' 13. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click the Find cards with Description variable button.
'     The cards in your vault with a Description variable are
'     printed to the Immediate window.
'  4. Examine the Immediate window.
'  5. Close the dialog.
'----------------------------------------------------------------------------
```

```
'Form1.vb

Imports EPDM.Interop.epdm

Public Class Exercise4

  Private Sub Exercise4_Load( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles MyBase.Load

    Try
      'Declare and create an instance of IEdmVault5
      'Cast IEdmVault5 to IEdmVault8
      Dim vault As IEdmVault8 = New EdmVault5
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

  Private Sub FindCardsButton_Click( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles FindCardsButton.Click

    Try
      'Declare and create an instance of IEdmVault5 object
      Dim vault As IEdmVault5 = New EdmVault5()

      'Log into selected vault as the current user
      vault.LoginAuto(VaultsComboBox.Text, _
        Me.Handle.ToInt32())

      Dim Cards As New ArrayList
      Cards.Clear()

      Dim Folder As IEdmFolder5
      Folder = vault.RootFolder

      Dim VarMgr As IEdmVariableMgr5
      VarMgr = vault

      'You could get the "Description" variable directly,
      'but get it by enumerating through all
      'the variables until it's found -
      'Dim DescVar As IEdmVariable5
      'DescVar = VarMgr.GetVariable("Description")

      Dim VarPos As IEdmPos5
      VarPos = VarMgr.GetFirstVariablePosition
      While Not VarPos.IsNull
        Dim Var As IEdmVariable5
        Var = VarMgr.GetNextVariable(VarPos)
        If Not Var.Name = "Description" _
          Then Continue While
        Dim AttPos As IEdmPos5
        AttPos = Var.GetFirstAttributePosition("")
        While Not AttPos.IsNull
          Dim Att As IEdmAttribute5
          Att = Var.GetNextAttribute(AttPos)
          Dim Extensions() As String
          Extensions = Att.Extensions.Split(",")
          Dim Extension As String
          For Each Extension In Extensions
            Dim Card As IEdmCard5
            Try
              Card = Folder.GetCard(Extension)
              If Card.cardtype = _
                EdmCardType.EdmCard_File Then
                If Not Cards.Contains(Card.Name) Then
                  Cards.Add(Card.Name)
                End If
              End If
            Catch ex As _
              Runtime.InteropServices.COMException
              'E_EDM_INVALID_NAME
              If Not ex.ErrorCode = &H8004021D Then
                Throw New _
                  Runtime.InteropServices.COMException _
                  (ex.Message, ex.ErrorCode)
              End If
            End Try
          Next Extension
        End While
      End While

      Dim CardName As String
      For Each CardName In Cards
        Debug.Print(CardName)
      Next CardName

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
Partial Class Exercise4
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
        Me.FindCardsButton = New System.Windows.Forms.Button()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'FindCardsButton
        '
        Me.FindCardsButton.Location = New System.Drawing.Point(37, 96)
        Me.FindCardsButton.Margin = New System.Windows.Forms.Padding(2)
        Me.FindCardsButton.Name = "FindCardsButton"
        Me.FindCardsButton.Size = New System.Drawing.Size(212, 41)
        Me.FindCardsButton.TabIndex = 20
        Me.FindCardsButton.Text = "Find cards with Description variable"
        Me.FindCardsButton.UseVisualStyleBackColor = True
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(58, 37)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(169, 21)
        Me.VaultsComboBox.TabIndex = 19
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(96, 9)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 18
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'Exercise4
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(301, 155)
        Me.Controls.Add(Me.FindCardsButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Margin = New System.Windows.Forms.Padding(2)
        Me.Name = "Exercise4"
        Me.Text = "Find cards with Description"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
  Friend WithEvents FindCardsButton As System.Windows.Forms.Button
  Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
  Friend WithEvents VaultsLabel As System.Windows.Forms.Label

End Class
```

```
Back to top
```
