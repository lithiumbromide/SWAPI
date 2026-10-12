---
title: "Pack and Go an Assembly (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Pack_and_Go_an_Assembly_Example_VBNET.htm"
---

# Pack and Go an Assembly (VB.NET)

This example shows how to get the names of the path and files of an assembly document, add a prefix and suffix to the names, and save the files to a different path using the Pack and Go interface.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Specified assembly exists.
 ' 2. The folder, c:\temp, exists.
 ' 3. Open the Immediate window.
 ' 4. Run the macro.
 '
 ' Postconditions:
 ' 1. Prints names of the current path and filenames
 '    of the assembly documents to the Immediate window.
 ' 2. Prints names of the default path and filenames to which to
 '    save assembly documents to Immediate window.
 ' 3. Specifies the Pack and Go destination folder.
 ' 4. Specifies that all files get saved to the root directory of the
 '    Pack and Go destination folder.
 ' 5. Adds prefix and suffix to user-named filenames.
 ' 6. Prints names of user-specified path and user-named filenames to
 '    Immediate window.
 ' 7. Creates user-named files in user-specified path using Pack and Go.
 ' 8. Examine c:\temp to verify.
 '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial  Class SolidWorksMacro

     Public  Sub Main()

         Dim swModelDoc As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swPackAndGo As PackAndGo
         Dim openFile  As  String
         Dim pgFileNames As  Object =  Nothing
         Dim pgFileStatus As  Object =  Nothing
         Dim pgSetFileNames() As  String
         Dim pgGetFileNames As  Object
         Dim pgDocumentStatus As  Object
         Dim status As  Boolean
         Dim warnings As  Integer
         Dim errors As  Integer
         Dim i As  Integer
         Dim namesCount As  Integer
         Dim myPath As  String
         Dim statuses As  Object

         ' Open assembly
         openFile =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\handle.sldasm"
         swModelDoc = swApp.OpenDoc6(openFile, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelDocExt = swModelDoc.Extension

         ' Get Pack and Go object
         Debug.Print("Pack and Go")
         swPackAndGo = swModelDocExt.GetPackAndGo

         ' Get number of documents in assembly
         namesCount = swPackAndGo.GetDocumentNamesCount
         Debug.Print("  Number of model documents: " & namesCount)

         ' Include any drawings, SOLIDWORKS Simulation results, and SOLIDWORKS Toolbox components
         swPackAndGo.IncludeDrawings = True
         Debug.Print("  Include drawings: " & swPackAndGo.IncludeDrawings)
         swPackAndGo.IncludeSimulationResults =  True
         Debug.Print("  Include SOLIDWORKS Simulation results: " & swPackAndGo.IncludeSimulationResults)
         swPackAndGo.IncludeToolboxComponents =  True
         Debug.Print   "  Include SOLIDWORKS Toolbox components: " & swPackAndGo.IncludeToolboxComponents

         ' Get current paths and filenames of the assembly's documents
         status = swPackAndGo.GetDocumentNames(pgFileNames)
         Debug.Print("")
         Debug.Print("  Current path and filenames: ")
         If  Not pgFileNames  Is  Nothing Then
             For i = 0 To UBound(pgFileNames)
                 Debug.Print("    The path and filename is: " & pgFileNames(i))
             Next i
         End  If

         ' Get current save-to paths and filenames of the assembly's documents
         status = swPackAndGo.GetDocumentSaveToNames(pgFileNames, pgFileStatus)
         Debug.Print("")
         Debug.Print("  Current default save-to filenames: ")
         If  Not pgFileNames  Is  Nothing Then
             For i = 0 To UBound(pgFileNames)
                 Debug.Print("   The path and filename is: " & pgFileNames(i))
             Next i
         End  If

         ' Set folder where to save the files
         myPath =  "C:\temp\"
         status = swPackAndGo.SetSaveToName(True, myPath)

         ' Flatten the Pack and Go folder structure; save all files to the root directory
         swPackAndGo.FlattenToSingleFolder =  True

         ' Add a prefix and suffix to the filenames
         swPackAndGo.AddPrefix =  "SW_"
         swPackAndGo.AddSuffix =  "_PackAndGo"

         ' Verify document paths and filenames after adding prefix and suffix
         ReDim pgGetFileNames(namesCount - 1)
         ReDim pgDocumentStatus(namesCount - 1)
         status = swPackAndGo.GetDocumentSaveToNames(pgGetFileNames, pgDocumentStatus)
         Debug.Print("")
         Debug.Print("  My Pack and Go path and filenames after adding prefix and suffix: ")
         For i = 0  To (namesCount - 1)
             Debug.Print("    My path and filename is: " & pgGetFileNames(i))
         Next i

         ' Pack and Go
         statuses = swModelDocExt.SavePackAndGo(swPackAndGo)

     End  Sub

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
