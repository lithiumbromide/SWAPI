---
title: "Graph a Workflow Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Graph_Workflow_Example_CSharp.htm"
---

# Graph a Workflow Example (C#)

This example shows how to graph a workflow.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type PaintWorkflowGraph_CSharp in Project name.
  // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9.  Add dependencies and safely pass arrays of structures.
 //10. Replace the code in Form1.cs with this code.
 //11. To create the form, replace the code in Form1.Designer.cs with this code.
 //12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Graph a workflow dialog box.
 // 2. Maximize the dialog box for the workflow graph.
 // 3. Select a vault view.
 // 4. Click a workflow.
 // 5. Click Graph workflow.
 // 6. Graphs the selected workflow in the dialog box.
  // 7. Close the Graph a workflow dialog box.
  //----------------------------------------------------------------------------

 //Form1.cs

 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace PaintWorkflowGraph_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         IEdmVault5 vault1 = null;
         IEdmWorkflow6 wf;
         IEdmWorkflowMgr6 wfmgr;
         IEdmPos5 pos;

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

         public void GraphWorkflow_Click(System.Object sender, System.EventArgs e)
         {
             //Graph workflow
             try
             {
                 IEdmVault7 vault2 = default(IEdmVault7);
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 //Retrieve the graphics interface of this window
                 System.Drawing.Graphics gfx = default(System.Drawing.Graphics);
                 gfx = this.CreateGraphics();
                 gfx.Clear(Color.AliceBlue);

                 //Create font with which to draw text
                 System.Drawing.Font font = default(System.Drawing.Font);
                 font = new System.Drawing.Font("Arial", 10, FontStyle.Bold);

                 //Loop over all the workflows to find the selected workflow
                 pos = wfmgr.GetFirstWorkflowPosition();
                 while (!pos.IsNull)
                 {
                     wf = wfmgr.GetNextWorkflow(pos);

                     if ((wf.Name == ListBox1.SelectedItem.ToString()))
                     {
                         //Loop over all workflow transitions
                         pos = default(IEdmPos5);
                         pos = wf.GetFirstTransitionPosition();
                         while (!pos.IsNull)
                         {
                             IEdmTransition7 trans = default(IEdmTransition7);
                             trans = (IEdmTransition7)wf.GetNextTransition(pos);

                             //Draw the arrow of the transition
                             EdmPoint[] vertices = null;
                             vertices = null;
                             trans.GetArrowVertices(out vertices);
                             PaintArrow(gfx, vertices);

                             //Get the transition box
                             EdmRect transRect = default(EdmRect);
                             trans.GetRect(out transRect);
                             System.Drawing.RectangleF rectF = default(System.Drawing.RectangleF);
                             rectF.X = transRect.mlLeft;
                             rectF.Y = transRect.mlTop;
                             rectF.Width = transRect.mlRight - transRect.mlLeft;
                             rectF.Height = transRect.mlBottom - transRect.mlTop;

                             //Draw the transition box
                             gfx.FillRectangle(Brushes.LightYellow, rectF);
                             gfx.DrawRectangle(Pens.Black, rectF.X, rectF.Y, rectF.Width, rectF.Height);
                             gfx.DrawString(trans.Name, font, Brushes.Black, rectF);
                         }

                         //Loop over all workflow states
                         pos = wf.GetFirstStatePosition();
                         while (!pos.IsNull)
                         {
                             IEdmState7 state = default(IEdmState7);
                             state = (IEdmState7)wf.GetNextState(pos);

                             //Get the state box
                             EdmRect stateRect = default(EdmRect);
                             state.GetRect(out stateRect);
                             System.Drawing.RectangleF rectF = default(System.Drawing.RectangleF);
                             rectF.X = stateRect.mlLeft;
                             rectF.Y = stateRect.mlTop;
                             rectF.Width = stateRect.mlRight - stateRect.mlLeft;
                             rectF.Height = stateRect.mlBottom - stateRect.mlTop;

                             //Draw the state box
                             gfx.FillRectangle(Brushes.Azure, rectF);
                             gfx.DrawRectangle(Pens.Black, rectF.X, rectF.Y, rectF.Width, rectF.Height);
                             gfx.DrawString(state.Name, font, Brushes.Black, rectF);
                         }
                     }
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

         //Draw the arrow of a transition
         private void PaintArrow(System.Drawing.Graphics gfx, EdmPoint[] vertices)
         {
             try
             {
                 System.Drawing.PointF[] points = new System.Drawing.PointF[vertices.GetUpperBound(0) + 1];
                 int i = 0;
                 i = vertices.GetLowerBound(0);
                 while (i <= vertices.GetUpperBound(0))
                 {
                     points[i].X = vertices[i].mlX;
                     points[i].Y = vertices[i].mlY;
                     i = i + 1;
                 }

                 //Draw the arrow lines
                 gfx.DrawLines(Pens.DarkRed, points);

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

         private void VaultsComboBox_SelectedIndexChanged(object sender, EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
                 IEdmVault8 vault = (IEdmVault8)vault1;

                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 ListBox1.Items.Clear();

                 wfmgr = (IEdmWorkflowMgr6)vault.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr);
                 pos = wfmgr.GetFirstWorkflowPosition();
                 while (!pos.IsNull)
                 {
                     wf = wfmgr.GetNextWorkflow(pos);
                     ListBox1.Items.Add(wf.Name);
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
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace PaintWorkflowGraph_CSharp
 {
     partial class Form1
     {
         /// <summary>
         /// Required designer variable.
         /// </summary>
         private System.ComponentModel.IContainer components = null;

         /// <summary>
         /// Clean up any resources being used.
         /// </summary>
         /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
         protected override void Dispose(bool disposing)
         {
             if (disposing && (components != null))
             {
                 components.Dispose();
             }
             base.Dispose(disposing);
         }

         #region Windows Form Designer generated code

         /// <summary>
         /// Required method for Designer support - do not modify
         /// the contents of this method with the code editor.
         /// </summary>
         private void InitializeComponent()
         {
             this.VaultsLabel = new System.Windows.Forms.Label();
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.GraphWorkflow = new System.Windows.Forms.Button();
             this.ListBox1 = new System.Windows.Forms.ListBox();
             this.Label1 = new System.Windows.Forms.Label();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(94, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = " Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(16, 42);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // GraphWorkflow
             //
             this.GraphWorkflow.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
             this.GraphWorkflow.Location = new System.Drawing.Point(15, 199);
             this.GraphWorkflow.Name = "GraphWorkflow";
             this.GraphWorkflow.Size = new System.Drawing.Size(121, 23);
             this.GraphWorkflow.TabIndex = 5;
             this.GraphWorkflow.Text = "Graph workflow";
             this.GraphWorkflow.UseVisualStyleBackColor = true;
             this.GraphWorkflow.Click += new System.EventHandler(this.GraphWorkflow_Click);
             //
             // ListBox1
             //
             this.ListBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
             this.ListBox1.FormattingEnabled = true;
             this.ListBox1.HorizontalScrollbar = true;
             this.ListBox1.Location = new System.Drawing.Point(15, 98);
             this.ListBox1.Name = "ListBox1";
             this.ListBox1.Size = new System.Drawing.Size(120, 95);
             this.ListBox1.TabIndex = 6;
             //
             // Label1
             //
             this.Label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
             this.Label1.AutoSize = true;
             this.Label1.Location = new System.Drawing.Point(13, 82);
             this.Label1.Name = "Label1";
             this.Label1.Size = new System.Drawing.Size(85, 13);
             this.Label1.TabIndex = 7;
             this.Label1.Text = "Select workflow:";
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(227, 262);
             this.Controls.Add(this.Label1);
             this.Controls.Add(this.ListBox1);
             this.Controls.Add(this.GraphWorkflow);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Graph a workflow";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button GraphWorkflow;
         internal System.Windows.Forms.ListBox ListBox1;
         internal System.Windows.Forms.Label Label1;
     }
 }
```

[Back to top](#top)
