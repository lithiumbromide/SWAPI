---
title: "3D Interconnect to Import Third-Party Native CAD Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import3DInterconnect_Example_CSharp.htm"
---

# 3D Interconnect to Import Third-Party Native CAD Files Example (C#)

This example demonstrates how to use the 3D Interconnect API to import and access third-party non-native CAD data.

```vb
  //---------------------------------------------------------------------------
// Preconditions:
//  1. Ensure  Tools > Options > System Options > Enable VSTA VERSION 3.0 is
//     selected.
//  2. Open a new C# macro in SOLIDWORKS Design. Save it with project name
//     Interconnect to a convenient location on your machine.
//  3. Add references, SolidWorks.interop.sldworks and
 //     SolidWorks.Interop.swconst.
 //  4. Open SolidWorksMacro.cs.
 //  5. Replace everything in  SolidWorksMacro.cs with this code.
//  6. Right-click the Interconnect project in Solution Explorer and select
//     Add > Windows Form.
//  7. Save the form with name,  InterConnectingApp.cs.
//  8. Open InterConnectingApp.Designer.cs and replace everything in it
//     with this code.
//  9. Open the InterConnectingApp.cs form. Right-click on the design
//     and select View Code.
// 10. Replace everything in InterConnectingApp.cs with this code.
// 11. Compile and save the project.
//
// Postconditions:
//  1. Opens the InterConnectingApp dialog.
//  2. Select 3D Interconnect checkbox to enable 3D Interconnect.
//  3. Click one of:
//     a. Load File
//     b. Open SOLIDWORKS File
//  4. If you clicked 3b, then click one of:
 //     a. Insert as Feature (if you opened a part)
//     b. Insert as Component (if you opened an assembly)
//  5. Select the third-party non-native CAD file to insert. Click OK.
//  6. Select the top-level imported item in the FeatureManager design tree.
//  7. Exercise the buttons in the Editing Third-Party File Data group box.
//     Observe the Information text box. Click Clear to refresh it.
//  8. Click Break Link to break the link between the imported
//     feature/component and its original file.
//  9. Click  Feature, Component, or Model to list all external references.
// 10. Click Close File to close the current files.
// 11. Click Close Application to close the InterConnectingApp dialog.
//
// -------------------------------------------------------------------------

  //SolidWorksMacro.cs:
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace Interconnect
 {
      public  partial  class  SolidWorksMacro
     {
          public  void Main()
         {
             swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit,   false);
              InterConnectingApp obj =  new   InterConnectingApp();
             obj.RunInterconnectApplication(swApp);
              return;
         }

          // The SldWorks swApp variable is pre-assigned for you.
          public  SldWorks swApp;

     }
```

}

```vb
    //InterConnectingApp.Designer.cs:
```

```vb
 namespace Interconnect
 {
      partial  class  InterConnectingApp
       {
          ///  <summary>
          /// Required designer variable.
          ///  </summary>
          private System.ComponentModel.IContainer components =  null;

          ///  <summary>
          /// Clean up any resources being used.
          ///  </summary>
          ///  <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
          protected  override  void Dispose(bool disposing)
           {
              if (disposing && (components !=  null))
               {
                   components.Dispose();
               }
              base.Dispose(disposing);
           }

          #region Windows Form Designer generated code

          ///  <summary>
          /// Required method for Designer support - do not modify
          /// the contents of this method with the code editor.
          ///  </summary>
          private  void InitializeComponent()
           {
              this.groupBox1 =  new System.Windows.Forms.GroupBox();
              this.chkTurnInterconnectOnOff =  new System.Windows.Forms.CheckBox();
              this.groupBox2 =  new System.Windows.Forms.GroupBox();
              this.btnInsertComponent =  new System.Windows.Forms.Button();
              this.btnInsertFeat =  new System.Windows.Forms.Button();
              this.groupBox3 =  new System.Windows.Forms.GroupBox();
              this.btnLoadFile =  new System.Windows.Forms.Button();
              this.groupBox4 =  new System.Windows.Forms.GroupBox();
              this.groupBox8 =  new System.Windows.Forms.GroupBox();
              this.chkSolidBodies =  new System.Windows.Forms.CheckBox();
              this.chkSurfaceBodies =  new System.Windows.Forms.CheckBox();
              this.chkPlanes =  new System.Windows.Forms.CheckBox();
             this.chkAxes =  new System.Windows.Forms.CheckBox();
              this.chkSketchedAndCurves =  new System.Windows.Forms.CheckBox();
              this.btnSetParams =  new System.Windows.Forms.Button();
              this.chkMaterial =  new System.Windows.Forms.CheckBox();
              this.chkCustomProps =  new System.Windows.Forms.CheckBox();
              this.chkIgnoreHiddenBodies =  new System.Windows.Forms.CheckBox();
              this.btn_IsInterFeat =  new System.Windows.Forms.Button();
             this.btnUpdate =  new System.Windows.Forms.Button();
              this.btnAuthorInfo =  new System.Windows.Forms.Button();
              this.btnIsUpdateNeeded =  new System.Windows.Forms.Button();
              this.btnGetParams =  new System.Windows.Forms.Button();
              this.btnGetRefFileName =  new System.Windows.Forms.Button();
              this.groupBox5 =  new System.Windows.Forms.GroupBox();
              this.btnClear =  new System.Windows.Forms.Button();
              this.richTextBox1 =  new System.Windows.Forms.RichTextBox();
              this.groupBox6 =  new System.Windows.Forms.GroupBox();
              this.btnBreakLink =  new System.Windows.Forms.Button();
              this.groupBox7 =  new System.Windows.Forms.GroupBox();
              this.btnModelExtRefs =  new System.Windows.Forms.Button();
              this.btnComponentExtRef =  new System.Windows.Forms.Button();
              this.btnFeatureExtRefs =  new System.Windows.Forms.Button();
              this.btnFormOpenFile =  new System.Windows.Forms.Button();
              this.btnCloseFile =  new System.Windows.Forms.Button();
              this.btnCloseApp =  new System.Windows.Forms.Button();
              this.groupBox1.SuspendLayout();
              this.groupBox2.SuspendLayout();
              this.groupBox3.SuspendLayout();
              this.groupBox4.SuspendLayout();
              this.groupBox8.SuspendLayout();
              this.groupBox5.SuspendLayout();
              this.groupBox6.SuspendLayout();
              this.groupBox7.SuspendLayout();
```

this.SuspendLayout();

```vb
 //
              // groupBox1
              //
              this.groupBox1.Controls.Add(this.chkTurnInterconnectOnOff);
              this.groupBox1.Location =  new System.Drawing.Point(12, 12);
              this.groupBox1.Name =  "groupBox1";
              this.groupBox1.Size =  new System.Drawing.Size(148, 51);
              this.groupBox1.TabIndex = 0;
              this.groupBox1.TabStop =  false;
              this.groupBox1.Text =  "On/Off";
              //
              // chkTurnInterconnectOnOff
              //
              this.chkTurnInterconnectOnOff.AutoSize =  true;
              this.chkTurnInterconnectOnOff.Location =  new System.Drawing.Point(7, 20);
              this.chkTurnInterconnectOnOff.Name =  "chkTurnInterconnectOnOff";
              this.chkTurnInterconnectOnOff.Size =  new System.Drawing.Size(103, 17);
              this.chkTurnInterconnectOnOff.TabIndex = 0;
              this.chkTurnInterconnectOnOff.Text =  "3D Interconnect";
              this.chkTurnInterconnectOnOff.UseVisualStyleBackColor =  true;
              this.chkTurnInterconnectOnOff.CheckStateChanged +=  new System.EventHandler(this.chkTurnInterconnectOnOff_CheckStateChanged);
              //
              // groupBox2
              //
              this.groupBox2.Controls.Add(this.btnInsertComponent);
              this.groupBox2.Controls.Add(this.btnInsertFeat);
              this.groupBox2.Location =  new System.Drawing.Point(12, 166);
              this.groupBox2.Name =  "groupBox2";
              this.groupBox2.Size =  new System.Drawing.Size(148, 127);
              this.groupBox2.TabIndex = 1;
              this.groupBox2.TabStop =  false;
              this.groupBox2.Text =  "Inserting Third-Party Files";
              //
              // btnInsertComponent
              //
             this.btnInsertComponent.Location =  new System.Drawing.Point(7, 70);
              this.btnInsertComponent.Name =  "btnInsertComponent";
              this.btnInsertComponent.Size =  new System.Drawing.Size(126, 34);
              this.btnInsertComponent.TabIndex = 1;
              this.btnInsertComponent.Text =  "Insert as Component";
              this.btnInsertComponent.UseVisualStyleBackColor =  true;
              this.btnInsertComponent.Click +=  new System.EventHandler(this.btnInsertComponent_Click);
              //
              // btnInsertFeat
              //
              this.btnInsertFeat.Location =  new System.Drawing.Point(6, 32);
              this.btnInsertFeat.Name =  "btnInsertFeat";
              this.btnInsertFeat.Size =  new System.Drawing.Size(127, 32);
              this.btnInsertFeat.TabIndex = 0;
              this.btnInsertFeat.Text =  "Insert as Feature";
              this.btnInsertFeat.UseVisualStyleBackColor =  true;
              this.btnInsertFeat.Click +=  new System.EventHandler(this.btnInsertFeat_Click);
              //
              // groupBox3
              //
              this.groupBox3.Controls.Add(this.btnLoadFile);
              this.groupBox3.Location =  new System.Drawing.Point(12, 328);
              this.groupBox3.Name =  "groupBox3";
              this.groupBox3.Size =  new System.Drawing.Size(148, 81);
              this.groupBox3.TabIndex = 2;
              this.groupBox3.TabStop =  false;
              this.groupBox3.Text =  "Opening Third-Party Files";
             //
              // btnLoadFile
              //
              this.btnLoadFile.Location =  new System.Drawing.Point(7, 31);
              this.btnLoadFile.Name =  "btnLoadFile";
              this.btnLoadFile.Size =  new System.Drawing.Size(126, 23);
              this.btnLoadFile.TabIndex = 0;
              this.btnLoadFile.Text =  "Load File";
              this.btnLoadFile.UseVisualStyleBackColor =  true;
              this.btnLoadFile.Click +=  new System.EventHandler(this.btnLoadFile_Click);
              //
              // groupBox4
              //
              this.groupBox4.Controls.Add(this.groupBox8);
              this.groupBox4.Controls.Add(this.btn_IsInterFeat);
              this.groupBox4.Controls.Add(this.btnUpdate);
              this.groupBox4.Controls.Add(this.btnAuthorInfo);
              this.groupBox4.Controls.Add(this.btnIsUpdateNeeded);
              this.groupBox4.Controls.Add(this.btnGetParams);
              this.groupBox4.Controls.Add(this.btnGetRefFileName);
              this.groupBox4.Location =  new System.Drawing.Point(188, 12);
              this.groupBox4.Name =  "groupBox4";
              this.groupBox4.Size =  new System.Drawing.Size(296, 386);
              this.groupBox4.TabIndex = 3;
              this.groupBox4.TabStop =  false;
```

this.groupBox4.Text = "Editing Third-Party File Data";

```vb
 //
              // groupBox8
              //
              this.groupBox8.Controls.Add(this.chkSolidBodies);
              this.groupBox8.Controls.Add(this.chkSurfaceBodies);
              this.groupBox8.Controls.Add(this.chkPlanes);
              this.groupBox8.Controls.Add(this.chkAxes);
              this.groupBox8.Controls.Add(this.chkSketchedAndCurves);
              this.groupBox8.Controls.Add(this.btnSetParams);
              this.groupBox8.Controls.Add(this.chkMaterial);
              this.groupBox8.Controls.Add(this.chkCustomProps);
              this.groupBox8.Controls.Add(this.chkIgnoreHiddenBodies);
              this.groupBox8.Location =  new System.Drawing.Point(6, 114);
              this.groupBox8.Name =  "groupBox8";
              this.groupBox8.Size =  new System.Drawing.Size(283, 203);
              this.groupBox8.TabIndex = 16;
              this.groupBox8.TabStop =  false;
              this.groupBox8.Text =  "Import Parameters";
              //
              // chkSolidBodies
              //
              this.chkSolidBodies.AutoSize =  true;
              this.chkSolidBodies.Location =  new System.Drawing.Point(6, 30);
              this.chkSolidBodies.Name =  "chkSolidBodies";
              this.chkSolidBodies.Size =  new System.Drawing.Size(84, 17);
             this.chkSolidBodies.TabIndex = 0;
              this.chkSolidBodies.Text =  "Solid Bodies";
              this.chkSolidBodies.UseVisualStyleBackColor =  true;
              //
              // chkSurfaceBodies
              //
              this.chkSurfaceBodies.AutoSize =  true;
              this.chkSurfaceBodies.Location =  new System.Drawing.Point(141, 30);
              this.chkSurfaceBodies.Name =  "chkSurfaceBodies";
              this.chkSurfaceBodies.Size =  new System.Drawing.Size(98, 17);
              this.chkSurfaceBodies.TabIndex = 1;
              this.chkSurfaceBodies.Text =  "Surface Bodies";
              this.chkSurfaceBodies.UseVisualStyleBackColor =  true;
              //
              // chkPlanes
              //
              this.chkPlanes.AutoSize =  true;
              this.chkPlanes.Location =  new System.Drawing.Point(6, 63);
              this.chkPlanes.Name =  "chkPlanes";
              this.chkPlanes.Size =  new System.Drawing.Size(58, 17);
              this.chkPlanes.TabIndex = 2;
              this.chkPlanes.Text =  "Planes";
              this.chkPlanes.UseVisualStyleBackColor =  true;
              //
              // chkAxes
              //
              this.chkAxes.AutoSize =  true;
              this.chkAxes.Location =  new System.Drawing.Point(141, 63);
              this.chkAxes.Name =  "chkAxes";
              this.chkAxes.Size =  new System.Drawing.Size(49, 17);
              this.chkAxes.TabIndex = 3;
              this.chkAxes.Text =  "Axes";
              this.chkAxes.UseVisualStyleBackColor =  true;
              //
             // chkSketchedAndCurves
              //
              this.chkSketchedAndCurves.AutoSize =  true;
              this.chkSketchedAndCurves.Location =  new System.Drawing.Point(6, 95);
              this.chkSketchedAndCurves.Name =  "chkSketchedAndCurves";
             this.chkSketchedAndCurves.Size =  new System.Drawing.Size(129, 17);
              this.chkSketchedAndCurves.TabIndex = 4;
              this.chkSketchedAndCurves.Text =  "Sketches And Curves";
              this.chkSketchedAndCurves.UseVisualStyleBackColor =  true;
              //
              // btnSetParams
              //
              this.btnSetParams.Location =  new System.Drawing.Point(73, 154);
              this.btnSetParams.Name =  "btnSetParams";
              this.btnSetParams.Size =  new System.Drawing.Size(117, 34);
              this.btnSetParams.TabIndex = 12;
              this.btnSetParams.Text =  "Set Parameters";
              this.btnSetParams.UseVisualStyleBackColor =  true;
              this.btnSetParams.Click +=  new System.EventHandler(this.btnSetParams_Click);
              //
              // chkMaterial
              //
              this.chkMaterial.AutoSize =  true;
              this.chkMaterial.Location =  new System.Drawing.Point(141, 95);
              this.chkMaterial.Name =  "chkMaterial";
              this.chkMaterial.Size =  new System.Drawing.Size(63, 17);
              this.chkMaterial.TabIndex = 6;
              this.chkMaterial.Text =  "Material";
```

this.chkMaterial.UseVisualStyleBackColor = true;

```vb
 //
              // chkCustomProps
              //
              this.chkCustomProps.AutoSize =  true;
              this.chkCustomProps.Location =  new System.Drawing.Point(6, 131);
              this.chkCustomProps.Name =  "chkCustomProps";
              this.chkCustomProps.Size =  new System.Drawing.Size(111, 17);
              this.chkCustomProps.TabIndex = 5;
              this.chkCustomProps.Text =  "Custom Properties";
              this.chkCustomProps.UseVisualStyleBackColor =  true;
              //
              // chkIgnoreHiddenBodies
              //
              this.chkIgnoreHiddenBodies.AutoSize =  true;
              this.chkIgnoreHiddenBodies.Location =  new System.Drawing.Point(141, 131);
              this.chkIgnoreHiddenBodies.Name =  "chkIgnoreHiddenBodies";
              this.chkIgnoreHiddenBodies.Size =  new System.Drawing.Size(128, 17);
              this.chkIgnoreHiddenBodies.TabIndex = 7;
              this.chkIgnoreHiddenBodies.Text =  "Ignore Hidden Bodies";
              this.chkIgnoreHiddenBodies.UseVisualStyleBackColor =  true;
              //
              // btn_IsInterFeat
              //
              this.btn_IsInterFeat.Location =  new System.Drawing.Point(6, 19);
              this.btn_IsInterFeat.Name =  "btn_IsInterFeat";
              this.btn_IsInterFeat.Size =  new System.Drawing.Size(111, 34);
              this.btn_IsInterFeat.TabIndex = 15;
              this.btn_IsInterFeat.Text =  "Is 3D Interconnect Feature?";
              this.btn_IsInterFeat.UseVisualStyleBackColor =  true;
              this.btn_IsInterFeat.Click +=  new System.EventHandler(this.btn_IsInterFeat_Click);
              //
              // btnUpdate
              //
              this.btnUpdate.Location =  new System.Drawing.Point(147, 335);
              this.btnUpdate.Name =  "btnUpdate";
              this.btnUpdate.Size =  new System.Drawing.Size(117, 34);
              this.btnUpdate.TabIndex = 14;
              this.btnUpdate.Text =  "Update";
              this.btnUpdate.UseVisualStyleBackColor =  true;
              this.btnUpdate.Click +=  new System.EventHandler(this.btnUpdate_Click);
              //
              // btnAuthorInfo
              //
              this.btnAuthorInfo.Location =  new System.Drawing.Point(138, 70);
              this.btnAuthorInfo.Name =  "btnAuthorInfo";
              this.btnAuthorInfo.Size =  new System.Drawing.Size(132, 31);
              this.btnAuthorInfo.TabIndex = 10;
              this.btnAuthorInfo.Text =  "Show Authoring Info";
              this.btnAuthorInfo.UseVisualStyleBackColor =  true;
              this.btnAuthorInfo.Click +=  new System.EventHandler(this.btnAuthorInfo_Click);
              //
              // btnIsUpdateNeeded
              //
              this.btnIsUpdateNeeded.Location =  new System.Drawing.Point(7, 335);
              this.btnIsUpdateNeeded.Name =  "btnIsUpdateNeeded";
             this.btnIsUpdateNeeded.Size =  new System.Drawing.Size(130, 34);
              this.btnIsUpdateNeeded.TabIndex = 13;
              this.btnIsUpdateNeeded.Text =  "Needs Update?";
              this.btnIsUpdateNeeded.UseVisualStyleBackColor =  true;
              this.btnIsUpdateNeeded.Click +=  new System.EventHandler(this.btnIsUpdateNeeded_Click);
              //
              // btnGetParams
              //
              this.btnGetParams.Location =  new System.Drawing.Point(8, 68);
              this.btnGetParams.Name =  "btnGetParams";
              this.btnGetParams.Size =  new System.Drawing.Size(111, 34);
              this.btnGetParams.TabIndex = 11;
              this.btnGetParams.Text =  "Show Parameters";
              this.btnGetParams.UseVisualStyleBackColor =  true;
              this.btnGetParams.Click +=  new System.EventHandler(this.btnGetParams_Click);
              //
              // btnGetRefFileName
              //
              this.btnGetRefFileName.Location =  new System.Drawing.Point(138, 20);
              this.btnGetRefFileName.Name =  "btnGetRefFileName";
              this.btnGetRefFileName.Size =  new System.Drawing.Size(132, 33);
              this.btnGetRefFileName.TabIndex = 8;
              this.btnGetRefFileName.Text =  "Show Reference File";
              this.btnGetRefFileName.UseVisualStyleBackColor =  true;
```

this.btnGetRefFileName.Click += new System.EventHandler(this.btnGetRefFileName_Click);

```vb
    //
              // groupBox5
              //
              this.groupBox5.Controls.Add(this.btnClear);
              this.groupBox5.Controls.Add(this.richTextBox1);
              this.groupBox5.Location =  new System.Drawing.Point(499, 12);
              this.groupBox5.Name =  "groupBox5";
              this.groupBox5.Size =  new System.Drawing.Size(325, 548);
              this.groupBox5.TabIndex = 4;
              this.groupBox5.TabStop =  false;
              this.groupBox5.Text =  "Information";
              //
              // btnClear
              //
              this.btnClear.Location =  new System.Drawing.Point(120, 473);
              this.btnClear.Name =  "btnClear";
              this.btnClear.Size =  new System.Drawing.Size(103, 33);
              this.btnClear.TabIndex = 1;
              this.btnClear.Text =  "Clear";
              this.btnClear.UseVisualStyleBackColor =  true;
              this.btnClear.Click +=  new System.EventHandler(this.btnClear_Click);
              //
              // richTextBox1
              //
              this.richTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.None;
              this.richTextBox1.Location =  new System.Drawing.Point(6, 20);
              this.richTextBox1.Name =  "richTextBox1";
              this.richTextBox1.Size =  new System.Drawing.Size(313, 422);
              this.richTextBox1.TabIndex = 0;
              this.richTextBox1.Text =  "";
              //
              // groupBox6
              //
              this.groupBox6.Controls.Add(this.btnBreakLink);
              this.groupBox6.Location =  new System.Drawing.Point(12, 430);
              this.groupBox6.Name =  "groupBox6";
              this.groupBox6.Size =  new System.Drawing.Size(148, 68);
              this.groupBox6.TabIndex = 5;
              this.groupBox6.TabStop =  false;
              this.groupBox6.Text =  "Link";
              //
              // btnBreakLink
              //
              this.btnBreakLink.Location =  new System.Drawing.Point(7, 30);
              this.btnBreakLink.Name =  "btnBreakLink";
              this.btnBreakLink.Size =  new System.Drawing.Size(126, 23);
              this.btnBreakLink.TabIndex = 0;
              this.btnBreakLink.Text =  "Break Link";
              this.btnBreakLink.UseVisualStyleBackColor =  true;
              this.btnBreakLink.Click +=  new System.EventHandler(this.btnBreakLink_Click);
              //
             // groupBox7
              //
              this.groupBox7.Controls.Add(this.btnModelExtRefs);
              this.groupBox7.Controls.Add(this.btnComponentExtRef);
              this.groupBox7.Controls.Add(this.btnFeatureExtRefs);
              this.groupBox7.Location =  new System.Drawing.Point(188, 432);
              this.groupBox7.Name =  "groupBox7";
              this.groupBox7.Size =  new System.Drawing.Size(283, 66);
              this.groupBox7.TabIndex = 6;
              this.groupBox7.TabStop =  false;
              this.groupBox7.Text =  "External References";
              //
              // btnModelExtRefs
              //
              this.btnModelExtRefs.Location =  new System.Drawing.Point(188, 26);
              this.btnModelExtRefs.Name =  "btnModelExtRefs";
             this.btnModelExtRefs.Size =  new System.Drawing.Size(85, 34);
              this.btnModelExtRefs.TabIndex = 2;
              this.btnModelExtRefs.Text =  "Model";
              this.btnModelExtRefs.UseVisualStyleBackColor =  true;
              this.btnModelExtRefs.Click +=  new System.EventHandler(this.btnModelExtRefs_Click);
              //
              // btnComponentExtRef
              //
              this.btnComponentExtRef.Location =  new System.Drawing.Point(97, 26);
              this.btnComponentExtRef.Name =  "btnComponentExtRef";
              this.btnComponentExtRef.Size =  new System.Drawing.Size(85, 34);
              this.btnComponentExtRef.TabIndex = 1;
              this.btnComponentExtRef.Text =  "Component";
              this.btnComponentExtRef.UseVisualStyleBackColor =  true;
              this.btnComponentExtRef.Click +=  new System.EventHandler(this.btnComponentExtRef_Click);
              //
              // btnFeatureExtRefs
              //
              this.btnFeatureExtRefs.Location =  new System.Drawing.Point(7, 26);
              this.btnFeatureExtRefs.Name =  "btnFeatureExtRefs";
              this.btnFeatureExtRefs.Size =  new System.Drawing.Size(85, 34);
              this.btnFeatureExtRefs.TabIndex = 0;
              this.btnFeatureExtRefs.Text =  "Feature";
             this.btnFeatureExtRefs.UseVisualStyleBackColor =  true;
              this.btnFeatureExtRefs.Click +=  new System.EventHandler(this.btnFeatureExtRefs_Click);
              //
              // btnFormOpenFile
              //
              this.btnFormOpenFile.Location =  new System.Drawing.Point(12, 92);
              this.btnFormOpenFile.Name =  "btnFormOpenFile";
              this.btnFormOpenFile.Size =  new System.Drawing.Size(126, 39);
              this.btnFormOpenFile.TabIndex = 7;
              this.btnFormOpenFile.Text =  "Open SOLIDWORKS File";
              this.btnFormOpenFile.UseVisualStyleBackColor =  true;
              this.btnFormOpenFile.Click +=  new System.EventHandler(this.btnFormOpenFile_Click);
              //
              // btnCloseFile
              //
              this.btnCloseFile.Location =  new System.Drawing.Point(92, 521);
              this.btnCloseFile.Name =  "btnCloseFile";
              this.btnCloseFile.Size =  new System.Drawing.Size(103, 39);
              this.btnCloseFile.TabIndex = 8;
              this.btnCloseFile.Text =  "Close File";
              this.btnCloseFile.UseVisualStyleBackColor =  true;
              this.btnCloseFile.Click +=  new System.EventHandler(this.btnCloseFile_Click);
              //
             // btnCloseApp
              //
              this.btnCloseApp.Location =  new System.Drawing.Point(236, 521);
              this.btnCloseApp.Name =  "btnCloseApp";
              this.btnCloseApp.Size =  new System.Drawing.Size(103, 39);
              this.btnCloseApp.TabIndex = 9;
              this.btnCloseApp.Text =  "Close Application";
              this.btnCloseApp.UseVisualStyleBackColor =  true;
              this.btnCloseApp.Click +=  new System.EventHandler(this.btnCloseApp_Click);
              //
              // InterConnectingApp
              //
              this.AutoScaleDimensions =  new System.Drawing.SizeF(6F, 13F);
              this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
              this.ClientSize =  new System.Drawing.Size(842, 579);
             this.Controls.Add(this.btnCloseApp);
              this.Controls.Add(this.btnCloseFile);
              this.Controls.Add(this.btnFormOpenFile);
              this.Controls.Add(this.groupBox7);
              this.Controls.Add(this.groupBox6);
              this.Controls.Add(this.groupBox5);
              this.Controls.Add(this.groupBox4);
              this.Controls.Add(this.groupBox3);
              this.Controls.Add(this.groupBox2);
              this.Controls.Add(this.groupBox1);
              this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
              this.Name =  "InterConnectingApp";
              this.Text =  "InterConnectingApp";
              this.groupBox1.ResumeLayout(false);
              this.groupBox1.PerformLayout();
             this.groupBox2.ResumeLayout(false);
              this.groupBox3.ResumeLayout(false);
              this.groupBox4.ResumeLayout(false);
              this.groupBox8.ResumeLayout(false);
              this.groupBox8.PerformLayout();
              this.groupBox5.ResumeLayout(false);
              this.groupBox6.ResumeLayout(false);
              this.groupBox7.ResumeLayout(false);
              this.ResumeLayout(false);

           }

          #endregion

          private System.Windows.Forms.GroupBox groupBox1;
          private System.Windows.Forms.CheckBox chkTurnInterconnectOnOff;
          private System.Windows.Forms.GroupBox groupBox2;
          private System.Windows.Forms.Button btnInsertComponent;
          private System.Windows.Forms.Button btnInsertFeat;
          private System.Windows.Forms.GroupBox groupBox3;
          private System.Windows.Forms.Button btnLoadFile;
          private System.Windows.Forms.GroupBox groupBox4;
          private System.Windows.Forms.Button btnAuthorInfo;
          private System.Windows.Forms.Button btnGetRefFileName;
          private System.Windows.Forms.CheckBox chkIgnoreHiddenBodies;
          private System.Windows.Forms.CheckBox chkMaterial;
          private System.Windows.Forms.CheckBox chkCustomProps;
          private System.Windows.Forms.CheckBox chkSketchedAndCurves;
          private System.Windows.Forms.CheckBox chkAxes;
          private System.Windows.Forms.CheckBox chkPlanes;
          private System.Windows.Forms.CheckBox chkSurfaceBodies;
          private System.Windows.Forms.CheckBox chkSolidBodies;
          private System.Windows.Forms.Button btnUpdate;
          private System.Windows.Forms.Button btnIsUpdateNeeded;
          private System.Windows.Forms.Button btnSetParams;
          private System.Windows.Forms.Button btnGetParams;
          private System.Windows.Forms.GroupBox groupBox5;
          private System.Windows.Forms.RichTextBox richTextBox1;
          private System.Windows.Forms.Button btnClear;
          private System.Windows.Forms.GroupBox groupBox6;
          private System.Windows.Forms.Button btnBreakLink;
          private System.Windows.Forms.GroupBox groupBox7;
          private System.Windows.Forms.Button btnModelExtRefs;
          private System.Windows.Forms.Button btnComponentExtRef;
          private System.Windows.Forms.Button btnFeatureExtRefs;
          private System.Windows.Forms.Button btnFormOpenFile;
          private System.Windows.Forms.Button btnCloseFile;
          private System.Windows.Forms.Button btnCloseApp;
          private System.Windows.Forms.Button btn_IsInterFeat;
          private System.Windows.Forms.GroupBox groupBox8;
       }
```

}

```vb
  //InterConnectingApp.cs:
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows.Forms;
 using System.IO;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace Interconnect
 {
      public  partial  class  InterConnectingApp :  Form
       {
          public  SldWorks m_SwApp =  default(SldWorks);
         public  ModelDoc2 swModelDoc =  default(ModelDoc2);
          public  PartDoc swPart =  default(PartDoc);
          public  AssemblyDoc swAssembly =  default(AssemblyDoc);
          public  Feature swFeat =  default(Feature);
          public  Component2 swComp =  default(Component2);
          public  Import3DInterconnectData swIntrConData =  default(Import3DInterconnectData);
          public  SelectionMgr swSelMgr =  default(SelectionMgr);
          public  string strCurModelDoc =  string.Empty;
          public  int m_LongStatus;
          public  int m_Warning;
          public  bool m_BoolStatus;
          public  StringBuilder strEventData;

          delegate  void  StringArgReturningVoidDelegate(string text);

          public InterConnectingApp()
           {
               InitializeComponent();
           }

          public  void RunInterconnectApplication(SldWorks swApp)
           {
               m_SwApp = swApp;
               swModelDoc = (ModelDoc2)m_SwApp.ActiveDoc;

              if (swModelDoc !=  null)
               {
                  strCurModelDoc = swModelDoc.GetPathName();
                  string strExt =  Path.GetExtension(strCurModelDoc);

                  if (strExt.ToLower() ==  ".sldprt")
                       swPart = (PartDoc)swModelDoc;
                  else  if (strExt.ToLower() ==  ".sldasm")
                       swAssembly = (AssemblyDoc)swModelDoc;
               }

               AttachEventHandlers();
                strEventData =  new  StringBuilder();

              Application.Run(this);
           }

          public  void AttachEventHandlers()
           {
               AttachSWEvents();
           }

          public  void AttachSWEvents()
           {
               m_SwApp.Begin3DInterconnectTranslationNotify += M_SwApp_Begin3DInterconnectTranslationNotify;
               m_SwApp.End3DInterconnectTranslationNotify += M_SwApp_End3DInterconnectTranslationNotify;
           }

          public  int M_SwApp_End3DInterconnectTranslationNotify(string FileName)
           {
               strEventData = strEventData.Append("3D Interconnect translation finished");
               strEventData = strEventData.Append("\r\n");

              return 0;
           }

          public  int M_SwApp_Begin3DInterconnectTranslationNotify(string FileName)
           {
               strEventData = strEventData.Append("3D Interconnect translation started");
               strEventData = strEventData.Append("\r\n");

              return 0;
           }

          public  int BeginTranslationNotify()
           {
              int i = 0;
              return i;
           }

          //Information field
          public  void SetRichTextBoxVal(string strText)
           {
              try
               {
                  if (this.richTextBox1.InvokeRequired ==  true)
                   {
                      StringArgReturningVoidDelegate d =  new  StringArgReturningVoidDelegate(SetRichTextBoxVal);
                      this.Invoke(d,  new  object[] { strText });

                   }
                  else
                   {
                      this.richTextBox1.Text = strText;
                   }
               }
              catch (Exception e)
               {
                  MessageBox.Show(e.Message);
               }
```

}

```vb
 //Turn 3D Interconnect on and off
          private  void chkTurnInterconnectOnOff_CheckStateChanged(object sender,  EventArgs e)
           {
              if (chkTurnInterconnectOnOff.CheckState ==  CheckState.Checked)
               {
                   m_SwApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect,  true);
               }
              else  if (chkTurnInterconnectOnOff.CheckState ==  CheckState.Unchecked)
               {
                   m_SwApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect,  false);
               }
           }

          //Open a SOLIDWORKS Design document
          private  void btnFormOpenFile_Click(object sender,  EventArgs e)
           {
              OpenFileDialog m_fileOpenDlg =  new  OpenFileDialog();
                m_fileOpenDlg.Filter =  "SolidWorks File | *.sldprt; *.sldasm";
                m_fileOpenDlg.Title =  "Open SolidWorks Design File";

              string FilePath =  string.Empty;
              string FileExtension =  string.Empty;

              if (m_fileOpenDlg.ShowDialog() ==  DialogResult.OK)
               {
                   FilePath = m_fileOpenDlg.FileName;
                    FileExtension =  Path.GetExtension(FilePath);

                  if (FileExtension.ToLower() ==  ".sldasm")
                   {
                       swModelDoc = (ModelDoc2)m_SwApp.OpenDoc6(FilePath, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent,  "",  ref m_LongStatus,  ref m_Warning);
                       swAssembly = (AssemblyDoc)swModelDoc;
                   }
                  else  if (FileExtension.ToLower() ==  ".sldprt")
                   {
                      swModelDoc = (ModelDoc2)m_SwApp.OpenDoc6(FilePath, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent,  "",  ref m_LongStatus,  ref m_Warning);
                       swPart = (PartDoc)swModelDoc;
                   }
               }
           }
           //Insert third-party feature into the current part
          private  void btnInsertFeat_Click(object sender,  EventArgs e)
           {
               swModelDoc = (ModelDoc2)m_SwApp.ActiveDoc;
              if (swModelDoc !=  null) {
                 if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                   {
                      if (swPart !=  null)
                       {
                          OpenFileDialog m_fileOpenDlg =  new  OpenFileDialog();
                          //m_fileOpenDlg.Filter = "Parasolid (*.x_t; *.x_b; *.xmt_txt; *.xmt_bin) | IGES (*.igs; *.iges) | ACIS (*.sat) | STEP (*.step; *.stp) | VDAFS (*.vda) | VRML (*.wrl) | STL (*.stl) | CGR (*.cgr) | 3MF (*.3mf) | Rhino (*.3dm)";
                            m_fileOpenDlg.Title =  "Insert Third-Party Feature";

                          string FilePath =  string.Empty;

                          if (m_fileOpenDlg.ShowDialog() ==  DialogResult.OK)
                           {
                              FilePath = m_fileOpenDlg.FileName;
                               swFeat = (Feature)swPart.InsertImportedFeature(FilePath,  out m_LongStatus);
                              if (swFeat ==  null)
                                   SetRichTextBoxVal(m_LongStatus.ToString());
                           }
                       }
                   }
               }

           }

          //Insert third-party component into the current assembly
          private  void btnInsertComponent_Click(object sender,  EventArgs e)
           {
               swModelDoc = (ModelDoc2)m_SwApp.ActiveDoc;
              if (swModelDoc !=  null)
               {
                  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                      if (swAssembly !=  null)
                      {
                          OpenFileDialog m_fileOpenDlg =  new  OpenFileDialog();
                            m_fileOpenDlg.Filter =  "All Files | *.*";
                            m_fileOpenDlg.Title =  "Insert Third-Party Component";

                          string FilePath =  string.Empty;

                          if (m_fileOpenDlg.ShowDialog() ==  DialogResult.OK)
                           {
                               FilePath = m_fileOpenDlg.FileName;
                              Object InsertedComp =  null;
                              int retVal = (int)swAssembly.InsertImportedComponent(FilePath, 0, 0, 0,  out InsertedComp);
                                swComp = (InsertedComp !=  null) ? (Component2)InsertedComp :  null;
                             if (swComp ==  null)
                                   SetRichTextBoxVal(retVal.ToString());
                              else
                               {
                                   SetRichTextBoxVal(strEventData.ToString());
                                  strEventData.Length = 0;
                               }
                           }
                       }
                   }
               }
```

}

```vb
 //Open a third-party file into a new document
          private  void btnLoadFile_Click(object sender,  EventArgs e)
           {
              OpenFileDialog m_fileOpenDlg =  new  OpenFileDialog();
                m_fileOpenDlg.Filter =  "All Files | *.*";
                m_fileOpenDlg.Title =  "Open Third-Party File";

              string FilePath =  string.Empty;

              if (m_fileOpenDlg.ShowDialog() ==  DialogResult.OK)
               {
                   FilePath = m_fileOpenDlg.FileName;

                    swModelDoc = m_SwApp.LoadFile4(FilePath,  "r",  null,  ref m_LongStatus);

                  string strLoadFileError =  "";
                  if (m_LongStatus != 0)
                        strLoadFileError =  "File load error as defined in swFileLoadError_e: " + m_LongStatus.ToString();

                  StringBuilder strLoadFileInfo =  new  StringBuilder();
                   strLoadFileInfo = strLoadFileInfo.Append(strLoadFileError);

                  strLoadFileInfo = strLoadFileInfo.Append("\r\n");
                   strLoadFileInfo = strLoadFileInfo.Append(strEventData.ToString());
                   SetRichTextBoxVal(strLoadFileInfo.ToString());
                   strEventData.Length = 0;

                  if (swModelDoc !=  null)
                   {
                      string strModelName = swModelDoc.GetPathName();
                      string strExt =  Path.GetExtension(strModelName);

                      if (strExt.ToLower() ==  ".sldprt")
                          swPart = (PartDoc)swModelDoc;
                      else  if (strExt.ToLower() ==  ".sldasm")
                           swAssembly = (AssemblyDoc)swModelDoc;
                   }
               }
           }

          private  void btnCloseApp_Click(object sender,  EventArgs e)
           {
              Application.Exit();
           }

          private  void btnCloseFile_Click(object sender,  EventArgs e)
           {
               m_SwApp.CloseDoc(strCurModelDoc);
           }

          //Get whether the selected feature is a 3D Interconnect feature
          private  void btn_IsInterFeat_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

                    m_BoolStatus =  false;

                  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                   {
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                      if (swFeat !=  null)
                          m_BoolStatus = swFeat.Is3DInterconnectFeature;
                      else
                          MessageBox.Show("No feature selected");
                   }
                  else  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                      object objSelected = swSelMgr.GetSelectedObject6(1, -1);
                      string strSelectedObjName;
                      string sType;
                      int iType;
                        swSelMgr.GetSelectByIdSpecification(objSelected,  out strSelectedObjName,  out sType,  out iType);
                       swAssembly = (AssemblyDoc)swModelDoc;
                      if (strSelectedObjName.Length > 0)
                       {
                         string[] vNames = strSelectedObjName.Split('@');
                           swFeat = (Feature)swAssembly.FeatureByName(vNames[0]);

                          if (swFeat ==  null && (iType != 22 || iType != 76))
                               swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

                          if (swFeat !=  null)
                               m_BoolStatus = swFeat.Is3DInterconnectFeature;
                          else
                              MessageBox.Show("No feature selected");
                       }
                   }

                  if (m_BoolStatus ==  false)
                       SetRichTextBoxVal("This is NOT a 3D Interconnect feature");
                  else
                       SetRichTextBoxVal("This is a 3D Interconnect feature");
               }
           }

          private  void btnClear_Click(object sender,  EventArgs e)
           {
               SetRichTextBoxVal("");
           }

          //Show the selected item's reference file name
          private  void btnGetRefFileName_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
                   swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                 if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      object DataObj =  null;
                       swFeat.GetImportedFeatureParameters(out DataObj);
                       swIntrConData = (Import3DInterconnectData)DataObj;

                      if (swIntrConData !=  null)
                       {
                           SetRichTextBoxVal(swIntrConData.GetReferencedFileName());
                       }
                   }
               }
           }

          //Show the selected item's authoring application
          private  void btnAuthorInfo_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
                  swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                  if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      object DataObj =  null;
                       swFeat.GetImportedFeatureParameters(out DataObj);
                       swIntrConData = (Import3DInterconnectData)DataObj;

                      if (swIntrConData !=  null)
                       {

                           SetRichTextBoxVal(swIntrConData.GetAuthoringInfo());
                       }
                  }
               }
           }

          //Show the import settings
          private  void btnGetParams_Click(object sender,  EventArgs e)
           {
              StringBuilder strBld =  new  StringBuilder();
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

                  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                  else  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                      object objSelected = swSelMgr.GetSelectedObject6(1, -1);
                      string strSelectedObjName, sType;
                      int iType;
                        swSelMgr.GetSelectByIdSpecification(objSelected,  out strSelectedObjName,  out sType,  out iType);
                       swAssembly = (AssemblyDoc)swModelDoc;
                      if (strSelectedObjName.Length > 0)
                       {
                          string[] vNames = strSelectedObjName.Split('@');
                           swFeat = (Feature)swAssembly.FeatureByName(vNames[0]);

                          if (swFeat ==  null && (iType != 22 || iType != 76))
                               swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                       }
                   }

                  if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      object DataObj =  null;
                       swFeat.GetImportedFeatureParameters(out DataObj);
                       swIntrConData = (Import3DInterconnectData)DataObj;

                      if (swIntrConData !=  null)
                       {
                          if (swIntrConData.SolidBodies ==  true)
                           {
                               strBld = strBld.Append("Solid Bodies"); strBld = strBld.Append("\r\n");
                           }
                          if (swIntrConData.SurfaceBodies ==  true)
                          {
                               strBld = strBld.Append("Surface Bodies"); strBld = strBld.Append("\r\n");
                           }
                          if (swIntrConData.Planes ==  true)
                           {
                              strBld = strBld.Append("Planes"); strBld = strBld.Append("\r\n");
                           }
                          if (swIntrConData.Axes ==  true)
                           {
                               strBld = strBld.Append("Axes"); strBld = strBld.Append("\r\n");
                           }
                          if (swIntrConData.SketchesAndCurves ==  true)
                           {
                               strBld = strBld.Append("Sketches And Curves"); strBld = strBld.Append("\r\n");
                          }
                          if (swIntrConData.CustomProperties ==  true)
                           {
                               strBld = strBld.Append("Custom Properties"); strBld = strBld.Append("\r\n");
                           }
                          if (swIntrConData.Material ==  true)
                           {
                               strBld = strBld.Append("Material"); strBld = strBld.Append("\r\n");
                           }
                          if (swIntrConData.IgnoreHiddenEntities ==  true)
                           {
                               strBld = strBld.Append("Ignore Hidden Entities"); strBld = strBld.Append("\r\n");
                           }

                           SetRichTextBoxVal(strBld.ToString());
                       }
                   }
               }
```

}

```vb
 //Set new import settings
          private  void btnSetParams_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

                  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                  else  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                      object objSelected = swSelMgr.GetSelectedObject6(1, -1);
                      string strSelectedObjName, sType;
                      int iType;
                        swSelMgr.GetSelectByIdSpecification(objSelected,  out strSelectedObjName,  out sType,  out iType);
                       swAssembly = (AssemblyDoc)swModelDoc;
                      if (strSelectedObjName.Length > 0)
                       {
                         string[] vNames = strSelectedObjName.Split('@');
                           swFeat = (Feature)swAssembly.FeatureByName(vNames[0]);

                          if (swFeat ==  null && (iType != 22 || iType != 76))
                               swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                       }
                   }

                  if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      object DataObj =  null;
                       swFeat.GetImportedFeatureParameters(out DataObj);
                       swIntrConData = (Import3DInterconnectData)DataObj;

                      if (swIntrConData !=  null)
                       {
                          if (chkSolidBodies.CheckState ==  CheckState.Checked)
                                swIntrConData.SolidBodies =  true;
                          else
                                swIntrConData.SolidBodies =  false;

                          if (chkSurfaceBodies.CheckState ==  CheckState.Checked)
                              swIntrConData.SurfaceBodies =  true;
                          else
                                swIntrConData.SurfaceBodies =  false;

                          if (chkPlanes.CheckState ==  CheckState.Checked)
                                swIntrConData.Planes =  true;
                          else
                                swIntrConData.Planes =  false;

                          if (chkAxes.CheckState ==  CheckState.Checked)
                                swIntrConData.Axes =  true;
                          else
                                swIntrConData.Axes =  false;

                          if (chkSketchedAndCurves.CheckState ==  CheckState.Checked)
                                swIntrConData.SketchesAndCurves =  true;
                         else
                                swIntrConData.SketchesAndCurves =  false;

                          if (chkCustomProps.CheckState ==  CheckState.Checked)
                                swIntrConData.CustomProperties =  true;
                         else
                                swIntrConData.CustomProperties =  false;

                          if (chkMaterial.CheckState ==  CheckState.Checked)
                                swIntrConData.Material =  true;
                          else
                                swIntrConData.Material =  false;

                          if (chkIgnoreHiddenBodies.CheckState ==  CheckState.Checked)
                                swIntrConData.IgnoreHiddenEntities =  true;
                          else
                                swIntrConData.IgnoreHiddenEntities =  false;

                           m_LongStatus = swFeat.SetImportedFeatureParameters(swIntrConData);

                          if (m_LongStatus != 0)
                           {
                              SetRichTextBoxVal("Error setting import parameters as defined in sw3DInterconnectImportErrors_e: " + m_LongStatus.ToString());
                           }

                       }
                   }
               }
           }

          //Get whether the selected 3D Interconnect item needs an update
          private  void btnIsUpdateNeeded_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

                 if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                  else  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                     object objSelected = swSelMgr.GetSelectedObject6(1, -1);
                      string strSelectedObjName, sType;
                      int iType;
                        swSelMgr.GetSelectByIdSpecification(objSelected,  out strSelectedObjName,  out sType,  out iType);
                       swAssembly = (AssemblyDoc)swModelDoc;
                      if (strSelectedObjName.Length > 0)
                       {
                          string[] vNames = strSelectedObjName.Split('@');
                           swFeat = (Feature)swAssembly.FeatureByName(vNames[0]);

                          if (swFeat ==  null && (iType != 22 || iType != 76))
                               swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                       }
                   }

                 if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      if (swFeat.Is3DInterconnectUpdateAvailable ==  true)
                           SetRichTextBoxVal("Need to update");
                      else
                          SetRichTextBoxVal("No update needed");
                   }
               }
           }

          //Update the selected 3D Interconnect item
          private  void btnUpdate_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

                  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                  else  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                      object objSelected = swSelMgr.GetSelectedObject6(1, -1);
                      string strSelectedObjName, sType;
                      int iType;
                      swSelMgr.GetSelectByIdSpecification(objSelected,  out strSelectedObjName,  out sType,  out iType);
                       swAssembly = (AssemblyDoc)swModelDoc;
                      if (strSelectedObjName.Length > 0)
                       {
                         string[] vNames = strSelectedObjName.Split('@');
                           swFeat = (Feature)swAssembly.FeatureByName(vNames[0]);

                          if (swFeat ==  null && (iType != 22 || iType != 76))
                               swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                       }
                   }

                  if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      bool isUpdated = swFeat.Update3DInterconnectModel();
                     if (isUpdated)
                           SetRichTextBoxVal("Updated");
                      else
                           SetRichTextBoxVal("Error during update");
                   }
               }
```

}

```vb
 //Break the link between the selected item and its original file
          private  void btnBreakLink_Click(object sender,  EventArgs e)
           {
              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

                  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                  else  if (swModelDoc.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
                   {
                     object objSelected = swSelMgr.GetSelectedObject6(1, -1);
                      string strSelectedObjName, sType;
                      int iType;
                        swSelMgr.GetSelectByIdSpecification(objSelected,  out strSelectedObjName,  out sType,  out iType);
                       swAssembly = (AssemblyDoc)swModelDoc;
                      if (strSelectedObjName.Length > 0)
                       {
                          string[] vNames = strSelectedObjName.Split('@');
                           swFeat = (Feature)swAssembly.FeatureByName(vNames[0]);

                          if (swFeat ==  null && (iType != 22 || iType != 76))
                               swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                       }
                   }

                  if ((swFeat !=  null) & (swFeat.Is3DInterconnectFeature))
                   {
                      bool Silent =  false;  bool allComp =  false;

                      DialogResult dRes =  MessageBox.Show("Silent?",  "Want Silent",  MessageBoxButtons.YesNo);
                      switch (dRes)
                       {
                          case  DialogResult.Yes:
                               {
                                    Silent =  true;
                                  break;
                               }
                         case  DialogResult.No:
                               {
                                    Silent =  false;
                                  break;
                               }
                       }

                      DialogResult dRes1 =  MessageBox.Show("All Components?",  "All Comp",  MessageBoxButtons.YesNo);
                      switch (dRes1)
                       {
                          case  DialogResult.Yes:
                               {
                                    allComp =  true;
                                 break;
                               }
                          case  DialogResult.No:
                               {
                                    allComp =  false;
                                  break;
                               }
                       }

                      int lError = swFeat.BreakLink(allComp, Silent);
                      string inp =  "Break Link Error" + lError.ToString();
                       SetRichTextBoxVal(inp);
                   }
               }
           }

          private  void btnFeatureExtRefs_Click(object sender,  EventArgs e)
           {
              object vModelPathName =  null;
              object vComponentPathName =  null;
              object vFeature =  null;
              object vDataType =  null;
              object vStatus =  null;
              object vRefEntity =  null;
              object vFeatComp =  null;
              int nConfigOpt = 0;
              string sConfigName =  null;
              int nRefCount = 0;
              int nSelType = 0;
              int i = 0;

             if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
                   nSelType = swSelMgr.GetSelectedObjectType3(1, -1);

                  if (nSelType != (int)swSelectType_e.swSelCOMPONENTS && nSelType != 0)
                   {
                       swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
                       nRefCount = swFeat.ListExternalFileReferencesCount();
                       swFeat.ListExternalFileReferences2(out vModelPathName,  out vComponentPathName,  out vFeature,  out vDataType,  out vStatus,  out vRefEntity,  out vFeatComp,  out nConfigOpt,  out sConfigName);

                      if (nRefCount >= 1)
                       {
                          object[] ModelPathName =  new  object[nRefCount - 1];
                          object[] ComponentPathName =  new  object[nRefCount - 1];
                          object[] Feature =  new  object[nRefCount - 1];
                          object[] DataType =  new  object[nRefCount - 1];
                          int[] Status =  new  int[nRefCount - 1];
                          object[] RefEntity =  new  object[nRefCount - 1];
                          object[] FeatComp =  new  object[nRefCount - 1];

                           ModelPathName = (object[])vModelPathName;
                           ComponentPathName = (object[])vComponentPathName;
                           Feature = (object[])vFeature;
                           DataType = (object[])vDataType;
                           Status = (int[])vStatus;
                          RefEntity = (object[])vRefEntity;
                           FeatComp = (object[])vFeatComp;

                          StringBuilder sb =  new  StringBuilder();

                          for (i = 0; i <= nRefCount - 1; i++)
                          {
                               sb = sb.Append("=>"); sb = sb.Append("Reference Count = "); sb = sb.Append(nRefCount.ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append(" "); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Model path + name = "); sb = sb.Append(ModelPathName[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Component path + name = "); sb = sb.Append(ComponentPathName[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Feature = "); sb = sb.Append(Feature[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Data type = "); sb = sb.Append(DataType[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Status = "); sb = sb.Append(System.Convert.ToString(Status[i])); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Reference entity = "); sb = sb.Append(RefEntity[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Feature component = "); sb = sb.Append(FeatComp[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Config option = "); sb = sb.Append(nConfigOpt.ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Config name = "); sb = sb.Append(sConfigName); sb = sb.Append("\r\n");

                               SetRichTextBoxVal(sb.ToString());
                           }
                       }
                   }
               }
```

}

```vb
 private  void btnComponentExtRef_Click(object sender,  EventArgs e)
           {
              object vModelPathName =  null;
              object vComponentPathName =  null;
              object vFeature =  null;
              object vDataType =  null;
              object vStatus =  null;
              object vRefEntity =  null;
              object vFeatComp =  null;
              int nConfigOpt = 0;
              string sConfigName =  null;
              int nRefCount = 0;
             int nSelType = 0;
              int i = 0;

              if (swModelDoc !=  null)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
                   nSelType = swSelMgr.GetSelectedObjectType3(1, -1);

                  if (nSelType == (int)swSelectType_e.swSelCOMPONENTS)
                   {
                       swComp = (Component2)swSelMgr.GetSelectedObject6(1, -1);
                       nRefCount = swComp.ListExternalFileReferencesCount();
                       swComp.ListExternalFileReferences2(out vModelPathName,  out vComponentPathName,  out vFeature,  out vDataType,  out vStatus,  out vRefEntity,  out vFeatComp,  out nConfigOpt,  out sConfigName);

                      if (nRefCount >= 1)
                       {
                          object[] ModelPathName =  new  object[nRefCount - 1];
                          object[] ComponentPathName =  new  object[nRefCount - 1];
                          object[] Feature =  new  object[nRefCount - 1];
                          object[] DataType =  new  object[nRefCount - 1];
                          int[] Status =  new  int[nRefCount - 1];
                          object[] RefEntity =  new  object[nRefCount - 1];
                          object[] FeatComp =  new  object[nRefCount - 1];

                           ModelPathName = (object[])vModelPathName;
                           ComponentPathName = (object[])vComponentPathName;
                           Feature = (object[])vFeature;
                           DataType = (object[])vDataType;
                           Status = (int[])vStatus;
                           RefEntity = (object[])vRefEntity;
                           FeatComp = (object[])vFeatComp;

                          StringBuilder sb =  new  StringBuilder();

                          for (i = 0; i <= nRefCount - 1; i++)
                          {
                               sb = sb.Append("=>"); sb = sb.Append("Reference Count = "); sb = sb.Append(nRefCount.ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append(" "); sb = sb.Append("\r\n");
                              sb = sb.Append("=>"); sb = sb.Append("Model path + name = "); sb = sb.Append(ModelPathName[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Component path + name = "); sb = sb.Append(ComponentPathName[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Feature = "); sb = sb.Append(Feature[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Data type = "); sb = sb.Append(DataType[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Status = "); sb = sb.Append(System.Convert.ToString(Status[i])); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Reference entity = "); sb = sb.Append(RefEntity[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Feature component = "); sb = sb.Append(FeatComp[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Config option = "); sb = sb.Append(nConfigOpt.ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Config name = "); sb = sb.Append(sConfigName); sb = sb.Append("\r\n");

                               SetRichTextBoxVal(sb.ToString());
                           }
                       }
                   }
                  else
                      SetRichTextBoxVal("This is not a component");
               }
           }

          private  void btnModelExtRefs_Click(object sender,  EventArgs e)
           {
              object vModelPathName =  null;
              object vComponentPathName =  null;
              object vFeature =  null;
              object vDataType =  null;
              object vStatus =  null;
              object vRefEntity =  null;
              object vFeatComp =  null;
              int nConfigOpt = 0;
              string sConfigName =  null;
              int nRefCount = 0;
              int nSelType = 0;
              int i = 0;

              if (swModelDoc !=  null && swModelDoc.GetType() == (int)swDocumentTypes_e.swDocPART)
               {
                   swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
                   nSelType = swSelMgr.GetSelectedObjectType3(1, -1);

                  if (nSelType != (int)swSelectType_e.swSelCOMPONENTS)
                   {
                       nRefCount = swModelDoc.Extension.ListExternalFileReferencesCount();
                      swModelDoc.Extension.ListExternalFileReferences(out vModelPathName,  out vComponentPathName,  out vFeature,  out vDataType,  out vStatus,  out vRefEntity,  out vFeatComp,  out nConfigOpt,  out sConfigName);

                      if (nRefCount >= 1)
                      {
                          object[] ModelPathName =  new  object[nRefCount - 1];
                          object[] ComponentPathName =  new  object[nRefCount - 1];
                          object[] Feature =  new  object[nRefCount - 1];
                          object[] DataType =  new  object[nRefCount - 1];
                          int[] Status =  new  int[nRefCount - 1];
                          object[] RefEntity =  new  object[nRefCount - 1];
                          object[] FeatComp =  new  object[nRefCount - 1];

                           ModelPathName = (object[])vModelPathName;
                           ComponentPathName = (object[])vComponentPathName;
                           Feature = (object[])vFeature;
                           DataType = (object[])vDataType;
                           Status = (int[])vStatus;
                           RefEntity = (object[])vRefEntity;
                           FeatComp = (object[])vFeatComp;

                          StringBuilder sb =  new  StringBuilder();

                         for (i = 0; i <= nRefCount - 1; i++)
                           {
                               sb = sb.Append("=>"); sb = sb.Append("Reference Count = "); sb = sb.Append(nRefCount.ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append(" "); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Model path + name = "); sb = sb.Append(ModelPathName[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Component path + name = "); sb = sb.Append(ComponentPathName[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Feature = "); sb = sb.Append(Feature[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Data type = "); sb = sb.Append(DataType[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Status = "); sb = sb.Append(System.Convert.ToString(Status[i])); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Reference entity = "); sb = sb.Append(RefEntity[i].ToString()); sb = sb.Append("\r\n");
                              sb = sb.Append("=>"); sb = sb.Append("Feature component = "); sb = sb.Append(FeatComp[i].ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Config option = "); sb = sb.Append(nConfigOpt.ToString()); sb = sb.Append("\r\n");
                               sb = sb.Append("=>"); sb = sb.Append("Config name = "); sb = sb.Append(sConfigName); sb = sb.Append("\r\n");

                               SetRichTextBoxVal(sb.ToString());
                          }
                       }
                   }
               }
           }

       }
```

}
