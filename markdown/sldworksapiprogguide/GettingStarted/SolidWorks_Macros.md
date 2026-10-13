---
title: "SOLIDWORKS Macros"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/SolidWorks_Macros.htm"
---

# SOLIDWORKS Macros

The quickest and easiest way to start programming with the SOLIDWORKS API is to record a SOLIDWORKS macro, which contains the SOLIDWORKS API calls that correspond to the actions performed in the user interface. You can modify the macro in Microsoft Visual Basic for Applications (VBA) or Microsoft Visual Studio Tools for Applications (VSTA) to fit your work site's needs.

- Microsoft VBA is a toolset based on Microsoft Visual Basic for Applications (VBA) and is embedded in SOLIDWORKS . Microsoft VBA lets you record, run, and edit Microsoft VBA macros in SOLIDWORKS. Recorded macros are saved as .swp files.
- Microsoft Visual Studio Tools for Applications (VSTA) is a toolset based on Microsoft VB.NET and C# and is installed with SOLIDWORKS. Microsoft VSTA lets you record, edit, debug, and run VB.NET and C# code with SOLIDWORKS. Recorded Microsoft VSTA macros are saved as Microsoft VB.NET or C# projects. Building or debugging a Microsoft VSTA macro creates an executable file that ends in the filename extension .dll, which can be used by SOLIDWORKS in the same manner as a .swp file.

  NOTES:

  - [SOLIDWORKS 2018 offers Visual Studio Tools for Applications (VSTA)](VSTA_2015.htm), impacting how VB.NET and C# macros are developed and run in SOLIDWORKS 2018 and later.
  - When debugging Microsoft VSTA macros with user-interface components such as PropertyManager pages, manipulators, or other objects that use events or handler objects, the debugger must continue to run after the main() method of the VSTA macro exits. Either deselect the user-interface system option Stop VSTA debugger on macro exit (located on the Tools > Options > System Options dialog) or set swUserPreferenceToggle_e.swStopDebuggingVstaOnExit to false to keep the debugger running after the main() method of the Microsoft VSTA macro exits.

Typically you would follow these steps to create a SOLIDWORKS API application using SOLIDWORKS macros:

1. Plan the user-interface actions before recording them.
2. [Record](Record_Solidworks_Macro.htm) the user-interface actions.

  NOTE: If you are not familiar with recording SOLIDWORKS macros, record the macro a couple of times to eliminate interactive changes to the view such as changing the view orientation, zooming in or out, panning, rotating the model, and so on.
3. [Edit](Edit_or_Debug_SolidWorks_Macro.htm) the macro to delete extra lines of code and explicitly declare and early bind variables.
4. [Run](Run_SolidWorks_Macro.htm) the macro to test it.
5. [Debug](Edit_or_Debug_SolidWorks_Macro.htm) the macro and test it again.
6. If the application has a user interface, create it in Microsoft VBA or Microsoft VSTA and then modify the macro to work with the user interface, run the modified macro, and debug it.

When done recording, testing, and debugging the macro, you can [assign the macro to button](Assign_SolidWorks_Macro_to_Button.htm).
