---
title: "Set and Get System Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_System_Files_Example_CSharp.htm"
---

# Set and Get System Files Example (C#)

This example shows how to set and get the paths of some DraftSight system files.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
 // 4. Add a reference to System.
 // 5. Start DraftSight.
 // 6. Open the Immediate window.
 //
 // Postconditions:
 // 1. Sets the paths to the DraftSight support and font files.
 // 2. Prints the current DraftSight system files and paths to the
 //    Immediate window.
 //---------------------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Diagnostics;

 namespace DSSystemFiles_CSharp
 {
     class Program
    {
          static void Main(string[] args)
         {
 Application dsApp;
 SystemFiles dsSystemFiles = default(SystemFiles);
 string[] setFontPaths = new string[2];
 string[] setSupportPaths = new string[3];
 object[] getFontPaths = null;
 object[] getSupportPaths = null;
                 object[] getDrawingBorderPaths = null;
                 object[] getTitleBlockPaths = null;

 int i = 0;

 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

 //Abort any command currently running in DraftSight
 //to avoid nested commands
 dsApp.AbortRunningCommand();

 //Get system files
 dsSystemFiles = dsApp.GetSystemFiles();

 //Set system files
 setFontPaths[0] = "C:\\Program Files\\Dassault Systemes\\DraftSight\\Fonts";
 dsSystemFiles.FontsPaths = setFontPaths;

 setSupportPaths[0] = "C:\\Program Files\\Dassault Systemes\\DraftSight\\Default Files\\Support";
 dsSystemFiles.SupportPaths = setSupportPaths;

 Debug.Print("System files:");
 Debug.Print("  Help file:                            " + dsSystemFiles.HelpFile);
 Debug.Print("  Logfile path:                         " + dsSystemFiles.LogFilePath);
 Debug.Print("  Dictionary file for SpellCheck:       " + dsSystemFiles.MainDictionaryFile);
 Debug.Print("  Custom dictionary file:               " + dsSystemFiles.CustomDictionaryFile);
 Debug.Print("  Location for temporary drawing files: " + dsSystemFiles.TempPath);

 getFontPaths = dsSystemFiles.FontsPaths;
 Debug.Print("  Font paths: ");
 for (i = 0; i < getFontPaths.Length; i++) {
 Debug.Print("                                        " + getFontPaths[i]);
 }

 getSupportPaths = dsSystemFiles.SupportPaths;
 Debug.Print("  Support paths: ");
 for (i = 0; i < getSupportPaths.Length; i++) {
 Debug.Print("                                        " + getSupportPaths[i]);
 }

                getDrawingBorderPaths = dsSystemFiles.DrawingBorderPaths;
                 Debug.Print("  Drawing border paths: ");
                 for (i = 0; i < getDrawingBorderPaths.Length; i++)
                 {
                     Debug.Print("                                        " + getDrawingBorderPaths[i]);
                 }

                 getTitleBlockPaths = dsSystemFiles.TitleBlockPaths;
                 Debug.Print("  Title block paths: ");
                 for (i = 0; i < getTitleBlockPaths.Length; i++)
                 {
                     Debug.Print("                                        " + getTitleBlockPaths[i]);
                 }
   }
      }
 }
```
