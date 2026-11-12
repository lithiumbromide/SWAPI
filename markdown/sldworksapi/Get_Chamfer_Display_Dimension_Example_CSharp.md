---
title: "Get Chamfer Display Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Display_Dimension_Example_CSharp.htm"
---

# Get Chamfer Display Dimension Example (C#)

This example shows how to get chamfer display dimension properties. This example also shows how to set and get lower display dimension text.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
// 2. Create a drawing from the part:
//    a. File > Make Drawing from Part.
//    b. Drag and drop the isometric view onto the sheet.
// 3. Create a chamfer display dimension.
//    a. Select Tools > Dimensions > Chamfer.
//    b. Select a chamfer edge.
//    c. Select a leading edge.
//    d. Click outside the part to place the display dimension.
//    e. Modify display dimension text in the PropertyManager:
//         1. In Dimension Text, click before <DIM>.
//         2. Select the diameter symbol.
//         3. Click after <DIM>.
//         4. Select the +/- symbol.
//         5. Type 0.5.
//         6. On the Other tab, select Override Units.
//         7. Click the green check mark to accept the
//            display dimension.
// 4. Open an Immediate Window.
// 5. Rename the namespace of this macro to match your C#
//    project name.
// 6. Run the macro.
//
// Postconditions: Inspect the Immediate Window and the
// display dimension in the graphics area.
//
// NOTE: Because the part document is used elsewhere,
// do not save any changes when closing it.
//-------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace ChamferDisplayDimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         DisplayDimension swDispDim;
         bool bRet;
         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             bRet = swModel.Extension.SelectByID2("RD1@Drawing View1",  "DIMENSION", 0.4935677398765, 0.3280800260301, 0, false, 0, null, 0);
             swDispDim = (DisplayDimension)swSelMgr.GetSelectedObject6(1, 0);
             swModel.ClearSelection2(true);

             Debug.Print("Dimension type as defined in swDimensionType_e: " + swDispDim.Type2);
             //10=swChamferDimension
             Debug.Print("");
             Debug.Print("Uses document units? " + swDispDim.GetUseDocUnits());
             //false if uses local override units

             if (swDispDim.GetUseDocUnits() == false)
             {
                 int LenUnit = 0;
                 int AngUnit = 0;
                 bRet = swDispDim.GetChamferUnits(out LenUnit, out AngUnit);
                 Debug.Print("Uses local length unit as defined in swLengthUnit_e: " + LenUnit);
                 //0=swMM
                 //0=swDegrees, 3=swRadians
                 Debug.Print("Uses local angle unit as defined in swAngleUnit_e: " + AngUnit);
             }
             Debug.Print("");

             int indx = 0;
             swDispDim.set_ChamferPrecision(indx, 0);
             Debug.Print("Precision of chamfer distance: " + indx +  " decimal places");
             swDispDim.set_ChamferPrecision(indx, 1);
             Debug.Print("Precision of chamfer angle: " + indx +  " decimal places");

             object objTokenFormats;
             object objTokenValues;
             string[] tokenformats = null;
             string[] tokenvalues = null;
             long n = 0;

             Debug.Print("");
             Debug.Print("Text format items in " + swDispDim.GetNameForSelection() + ":");
             Debug.Print("");
             long count = 0;

             count = swDispDim.GetTextFormatItems((int)swDimensionTextParts_e.swDimensionTextCalloutAbove, out objTokenFormats, out objTokenValues);
             Debug.Print("Number of callout above items: " + count);

             if (!(count == 0))
             {
                 tokenformats = (string[])objTokenFormats;
                 Debug.Print(" tokenformats: ");
                 for (n = tokenformats.GetLowerBound(0); n <= tokenformats.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenformats[n]);
                 }
                 tokenvalues = (string[])objTokenValues;
                 Debug.Print(" tokenvalues: ");
                 for (n = tokenvalues.GetLowerBound(0); n <= tokenvalues.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenvalues[n]);
                 }
             }
             Debug.Print("");
             count = swDispDim.GetTextFormatItems((int)swDimensionTextParts_e.swDimensionTextPrefix, out objTokenFormats, out objTokenValues);
             Debug.Print("Number of prefix items: " + count);
             if (!(count == 0))
             {
                 tokenformats = (string[])objTokenFormats;
                 Debug.Print(" tokenformats: ");
                 for (n = tokenformats.GetLowerBound(0); n <= tokenformats.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenformats[n]);
                 }
                 tokenvalues = (string[])objTokenValues;
                 Debug.Print(" tokenvalues: ");
                 for (n = tokenvalues.GetLowerBound(0); n <= tokenvalues.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenvalues[n]);
                 }
             }
             Debug.Print("");
             count = swDispDim.GetTextFormatItems((int)swDimensionTextParts_e.swDimensionTextSuffix, out objTokenFormats, out objTokenValues);
             Debug.Print("Number of suffix items: " + count);

             if (!(count == 0))
             {
                 tokenformats = (string[])objTokenFormats;
                 Debug.Print(" tokenformats: ");
                 for (n = tokenformats.GetLowerBound(0); n <= tokenformats.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenformats[n]);
                 }
                 tokenvalues = (string[])objTokenValues;
                 Debug.Print(" tokenvalues: ");
                 for (n = tokenvalues.GetLowerBound(0); n <= tokenvalues.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenvalues[n]);
                 }
             }
             Debug.Print("");
             count = swDispDim.GetTextFormatItems((int)swDimensionTextParts_e.swDimensionTextCalloutBelow, out objTokenFormats, out objTokenValues);
             Debug.Print("Number of callout below items: " + count);

             if (!(count == 0))
             {
                 tokenformats = (string[])objTokenFormats;
                 Debug.Print(" tokenformats: ");
                 for (n = tokenformats.GetLowerBound(0); n <= tokenformats.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenformats[n]);
                 }
                 tokenvalues = (string[])objTokenValues;
                 Debug.Print(" tokenvalues: ");
                 for (n = tokenvalues.GetLowerBound(0); n <= tokenvalues.GetUpperBound(0); n++)
                 {

                     Debug.Print(" " + tokenvalues[n]);
                 }
             }
```

```
            //Create lower display dimension text and enclose
            //in parentheses
            swDispDim.SetLowerText("Example of lower text");
            swDispDim.ShowLowerParenthesis = true;
```

```
            Debug.Print("");
            Debug.Print("Lower Dimension Text: " + swDispDim.GetLowerText());
            Debug.Print("  Show lower parenthesis: " + swDispDim.ShowLowerParenthesis);
            Debug.Print("  Show lower inspection:  " + swDispDim.LowerInspection);
            Debug.Print("  Split dual dimensions:  " + swDispDim.Split);

	    }

	    public SldWorks swApp;

    }

}
```
