# VBA macros
DraftSight has no VBA editor of its own. VBA code runs in another VBA host (Excel, Word, the SOLIDWORKS VBA editor, any Office VBA editor) and drives a running DraftSight through COM, exactly as the shipped VBA examples do. Macros recorded by DraftSight Premium in VBA format are `.swb` files for the SOLIDWORKS VBA editor or an Office VBA editor.
## Project setup
1. Open the VBA editor of the host (Alt+F11 in Office).
2. Tools > References > Browse, select `install_dir\bin\dsAutomation.dll` (typically `C:\Program Files\Dassault Systemes\DraftSight\bin\dsAutomation.dll`) and tick it. The library appears as DraftSight, which gives early-bound types such as `DraftSight.Application`, `DraftSight.Document` and `DraftSight.SketchManager` and the `ds*_e` enum names.
3. Insert a module, paste or import [Macro.bas](../assets/vba/Macro.bas), and keep `Option Explicit` at the top.
4. Start DraftSight and open a drawing before running the macro; `GetObject` attaches to the running instance and does not start one.
## Template
[assets/vba/Macro.bas](../assets/vba/Macro.bas) connects with `GetObject(, "DraftSight.Application")`, traps error 429 when DraftSight is not running, calls `AbortRunningCommand`, gets the active document and model-space sketch manager, creates or reuses a layer, inserts a line and a circle on it inside one undo record, writes a status line to the command window and reports every failure with a message box. Replace `Process` with the task; keep the connection, null checks and error handler.
## Writing the code
- Interface names drop the leading `I` and take the library prefix: `IDocument` is `DraftSight.Document`, `ISketchManager` is `DraftSight.SketchManager`. Names such as `Application` and `Document` also exist in the host's own library (every Office host has an `Application`, Word has a `Document`), so always write the `DraftSight.` prefix.
- Translate the help's .NET signatures: `int` and `long` to `Long`, `double` to `Double`, `bool` to `Boolean`, `string` to `String`, `object` to `Variant` (arrays) or the class type (single objects), and `out` parameters to variables passed ByRef (declare them first).
- Call methods without parentheses when you discard the result (`dsSketchManager.InsertLine 0, 0, 0, 10, 0, 0`), and with `Set` and parentheses when you keep an object (`Set dsLine = dsSketchManager.InsertLine(0, 0, 0, 10, 0, 0)`).
- Arrays the API returns arrive as `Variant`: `If IsArray(v) Then For i = LBound(v) To UBound(v)`. Arrays you pass are `Variant` holding a `Double`, `Long` or `String` array, or an array of DraftSight objects; build them with `ReDim` and assign each element (`Set` for objects).
- Enum members may be written bare (`dsDocumentSaveAs_R2018_DWG`) or qualified (`dsDocumentSaveAsOption_e.dsDocumentSaveAs_R2018_DWG`); both need the reference.
## Running and debugging
- Run with F5 inside `Sub main()`, or from the host's macro list. Errors stop at the failing line when the error handler is commented out; the template reports `Err.Number` and `Err.Description` instead.
- Error 429 at `GetObject`: DraftSight is not running or runs elevated while the host does not (start both at the same integrity level). Error 438 on a member: it does not exist in the installed release; run `check` with `--target` and compare `IApplication.GetVersion`. "User-defined type not defined": the `dsAutomation.dll` reference is missing or broken after an upgrade; remove it and browse to the new file.
- After a DraftSight upgrade, re-add the type library reference, as the Getting Started topic requires for every project.
- `ICommandMessage.PrintLine` writes to the DraftSight command window, which is the least intrusive way to report progress from long macros; `MsgBox` blocks the host until clicked.
