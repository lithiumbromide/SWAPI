---
title: "Set Initial Revision Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Set_Initial_Revision_Example_VBNET.htm"
---

# Set Initial Revision Example (VB.NET)

This example shows how to set the initial revision of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'---------------------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '  2. Click File > New > Project > Visual Basic > Windows Forms Application.
 '  3. Select .NET Framework 4 in the top dropdown.
 '  4. Click Browse and navigate to the folder where to create the project.
 '  5. Type SetRevision in Name.
 '  6. Click OK.
 '  7. Right-click the project name in the Solution Explorer and click Add Reference.
'  8. In the Add Reference dialog:
'     a. Click Assemblies > Framework in the left-side panel,
'        browse to the top folder of your SOLIDWORKS PDM Professional installation,
'        locate and click EPDM.Interop.epdm.dll, click Open, and click Add.
'     b. Click Close.
 '  9. Right-click References > EPDM.Interop.epdm in the Solution Explorer,
 '     click Properties, and set Embed Interop Types to False to handle methods
 '     that pass arrays of structures.
 ' 10. Create a form similar to the form shown above and change:
 '     a. Label to VaultsLabel.
 '     b. Combo box to VaultsComboBox.
 '     c. Button to SetInitialRevisionButton.
  ' 11. Click Show All Files in the Solution Explorer toolbar and expand Form1.vb.
 ' 12. Replace the code in Form1.vb with this code.
 ' 13. Replace the code in Form1.Designer.vb with this code.
 ' 14. Copy a SOLIDWORKS part to a PDM vault view.
 '     a. Check in the part.
 '     b. Right-click the part and click  Change State > No Approval Required.
 '        Part is now in the Approved state, and data card Revision is A.
 '     c. Check out the part.
 '     d. In the part's data card, type G in Revision.
 '     e. Save the data card.
 '     f. Check in the part.
 ' 15. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. The Set Revision dialog opens.
 ' 2. Select the vault containing the SOLIDWORKS part you just checked in.
 ' 3. Click Set Initial Revision.
 ' 4. In the Select files on which to set initial revision dialog, click the
 '    SOLIDWORKS part you just checked in and click Open.
 ' 5. In the File already has a revision dialog, click OK to set the initial
 '    revision.
 ' 6. Refresh the vault view, click the SOLIDWORKS part, and click the Version tab.
 '    Observe that the local revision of the file is now G.
 ' 7. Close the Set Revision dialog.
 '---------------------------------------------------------------------------------------
 'Form1.vb
 Imports EPDM.Interop.epdm

 Public Class Form1

   Private Sub Form1_Load(ByVal sender As _
     System.Object, ByVal e As System.EventArgs) _
     Handles MyBase.Load

     Dim vault As IEdmVault8 = New EdmVault5
     Dim Views() As EdmViewInfo = {}

     vault.GetVaultViews(Views, False)
     VaultsComboBox.Items.Clear()
     For Each View As EdmViewInfo In Views
       VaultsComboBox.Items.Add(View.mbsVaultName)
     Next
     If VaultsComboBox.Items.Count > 0 Then
       VaultsComboBox.Text = VaultsComboBox.Items(0)
     End If
   End Sub

   Private Sub SetInitialRevisionButton_Click( _
     ByVal sender As System.Object, _
     ByVal e As System.EventArgs) _
     Handles SetInitialRevisionButton.Click

         'Declare and create an instance of IEdmVault5
     Dim vault As IEdmVault5 = New EdmVault5()

     'Log into selected vault as the current user
     vault.LoginAuto(VaultsComboBox.Text, _
        Me.Handle.ToInt32())

         'Display a File Open dialog for user to
         'choose the files on which set the initial revision
     Dim PathList As EdmStrLst5
         PathList = vault.BrowseForFile( _
            Me.Handle.ToInt32(), _
            EdmBrowseFlag.EdmBws_ForOpen + _
            EdmBrowseFlag.EdmBws_PermitMultipleSel + _
            EdmBrowseFlag.EdmBws_PermitVaultFiles, _
            "SOLIDWORKS files " + _
            "(*.sldprt; *.sldasm; *.slddrw)|" + _
            "*.sldprt;*.sldasm;*.slddrw|" + _
            "All Files (*.*)|*.*||", _
            "", "", vault.RootFolderPath, _
            "Select Files to Set Initial Revision on")

         'Exit if the user clicks Cancel
     If PathList Is Nothing Then Exit Sub

     'Traverse the selected files
     Dim pos As IEdmPos5
     pos = PathList.GetHeadPosition
     While Not pos.IsNull
       'Get each file path from the selected files list
       Dim FilePath As String
       FilePath = PathList.GetNext(pos)
       'Get the IEdmFile5 object corresponding
       'to the path
       Dim FileObj As IEdmFile5
       FileObj = vault.GetFileFromPath(FilePath)

       'Skip any files that are checked out
       If FileObj.IsLocked Then
         MessageBox.Show(FilePath + _
            " is checked out." _
            + vbCrLf + "Check it in and try again." _
            + vbCrLf + "Skipping this file.", _
            "File is checked out.", _
            MessageBoxButtons.OK, _
            MessageBoxIcon.Warning)
         Continue While
       End If

       'Get the value of the file data
             'card variable named Revision
       Dim EnumVarObj As IEdmEnumeratorVariable8
       'Keeps the file open
       EnumVarObj = FileObj.GetEnumeratorVariable

       Dim GetVarSuccess As Boolean
       'GetVar returns a Variant
       Dim RevisionObj As Object = Nothing
       GetVarSuccess = EnumVarObj.GetVar("Revision", _
          "@", RevisionObj)
       EnumVarObj.CloseFile(False) 'Pass True to flush

             'Skip any files without a Revision
             'card variable value
       If RevisionObj Is Nothing Then
         MessageBox.Show("The ""Revision"" custom " + _
            "property of " + FilePath + _
            " is not set to a value." _
            + vbCrLf + "Skipping this file.", _
            "Revision custom property empty.", _
            MessageBoxButtons.OK, _
            MessageBoxIcon.Warning)
         Continue While
       End If

             'Check type
       Dim RevType As System.Type
       RevType = RevisionObj.GetType()
       If Not RevType.Name = "String" Then
         MessageBox.Show("The ""Revision"" " + _
            "variable type is not ""String""." _
            + vbCrLf + "Skipping this file.", _
            "Revision custom property empty.", _
            MessageBoxButtons.OK, _
            MessageBoxIcon.Warning)
         Continue While
       End If

       Dim RevisionProp As String
       RevisionProp = RevisionObj

             'Skip any files whose Revision value
             'is not formatted appropriately
       If Not RevisionProp.Length = 1 Then
                 MessageBox.Show("The ""Revision"" custom " + _
                    "property of " + FilePath + _
                    " does not conform to the expected " + _
                    "revision number format." + vbCrLf + _
                    "Skipping this file.", _
                    "Revision custom property in the wrong format.", _
                    MessageBoxButtons.OK, _
                    MessageBoxIcon.Warning)
         Continue While
       End If

       'Create an IEdmRevisionMgr2 object
       Dim RevMgr As IEdmRevisionMgr2
       RevMgr = vault.CreateUtility( _
          EdmUtility.EdmUtil_RevisionMgr)

       'Get the revision number ID
       Dim CanIncrement As Boolean
       Dim RevisionNumberID As Long
             'Return 0 if there is no revision number
       'generator defined for the file's current state
       RevisionNumberID = _
          RevMgr.GetRevisionNumberIDFromFile( _
          FileObj.ID, CanIncrement)

       'Skip this file if there is no
       'revision number generator for it
       If RevisionNumberID = 0 Then
                 MessageBox.Show("Move " + FilePath + _
                    " to a state where a Revision Number " + _
                    "is defined." + vbCrLf + _
                    "Skipping this file.", _
                    "No Revision Number is defined " + _
                    "for this state.", MessageBoxButtons.OK, _
                    MessageBoxIcon.Warning)
         Continue While
       End If

       'Get the revision number info for this file
       Dim RevNumbers() As EdmRevNo = {}
       RevMgr.GetRevisionNumbers(RevisionNumberID, _
          RevNumbers)
       Dim RevNoFormatString As String
       RevNoFormatString = RevNumbers(0).mbsData
       Dim RevNoFormatLiteral As String
       Dim PercentPos As Integer
       PercentPos = RevNoFormatString.IndexOf("%")
       RevNoFormatLiteral = _
          RevNoFormatString.Substring(0, PercentPos)
       Dim NewRev As String
       NewRev = RevNoFormatLiteral + RevisionProp

       'Check the file's current revision
       Dim CurRev As String
       CurRev = FileObj.CurrentRevision

       'Give the user the option to skip this file
       'if it already has a revision set
       If Not CurRev = String.Empty Then
         Dim MsgBoxResult As _
            System.Windows.Forms.DialogResult
         MsgBoxResult = MessageBox.Show( _
            "The current revision of " _
            + FilePath + " is """ + CurRev + """." + _
            vbCrLf + "The new revision will be """ + _
            NewRev + """" + vbCrLf _
            + "Would you like to continue?", _
            "File already has a revision", _
            MessageBoxButtons.OKCancel, _
            MessageBoxIcon.Question)
         If MsgBoxResult = _
            Windows.Forms.DialogResult.Cancel Then _
            Continue While
       End If

       'Get the revision number components for the
       'revision number used by this file
       Dim RevComponents() As EdmRevComponent2 = {}
       RevMgr.GetRevisionNumberComponents2( _
          -RevisionNumberID, RevComponents)
       Dim RevComponentName As String
       RevComponentName = _
          RevComponents(0).mbsComponentName

             'Declare an array of EdmRevCounter structures,
             'even though only one is used,
       'and assign the values to set
       Dim RevCounters(0) As EdmRevCounter
       'Assign the name of the revision counter
       'to set
       RevCounters(0).mbsComponentName = _
          RevComponentName
       'Assign the new revision counter value to the
       'value stored in the Revision card variable
       'converted to an integer
       Dim RevInt As Long
       RevInt = _
          Asc(RevisionProp.ToUpper()) - Asc("A") + 1
       RevCounters(0).mlCounter = RevInt

       'Set the revision counter to the new values
       RevMgr.SetRevisionCounters(FileObj.ID, _
          RevCounters)

       'Set the revision of the file to the new values
       RevMgr.IncrementRevision(FileObj.ID)

       'Save the new values to the database
       Dim RevErrors() As EdmRevError = {}
       RevMgr.Commit("Set starting revision for " + _
          "legacy file.", RevErrors)
     End While
   End Sub
 End Class
```

```
Back to top
```

```
'Form1.Designer.vb
```

```vb
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
         Me.SetInitialRevisionButton = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(22, 16)
         Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(136, 13)
         Me.VaultsLabel.TabIndex = 10
         Me.VaultsLabel.Text = "Select Preferred Vault View"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(26, 32)
         Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(132, 21)
         Me.VaultsComboBox.TabIndex = 11
         '
         'SetInitialRevisionButton
         '
         Me.SetInitialRevisionButton.Location = New System.Drawing.Point(41, 57)
         Me.SetInitialRevisionButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
         Me.SetInitialRevisionButton.Name = "SetInitialRevisionButton"
         Me.SetInitialRevisionButton.Size = New System.Drawing.Size(101, 41)
         Me.SetInitialRevisionButton.TabIndex = 14
         Me.SetInitialRevisionButton.Text = "Set Initial Revision"
         Me.SetInitialRevisionButton.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(222, 119)
         Me.Controls.Add(Me.SetInitialRevisionButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
         Me.Name = "Form1"
         Me.Text = "Set Revision"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents SetInitialRevisionButton As System.Windows.Forms.Button

 End Class
```

[Back to top](#Top)
