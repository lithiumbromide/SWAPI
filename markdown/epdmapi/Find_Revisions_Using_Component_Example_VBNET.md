---
title: "Find Revisions Using Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Find_Revisions_Using_Component_Example_VBNET.htm"
---

# Find Revisions Using Component Example (VB.NET)

This example shows how to find the revision numbers using the revision number component named **Alpha Revision Component**.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio.
'  2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
'  3. Type Exercise5 in Project name.
'  4. For Location, click ... and navigate to the folder where to create the project.
'  5. Click Next.
'  6. Select Framework.
'  7. Click Create.
'  8. Click Show All Files in the Solution Explorer toolbar and expand
'     Form1.vb in the Solution Explorer.
'  9. Replace the code in Form1.vb with this code.
' 10. Replace the code in Form1.Designer.vb with this code.
' 11. Add dependencies and safely pass arrays of structures.
' 12. Open the Immediate window.
' 13. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click the Find revisions that use Alpha Revision Component button.
'  4. Prints the names of the revision numbers using the revision number
'     component named Alpha Revision Component to the Immediate window.
'  5. Examine the Immediate window.
'  6. Close the dialog.
'----------------------------------------------------------------------------
'Form1.vb

Imports EPDM.Interop.epdm

Public Class Exercise5

  Private Sub Exercise5_Load( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles MyBase.Load

    Try
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

  Private Sub FindRevisionsButton_Click( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles FindRevisionsButton.Click

    Try
      'Declare and create an instance of IEdmVault5 object
      Dim vault As IEdmVault5 = New EdmVault5()

      'Log into selected vault as the current user
      vault.LoginAuto(VaultsComboBox.Text, _
         Me.Handle.ToInt32())

            Debug.Print _
              ("Revision numbers that use revision number component ""Alpha Revision Component"":")
      Debug.Print("")

      Dim RevMgr As IEdmRevisionMgr2
      RevMgr = vault.CreateUtility( _
        EdmUtility.EdmUtil_RevisionMgr)

      Dim RevNumbers() As EdmRevNo = Nothing
      RevMgr.GetRevisionNumbers(Nothing, RevNumbers)
      Dim RevNo As EdmRevNo
      For Each RevNo In RevNumbers
        Dim RevComponents() As EdmRevComponent2 = Nothing
        RevMgr.GetRevisionNumberComponents2 _
          (-RevNo.mlRevNoID, RevComponents)
        Dim RevComponent As EdmRevComponent2
        For Each RevComponent In RevComponents
                    If RevComponent.mbsCocmponentName = "  " & Alpha Revision Component" _
            Then
                        Debug.Print(RevNo.mbsRevNoName)
                    End If
        Next RevComponent
      Next RevNo

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
<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Exercise5
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
        Me.FindRevisionsButton = New System.Windows.Forms.Button()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'FindRevisionsButton
        '
        Me.FindRevisionsButton.Location = New System.Drawing.Point(95, 107)
        Me.FindRevisionsButton.Margin = New System.Windows.Forms.Padding(2)
        Me.FindRevisionsButton.Name = "FindRevisionsButton"
        Me.FindRevisionsButton.Size = New System.Drawing.Size(132, 50)
        Me.FindRevisionsButton.TabIndex = 23
        Me.FindRevisionsButton.Text = "Find revisions that use Alpha Revision Component"
        Me.FindRevisionsButton.UseVisualStyleBackColor = True
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(95, 47)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(132, 21)
        Me.VaultsComboBox.TabIndex = 22
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(113, 24)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 21
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'Exercise5
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(328, 176)
        Me.Controls.Add(Me.FindRevisionsButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Margin = New System.Windows.Forms.Padding(2)
        Me.Name = "Exercise5"
        Me.Text = "Find revisions using component"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents FindRevisionsButton As System.Windows.Forms.Button
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label

End Class
```

[Back to top](#Top)
