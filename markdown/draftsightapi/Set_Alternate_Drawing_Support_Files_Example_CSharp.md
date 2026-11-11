---
title: "Set Alternate Drawing Support Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_Alternate_Drawing_Support_Files_Example_CSharp.htm"
---

# Set Alternate Drawing Support Files Example (C#)

This example shows how to set alternate drawing support files.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight.
// 6. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Gets active document.
// 3. Gets instance of drawing support files.
// 4. Displays message boxes informing you that these alternate
//    font files were set:
//    a. Big font file. Click OK.
//    b. Shape font file. Click OK.
//    c. SHX font file. Click OK.
//    d. Drawing template file. Click OK.
// 5. Click Tools > Options > File Locations and expand Drawing Support.
//    a. Expand and examine Alternate Font File > SHX font, Big font,
//       and Shape file.
//    b. Expand and examine Drawing Template File Location.
// 6. Exit DraftSight.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace DrawingSupportFilesCSharp
{
    class Program
    {

        public static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get drawing support files
            DrawingSupportFiles dsDrawingSupportFiles = dsApp.GetDrawingSupportFiles();
            if (null == dsDrawingSupportFiles)
            {
                MessageBox.Show("There are no valid drawing support files.");
                return;
            }

            SystemFiles dsSysFile = dsApp.GetSystemFiles();
            object[] FontsPathObj = (object[])dsSysFile.FontsPaths;
            string fontPath = "";
            if (FontsPathObj.Length > 0)
                fontPath = FontsPathObj[0].ToString();

            //Set alternate big font file
            string fontFileName = System.IO.Path.Combine(fontPath, "ARAGDTM.ttf");
            dsDrawingSupportFiles.AlternateBigFontFile = fontFileName;
            MessageBox.Show("Alternate big font file: " + dsDrawingSupportFiles.AlternateBigFontFile);

            //Set alternate shape font file
            string shapeFileName = System.IO.Path.Combine(fontPath, "LTypeShp.shx");
            dsDrawingSupportFiles.AlternateShapeFile = shapeFileName;
            MessageBox.Show("Alternate shape font file: " + dsDrawingSupportFiles.AlternateShapeFile);

            //Set alternate SHX font file
            string ShxFontFileName = System.IO.Path.Combine(fontPath, "LTypeShp.shx");
            dsDrawingSupportFiles.AlternateShxFontFile = ShxFontFileName;
            MessageBox.Show("Alternate SHX font file: " + dsDrawingSupportFiles.AlternateShxFontFile);

            //Set alternate drawing template file
            string TemplateFilePath = System.IO.Path.Combine(dsApp.GetSystemFiles().GetUserDataPath(), "Template");

            string drawingTemplateFile = System.IO.Path.Combine(TemplateFilePath, "standard.dwt");
            dsDrawingSupportFiles.DrawingTemplateFilesPath = drawingTemplateFile;
            MessageBox.Show("Alternate drawing template file: " + dsDrawingSupportFiles.DrawingTemplateFilesPath);

        }

    }

}
```
