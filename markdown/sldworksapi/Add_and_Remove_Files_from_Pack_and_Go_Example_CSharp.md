---
title: "Add and Remove Files from Pack and Go Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm"
---

# Add and Remove Files from Pack and Go Example (C#)

This example shows how to add SOLIDWORKS, render reference, and
non-SOLIDWORKS files to Pack and Go. This example also shows how to remove a
non-SOLIDWORKS file from Pack and Go.

```vb
 //-------------------------------------------
 // Preconditions:
 // 1. Verify that the specified assembly exists.
 // 2. Create c:\PackAndGo.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the names of SOLIDWORKS, render reference, and
 //    non-SOLIDWORKS files for Pack and Go.
 // 2. Gets the the name of non-SOLIDWORKS file to remove.
 // 3. Packs up SOLIDWORKS, render reference, and
 //    non-SOLIDWORKS files and copies them to c:\PackAndGo.
 // 4. Examine c:\PackAndGo and the Immediate window.
 //-------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace AddExternalDocumentsPackAndGo.csproj
 {
     partial  class  SolidWorksMacro
     {
         public  void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             PackAndGo swPackAndGo = default(PackAndGo);
             string openFile = null;
             int namesCount = 0;
             int errors = 0;
             int warnings = 0;
             bool status = false;
             int i = 0;
             object[] renderReferences = null;
             string myPath = null;
             object statuses = null;

             // Open assembly document
             openFile =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2025\\samples\\tutorial\\EDraw\\claw\\claw-mechanism.sldasm";
             swModel = (ModelDoc2)swApp.OpenDoc6(openFile, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "",  ref errors,  ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Get Pack and Go object
             Debug.Print("Pack and Go");
             swPackAndGo = (PackAndGo)swModelDocExt.GetPackAndGo();

             // Get number of documents in assembly
             namesCount = swPackAndGo.GetDocumentNamesCount();

             // Get current paths and filenames of the assembly's documents
             object fileNames;
             object[] pgFileNames = new  object[namesCount - 1];
             status = swPackAndGo.GetDocumentNames(out fileNames);
             pgFileNames = (object[])fileNames;

             Debug.Print("");
             Debug.Print("  Add SOLIDWORKS files' paths and filenames: ");
             if ((pgFileNames != null))
             {
                 for (i = 0; i <= pgFileNames.GetUpperBound(0); i++)
                 {
                     Debug.Print("    The path and filename is: " + pgFileNames[i]);
                 }
             }

             // Set document paths and names for Pack and Go
             status = swPackAndGo.SetDocumentSaveToNames(pgFileNames);

             // Get the render stock references in this assembly
             // and print them to the Immediate window
             Debug.Print(" ");
             renderReferences = (object[])swModelDocExt.GetRenderStockReferences();
             Debug.Print("  Add render references:");
             for (i = 0; i <= renderReferences.GetUpperBound(0); i++)
             {
                 Debug.Print("    The path and filename is: " + renderReferences[i]);
             }

             // Add render stock files to Pack and Go
             status = swPackAndGo.AddExternalDocuments(renderReferences);

             // Add other non-SOLIDWORKS files to Pack and Go
             object[] otherFiles = new  object[2];
             string otherFile = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2025\\samples\\tutorial\\edraw\\claw\\claw-mechanism.easm";
             otherFiles[0] = (object)otherFile;
             otherFile = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2025\\samples\\tutorial\\edraw\\claw\\claw-mechanism.emodel_debugonly.xml";
             otherFiles[1] = (object)otherFile;

             Debug.Print(" ");
             Debug.Print("  Add non-SOLIDWORKS files:");
             for (i = 0; i <= otherFiles.GetUpperBound(0); i++)
             {
                 Debug.Print("    The path and filename is: " + otherFiles[i]);
             }

             // Add non-SOLIDWORKS file to Pack and Go
             status = swPackAndGo.AddExternalDocuments(ObjectArrayToBStrWrapperArray(otherFiles));

             // Remove one of the non-SOLIDWORKS files from Pack and Go
             object[] delOtherFiles = new  object[1];
             delOtherFiles[0] = (object)otherFiles[0];

             Debug.Print(" ");
             Debug.Print("  Remove non-SOLIDWORKS file:");
             Debug.Print("    The path and filename is: " + delOtherFiles[0]);

             status = swPackAndGo.RemoveExternalDocuments(ObjectArrayToBStrWrapperArray(delOtherFiles));

             // Override path where to save documents
             myPath =  "c:\\PackAndGo\\";
             status = swPackAndGo.SetSaveToName2(true, myPath);

             // Pack and Go both SOLIDWORKS and non-SOLIDWORKS files
             statuses = swModelDocExt.SavePackAndGo(swPackAndGo);
         }

         public  BStrWrapper[] ObjectArrayToBStrWrapperArray(object[] SwObjects)
         {
             int arraySize;
             arraySize = SwObjects.GetUpperBound(0);
             BStrWrapper[] dispwrap = new  BStrWrapper[arraySize + 1];
             int arrayIndex;

             for (arrayIndex = 0; arrayIndex < arraySize + 1; arrayIndex++)
             {
                 dispwrap[arrayIndex] = new BStrWrapper((string)(SwObjects[arrayIndex]));
             }

             return dispwrap;

         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
