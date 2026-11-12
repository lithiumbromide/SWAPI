---
title: "Access Check-in Flags in Check in Dialog Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Access_Check-in_Flags_in_Check_in_Dialog_Example_VBNET.htm"
---

# Access Check-in Flags in Check in Dialog Example (VB.NET)

This example shows how to access the check-in flags in the SOLIDWORKS PDM Check in dialog.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'--------------------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio 2010.
'     a. Click File > New > Project > Visual Basic > Windows Forms Application.
'     b. Type RefItemContainerVBNET in Name.
'     c. Click Browse and navigate to the folder where to create the project.
'     d. Click OK.
'     e. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
'     f. Replace the code in Form1.vb with this code.
'     g. To create the form, replace the code in Form1.Designer.vb with
'        this code.
'     h. To create the class for the callback:
'        1. Right-click RefItemContainerVBNET in the Solution Explorer.
'        2. Click Add > Class.
'        3. Type Callback.vb in Name and click Add.
'        4. Replace the code in Callback.vb with this code.
'  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
'     name in the Solution Explorer, click Add Reference, click
'     Assemblies > Framework in the left-side panel, browse to the top folder of
'     your SOLIDWORKS PDM Professional installation, locate and click
'     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
'  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
'     Embed Interop Types to False to handle methods that pass arrays of
'     structures.
'  4. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Access Check-in Flags in Check in Dialog dialog box.
'  2. Select a vault view.
'  3. Click Select checked-out files to check in.
'     a. Displays the Select files dialog box.
'     b. Click one or more checked-out files to check in.
'     c. Click Open.
'  4. Click Create batch check-in.
'     a. At the end of an attempted check-in, displays three message
'        boxes containing ProgressEnd called. Three operations occur for an
'        attempted check-in.
'     b. Click OK to close each message box.
'     c. Displays either:
'        * Message box containing Batch check-in created. Click OK to
'          close the message box.
'          - or -
'        * Message box containing You did not select a file to check in. Please try
'          again. Click OK to close the message box, and repeat steps 3 and 4.
'  5. Click Update check-in flags.
'  6. Click OK to close the message box.
'  7. Click Check in files.
'  8. Displays the Check in dialog box.
'  9. Click Check in to check in the files or Cancel to cancel the check in.
' 10. Displays a message box containing ProgressEnd called. Click OK to close
'     the message box.
' 11. Examine the files in the vault to verify their checked-in or checked-out status.
' 12. Close the Access Check-in Flags in Check in Dialog dialog box.
'--------------------------------------------------------------------------------------

'Form1.vb
Imports System.Windows.Forms
Imports EPDM.Interop.epdm

Public Class Form1

    Private vault1 As IEdmVault5 = Nothing
    Private vault As IEdmVault8 = Nothing
    Private selFiles As EdmSelItem() = Nothing
    Private bUnlock As IEdmBatchUnlock = Nothing
    Private pathList As EdmStrLst5 = Nothing
    Private pos As IEdmPos5 = Nothing
    Private UnlockCallback As MyCallback

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        Try
            vault1 = New EdmVault5()
            vault = DirectCast(vault1, IEdmVault8)
            Dim Views As EdmViewInfo() = {}

            vault.GetVaultViews(Views, False)
            VaultsComboBox.Items.Clear()
            For Each View As EdmViewInfo In Views
                VaultsComboBox.Items.Add(View.mbsVaultName)
            Next
            If VaultsComboBox.Items.Count > 0 Then
                VaultsComboBox.Text = DirectCast(VaultsComboBox.Items(0), String)
            End If
        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Private Sub BrowseButton_Click(ByVal sender As Object, ByVal e As EventArgs) Handles BrowseButton.Click
        Try
            'Only create a new vault object
            'if one hasn't been created yet
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If

            If Not vault1.IsLoggedIn Then
                'Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If

            'Display the Select file dialog for user to
            'select the files
            Dim pathList As EdmStrLst5 = Nothing
            pathList = vault.BrowseForFile(Me.Handle.ToInt32(), _
                        CInt(EdmBrowseFlag.EdmBws_ForOpen) + CInt(EdmBrowseFlag.EdmBws_PermitMultipleSel) + _
                        CInt(EdmBrowseFlag.EdmBws_PermitVaultFiles), "SOLIDWORKS files " + _
                        "(*.sldprt; *.sldasm; *.slddrw)|" + "*.sldprt;*.sldasm;*.slddrw|" + _
                        "All Files (*.*)|*.*||", "", "", vault.RootFolderPath, _
             "Select files")

            'Exit if the user clicks Cancel
            If pathList Is Nothing Then
                Return
            End If

            'Traverse the selected files
            Dim pos As IEdmPos5 = Nothing
            pos = pathList.GetHeadPosition()

            'Convert the selected files to an
            'array of EdmSelItem structs
            Dim nbrFiles As Integer = 0
            nbrFiles = pathList.Count
            Array.Resize(selFiles, nbrFiles)

            Dim i As Integer = 0
            While Not pos.IsNull
                'Get each file path from the selected files list
                Dim filePath As String = Nothing
                Dim file As IEdmFile5 = Nothing
                Dim retFolder As IEdmFolder5 = Nothing
                filePath = pathList.GetNext(pos)
                file = vault.GetFileFromPath(filePath, retFolder)
                selFiles(i).mlDocID = file.ID
                selFiles(i).mlProjID = retFolder.ID
                i = i + 1

            End While
        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbLf + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try

    End Sub

    Private Sub CreateBatchCheckinButton_Click(ByVal sender As Object, ByVal e As EventArgs) Handles CreateBatchCheckinButton.Click
        Try
            'Only create a new vault object
            'if one hasn't been created yet
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If

            If Not vault1.IsLoggedIn Then
                'Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If

            Dim vault2 As IEdmVault7 = DirectCast(vault1, IEdmVault7)
            bUnlock = DirectCast(vault2.CreateUtility(EdmUtility.EdmUtil_BatchUnlock), IEdmBatchUnlock)
            bUnlock.AddSelection(DirectCast(vault1, EdmVault5), selFiles)
            Dim tree As Boolean = False
            Dim UnlockCallback = New MyCallback
            tree = bUnlock.CreateTree(Me.Handle.ToInt32(), CInt(EdmUnlockBuildTreeFlags.Eubtf_MayUnlock), _
                    UnlockCallback)
            If tree = False Then
                MessageBox.Show("You did not select a file to check in. Please try again.")
                Return
            End If

            MessageBox.Show("Batch check in created.")
        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbLf + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Private Sub UpdateBatchCheckInButton_Click(ByVal sender As Object, ByVal e As EventArgs) Handles UpdateBatchCheckInButton.Click
        Try
            'Only create a new vault object
            'if one hasn't been created yet
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If

            If Not vault1.IsLoggedIn Then
                'Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If
```

```
            Dim container As IEdmRefItemContainer = Nothing
            container = DirectCast(bUnlock, IEdmRefItemContainer)
            Dim items As Object() = Nothing
            Dim theItem As IEdmRefItem = Nothing
            container.GetItems(EdmRefItemType.Edmrit_All, items)
            Dim j As Integer = 0
            While j < items.Length
                Dim aItem As IEdmRefItem = Nothing
                theItem = DirectCast(items(j), IEdmRefItem)
                aItem = theItem
                Dim value As Object = Nothing
                aItem.SetProperty(EdmRefItemProperty.Edmrip_CheckKeepLocked, value)
                j = j + 1
            End While

            MessageBox.Show("Check-in flags updated.")

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbLf + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try

    End Sub

    Private Sub CheckInButton_Click(ByVal sender As Object, ByVal e As EventArgs) Handles CheckInButton.Click
        Try
            'Only create a new vault object
            'if one hasn't been created yet
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If

            If Not vault1.IsLoggedIn Then
                'Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If
```

```
            Dim UnlockCallback = New MyCallback
            If bUnlock.ShowDlg(Me.Handle.ToInt32()) Then
                bUnlock.UnlockFiles(Me.Handle.ToInt32(), UnlockCallback)
            End If

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbLf + ex.Message)
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
'Form1.Desgner.vb
```

```
<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
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
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.CreateBatchCheckinButton = New System.Windows.Forms.Button()
        Me.UpdateBatchCheckInButton = New System.Windows.Forms.Button()
        Me.CheckInButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(22, 26)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 0
        Me.VaultsLabel.Text = "Select view vault:"
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(25, 54)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(199, 21)
        Me.VaultsComboBox.TabIndex = 1
        '
        'BrowseButton
        '
        Me.BrowseButton.Location = New System.Drawing.Point(25, 81)
        Me.BrowseButton.Name = "BrowseButton"
        Me.BrowseButton.Size = New System.Drawing.Size(199, 23)
        Me.BrowseButton.TabIndex = 2
        Me.BrowseButton.Text = "Select checked-out files to check in"
        Me.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.BrowseButton.UseVisualStyleBackColor = True
        '
        'CreateBatchCheckinButton
        '
        Me.CreateBatchCheckinButton.Location = New System.Drawing.Point(25, 110)
        Me.CreateBatchCheckinButton.Name = "CreateBatchCheckinButton"
        Me.CreateBatchCheckinButton.Size = New System.Drawing.Size(199, 23)
        Me.CreateBatchCheckinButton.TabIndex = 3
        Me.CreateBatchCheckinButton.Text = "Create batch check-in"
        Me.CreateBatchCheckinButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.CreateBatchCheckinButton.UseVisualStyleBackColor = True
        '
        'UpdateBatchCheckInButton
        '
        Me.UpdateBatchCheckInButton.Location = New System.Drawing.Point(25, 139)
        Me.UpdateBatchCheckInButton.Name = "UpdateBatchCheckInButton"
        Me.UpdateBatchCheckInButton.Size = New System.Drawing.Size(199, 23)
        Me.UpdateBatchCheckInButton.TabIndex = 4
        Me.UpdateBatchCheckInButton.Text = "Update check-in flags"
        Me.UpdateBatchCheckInButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.UpdateBatchCheckInButton.UseVisualStyleBackColor = True
        '
        'CheckInButton
        '
        Me.CheckInButton.Location = New System.Drawing.Point(25, 168)
        Me.CheckInButton.Name = "CheckInButton"
        Me.CheckInButton.Size = New System.Drawing.Size(199, 23)
        Me.CheckInButton.TabIndex = 5
        Me.CheckInButton.Text = "Check in files"
        Me.CheckInButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.CheckInButton.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(355, 222)
        Me.Controls.Add(Me.CheckInButton)
        Me.Controls.Add(Me.UpdateBatchCheckInButton)
        Me.Controls.Add(Me.CreateBatchCheckinButton)
        Me.Controls.Add(Me.BrowseButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Name = "Form1"
        Me.Text = "Access Check-in Flags in Check in Dialog"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents BrowseButton As System.Windows.Forms.Button
    Friend WithEvents CreateBatchCheckinButton As System.Windows.Forms.Button
    Friend WithEvents UpdateBatchCheckInButton As System.Windows.Forms.Button
    Friend WithEvents CheckInButton As System.Windows.Forms.Button

End Class
```

```
Back to top
```

```
'Callback.vb
```

```
Imports EPDM.Interop.epdm

Public Class MyCallback
    Implements IEdmUnlockOpCallback

    Public Function MsgBox(ByVal eMsg As EPDM.Interop.epdm.EdmUnlockOpMsg, ByVal lDocID As Integer, ByVal lProjID As Integer, ByVal bsPath As String, ByRef poError As EPDM.Interop.epdm.EdmUnlockErrInfo) As EPDM.Interop.epdm.EdmUnlockOpReply Implements EPDM.Interop.epdm.IEdmUnlockOpCallback.MsgBox
        Return EdmUnlockOpReply.Euor_OK
    End Function

    Public Sub ProgressBegin(ByVal eType As EPDM.Interop.epdm.EdmProgressType, ByVal eEvent As EPDM.Interop.epdm.EdmUnlockEvent, ByVal lSteps As Integer) Implements EPDM.Interop.epdm.IEdmUnlockOpCallback.ProgressBegin

    End Sub

    Public Sub ProgressEnd(ByVal eType As EPDM.Interop.epdm.EdmProgressType) Implements EPDM.Interop.epdm.IEdmUnlockOpCallback.ProgressEnd
        'Demonstrates callback
        MessageBox.Show("ProgressEnd called.")
        Return
    End Sub

    Public Function ProgressStep(ByVal eType As EPDM.Interop.epdm.EdmProgressType, ByVal bsText As String, ByVal lProgressPos As Integer) As Boolean Implements EPDM.Interop.epdm.IEdmUnlockOpCallback.ProgressStep
        Return True
    End Function

    Public Function ProgressStepEvent(ByVal eType As EPDM.Interop.epdm.EdmProgressType, ByVal eText As EPDM.Interop.epdm.EdmUnlockEventMsg, ByVal lProgressPos As Integer) As Boolean Implements EPDM.Interop.epdm.IEdmUnlockOpCallback.ProgressStepEvent
        Return True
    End Function
End Class
```

```
Back to top
```
