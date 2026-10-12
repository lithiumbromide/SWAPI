---
title: "Get File References for a File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_File_References_for_File_Example_VBNET.htm"
---

# Get File References for a File Example (VB.NET)

This example shows how to get the file references for a file and export any file references to an XML file. This example also shows how to get whether the file and any file references in local cache are valid or obsolete.

**NOTE:**

- This example does not work with assemblies that contain weldment components.
- If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
' 3. Type GetFiles2 in Project name.
' 4. For Location, click ... and navigate to the folder where to
create the project.

' 5. Click Next.

' 6. Select Framework.

' 7. Click Create.

' 8. Click Show All Files in the Solution Explorer toolbar and expand

'    Form1.vb in the Solution Explorer.

' 9. Add dependencies and
safely pass arrays of structures.
'10. Replace the code in Form1.vb with this code.
'11. To create the form, replace the code in Form1.Designer.vb with this code.
'12. Right-click the GetFiles2 project name in the Solution Explorer.
'        1. Click Add > Class > Class.
'        2. Type FileRef.vb in Name.
'        3. Click Add.
'        4. Replace the code in FileRef.vb with this code.
'13. Verify that C:\temp exists.
'14. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click Browse, locate and select a file in the vault that
'     has file references, and click Open.
'  4. Click Write file references to an XML file, which exports
'     the names of any file references to C:\temp\BatchFileRefInfo.xml.
'  5. Displays a message box that says file references were exported
'     to an XML file.
'  6. Click OK to close the message box.
'  7. Double-click C:\temp\BatchFileRefInfo.xml and examine its contents.
'----------------------------------------------------------------------------

'Form1.vb
Imports System.IO
Imports System.Xml.Serialization

Imports EPDM.Interop.epdm

Public Class Form1

  Dim vault As IEdmVault5 = Nothing

  Private Sub BatchRefTreeInfo_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Try
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
    Catch ex As Runtime.InteropServices.COMException
      MessageBox.Show("HRESULT = 0x" + _
      ex.ErrorCode.ToString("X") + vbCrLf + _
      ex.Message)
    Catch ex As Exception
      MessageBox.Show(ex.Message)
    End Try
  End Sub

  Private Sub BrowseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BrowseButton.Click
    Try
      BatchRefListBox.Items.Clear()

            'Only create a new vault object
            'if one hasn't been created yet
            If vault Is Nothing Then vault = New EdmVault5
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                  Me.Handle.ToInt32())
            End If

            'Set the initial directory in the File Open dialog
            BatchRefOpenFileDialog.InitialDirectory = vault.RootFolderPath
            'Show the File Open dialog
            Dim DialogResult As System.Windows.Forms.DialogResult
            DialogResult = BatchRefOpenFileDialog.ShowDialog()
            'If the user didn't click Open, exit the sub
            If Not DialogResult = System.Windows.Forms.DialogResult.OK Then Exit Sub

            For Each FileName As String In BatchRefOpenFileDialog.FileNames
                BatchRefListBox.Items.Add(FileName)
            Next FileName
        Catch ex As Runtime.InteropServices.COMException
      MessageBox.Show("HRESULT = 0x" + _
      ex.ErrorCode.ToString("X") + vbCrLf + _
        ex.Message)
    Catch ex As Exception
      MessageBox.Show(ex.Message)
    End Try
  End Sub

  Private Sub GetReferencedFiles( _
    ByVal Reference As IEdmReference10, _
    ByVal FilePath As String, _
    ByVal Level As Integer, _
    ByVal ProjectName As String, _
    ByRef RefFilesDictionary _
    As Dictionary(Of String, String))

        Try
            Dim Top As Boolean = False
            If Reference Is Nothing Then
                'This is the first time this function is called for this
                'file reference tree; i.e., this is the root
                Top = True
                'Add the top-level file path to the dictionary
                RefFilesDictionary.Add(FilePath, Level.ToString())
                Dim File As IEdmFile5 = Nothing
                Dim ParentFolder As IEdmFolder5 = Nothing
                File = vault.GetFileFromPath(FilePath, ParentFolder)
                'Get the file reference tree for this file
                Reference = File.GetReferenceTree(ParentFolder.ID)
                GetReferencedFiles(Reference, "", Level + 1, ProjectName, RefFilesDictionary)
            Else
                'Execute this code when this function is called recursively;
                'i.e., this is not the top-level IEdmReference in the tree

                'Recursively traverse the references
                Dim pos As IEdmPos5
                pos = Reference.GetFirstChildPosition4(ProjectName, Top, True, True, EdmRefFlags.EdmRef_file, "", 0)
                Dim ref As IEdmReference10
                While (Not pos.IsNull)
                    ref = Reference.GetNextChild(pos)
                    RefFilesDictionary.Add(ref.FoundPath, Level.ToString())
                    GetReferencedFiles(ref, "", Level + 1, ProjectName, RefFilesDictionary)
                End While
            End If

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
  End Sub

  Private Sub WriteXmlButton_Click( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles WriteXmlButton.Click

        Try
            'Only create a new vault object
            'if one hasn't been created yet
            If vault Is Nothing Then vault = New EdmVault5
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If

            'Get the file paths of all of the referenced files
            'and store them in RefFilesDictionary as keys;
            'the levels where they are found in the file hierarchy
            'are stored as values
            Dim RefFilesDictionary As Dictionary(Of String, String) = _
                    New Dictionary(Of String, String)()
            For Each FileName As String In BatchRefListBox.Items
                GetReferencedFiles(Nothing, FileName, 0, "A", RefFilesDictionary)
            Next FileName

            'Because selecting a file in the Open File dialog
            'adds the file and its references to the local cache,
            'clear the local cache to demonstrate that the
            'IEdmBatchListing methods don't add the files to
            'the local cache

            'Declare and create the IEdmClearLocalCache3 object
            Dim ClearLocalCache As IEdmClearLocalCache3
            ClearLocalCache = vault.CreateUtility(EdmUtility.EdmUtil_ClearLocalCache)
	    ClearLocalCache.IgnoreToolboxFiles = True
	    ClearLocalCache.UseAutoClearCacheOption = True
            'Declare and create the IEdmBatchListing object
            Dim BatchListing As IEdmBatchListing4
            BatchListing = vault.CreateUtility(EdmUtility.EdmUtil_BatchList)

            'Add all of the file reference paths to the
            'IEdmClearLocalCache object to clear from the
            'local cache and to the IEdmBatchListing object
            'to get the file information in batch mode
            For Each KvPair As KeyValuePair(Of String, String) In RefFilesDictionary
                ClearLocalCache.AddFileByPath(KvPair.Key)
                DirectCast(BatchListing, IEdmBatchListing4).AddFileCfg(KvPair.Key, Nothing, KvPair.Value, "@", EdmListFileFlags.EdmList_Nothing)
            Next
            'Clear the local cache of the file references
            ClearLocalCache.CommitClear()

            'Create the batch file listing along with the file
            'card variables Description and Number
            Dim BatchListCols() As EdmListCol = Nothing
            DirectCast(BatchListing, IEdmBatchListing4). _
                CreateListEx(vbLf + "Description" + vbLf + _
                    "Number", EdmCreateListExFlags.Edmclef_MayReadFiles, _
                    BatchListCols, Nothing)
            'Get the generated file information
            Dim BatchListFiles() As EdmListFile2 = Nothing
            BatchListing.GetFiles2(BatchListFiles)

            'Create the list where to store all the file information
            Dim FileRefs As New List(Of FileRef)

            'Recursively add the file information to the list
            AddFileRef(BatchListFiles, 0, 0, FileRefs)

            If Not Directory.Exists("C:\temp") Then
                MessageBox.Show("Directory ""c:\temp"" does " + _
                                "not exist; please create it and try again.")
            Else
                'Write out the file references to an XML file
                Dim XmlSer As New XmlSerializer(GetType(List(Of FileRef)))
                Dim StrWriter As New StreamWriter("C:\temp\BatchFileRefInfo.xml")
                XmlSer.Serialize(StrWriter, FileRefs)
                StrWriter.Close()
                MessageBox.Show( _
                    "File references successfully exported to an XML file.")
            End If

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
  End Sub

  Private Sub AddFileRef( _
    ByRef BatchListFiles() As EdmListFile2, _
    ByRef curIndex As Integer, _
    ByVal curLevel As Integer, _
    ByRef FileRefs As List(Of FileRef))

        Try
            While curIndex < BatchListFiles.Length
                Dim curListFile As EdmListFile2 = BatchListFiles(curIndex)
                'If the depth level of this listfile is <
                'the current depth level, then...
                If curListFile.mlParam > curLevel Then
                    'Create a new FileRefs list
                    FileRefs(FileRefs.Count - 1).FileRefs = New List(Of FileRef)
                    'Recurse using a new FileRefs list
                    AddFileRef(BatchListFiles, curIndex, curListFile.mlParam, _
                               FileRefs.Item(FileRefs.Count - 1).FileRefs)
                Else
                    'Create a new FileRef object to hold
                    'the file information
                    Dim FileRef As New FileRef
                    'Assign the FileRef properties
                    FileRef.CheckedOutBy = curListFile.mbsLockUser
                    FileRef.CurrentState = curListFile.moCurrentState.mbsStateName
                    FileRef.Description = curListFile.moColumnData(0)
                    Dim File As IEdmFile5
                    File = vault.GetObject(EdmObjectType.EdmObject_File, curListFile.mlFileID)
                    FileRef.FileName = File.Name
                    FileRef.LatestRevision = curListFile.mbsRevisionName
                    FileRef.LatestVersion = curListFile.mlLatestVersion
                    FileRef.Number = curListFile.moColumnData(1)
                    FileRef.FileRefs = Nothing
                    'Add the FileRef to this level's list
                    FileRefs.Add(FileRef)
                    curIndex += 1
                End If
            End While

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

    'Required by the Windows Form Designer.
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.BatchRefOpenFileDialog = New System.Windows.Forms.OpenFileDialog()
        Me.BatchRefListBox = New System.Windows.Forms.ListBox()
        Me.BatchRefLabel = New System.Windows.Forms.Label()
        Me.WriteXmlButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'BrowseButton
        '
        Me.BrowseButton.Location = New System.Drawing.Point(180, 65)
        Me.BrowseButton.Margin = New System.Windows.Forms.Padding(2)
        Me.BrowseButton.Name = "BrowseButton"
        Me.BrowseButton.Size = New System.Drawing.Size(64, 19)
        Me.BrowseButton.TabIndex = 17
        Me.BrowseButton.Text = "Browse..."
        Me.BrowseButton.UseVisualStyleBackColor = True
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(16, 32)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(136, 21)
        Me.VaultsComboBox.TabIndex = 15
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(16, 16)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 16
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'BatchRefOpenFileDialog
        '
        Me.BatchRefOpenFileDialog.InitialDirectory = "C:\"
        Me.BatchRefOpenFileDialog.Multiselect = True
        '
        'BatchRefListBox
        '
        Me.BatchRefListBox.FormattingEnabled = True
        Me.BatchRefListBox.Location = New System.Drawing.Point(18, 94)
        Me.BatchRefListBox.Margin = New System.Windows.Forms.Padding(2)
        Me.BatchRefListBox.Name = "BatchRefListBox"
        Me.BatchRefListBox.Size = New System.Drawing.Size(218, 56)
        Me.BatchRefListBox.TabIndex = 18
        '
        'BatchRefLabel
        '
        Me.BatchRefLabel.AutoSize = True
        Me.BatchRefLabel.Location = New System.Drawing.Point(16, 71)
        Me.BatchRefLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.BatchRefLabel.Name = "BatchRefLabel"
        Me.BatchRefLabel.Size = New System.Drawing.Size(160, 13)
        Me.BatchRefLabel.TabIndex = 19
        Me.BatchRefLabel.Text = "Files for which to get references:"
        '
        'WriteXmlButton
        '
        Me.WriteXmlButton.Location = New System.Drawing.Point(19, 169)
        Me.WriteXmlButton.Margin = New System.Windows.Forms.Padding(2)
        Me.WriteXmlButton.Name = "WriteXmlButton"
        Me.WriteXmlButton.Size = New System.Drawing.Size(217, 19)
        Me.WriteXmlButton.TabIndex = 20
        Me.WriteXmlButton.Text = "Write file references to an XML file"
        Me.WriteXmlButton.UseVisualStyleBackColor = True
        '
        'BatchRefTreeInfo
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(255, 227)
        Me.Controls.Add(Me.WriteXmlButton)
        Me.Controls.Add(Me.BatchRefLabel)
        Me.Controls.Add(Me.BatchRefListBox)
        Me.Controls.Add(Me.BrowseButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Margin = New System.Windows.Forms.Padding(2)
        Me.Name = "BatchRefTreeInfo"
        Me.Text = "Get file references"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents BrowseButton As System.Windows.Forms.Button
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents BatchRefOpenFileDialog As System.Windows.Forms.OpenFileDialog
    Friend WithEvents BatchRefListBox As System.Windows.Forms.ListBox
    Friend WithEvents BatchRefLabel As System.Windows.Forms.Label
    Friend WithEvents WriteXmlButton As System.Windows.Forms.Button

End Class
```

```
Back to top
```

```
'FileRef.vb
Public Class FileRef
  Private mLocalOverwittenVersionObsolete As Short
  Private mFileName As String
  Private mLatestVersion As String
  Private mLatestRevision As String
  Private mNumber As String
  Private mDescription As String
  Private mCurrentState As String
  Private mCheckedOutBy As String
  Private mFileRefs As List(Of FileRef)

  Public Sub New()

  End Sub

  Public Property FileName() As String
    Get
      Return mFileName
    End Get
    Set(ByVal value As String)
      mFileName = value
    End Set
  End Property

  Public Property LatestVersion() As String
    Get
      Return mLatestVersion
    End Get
    Set(ByVal value As String)
      mLatestVersion = value
    End Set
  End Property

  Public Property LatestRevision() As String
    Get
      Return mLatestRevision
    End Get
    Set(ByVal value As String)
      mLatestRevision = value
    End Set
  End Property

  Public Property Number() As String
    Get
      Return mNumber
    End Get
    Set(ByVal value As String)
      mNumber = value
    End Set
  End Property

  Public Property Description() As String
    Get
      Return mDescription
    End Get
    Set(ByVal value As String)
      mDescription = value
    End Set
  End Property

  Public Property CurrentState() As String
    Get
      Return mCurrentState
    End Get
    Set(ByVal value As String)
      mCurrentState = value
    End Set
  End Property

  Public Property CheckedOutBy() As String
    Get
      Return mCheckedOutBy
    End Get
    Set(ByVal value As String)
      mCheckedOutBy = value
    End Set
  End Property
```

```
  Public Property LocalOverwrittenVersionObsolete() As Short
    Get
        Return mLocalOverwittenVersionObsolete
    End Get
    Set(ByVal value As Short)
        mLocalOverwittenVersionObsolete = value
    End Set
  End Property

  Public Property FileRefs() As List(Of FileRef)
    Get
      Return mFileRefs
    End Get
    Set(ByVal value As List(Of FileRef))
      mFileRefs = value
    End Set
  End Property

End Class
```

```
Back to top
```
