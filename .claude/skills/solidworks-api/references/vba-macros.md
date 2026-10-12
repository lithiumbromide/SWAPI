# VBA macros
How to build, run and debug SOLIDWORKS VBA macros from the template in [../assets/vba/Macro.bas](../assets/vba/Macro.bas).
## Contents
- [Project setup](#project-setup)
- [Template walkthrough](#template-walkthrough)
- [Early binding and type names](#early-binding-and-type-names)
- [Arguments and data types](#arguments-and-data-types)
- [Running macros](#running-macros)
- [Debugging](#debugging)
- [64-bit VBA and upgrades](#64-bit-vba-and-upgrades)
- [VSTA macros](#vsta-macros)
## Project setup
- A SOLIDWORKS VBA project is a binary `.swp` file. Create one with Tools > Macro > New, then in the VBA editor use File > Import File to add the `.bas` module, or paste the code into the default module. Import expects Windows line endings; if the `Attribute VB_Name` line shows up as code, paste the code without that line instead.
- Tools > References must include `SldWorks <version> Type Library` (`sldworks.tlb`) and `SOLIDWORKS <version> Constant type library` (`swconst.tlb`). Recorded macros reference both automatically; macros started from an empty project often do not. Add `SOLIDWORKS <version> Commands type library` only when the code uses `swCommands_e` IDs with `IModelDocExtension.RunCommand` or `ISldWorks.RunCommand`.
- Without the Constant type library every enum name is an undeclared variable: `Option Explicit` turns that into a compile error instead of a silent 0.
## Template walkthrough
- `Attribute VB_Name = "Macro"` fixes the module name on import, which `ISldWorks.RunMacro2` needs.
- `Option Explicit` and the module-level `swApp As SldWorks.SldWorks` follow [VBA declarations](correctness-rules.md#vba-declarations).
- `main` is the entry point, as in recorded macros. It gets `Application.SldWorks`, guards `ActiveDoc` against Nothing and checks `IModelDoc2.GetType` against `swDocumentTypes_e` names before doing anything.
- `main` records state it may change (the active configuration) and restores it under `Cleanup`. `On Error GoTo Failed` sends run-time errors to `Failed`, which reports them and resumes at `Cleanup`, so the restore code runs on every path and an error never leaves the model or the session altered ([user preferences](correctness-rules.md#user-preferences), [configurations](correctness-rules.md#configurations)).
- `Process` holds the task; replace its body. `SaveCopy` shows the call pattern for members with ByRef Long Errors and Warnings ([errors and warnings](correctness-rules.md#errors-and-warnings)). `Report` routes messages through `ISldWorks.SendMsgToUser2`.
## Early binding and type names
Declare variables with their interface types (`Dim swModel As SldWorks.ModelDoc2`). Early binding gives compile-time checks, IntelliSense and faster calls; `As Object` defers every typo to run time. VBA type names drop the leading `I` of the .NET interface names: `SldWorks.SldWorks` (`ISldWorks`), `ModelDoc2`, `ModelDocExtension`, `PartDoc`, `AssemblyDoc`, `DrawingDoc`, `Component2`, `Feature`, `SelectionMgr`, `CustomPropertyManager`, `Configuration`, `View`, `Sheet`. `swapi.py sig IModelDoc2.GetType --vba` prints the VBA form. VBA casts by assignment: `Set swPart = swModel` turns a `ModelDoc2` into a `PartDoc` when the document is a part, so check `GetType` first.
## Arguments and data types
The general rules are in [VBA declarations](correctness-rules.md#vba-declarations), [arrays and Variants](correctness-rules.md#arrays-and-variants), [enums and bitmasks](correctness-rules.md#enums-and-bitmasks) and [errors and warnings](correctness-rules.md#errors-and-warnings). VBA adds these traps:
- Pass out parameters (Errors, Warnings, result codes) as declared `Long` variables. A literal, an expression or an extra pair of parentheses passes a temporary copy, so the result is lost without any error.
- Call functions without parentheses when you ignore the result (`swModel.ClearSelection2 True`), or with `Call`; parentheses around a single argument evaluate it instead.
- VBA has no `finally`; route every exit through one cleanup label, as the template does.
## Running macros
- Interactive: Tools > Macro > Run and select the `.swp`. Assign frequent macros to a toolbar button via Tools > Customize > Commands > Macro (16 x 16 bitmap).
- From code: `ISldWorks.RunMacro2(path, moduleName, procedureName, swRunMacroUnloadAfterRun, errorCode)` runs a VBA macro from an add-in, an EXE or another macro and reports `swRunMacroError_e`; for a compiled VSTA DLL pass the DLL path, an empty module and `Main` (case-sensitive for C#).
- Macro features (`swm*` rebuild and edit functions stored in a `.swp`) are covered in [features-and-sketches.md](features-and-sketches.md).
## Debugging
- Record a macro (Tools > Macro > Record) to discover the calls and enum names behind a UI action, then clean it up as the help recommends: delete view manipulation lines, declare and early-bind variables, and run `swapi.py check` on the result before reusing it.
- Step with F8, set breakpoints with F9, print with `Debug.Print` to the Immediate window and inspect objects in the Locals window.
- Map the common run-time errors: 91 (object variable not set) is a missing [null check](correctness-rules.md#null-checks-and-return-values); 438 (object does not support this property or method) is a member newer than the running release or a misspelled late-bound call ([version availability](correctness-rules.md#version-availability)); 13 (type mismatch) is usually an `Integer` or a non-Variant array.
- When a call returns False, check selection and document state before suspecting the API ([selection](correctness-rules.md#selection), [active and visible documents](correctness-rules.md#active-and-visible-documents)).
## 64-bit VBA and upgrades
- SOLIDWORKS 2013 SP0 and later ship VBA 7. `Declare` statements must carry `PtrSafe`, and pointer or handle arguments use `LongPtr` so one declaration works on 32-bit and 64-bit. 32-bit ActiveX controls used by old macros must be recompiled for 64-bit.
- After a SOLIDWORKS upgrade a macro can stop at `Set swApp = Application.SldWorks` with "Compile error: Object library feature not supported". Open Tools > References and move the SOLIDWORKS type libraries up in priority; if that fails, check an unused library, close the dialog, reopen it and uncheck it again so VBA rereads the libraries.
## VSTA macros
- SOLIDWORKS also records and runs VB.NET and C# macros through Visual Studio Tools for Applications: Tools > Macro > New with `SW VSTA C# Macro (*.csproj)` or `SW VSTA VB Macro (*.vbproj)`. Recording, editing and debugging need Visual Studio installed before SOLIDWORKS; without it SOLIDWORKS only runs existing VSTA DLLs.
- The generated `SolidWorksMacro` class has a pre-assigned `swApp` field and a GUID attribute that must not change. Building saves only a release DLL under the project's `bin` folder.
- Classes that implement `SolidWorks.Interop.swpublished` interfaces (PropertyManager page handlers, for example) need `ComVisible(true)`. For anything you distribute, prefer an add-in or a standalone EXE ([dotnet-addins.md](dotnet-addins.md)).
## Sources
- `markdown/sldworksapiprogguide/GettingStarted/SolidWorks_Macros.md`
- `markdown/sldworksapiprogguide/GettingStarted/Record_Solidworks_Macro.md`
- `markdown/sldworksapiprogguide/GettingStarted/Run_SolidWorks_Macro.md`
- `markdown/sldworksapiprogguide/GettingStarted/Edit_or_Debug_SolidWorks_Macro.md`
- `markdown/sldworksapiprogguide/GettingStarted/Early_and_Late_Binding.md`
- `markdown/sldworksapiprogguide/GettingStarted/Option_Explicit_Statement.md`
- `markdown/sldworksapiprogguide/GettingStarted/Assign_SolidWorks_Macro_to_Button.md`
- `markdown/sldworksapiprogguide/GettingStarted/VSTA_2015.md`
- `markdown/sldworksapiprogguide/Overview/Type_Libraries.md`
- `markdown/sldworksapiprogguide/Overview/VBA_and_SolidWorks_x64.md`
- `markdown/sldworksapiprogguide/Overview/VBA_Macros_Type_Libraries_and_SolidWorks_Upgrade.md`
- `markdown/sldworksapiprogguide/Overview/Long_vs_Integer.md`
- `markdown/sldworksapiprogguide/Overview/Arrays.md`
- `markdown/sldworksapiprogguide/Overview/SafeArraysVB.md`
- `markdown/sldworksapiprogguide/Overview/Return_Values.md`
- `markdown/sldworksapiprogguide/Overview/ComVisibleAttribute_in_VSTA_macros.md`
- `markdown/apihelp/ContactingAPISupport/earlyBinding.md`
- `markdown/apihelp/ContactingAPISupport/OptionExplicit.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2.md`
- `markdown/sldworksapi/Run_SOLIDWORKS_Commands_Example_VB.md`
- `markdown/sldworksapivb6/SldWorks~ModelDocExtension~SaveAs3.md`
