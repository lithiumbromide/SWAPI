---
title: "Read and Write to Third-party Storage Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_and_Set_3rd_Party_Storage_Example_VBNET.htm"
---

# Read and Write to Third-party Storage Example (VB.NET)

This example shows how to read and write to third-party storage in a document.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Read the SOLIDWORKS Document Manager API Getting Started
  '     topic and ensure that the required DLLs are registered.
 '  2. Start Microsoft Visual Studio 2010.
 '  3. Click File > New > Project > Visual Basic > Windows Forms Application.
 '     a. Type SwDocMgrStorageApp_VBNET in Name.
 '     b. Click Browse and navigate to the folder where to create
 '        the project.
 '     c. Click OK.
 '  4. Add references to the project:
  '     a. Right-click the solution in Solution Explorer.
 '     b. Click Add Reference.
 '     c. Click Browse.
 '     d. Click:
 '        install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 '     e. Click Open.
 '     f. Click Add.
 '     g. Click Browse.
 '     h. Click:
 '        C:\Program Files\Microsoft Visual Studio 11.0\Common7\IDE\Remote Debugger\x64\Microsoft.VisualStudio.OLE.Interop.dll
 '     i. Click Open.
 '     j. Click Add.
 '     k. Click Close.
 '  5. Click Show All Files in the Solution Explorer toolbar and expand
 '     Form1.vb in the Solution Explorer.
 '  6. Replace the code in Form1.vb with this code.
 '  7. Replace the code in Form1.Designer.vb with this code.
 '  8. Substitute your_license_key with your SOLIDWORKS Document
 '     Manager license key.
 '
 ' Postconditions:
 '  1. Displays a dialog.
 '  2. Click Browse.
 '     a. Locate and click a SOLIDWORKS document.
 '     b. Click Open.
 '  3. Type temp in StoreName and in both StorageName  fields.
 '  4. Type Some third-party text in both text boxes.
 '  5. Click Write.
 '  6. Click Exit.
 '  7. Press F5.
 '  8. In the dialog, click Browse.
  '     a. Locate and click the document you clicked in step 2a.
 '     b. Click Open.
 '  9. Type temp in StoreName and in both StorageName  fields.
 ' 10. Click Read.
 ' 11. Displays Some third-party text in both text boxes.
 ' 12. Click Exit.
  '----------------------------------------------------------------------------
'Form1.vb

 Imports System.Collections.Generic
 Imports System.ComponentModel
 Imports System.Data
 Imports System.Drawing
 Imports System.Linq
 Imports System.Text
 Imports System.Windows.Forms
 Imports SwDocumentMgr
 Imports Microsoft.VisualStudio.OLE.Interop
 Imports System.IO
 Imports System.Diagnostics
 Imports System.Runtime.InteropServices

 Public Class Form1
     Inherits Form
     Public Sub New()
         InitializeComponent()
     End Sub
     Public swDoc19 As SwDMDocument19
     Public swDocMgr As SwDMApplication
     Public swClassFact As SwDMClassFactory
     Public sLicenseKey As String = "your_license_key"

     Public Sub btnFile_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnFile.Click
         OpenFileDialog1.Filter = "SOLIDWORKS Files (*.sldprt;*sldasm;*slddrw)|*.sldprt;*sldasm;*slddrw|SOLIDWORKS Part (*.sldprt)|*.sldprt|SOLIDWORKS Assembly (*.sldasm)|*.sldasm|SOLIDWORKS Drawing (*.slddrw)|*.slddrw"
         If OpenFileDialog1.ShowDialog() = System.Windows.Forms.DialogResult.OK Then
             txtFileName.Text = OpenFileDialog1.FileName
         End If
     End Sub

     Public Sub btnOpen_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnOpen.Click
         OpenFile()
         If (swDoc19 IsNot Nothing) Then
             If txtStorageName.Text <> String.Empty Then
                 Read3rdPartyStorageData()
             End If
             If txtStoreName.Text <> String.Empty AndAlso txtStreamName.Text <> String.Empty Then
                 Read3rdPartyStorageStoreData()
             End If
         End If
         CloseFile()
         Me.Refresh()
     End Sub

     Public Sub btnSave_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSave.Click
         OpenFile()
         If (swDoc19 IsNot Nothing) Then
             If txtStorageName.Text <> String.Empty Then
                 Write3rdPartyStorageData()
             End If
             If txtStoreName.Text <> String.Empty AndAlso txtStreamName.Text <> String.Empty Then
                 Write3rdPartyStorageStoreData()
             End If
         End If
         rtbStorage.Text = String.Empty
         rtbStore.Text = String.Empty
         CloseFile()
         Me.Refresh()
     End Sub

     Public Sub btnExit_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnExit.Click
         Me.Close()
     End Sub

     Public Sub OpenFile()
         If (swDoc19 IsNot Nothing) Then
             swDoc19.CloseDoc()
             swDoc19 = Nothing
         End If

         Dim sDocFileName As String = Nothing
         Dim nDocType As SwDmDocumentType = 0
         Dim nRetVal As SwDmDocumentOpenError = 0

         sDocFileName = txtFileName.Text
         If sDocFileName.ToLower().EndsWith("sldprt") Then
             nDocType = SwDmDocumentType.swDmDocumentPart
         ElseIf sDocFileName.ToLower().EndsWith("sldasm") Then
             nDocType = SwDmDocumentType.swDmDocumentAssembly
         ElseIf sDocFileName.ToLower().EndsWith("slddrw") Then
             nDocType = SwDmDocumentType.swDmDocumentDrawing
         Else

             ' Not a SOLIDWORKS file
             nDocType = SwDmDocumentType.swDmDocumentUnknown

             Return
         End If

         swClassFact = New SwDMClassFactory()
         swDocMgr = TryCast(swClassFact.GetApplication(sLicenseKey), SwDMApplication)
         swDoc19 = TryCast(swDocMgr.GetDocument(sDocFileName, nDocType, False, nRetVal), SwDMDocument19)
         Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone = nRetVal)
     End Sub

     Public Sub CloseFile()
         If (swDoc19 IsNot Nothing) Then
             swDoc19.CloseDoc()
             System.Runtime.InteropServices.Marshal.ReleaseComObject(swDoc19)
             GC.Collect()
             GC.WaitForPendingFinalizers()
             GC.Collect()
             GC.WaitForPendingFinalizers()
             swDoc19 = Nothing
         End If

     End Sub

     Public Sub Read3rdPartyStorageData()
         Try
             Dim pIStream As IStream = Nothing
             pIStream = swDoc19.Get3rdPartyStorage(txtStorageName.Text, False)
             If pIStream Is Nothing Then
                 rtbStorage.Text = "Error: " + "Storage " + txtStorageName.Text + " not found"
                 Return
             End If
             Dim strStream As String = Nothing
             Dim byteArray As Byte() = New Byte(999) {}
             Dim outlength As UInteger = 0
             pIStream.Read(byteArray, CUInt(byteArray.Length), outlength)
             strStream = Encoding.UTF8.GetString(byteArray)
             rtbStorage.Text = strStream.Substring(0, CInt(outlength))
             swDoc19.Release3rdPartyStorage(txtStorageName.Text)
             System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream)
             GC.Collect()
             GC.WaitForPendingFinalizers()
             GC.Collect()
             GC.WaitForPendingFinalizers()
         Catch ex As Exception
             rtbStorage.Text = "Error: " + ex.Message
         End Try
     End Sub

     Public Sub Read3rdPartyStorageStoreData()
         Try
             Dim storage As IStorage = Nothing
             storage = swDoc19.Get3rdPartyStorageStore(txtStoreName.Text, False)
             If storage Is Nothing Then
                 rtbStore.Text = "Error: " + "Store " + txtStoreName.Text + " not found"
                 Return
             End If
             Dim pIStream As IStream = Nothing
             Dim grfmode As Integer = 0
             grfmode = grfmode Or CInt(STGM.SHARE_EXCLUSIVE)
             storage.OpenStream(txtStreamName.Text, IntPtr.Zero, CUInt(grfmode), 0, pIStream)
             If pIStream Is Nothing Then
                 rtbStore.Text = "Error: " + "Stream " + txtStreamName.Text + " not found"
                 Return
             End If
             Dim strStream As String = Nothing
             Dim byteArray As Byte() = New Byte(999) {}
             Dim outlength As UInteger = 0
             pIStream.Read(byteArray, CUInt(byteArray.Length), outlength)
             strStream = Encoding.UTF8.GetString(byteArray)
             rtbStore.Text = strStream
             System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream)
             GC.Collect()
             GC.WaitForPendingFinalizers()
             GC.Collect()
             GC.WaitForPendingFinalizers()
             swDoc19.Release3rdPartyStorageStore(txtStoreName.Text)
         Catch ex As Exception
             rtbStore.Text = "Error: " + ex.Message
         End Try
     End Sub

     Public Sub Write3rdPartyStorageData()
         Try
             Dim pIStream As IStream = Nothing
             pIStream = swDoc19.Get3rdPartyStorage(txtStorageName.Text, True)
             If pIStream Is Nothing Then
                 rtbStorage.Text = "Error: " + "Storage " + txtStorageName.Text + " not found"
                 Return
             End If
             Dim strStream As Byte() = Nothing
             strStream = Encoding.UTF8.GetBytes(rtbStorage.Text)
             Dim outlength As UInteger = 0
             pIStream.Write(strStream, CUInt(strStream.Length), outlength)
             System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream)
             GC.Collect()
             GC.WaitForPendingFinalizers()
             GC.Collect()
             GC.WaitForPendingFinalizers()
             swDoc19.Release3rdPartyStorage(txtStorageName.Text)
             swDoc19.Save()
         Catch ex As Exception
             rtbStorage.Text = "Error: " + ex.Message
         End Try
     End Sub

     Public Sub Write3rdPartyStorageStoreData()
         Try
             Dim storage As IStorage = Nothing
             storage = swDoc19.Get3rdPartyStorageStore(txtStoreName.Text, True)
             If storage Is Nothing Then
                 rtbStore.Text = "Error: " + "Store " + txtStoreName.Text + " not found"
                 Return
             End If
             Dim pIStream As IStream = Nothing
             Dim grfmode As Integer = 0
             grfmode = grfmode Or CInt(STGM.SHARE_EXCLUSIVE)
             grfmode = grfmode Or CInt(STGM.READWRITE)
             grfmode = grfmode Or CInt(STGM.CREATE)
             storage.CreateStream(txtStreamName.Text, CUInt(grfmode), 0, 0, pIStream)
             If pIStream Is Nothing Then
                 rtbStore.Text = "Error: " + "Stream " + txtStreamName.Text + " not found"
                 Return
             End If
             Dim strStream As Byte() = Nothing
             strStream = Encoding.UTF8.GetBytes(rtbStore.Text)
             Dim outlength As UInteger = 0
             pIStream.Write(strStream, CUInt(strStream.Length), outlength)
             System.Runtime.InteropServices.Marshal.ReleaseComObject(storage)
             System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream)
             GC.Collect()
             GC.WaitForPendingFinalizers()
             GC.Collect()
             GC.WaitForPendingFinalizers()
             swDoc19.Release3rdPartyStorageStore(txtStoreName.Text)
             swDoc19.Save()
         Catch ex As Exception
             rtbStore.Text = "Error: " + ex.Message
         End Try
     End Sub

     <Flags()> _
     Public Enum STGM As UInteger
         DIRECT = &H0
         TRANSACTED = &H10000
         SIMPLE = &H8000000
         READ = &H0
         WRITE = &H1
         READWRITE = &H2
         SHARE_DENY_NONE = &H40
         SHARE_DENY_READ = &H30
         SHARE_DENY_WRITE = &H20
         SHARE_EXCLUSIVE = &H10
         PRIORITY = &H40000
         DELETEONRELEASE = &H4000000
         NOSCRATCH = &H100000
         CREATE = &H1000
         CONVERT = &H20000
         FAILIFTHERE = &H0
         NOSNAPSHOT = &H200000
         DIRECT_SWMR = &H400000
     End Enum

 End Class
'Form1.Designer.vb
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

         Me.rtbStorage = New System.Windows.Forms.RichTextBox()
         Me.rtbStore = New System.Windows.Forms.RichTextBox()
         Me.btnExit = New System.Windows.Forms.Button()
         Me.btnSave = New System.Windows.Forms.Button()
         Me.btnOpen = New System.Windows.Forms.Button()
         Me.btnFile = New System.Windows.Forms.Button()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.txtFileName = New System.Windows.Forms.TextBox()
         Me.groupBox1 = New System.Windows.Forms.GroupBox()
         Me.txtStoreName = New System.Windows.Forms.TextBox()
         Me.label1 = New System.Windows.Forms.Label()
         Me.label3 = New System.Windows.Forms.Label()
         Me.txtStreamName = New System.Windows.Forms.TextBox()
         Me.groupBox2 = New System.Windows.Forms.GroupBox()
         Me.label5 = New System.Windows.Forms.Label()
         Me.txtStorageName = New System.Windows.Forms.TextBox()
         Me.groupBox1.SuspendLayout()
         Me.groupBox2.SuspendLayout()
         Me.SuspendLayout()
         '
         ' rtbStorage
         '
         Me.rtbStorage.Location = New System.Drawing.Point(6, 83)
         Me.rtbStorage.Name = "rtbStorage"
         Me.rtbStorage.Size = New System.Drawing.Size(198, 91)
         Me.rtbStorage.TabIndex = 15
         Me.rtbStorage.Text = ""
         '
         ' rtbStore
         '
         Me.rtbStore.Location = New System.Drawing.Point(6, 83)
         Me.rtbStore.Name = "rtbStore"
         Me.rtbStore.Size = New System.Drawing.Size(198, 91)
         Me.rtbStore.TabIndex = 14
         Me.rtbStore.Text = ""
         '
         ' btnExit
         '
         Me.btnExit.Location = New System.Drawing.Point(448, 197)
         Me.btnExit.Name = "btnExit"
         Me.btnExit.Size = New System.Drawing.Size(75, 23)
         Me.btnExit.TabIndex = 13
         Me.btnExit.Text = "Exit"
         Me.btnExit.UseVisualStyleBackColor = True
         'Me.btnExit.Click += New System.EventHandler(Me.btnExit_Click)
         '
         ' btnSave
         '
         Me.btnSave.Location = New System.Drawing.Point(448, 168)
         Me.btnSave.Name = "btnSave"
         Me.btnSave.Size = New System.Drawing.Size(75, 23)
         Me.btnSave.TabIndex = 12
         Me.btnSave.Text = "Write"
         Me.btnSave.UseVisualStyleBackColor = True
         'Me.btnSave.Click += New System.EventHandler(Me.btnSave_Click)
         '
         ' btnOpen
         '
         Me.btnOpen.Location = New System.Drawing.Point(448, 139)
         Me.btnOpen.Name = "btnOpen"
         Me.btnOpen.Size = New System.Drawing.Size(75, 23)
         Me.btnOpen.TabIndex = 11
         Me.btnOpen.Text = "Read"
         Me.btnOpen.UseVisualStyleBackColor = True
         'Me.btnOpen.Click += New System.EventHandler(Me.btnOpen_Click)
         '
         ' btnFile
         '
         Me.btnFile.Location = New System.Drawing.Point(448, 12)
         Me.btnFile.Name = "btnFile"
         Me.btnFile.Size = New System.Drawing.Size(75, 23)
         Me.btnFile.TabIndex = 10
         Me.btnFile.Text = "Browse..."
         Me.btnFile.UseVisualStyleBackColor = True
         'Me.btnFile.Click += New System.EventHandler(Me.btnFile_Click)
         '
         ' OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         '
         ' txtFileName
         '
         Me.txtFileName.Location = New System.Drawing.Point(12, 12)
         Me.txtFileName.Name = "txtFileName"
         Me.txtFileName.Size = New System.Drawing.Size(430, 20)
         Me.txtFileName.TabIndex = 9
         '
         ' groupBox1
         '
         Me.groupBox1.Controls.Add(Me.label3)
         Me.groupBox1.Controls.Add(Me.txtStreamName)
         Me.groupBox1.Controls.Add(Me.label1)
         Me.groupBox1.Controls.Add(Me.txtStoreName)
         Me.groupBox1.Controls.Add(Me.rtbStore)
         Me.groupBox1.Location = New System.Drawing.Point(13, 39)
         Me.groupBox1.Name = "groupBox1"
         Me.groupBox1.Size = New System.Drawing.Size(210, 180)
         Me.groupBox1.TabIndex = 18
         Me.groupBox1.TabStop = False
         Me.groupBox1.Text = "Store:"
         '
         ' txtStoreName
         '
         Me.txtStoreName.Location = New System.Drawing.Point(88, 17)
         Me.txtStoreName.Name = "txtStoreName"
         Me.txtStoreName.Size = New System.Drawing.Size(116, 20)
         Me.txtStoreName.TabIndex = 15
         '
         ' label1
         '
         Me.label1.AutoSize = True
         Me.label1.Location = New System.Drawing.Point(7, 20)
         Me.label1.Name = "label1"
         Me.label1.Size = New System.Drawing.Size(63, 13)
         Me.label1.TabIndex = 16
         Me.label1.Text = "StoreName:"
         '
         ' label3
         '
         Me.label3.AutoSize = True
         Me.label3.Location = New System.Drawing.Point(7, 53)
         Me.label3.Name = "label3"
         Me.label3.Size = New System.Drawing.Size(75, 13)
         Me.label3.TabIndex = 18
         Me.label3.Text = "StorageName:"
         '
         ' txtStreamName
         '
         Me.txtStreamName.Location = New System.Drawing.Point(88, 50)
         Me.txtStreamName.Name = "txtStreamName"
         Me.txtStreamName.Size = New System.Drawing.Size(116, 20)
         Me.txtStreamName.TabIndex = 17
         '
         ' groupBox2
         '
         Me.groupBox2.Controls.Add(Me.rtbStorage)
         Me.groupBox2.Controls.Add(Me.label5)
         Me.groupBox2.Controls.Add(Me.txtStorageName)
         Me.groupBox2.Location = New System.Drawing.Point(232, 39)
         Me.groupBox2.Name = "groupBox2"
         Me.groupBox2.Size = New System.Drawing.Size(210, 180)
         Me.groupBox2.TabIndex = 19
         Me.groupBox2.TabStop = False
         Me.groupBox2.Text = "Storage:"
         '
         ' label5
         '
         Me.label5.AutoSize = True
         Me.label5.Location = New System.Drawing.Point(7, 20)
         Me.label5.Name = "label5"
         Me.label5.Size = New System.Drawing.Size(75, 13)
         Me.label5.TabIndex = 16
         Me.label5.Text = "StorageName:"
         '
         ' txtStorageName
         '
         Me.txtStorageName.Location = New System.Drawing.Point(88, 17)
         Me.txtStorageName.Name = "txtStorageName"
         Me.txtStorageName.Size = New System.Drawing.Size(116, 20)
         Me.txtStorageName.TabIndex = 15
         '
         ' Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0F, 13.0F)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(536, 231)
         Me.Controls.Add(Me.btnExit)
         Me.Controls.Add(Me.btnSave)
         Me.Controls.Add(Me.btnOpen)
         Me.Controls.Add(Me.btnFile)
         Me.Controls.Add(Me.txtFileName)
         Me.Controls.Add(Me.groupBox1)
         Me.Controls.Add(Me.groupBox2)
         Me.MaximumSize = New System.Drawing.Size(552, 269)
         Me.MinimumSize = New System.Drawing.Size(552, 269)
         Me.Name = "Form1"
         Me.Text = "DocManager Test"
         Me.groupBox1.ResumeLayout(False)
         Me.groupBox1.PerformLayout()
         Me.groupBox2.ResumeLayout(False)
         Me.groupBox2.PerformLayout()
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

     Friend WithEvents rtbStorage As System.Windows.Forms.RichTextBox
     Friend WithEvents rtbStore As System.Windows.Forms.RichTextBox
     Friend WithEvents btnExit As System.Windows.Forms.Button
     Friend WithEvents btnSave As System.Windows.Forms.Button
     Friend WithEvents btnOpen As System.Windows.Forms.Button
     Friend WithEvents btnFile As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
     Friend WithEvents txtFileName As System.Windows.Forms.TextBox
     Private groupBox1 As System.Windows.Forms.GroupBox
     Private label3 As System.Windows.Forms.Label
     Private txtStreamName As System.Windows.Forms.TextBox
     Private label1 As System.Windows.Forms.Label
     Private txtStoreName As System.Windows.Forms.TextBox
     Private groupBox2 As System.Windows.Forms.GroupBox
     Private label5 As System.Windows.Forms.Label
     Private txtStorageName As System.Windows.Forms.TextBox

 End Class
```
