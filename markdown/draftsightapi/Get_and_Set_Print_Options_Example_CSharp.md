---
title: "Get and Set Print Options Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Print_Options_Example_CSharp.htm"
---

# Get and Set Print Options Example (C#)

This example shows how to get and set print options and print to a specified device.

```
//-------------------------------------------------------------------------
// Preconditions:
// 1.  Create a C# Windows console project with name PrintJPG_CSharp.
// 2.  Copy and paste this example into the C# IDE.
//     (Modify the namespace as needed.)
// 3.  Add a reference to:
//     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4.  Add references to System, System.Windows.Forms, and others as needed.
// 5.  Start DraftSight and open a document that has Sheet1.
// 6.  Run the macro to see the available printers in the Immediate window.
// 7.  Reset the macro.
// 8.  Substitute a valid printer in the PrinterName property. If you specify
//     PDF, JPG, PNG, or SVG, then you must also provide a full pathname
//     to print to in IPrintManager::PrintOut at the bottom of this macro.
// 9.  Comment out the first Stop.
// 10. Save the macro.
// 11. Run the macro to see the available paper sizes in the Immediate window.
// 12. Reset the macro.
// 13. Substitute a valid paper size for the PaperSize property.
// 14. Comment out the second Stop.
// 15. Save the macro.
// 16. Run the macro to see the available print styles in the Immediate window.
// 17. Reset the macro.
// 18. Substitute a valid print style in the StyleTable property.
// 19. Comment out the third Stop.
// 20. Save the macro.
// 21. Run the macro to completion.
//
// Postconditions: Sheet1 of the open document is printed to the
// specified printer on paper of the specified size.
//----------------------------------------------------------------------------

using System.Windows.Forms;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.Xml.Linq;
using System.Threading.Tasks;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using Microsoft.CSharp.RuntimeBinder;

namespace PrintJPG_CSharp
{

    static class Module1
    {

        private static Document dsDoc;
        public static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
            //Abort any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();
            //Get active document
            dsDoc = dsApp.GetActiveDocument();
            if (dsDoc != null)
            {
                //Get and set printing options
                GetSetPrintOptions(dsApp);
            }

        }
        public static void GetSetPrintOptions(DraftSight.Interop.dsAutomation.Application dsApp)
        {
            PrintManager dsPrintMgr = null;
            string printerName = null;
            string[] dsVarPaperSizes = null;
            string[] dsVarPrinters = null;
            string[] dsVarPrintStyles = null;
            object printStyles = null;
            double paperLength = 0;
            double paperWidth = 0;
            Sheet dsSheet = null;
            double top = 0;
            double bottom = 0;
            double left = 0;
            double right = 0;
            string[] sheetArray = new string[1];
            object sheetObj = null;

            //Get PrintManager
            dsPrintMgr = dsApp.GetPrintManager();
            dsDoc = dsApp.GetActiveDocument();
            dsSheet = dsDoc.GetSheet("Sheet1");
            dsSheet.Activate();

            if (dsPrintMgr != null)
            {

                //Get available printers
                dsVarPrinters = dsPrintMgr.GetAvailablePrinters();
                Debug.Print("Available printers:");
                Debug.Print(" PDF");
                Debug.Print(" JPG");
                Debug.Print(" PNG");
                Debug.Print(" SVG");
                for (var i = 0; i <= dsVarPrinters.GetUpperBound(0); i++)
                {
                    Debug.Print(" " + dsVarPrinters[i]);
                }

                System.Diagnostics.Debugger.Break();

                //Set the printer name
                printerName = "JPG";
                dsPrintMgr.Printer = printerName;
                if (string.IsNullOrEmpty(printerName))
                {
                    MessageBox.Show("Failed to set IPrintManager.Printer property " + printerName + " value.");
                }

                //Get available paper sizes for printer
                dsVarPaperSizes = dsPrintMgr.AvailablePaperSizes();

                if (Microsoft.VisualBasic.Information.IsArray(dsVarPaperSizes) && dsVarPaperSizes.GetUpperBound(0) == 0)
                {
                    MessageBox.Show("List of available paper sizes is empty for " + dsPrintMgr.Printer + " printer.");
                }
                else
                {
                    Debug.Print("Available paper sizes for " + printerName + ":");
                    for (var i = 0; i <= dsVarPaperSizes.GetUpperBound(0); i++)
                    {
                        Debug.Print(" " + dsVarPaperSizes[i]);
                    }
                }

                System.Diagnostics.Debugger.Break();

                //Set paper size
                dsPrintMgr.PaperSize = "VGA_(480.00_x_640.00_Pixels)";

                //Get paper size
                dsPrintMgr.GetPaperSize(out paperLength, out paperWidth);
                Debug.Print("Paper length: " + paperLength);
                Debug.Print("Paper width: " + paperWidth);

                //Get print margins

                dsPrintMgr.GetPrintMargins(out top, out bottom, out left, out right);

                Debug.Print("Top margin: " + top);
                Debug.Print("Bottom margin: " + bottom);
                Debug.Print("Left margin: " + left);
                Debug.Print("Right margin: " + right);

                //Set print orientation
                dsPrintMgr.Orientation = dsPrintOrientation_e.dsPrintOrientation_Landscape;

                //Set the sheets to print
                sheetArray[0] = "Sheet1";
                dsPrintMgr.SetSheets(sheetArray);
                //Verify the sheets to print
                sheetObj = dsPrintMgr.GetSheets();
                if ((sheetObj == null))
                {
                    MessageBox.Show("Failed to set sheets to print");
                }
                //Center the printout
                dsPrintMgr.PrintOnCenter = true;

                //Set print quality as defined in dsStandardPrintQuality_e
                dsPrintMgr.Quality = (int)dsStandardPrintQuality_e.dsStandardPrintQuality_Normal;

                //Scale the line weights
                dsPrintMgr.ScaleLineWeight = true;

                //Scale the printout to fit the paper
                dsPrintMgr.ScaleToFit = true;

                dsPrintMgr.GetAvailablePrintStyleTables(out printStyles);
                dsVarPrintStyles = (string[])printStyles;
                Debug.Print("Available print style tables:");
                for (var i = 0; i <= dsVarPrintStyles.GetUpperBound(0); i++)
                {
                    Debug.Print(" " + dsVarPrintStyles[i]);
                }

                System.Diagnostics.Debugger.Break();

                //Set the style table
                dsPrintMgr.StyleTable = "default.ctb";

                //Set the printing range
                dsPrintMgr.SetPrintRange(dsPrintRange_e.dsPrintRange_AllGeometry, "", false, 0D, 0D, 0D, 0D);

                //Use the assigned print style
                dsPrintMgr.UseAssignedPrintStyle = true;
                dsPrintMgr.PrintOut(1, "c:\\temp\\printout.jpg"); // If printerName is set to JPG
                //dsPrintMgr.PrintOut (1, "") ' If printerName is a physical device

                dsSheet.Activate();

            }
            else
            {
                MessageBox.Show("IDocument.GetPrintManager returns Nothing.");
            }
        }

    }
}
```
