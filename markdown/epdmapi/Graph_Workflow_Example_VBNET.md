---
title: "Graph a Workflow Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Graph_Workflow_Example_VBNET.htm"
---

# Graph a Workflow Example (VB.NET)

This example shows how to graph a workflow.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App
 ' 3. Type PaintWorkflowGraph in Project name.
  ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
 ' 8. Click Show All Files in the Solution Explorer toolbar and expand
 '    Form1.vb in the Solution Explorer.
 ' 9.  Add dependencies and safely pass arrays of structures.
 '10. Replace the code in Form1.vb with this code.
 '11. To create the form, replace the code in Form1.Designer.vb with this code.
 '12. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Graph a workflow dialog box.
 ' 2. Maximize the dialog box for the workflow graph.
 ' 3. Select a vault view.
 ' 4. Click a workflow.
 ' 5. Click Graph workflow.
  ' 6. Graphs the selected workflow in the dialog box.
  ' 7. Close the Graph a workflow dialog box.
  '----------------------------------------------------------------------------

 'Form1.vb

 Imports System.IO
 Imports System.Xml.Serialization
 Imports System.Collections
 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public Class Form1

     Private vault1 As IEdmVault5 = Nothing
     Dim wf As IEdmWorkflow6
     Dim wfmgr As IEdmWorkflowMgr6
     Dim pos As IEdmPos5

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
             vault1 = New EdmVault5()
             Dim vault As IEdmVault8 = DirectCast(vault1, IEdmVault8)
             Dim Views As EdmViewInfo() = Nothing

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

     Public Sub GraphWorkflow_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GraphWorkflow.Click
         'Graph workflow
         Try
             Dim vault2 As IEdmVault7
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

             vault2 = vault1
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Retrieve the graphics interface of this window
             Dim gfx As System.Drawing.Graphics
             gfx = Me.CreateGraphics()
             gfx.Clear(Color.AliceBlue)

             'Create font with which to draw text
             Dim font As System.Drawing.Font
             font = New System.Drawing.Font("Arial", 10, FontStyle.Bold)

             'Loop over all the workflows to find the selected workflow
             pos = wfmgr.GetFirstWorkflowPosition()
             While Not pos.IsNull
                 wf = wfmgr.GetNextWorkflow(pos)
                 If (wf.Name = ListBox1.SelectedItem.ToString) Then

                     'Loop over all workflow transitions
                     Dim pos As IEdmPos5
                     pos = wf.GetFirstTransitionPosition
                     While Not pos.IsNull
                         Dim trans As IEdmTransition7
                         trans = wf.GetNextTransition(pos)

                         'Draw the arrow of the transition
                         Dim vertices() As EdmPoint
                         vertices = Nothing
                         trans.GetArrowVertices(vertices)
                         PaintArrow(gfx, vertices)

                         'Get the transition box
                         Dim transRect As EdmRect
                         trans.GetRect(transRect)
                         Dim rectF As System.Drawing.RectangleF
                         rectF.X = transRect.mlLeft
                         rectF.Y = transRect.mlTop
                         rectF.Width = transRect.mlRight - transRect.mlLeft
                         rectF.Height = transRect.mlBottom - transRect.mlTop

                         'Draw the transition box
                         gfx.FillRectangle(Brushes.LightYellow, rectF)
                         gfx.DrawRectangle(Pens.Black, rectF.X, rectF.Y, rectF.Width, rectF.Height)
                         gfx.DrawString(trans.Name, font, Brushes.Black, rectF)
                     End While

                     'Loop over all workflow states
                     pos = wf.GetFirstStatePosition
                     While Not pos.IsNull
                         Dim state As IEdmState7
                         state = wf.GetNextState(pos)

                         'Get the state box
                         Dim stateRect As EdmRect
                         state.GetRect(stateRect)
                         Dim rectF As System.Drawing.RectangleF
                         rectF.X = stateRect.mlLeft
                         rectF.Y = stateRect.mlTop
                         rectF.Width = stateRect.mlRight - stateRect.mlLeft
                         rectF.Height = stateRect.mlBottom - stateRect.mlTop

                         'Draw the state box
                         gfx.FillRectangle(Brushes.Azure, rectF)
                         gfx.DrawRectangle(Pens.Black, rectF.X, rectF.Y, rectF.Width, rectF.Height)
                         gfx.DrawString(state.Name, font, Brushes.Black, rectF)
                     End While
                 End If
             End While
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try

     End Sub

     'Draw the arrow of a transition
     Private Sub PaintArrow(ByVal gfx As System.Drawing.Graphics, ByVal vertices() As EdmPoint)
         Try
             Dim points(UBound(vertices)) As System.Drawing.PointF
             Dim i As Integer
             i = LBound(vertices)
             While i <= UBound(vertices)
                 points(i).X = vertices(i).mlX
                 points(i).Y = vertices(i).mlY
                 i = i + 1
             End While

             'Draw the arrow lines
             gfx.DrawLines(Pens.DarkRed, points)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub VaultsComboBox_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles VaultsComboBox.SelectedIndexChanged
         Try
             vault1 = New EdmVault5()
             Dim vault As IEdmVault8 = DirectCast(vault1, IEdmVault8)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             ListBox1.Items.Clear()

             wfmgr = vault.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr)
             pos = wfmgr.GetFirstWorkflowPosition()
             While Not pos.IsNull
                 wf = wfmgr.GetNextWorkflow(pos)
                 ListBox1.Items.Add(wf.Name)
             End While

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub
 End Class

 Back to top
 'Form1.Designer.vb
 <Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
 Partial Class Form1
     Inherits System.Windows.Forms.Form
     ''' <summary>
     ''' Required designer variable.
     ''' </summary>
     Private components As System.ComponentModel.IContainer = Nothing

     ''' <summary>
     ''' Clean up any resources being used.
     ''' </summary>
     ''' <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
     Protected Overrides Sub Dispose(ByVal disposing As Boolean)
         If disposing AndAlso (components IsNot Nothing) Then
             components.Dispose()
         End If
         MyBase.Dispose(disposing)
     End Sub

 #Region "Windows Form Designer generated code"

     ''' <summary>
     ''' Required method for Designer support - do not modify
     ''' the contents of this method with the code editor.
     ''' </summary>
     Private Sub InitializeComponent()
         Me.VaultsLabel = New System.Windows.Forms.Label()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.GraphWorkflow = New System.Windows.Forms.Button()
         Me.ListBox1 = New System.Windows.Forms.ListBox()
         Me.Label1 = New System.Windows.Forms.Label()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(13, 26)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(94, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = " Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(16, 42)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'GraphWorkflow
         '
         Me.GraphWorkflow.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
         Me.GraphWorkflow.Location = New System.Drawing.Point(15, 199)
         Me.GraphWorkflow.Name = "GraphWorkflow"
         Me.GraphWorkflow.Size = New System.Drawing.Size(121, 23)
         Me.GraphWorkflow.TabIndex = 5
         Me.GraphWorkflow.Text = "Graph workflow"
         Me.GraphWorkflow.UseVisualStyleBackColor = True
         '
         'ListBox1
         '
         Me.ListBox1.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
         Me.ListBox1.FormattingEnabled = True
         Me.ListBox1.HorizontalScrollbar = True
         Me.ListBox1.Location = New System.Drawing.Point(15, 98)
         Me.ListBox1.Name = "ListBox1"
         Me.ListBox1.Size = New System.Drawing.Size(120, 95)
         Me.ListBox1.TabIndex = 6
         '
         'Label1
         '
         Me.Label1.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(13, 82)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(85, 13)
         Me.Label1.TabIndex = 7
         Me.Label1.Text = "Select workflow:"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(227, 262)
         Me.Controls.Add(Me.Label1)
         Me.Controls.Add(Me.ListBox1)
         Me.Controls.Add(Me.GraphWorkflow)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Graph a workflow"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents GraphWorkflow As System.Windows.Forms.Button
     Friend WithEvents ListBox1 As System.Windows.Forms.ListBox
     Friend WithEvents Label1 As System.Windows.Forms.Label

 End Class
```

[Back to top](#top)
