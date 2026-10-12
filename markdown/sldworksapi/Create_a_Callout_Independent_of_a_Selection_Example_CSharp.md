---
title: "Create a Callout Independent of a Selection Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm"
---

# Create a Callout Independent of a Selection Example (C#)

This example shows how to create a callout that is independent of a selection.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document.
 // 2. Click Project > Add Reference > SolidWorks.interop.swpublished
 //    on the .NET tab.
 // 3. Rename the namespace of this macro to match the name of your C# project.
 //
 // Postconditions:
 // 1. Creates a callout with the specified properties.
 // 2. Inspect the Immediate window for its text format properties.
 //--------------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swpublished;
 using System.Diagnostics;
 namespace CreateCallout_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 swModel;
         ModelDocExtension swExt;
         SelectionMgr swSelMgr;
         MathUtility mathUtil;
         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             mathUtil = (MathUtility)swApp.GetMathUtility();
             calloutHandler handle = new calloutHandler();
             MathPoint mp;
             double[] vPnt = new double[3];
             vPnt[0] = 0.0;
             vPnt[1] = 0.0;
             vPnt[2] = 0.0;
             mp = (MathPoint)mathUtil.CreatePoint(vPnt);
             Callout myCallout;
             myCallout = swExt.CreateCallout(2, handle);
             myCallout.set_Value(1,  "");
             myCallout.set_IgnoreValue(1,  true);
             myCallout.set_Label2(1,  "SldWorks API");
             myCallout.SkipColon =  true;
             myCallout.SetLeader(true, true);
             myCallout.SetTargetPoint(1, 0.001, 0.001, 0);
             myCallout.SetTargetPoint(2, -0.001, 0.001, 0);
             myCallout.Position = mp;
             myCallout.set_ValueInactive(0,  true);
             myCallout.TextBox =  false;
             myCallout.Display(true);
            TextFormat swTextFormat = myCallout.TextFormat;
             ProcessTextFormat(swApp, swModel, swTextFormat);
         }
        public  void ProcessTextFormat(SldWorks swApp, ModelDoc2 swModel, TextFormat swTextFormat)
         {

            Debug.Print("    BackWards                    = " + swTextFormat.BackWards);
            Debug.Print("    Bold                         = " + swTextFormat.Bold);
            Debug.Print("    CharHeight                   = " + swTextFormat.CharHeight);
            Debug.Print("    CharHeightInPts              = " + swTextFormat.CharHeightInPts);
            Debug.Print("    CharSpacingFactor            = " + swTextFormat.CharSpacingFactor);
            Debug.Print("    Escapement                   = " + swTextFormat.Escapement);
            Debug.Print("    IsHeightSpecifiedInPts       = " + swTextFormat.IsHeightSpecifiedInPts());
            Debug.Print("    Italic                       = " + swTextFormat.Italic);
            Debug.Print("    LineLength                   = " + swTextFormat.LineLength);
            Debug.Print("    LineSpacing                  = " + swTextFormat.LineSpacing);
            Debug.Print("    ObliqueAngle                 = " + swTextFormat.ObliqueAngle);
            Debug.Print("    Strikeout                    = " + swTextFormat.Strikeout);
            Debug.Print("    TypeFaceName                 = " + swTextFormat.TypeFaceName);
            Debug.Print("    Underline                    = " + swTextFormat.Underline);
            Debug.Print("    UpsideDown                   = " + swTextFormat.UpsideDown);
            Debug.Print("    Vertical                     = " + swTextFormat.Vertical);
            Debug.Print("    WidthFactor                  = " + swTextFormat.WidthFactor);
            Debug.Print("");
        }

         public SldWorks swApp;
     }
     [System.Runtime.InteropServices.ComVisible(true)]
     public class calloutHandler : SwCalloutHandler
     {
         #region ISwCalloutHandler Members
         bool ISwCalloutHandler.OnStringValueChanged(object pManipulator, int RowID, string Text)
         {
             Debug.Print("Text: " + Text);
             Debug.Print("Row: " + RowID.ToString());
             return true;
         }
         #endregion
     }
 }
```
