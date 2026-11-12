# Correctness rules
Single home of the DraftSight API correctness rules: each section names the failure it prevents, the rule, and the lookup that verifies it. Domain references link here instead of repeating these facts.
## Contents
- [Current members only](#current-members-only)
- [Version availability](#version-availability)
- [Running commands](#running-commands)
- [Enums and bitmasks](#enums-and-bitmasks)
- [Null checks and result codes](#null-checks-and-result-codes)
- [Arrays and Variants](#arrays-and-variants)
- [Units and coordinates](#units-and-coordinates)
- [Model and sheets](#model-and-sheets)
- [Layers, colors and styles](#layers-colors-and-styles)
- [Saving](#saving)
- [Undo and batch work](#undo-and-batch-work)
- [.NET runtime and COM](#net-runtime-and-com)
- [VBA declarations](#vba-declarations)
## Current members only
Failure: code calls an obsolete member that still compiles (it stays in the type library and the interop, so nothing warns) but has a narrower parameter list, or a name that does not exist, which fails at compile time in C# and at run time in late-bound VBA. The DraftSight SDK samples themselves still call `IApplication.CreateCommand2`, `IApplication.AddMenu` and `IApplication.AddToolbar`, so copied code spreads them.
Rule: take every member from `sig` or `find` output, and run `check` on finished files. When a row reads `OBSOLETE -> ... current X`, use X. The complete obsolete list of this release:
- Documents: `IApplication.OpenDocument` -> `OpenDocument2` (adds `dsEncoding_e`); `IDocument.SaveAs` -> `SaveAs2` (adds Overwrite); `IDocument.GetSheets` -> `GetSheets2` (the old member returned the model as the first element, `GetSheets2` returns only the layouts); `IDocumentExporter.ExportToPdf` -> `ExportToPdf2` (takes an `IExportSettings`); `IApplication.ExportToSvg` -> `ExportToSvg2`; `_IDocumentEvents.FileSavePostNotify` -> `FileSavePostNotify2`.
- Commands and user interface: `IApplication.CreateCommand` -> `CreateCommand2` -> `CreateCommand3` (one name) or `CreateCommand4` (global and local name); `IApplication.RunCommand` -> `RunCommand2`; `IApplication.AddMenu`, `AddToolbar`, `GetMenuItems` and `GetToolbars` -> the same members on `IWorkspace` from `IApplication.GetActiveWorkspace`; `IApplication.CreateCustomPropertyControl` -> `CreateCustomPropertyControl2`.
- Prompts: `ICommandMessage.PromptForPoint` -> `PromptForPoint2`; `PromptForKeyword` -> `PromptForKeyword2`; `PromptForAngleOrKeyword`, `PromptForDistanceOrKeyword`, `PromptForMouseOrKeyword` and `PromptForOrientationOrKeyword` -> the same names ending in `2`.
- Geometry: `ISketchManager.InsertBlock` -> `InsertBlock2` (separate X, Y and Z scale); `CopyEntities` -> `CopyEntities2` (returns the copies); `InsertArcByCenter2Points` -> `InsertArcByCenter2Points2`; `InsertAttributeDefinition` -> `InsertAttributeDefinition2`.

Names that look plausible but do not exist: `IDocument.Close` (use `IApplication.CloseDocument`), `ISketchManager.InsertMText` (use `InsertNote`), `ILine.GetStartPoint` (use `ILine.GetFirstPoint`), `IDocumentExporter.ExportImage` (use `ExportToPng`, `ExportToJpg` and the other `ExportTo*`), `ISketchManager.EraseEntities` (use `SetObjectErased` or the entity's `Erased` property).
Verify: `swapi.py check FILE` flags obsolete and near-miss names; `swapi.py members IApplication --obsolete` lists what to avoid on one interface.
## Version availability
Failure: the newest member compiles against the newest interop but fails on the user's older install (C#: missing method at run time; VBA: error 438 "Object doesn't support this property or method").
Rule: the `since` value must not exceed the target release. When it does, use the obsolete predecessor whose `since` fits and say why. The replacements that most often exceed a target: `RunCommand2` is 2024 SP2 (older installs call `RunCommand`), `CreateCommand3` and `CreateCommand4` are 2019 (older add-ins call `CreateCommand2`), `IWorkspace.AddMenu` and `AddToolbar` are 2017, `ExportToPdf2` is 2018, `CopyEntities2` is 2020, `ExportToSvg2` is 2021, `PromptForMouseOrKeyword2` is 2020 SP3, and `ISketchManager.StartUndoRecord` is 2019. Release names and ordering are in [versions.md](versions.md).
Verify: `swapi.py check FILE --target 2019`; `swapi.py sig IApplication.RunCommand2`.
## Running commands
Failure: a macro or EXE starts while the user is inside a command (for example LINE waiting for a point), so API calls nest inside it and fail or leave the command in a broken state; or an add-in aborts its own command.
Rule: in VBA macros and standalone EXEs call `IApplication.AbortRunningCommand` right after connecting, as every shipped example does. Never call it inside an add-in command handler or event handler; the help says it breaks the current command flow there. Use `IApplication.GetRunningCommand` to report what was running. Prefer API members over `RunCommand2`: command strings depend on the UI language, need `\n` (C#) or `Chr(10)` (VBA) for every Enter the command expects, and return only a `dsRunCommandError_e`.
Verify: `swapi.py doc IApplication.AbortRunningCommand --full`; `swapi.py doc IApplication.RunCommand2`.
## Enums and bitmasks
Failure: bare numbers that are wrong for the parameter, change meaning between enums, or hide intent.
Rule: pass `ds*_e` member names. `sig` annotates enum-typed parameters, either as the parameter type (`dsDocumentSaveAsOption_e Options`) or after a colon on `int` and array parameters (`int PromptInit:dsPromptInit_e`, `object EntityTypeLongArray:dsObjectType_e`). C# and VB.NET qualify the member (`dsDocumentSaveAsOption_e.dsDocumentSaveAs_R2018_DWG`); VBA may use the bare name (`dsDocumentSaveAs_R2018_DWG`) because the type library is referenced. Enum member names carry the version or variant in full (`dsDocumentSaveAs_R2018_DWG`, not `dsDocumentSaveAs_R2018`), so look them up. Decode bitmask results such as `dsDocumentSaveError_e` per flag with `And` or `&`, and combine bitmask inputs with `Or` or `|`; in JavaScript list several flags separated by semicolons.
Verify: `swapi.py enum dsDocumentSaveAsOption_e`; reverse lookup `swapi.py enum dsDocumentSave_ReadOnlyError`.
## Null checks and result codes
Failure: a call fails silently and the next line throws "Object variable not set" or a NullReferenceException far from the cause.
Rule: test every returned object for Nothing or null before use: `GetActiveDocument` with no open drawing, `OpenDocument2` when the open fails, `GetLayer`, `GetSheet` and `GetBlockDefinition` for unknown names, every `Insert*` call that cannot build the entity, and every array getter that returns an empty Variant. Read and report every status the API returns instead of an exception:
- `IDocument.SaveAs2` and `IDocument.Save`: `dsDocumentSaveError_e` (bitmask; `dsDocumentSave_Succeeded` is 0).
- `ILayerManager.CreateLayer`, `ITextStyleManager.CreateTextStyle` and other `Create*` with an out `Result`: `dsCreateObjectResult_e`; on `dsCreateObjectResult_AlreadyExists` fetch the existing object with the matching `Get*` (`GetLayer`, `GetTextStyle`) instead of trusting the out object.
- `IApplication.CreateCommand4`, `CreateCommand3` and `CreateUserCommand`: `dsCreateCommandError_e`; `dsCreateCommand_CommandNameExisted` means the global or local command name already exists.
- `IApplication.RunCommand2`: `dsRunCommandError_e`; prompts (`PromptForPoint2`, `PromptForSelection`, `PromptForString`) return False or a `dsPromptResultType_e` when the user cancels.

Verify: `swapi.py enum dsCreateObjectResult_e`; `swapi.py doc ILayerManager.CreateLayer`.
## Arrays and Variants
Failure: an array argument is rejected or silently ignored, or a returned array is used as if it were typed.
Rule: the parameter name says the element type: `...DblArray` is a flat array of Double (`x1, y1, x2, y2` for 2D polylines, triples for 3D points), `...LongArray` holds integers (for `EntityTypeLongArray` the `dsObjectType_e` of each entity, same length and order as the entity array), `...StrArray` holds strings, and `EntitiesArray` holds entity objects. In C# pass entity arrays as `DispatchWrapper[]` (`new DispatchWrapper(dsCircle)` per element), as every shipped C# and VB.NET example does, so each element marshals as IDispatch. Getters declared `object` return arrays as `object`: cast to `object[]`, `double[]` or `int[]` in C# after a null check; in VBA assign to a `Variant`, test `IsArray`, and loop `LBound` to `UBound`. `ISketchManager.GetEntities` returns its entities and their `dsObjectType_e` codes through two out arrays; use `IApplication.GetObjectType` for a single object.
Verify: `swapi.py doc ISketchManager.GetEntities`; `swapi.py example "Rotate and Copy Entities Example (C#)"`.
## Units and coordinates
Failure: values converted to millimeters or degrees by habit, producing entities at the wrong size or angle.
Rule: coordinates and lengths are drawing units, exactly the numbers a user types in the command window; the API never converts them to the document's length unit, which only affects display (`IDocument.GetLengthUnitExpression`). Angles are radians (`InsertArc` StartAngle and EndAngle, `InsertSimpleNote` Angle, `RotateEntities` RotateAngle); convert with `deg * Pi / 180`. Z is 0 for 2D work. When the drawing uses a custom coordinate system, read the member's Remarks to see which system its points use.
Verify: `swapi.py doc ISketchManager.InsertArc`.
## Model and sheets
Failure: entities appear on the wrong layout, or code that iterates the "drawing" misses everything in paper space.
Rule: model space is `IDocument.GetModel` then `IModel.GetSketchManager`; each layout is an `ISheet` from `GetSheets2` or `GetSheet(name)` with its own `ISheet.GetSketchManager`. Insert into the space the user named, and when you enumerate entities, enumerate model space and every sheet. Activate a sheet with `ISheet.Activate` only when the user should see it, and restore the previously active sheet (`ISheet.IsActive`) afterwards.
Verify: `swapi.py example "Activate Sheets Example (VBA)"`; `swapi.py members ISheet`.
## Layers, colors and styles
Failure: assigning a layer, line style or text style by a name that does not exist fails or leaves the entity on layer 0; changing the active layer surprises the user afterwards.
Rule: get or create layers through `IDocument.GetLayerManager` (`GetLayer`, then `CreateLayer` with its `dsCreateObjectResult_e`), then assign the name to the entity's `Layer` property or through `IEntityHelper.SetLayer`. Line styles must be loaded (`ILineStyleManager.LoadLineStyle`) before use. Colors are `IColor` objects from `IApplication.GetNamedColor`, `GetColorByIndex` or `GetRGBColor`, not integers. New entities go on the drawing's current layer, as they do in the UI, so either set `Layer` on each entity or record `ILayerManager.GetActiveLayer`, `ILayer.Activate` yours, and reactivate the original at the end.
Verify: `swapi.py doc ILayerManager.CreateLayer`; `swapi.py sig IApplication.GetRGBColor`.
## Saving
Failure: the user's drawing is overwritten, saved in a format their other tools cannot read, or the save fails and the script reports success.
Rule: write to a new path unless the user asked to save in place. Call `IDocument.SaveAs2(Name, dsDocumentSaveAsOption_e, Overwrite, out Errors)` with an explicit format (`dsDocumentSaveAs_R2018_DWG`, a `..._DXF` member for DXF) and decide Overwrite deliberately; check Errors. `IDocument.Save` returns its `dsDocumentSaveError_e` directly. Check `IDocument.IsReadOnly` first; unlike `IsDirty`, it answers through an out Boolean (`dsDoc.IsReadOnly readOnly`), and `check` flags `IsReadOnly()`. Close documents you opened with `IApplication.CloseDocument(path, SaveChanges)` and leave documents the user had open.
Verify: `swapi.py enum dsDocumentSaveAsOption_e`; `swapi.py doc IDocument.SaveAs2`.
## Undo and batch work
Failure: one script run creates hundreds of undo steps, or a batch over many files leaves documents open and memory growing.
Rule: on 2019 and later wrap bulk edits in `ISketchManager.StartUndoRecord` and `StopUndoRecord` so one undo reverts them, calling Stop in a finally or error handler. In batches open each file with `OpenDocument2`, process, save to the output path, close it, and continue after a failure while recording it; report the failures at the end. `dsDocumentOpen_Hidden` and `dsDocumentOpen_ReadOnly` open files the user does not need to see or change.
Verify: `swapi.py sig ISketchManager.StartUndoRecord`; `swapi.py enum dsDocumentOpenOption_e`.
## .NET runtime and COM
Failure: a .NET 6 or 8 console app fails to compile `Marshal.GetActiveObject`, an add-in never appears in DraftSight, or a long batch leaks COM objects.
Rule: target .NET Framework 4.8 (`net48`) and x64 for EXEs and add-ins; `Marshal.GetActiveObject` does not exist in .NET 5 and later, and the SDK projects register add-ins with the 64-bit `RegAsm /codebase`. Reference `DraftSight.Interop.dsAutomation.dll` (and `DraftSight.Interop.dsAddin.dll` for add-ins) from `install_dir\APISDK\tlb`; the SDK projects embed interop types. An add-in class is `ComVisible(true)` with its own `Guid`, implements `DsAddin` (`ConnectToDraftSight`, `DisconnectFromDraftSight`), uses its GUID string as the `ApiUuid` for every command and UI element, and calls `IApplication.RemoveUserInterface` with it on disconnect. In standalone batches release per-file COM objects with `Marshal.ReleaseComObject`; never release the application object an add-in received. Registration and the `addinConfigs` XML are in [dotnet.md](dotnet.md).
Verify: `swapi.py doc IDsAddin.ConnectToDraftSight`; `swapi.py topic "Getting Started"`.
## VBA declarations
Failure: overflow on counts above 32,767, typos that only surface at run time, or "User-defined type not defined".
Rule: start modules with `Option Explicit`, reference the DraftSight type library (`install_dir\bin\dsAutomation.dll`) and declare objects early bound (`Dim dsDoc As DraftSight.Document`); use `Long` for every integer and `Variant` for every array the API returns or takes. Connect with `GetObject(, "DraftSight.Application")`, which fails with error 429 when DraftSight is not running; trap that and tell the user to start DraftSight.
Verify: `swapi.py example "Activate Sheets Example (VBA)"`.
