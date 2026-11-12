---
title: "Edit or Debug SOLIDWORKS Macro"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Edit_or_Debug_SolidWorks_Macro.htm"
---

# Edit or Debug SOLIDWORKS Macro

Edit or debug SOLIDWORKS macros using Microsoft VBA or Microsoft VSTA.

NOTES:

- [SOLIDWORKS 2018 offers Visual Studio Tools for Applications (VSTA)](VSTA_2015.htm), impacting how VB.NET and C# macros are developed and run in SOLIDWORKS 2018 and later.
- When debugging Microsoft VSTA macros with user-interface components such as PropertyManager pages, manipulators, or other objects that use events or handler objects, the debugger must continue to run after the main() method of the VSTA macro exits. Either deselect the user-interface system option Stop VSTA debugger on macro exit (located on the Tools > Options > System Options dialog) or set swUserPreferenceToggle_e swStopDebuggingVstaOnExit to false to keep the debugger running after the main() method of the Microsoft VSTA macro exits.
- To automatically edit a macro after recording it, click Tools > Options > Systems Options. On the General tab, select Automatically edit macro after recording and click OK. This setting is persistent across SOLIDWORKS sessions unless you selected to save a just recorded macro as SW All Macros Types (*.swp, *.csproj, *.vbproj). This setting has no effect when you select to save a macro as multiple macro types.
- If you recently edited the macro, you can select it from the menu when you click Tools > Macro. This menu lists the last nine macros that you edited.

#### To edit or debug a SOLIDWORKS VBA macro:

1. Click Edit Macro on the Macro toolbar, or click Tools > Macro > Edit.

1. In the dialog, select SW VBA Macros (*.swp) in Files of type (selected by default).
2. Click Open.

#### To edit a .NET macro

Read [SOLIDWORKS 2018 offers Visual Studio Tools for Applications (VSTA)](VSTA_2015.htm).

#### New macro tasks

- Delete extra lines of code automatically inserted in the macro when it was created:
- [Explicitly declare all variables](Option_Explicit_Statement.htm) in a Microsoft VBA macro.
- [Early bind all variables](Early_and_Late_Binding.htm).
