---
title: "Record SOLIDWORKS Macro"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Record_Solidworks_Macro.htm"
---

# Record SOLIDWORKS Macro

#### To record a SOLIDWORKS macro:

1. Click Record\Pause Macro on the Macro toolbar, or click Tools, Macro, Record.
2. Perform the actions that you want to record.
3. When you are done recording, click Stop Macro on the Macro toolbar or click Tools, Macro, Stop.
4. In the dialog, type a name for the macro in File name, select the type of macro in Save as type, and click Save.

NOTES:

- [SOLIDWORKS 2018 offers Visual Studio Tools for Applications (VSTA)](VSTA_2015.htm).
- If you selected SW VBA Macros (*.swp), then the .swp extension is automatically added to the filename.
- If you selected SW VSTA VB Macro (*.vbproj), then a Visual Basic .NET project is created. Building or debugging the project creates an executable file with an filename extension of .dll.
- If you selected SW VSTA C# Macro (*.csproj), then a C# project is created. Building or debugging the project creates an executable file with an filename extension of .dll.
- If you selected SW All Macros Types (*.swp, *.csproj, *.vbproj), then a VBA macro file is created and VB.NET, and C# projects are created. A .swp extension is automatically added to the VBA macro's filename. Two folders are created for the VB.NET and C# projects.
- The VB.NET project folder's name is the name of the macro plus -vbnet.
- The C# project folder name is the name of the project plus -csharp.

  For example, if you saved the just recorded macro as Macro1 and selected SW All Macros Types (*.swp, *.csproj, *.vbproj) in Save as type, then the folder where you saved the macros would contain a file called Macro1.swp and two project folders, Macro1-vbnet and Macro1-csharp. The VB.NET and C# projects reside in their respective folders.

  NOTE: The Automatically edit macro after recording system option has no effect when you select to save a just recorded macro as SW All Macros Types (*.swp, *.csproj, *.vbproj).

To pause while recording a macro, click Record\Pause Macro or Tools, Macro, Pause. Click Record\Pause Macro again to continue recording.
