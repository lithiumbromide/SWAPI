# .NET EXEs and add-ins
C# and VB.NET code reaches DraftSight either as a standalone EXE that attaches to a running DraftSight, or as an add-in DLL that DraftSight loads and that adds commands, menus, toolbars and event handlers. Both use the primary interop assemblies in `install_dir\APISDK\tlb`.
## Contents
- [Project settings](#project-settings)
- [Standalone EXE](#standalone-exe)
- [Add-in class](#add-in-class)
- [Commands and user interface](#commands-and-user-interface)
- [Registration](#registration)
- [Events](#events)
- [VB.NET](#vbnet)
## Project settings
- Target .NET Framework 4.8 (`net48`), platform x64 (or AnyCPU with Prefer32Bit off), because `Marshal.GetActiveObject` and `RegAsm /codebase` exist only in .NET Framework and DraftSight is a 64-bit process.
- Reference `DraftSight.Interop.dsAutomation.dll` and, for add-ins, `DraftSight.Interop.dsAddin.dll` from `install_dir\APISDK\tlb` (typically `C:\Program Files\Dassault Systemes\DraftSight\APISDK\tlb`). The SDK projects set Embed Interop Types to true; keep that, so the build does not ship or version-lock the interop DLLs.
- After upgrading DraftSight, re-point the references at the new `tlb` folder and rebuild, as the Getting Started topic requires.
- The templates are SDK-style projects: [DraftSightTool.csproj](../assets/csharp-standalone/DraftSightTool.csproj) and [DraftSightAddin.csproj](../assets/csharp-addin/DraftSightAddin.csproj). Pass `-p:DraftSightTlb=<folder>` when DraftSight is installed elsewhere.
## Standalone EXE
[assets/csharp-standalone/Program.cs](../assets/csharp-standalone/Program.cs) is a batch tool: it attaches to the running DraftSight with `Marshal.GetActiveObject("DraftSight.Application")`, calls `AbortRunningCommand`, opens every DWG in a folder with `OpenDocument2` and `dsDocumentOpen_ReadOnly`, reads model-space entities with `ISketchManager.GetEntities`, exports each drawing to PDF with `IDocumentExporter.CreateExportSettings` and `ExportToPdf2`, closes it with `CloseDocument`, and returns a non-zero exit code when any file failed. The shipped C# examples are console programs of the same shape (`swapi.py examples --lang csharp`).
- `[STAThread]` on `Main`, because the COM objects are apartment-threaded.
- `Marshal.GetActiveObject` throws `COMException` when DraftSight is not running; the help documents only attaching to a running instance, so tell the user to start DraftSight and open what the tool needs.
- Release per-file objects (`Document`, `Model`, `SketchManager`, entity arrays) with `Marshal.ReleaseComObject` in long batches, and the application object at exit.
## Add-in class
[assets/csharp-addin/DsAddin.cs](../assets/csharp-addin/DsAddin.cs) is a minimal add-in: a `ComVisible(true)` class with a fixed `Guid` that implements `DsAddin` from `DraftSight.Interop.dsAddin`.
- `ConnectToDraftSight(object DsApp, int Cookie)` receives the application; cast it to `DraftSight.Interop.dsAutomation.Application`, build commands and UI, and return true. Returning false or throwing leaves the add-in inactive.
- `DisconnectFromDraftSight()` removes the UI with `IApplication.RemoveUserInterface(ApiUuid)`, detaches event handlers and drops references; return true.
- Use the class GUID as a string (`GetType().GUID.ToString()`) for every `ApiUuid` argument, so DraftSight can remove everything the add-in created.
- Never call `AbortRunningCommand` inside command or event handlers, because the add-in's own command is the one running ([running commands](correctness-rules.md#running-commands)).
## Commands and user interface
- Command-window commands: `IApplication.CreateCommand4(ApiUuid, GlobalCmdName, LocalCmdName, HelpID, ProductID, out dsCreateCommandError_e)` (2019 and later; `CreateCommand3` takes one name). HelpID and ProductID only select the F1 help topic, so pass 0 for both when the add-in has no help file. Attach the handler to the returned command's `ExecuteNotify` event (`_ICommandEvents.ExecuteNotify`); keep a reference to the command object for the add-in's lifetime, or the handler is collected.
- Global names conventionally start with an underscore (`_MYCMD`) and stay English; local names are what users type in their language.
- Menu and toolbar items run a user command: `IApplication.CreateUserCommand(ApiUuid, UserCmdName, CmdString, Description, SmallIcon, LargeIcon, dsUIState_e, out Error)` with `CmdString` set to `"^C^C" + GlobalCmdName`, then insert it with `IMenuItem.InsertMenuItem` or `IToolbar.InsertToolbarItem` using `IUserCommand.GetID()`.
- Menus and toolbars belong to a workspace: `IApplication.GetActiveWorkspace()` then `IWorkspace.AddMenu(ApiUuid, Position, MenuName)` and `AddToolbar(ApiUuid, ToolBarName)` (2017 and later). Ribbon UI uses `IWorkspace.AddRibbonTab` and `AddRibbonPanel`. The `IApplication.AddMenu` and `AddToolbar` used by older samples are obsolete.
- `dsUIState_Document` adds items to the user interface shown while a drawing is open, `dsUIState_Frame` to the one shown with no drawing open; most add-ins use `dsUIState_Document`.
## Registration
1. Build, then register the DLL for COM from an elevated prompt with the 64-bit framework tool: `%WINDIR%\Microsoft.NET\Framework64\v4.0.30319\RegAsm.exe /codebase DraftSightAddin.dll` (`dotnet build -p:RegisterAddin=true` from an elevated prompt runs it after the template builds). Unregister with `/u`. Replace the zero GUID in [DsAddin.cs](../assets/csharp-addin/DsAddin.cs) first; the template refuses to connect while it is empty.
2. Create `%PROGRAMDATA%\Dassault Systemes\DraftSight\addinConfigs` if missing and copy [DraftSightAddin.xml](../assets/csharp-addin/DraftSightAddin.xml) into it, named after the project, with `com clsid` set to the class GUID without braces, as the add-ins DraftSight installs write it. `startup="1"` lists the add-in in Tools > Add-Ins; `premiumOnly="2"` loads it only in DraftSight Premium and `premiumOnly="1"` in Pro and Premium.
3. In DraftSight open Tools > Add-Ins, tick Active (and Start Up to load it with DraftSight).

Templates created with the SDK's Visual Studio extension (`APISDK\DraftSightAddin2022VS`) generate the same XML and registration. A missing add-in in Tools > Add-Ins means the XML is not in `addinConfigs` or its CLSID differs from the class GUID; an add-in that appears but does not activate means the COM registration failed or `ConnectToDraftSight` returned false.
## Events
- Application events are on the application object: `dsApp.FileOpenPostNotify += new _IApplicationEvents_FileOpenPostNotifyEventHandler(OnOpen)`; document events on each `Document` (`ModifyNotify`, `FileSavePreNotify`, `FileSavePostNotify2`, `DestroyNotify`); command events on each `Command`.
- List them with `swapi.py members _IApplicationEvents` (also `_IDocumentEvents`, `_ICommandEvents`, `_ISelectionManagerEvents`, `_ITrackerEvents`, `_ICustomPropertyControlEvents`, `_ILispFunctionEvents`) and read the delegate signature with `sig`.
- Attach document handlers when a document opens or becomes active (`FileOpenPostNotify`, `FileNewNotify`, `ActiveDocumentChangedNotify`) and detach them in `DestroyNotify` and on disconnect; handlers left attached keep documents alive.
- Keep handlers short and never show modal UI from `*PreNotify` handlers during saves or opens.
## VB.NET
The same project settings apply. Connect with `DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)` or `GetObject(, "DraftSight.Application")`, attach events with `AddHandler dsApp.FileOpenPostNotify, AddressOf OnOpen`, and pass entity arrays as `DispatchWrapper()` like C#. Every shipped C# example has a VB.NET twin (`swapi.py examples --lang vbnet`).
