# .NET add-ins and standalone applications
How to structure C# and VB.NET add-ins (CommandManager, task panes, PropertyManager pages, events) and standalone EXEs, based on the templates in [../assets/csharp-addin/](../assets/csharp-addin/) and [../assets/csharp-standalone/](../assets/csharp-standalone/).
## Contents
- [Choosing the host](#choosing-the-host)
- [Project and interop references](#project-and-interop-references)
- [Add-in anatomy](#add-in-anatomy)
- [Registration and debugging](#registration-and-debugging)
- [CommandManager](#commandmanager)
- [Task panes and other hosted controls](#task-panes-and-other-hosted-controls)
- [PropertyManager pages](#propertymanager-pages)
- [Events](#events)
- [Standalone applications](#standalone-applications)
- [VB.NET differences](#vbnet-differences)
- [Distribution](#distribution)
## Choosing the host
- Add-in (DLL loaded into the SOLIDWORKS process): fastest API calls, native menus, toolbars, task panes and PropertyManager pages. SOLIDWORKS hosts the .NET Framework runtime, so in-process add-ins target .NET Framework 4.8 (`net48`) and x64; .NET 5 and later cannot be loaded as add-ins.
- Standalone EXE (out-of-process): batch jobs, schedulers and external tools. Every call crosses process boundaries, so wrap call sequences in `ISldWorks.CommandInProgress` ([batch performance](correctness-rules.md#batch-performance)). It may target `net48` or `net8.0-windows`.
- VSTA macro: quick automation inside SOLIDWORKS, not for distribution ([VSTA macros](vba-macros.md#vsta-macros)).
- Reading properties, configurations or references of many files without geometry: Document Manager ([document-manager.md](document-manager.md)).
## Project and interop references
- Reference the primary interop assemblies from `install_dir\api\redist`: `SolidWorks.Interop.sldworks`, `SolidWorks.Interop.swconst`, and for add-ins `SolidWorks.Interop.swpublished` (`ISwAddin`, PropertyManager handler interfaces). Add-on APIs ship their own interops, for example `SolidWorks.Interop.swdocumentmgr` and `SolidWorks.Interop.cosworks`.
- The templates read the folder from the MSBuild property `$(SolidWorksApiRedist)`, defaulting to `C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\api\redist`; override it with `-p:SolidWorksApiRedist=...` or an environment variable of that name for other install folders or for building against an older release's interops ([versions.md](versions.md)).
- Set Embed Interop Types to False, as the SDK templates do: the code constructs coclasses (`new SwDMClassFactory()`) and subscribes to events through the `SldWorks` class type, which embedded interop types do not provide.
- Build x64 (`PlatformTarget`), because SOLIDWORKS and the Document Manager DLL are 64-bit.
- When the wrong interop version loads, the Fusion log viewer (`Fuslogvw.exe`) shows which assemblies .NET searched for and which it loaded.
## Add-in anatomy
- One public class implements `ISwAddin` and carries `[ComVisible(true)]` and a fixed `[Guid]`. Every class that implements a `SolidWorks.Interop.swpublished` interface (`ISwAddin`, `IPropertyManagerPage2Handler9`, `ISwComFeature`) needs `ComVisible(true)`. The template sets `[assembly: ComVisible(false)]` so that only these classes are registered.
- Replace both placeholder GUIDs in the template (`00000000-0000-0000-0000-000000000000` on the add-in, `...0001` on the task pane control) with new ones, because the GUID is the add-in's registry identity.
- `ISwAddin.ConnectToSW(ThisSW, Cookie)` runs when SOLIDWORKS loads the add-in: cast ThisSW to `ISldWorks`, keep the cookie (add-in ID), call `ISldWorks.SetAddinCallbackInfo2(0, this, cookie)` so SOLIDWORKS can call the menu callbacks on this object, build the UI and attach events, then return True. `ISldWorks.ExitApp` does not work inside `ConnectToSW`.
- `ISwAddin.DisconnectFromSW` runs before SOLIDWORKS unloads the add-in: remove command groups, delete task pane views, detach events, release `ISldWorks` and force garbage collection as the template does ([COM object lifetime](correctness-rules.md#com-object-lifetime)).
- Call the API only from the threads SOLIDWORKS calls you on (callbacks, event handlers, control events); keep long work short or show progress instead of starting worker threads that call the API.
## Registration and debugging
- `[ComRegisterFunction]` writes `HKLM\SOFTWARE\SolidWorks\Addins\{guid}` (default DWORD value, `Description`, `Title`) so the add-in appears in Tools > Add-Ins, and `HKCU\Software\SolidWorks\AddInsStartup\{guid}` (default DWORD 1) so it loads at startup. `[ComUnregisterFunction]` deletes both keys.
- Register from an elevated prompt with the 64-bit tool: `%WINDIR%\Microsoft.NET\Framework64\v4.0.30319\RegAsm.exe /codebase SolidWorksAddin.dll` (`/u` unregisters). The 32-bit RegAsm writes to the wrong registry view. The template's `RegisterAddin` target runs the same command after a build started with `-p:RegisterAddin=true` from an elevated shell.
- `/codebase` also registers the task pane control's ProgID, which `ITaskpaneView.AddControl` needs.
- Debug by setting the project's start action to `SLDWORKS.exe`. Registry and icon changes take effect after SOLIDWORKS restarts.
- Add-in Manager icons are PNG or BMP files named after the DLL with a size suffix (`MyAddin_20.png` up to `_128`) in the DLL folder, or an `Icon Path` value under the add-in key.
## CommandManager
- Get the add-in's single `ICommandManager` with `ISldWorks.GetCommandManager(cookie)`.
- `ICommandManager.CreateCommandGroup2(UserID, Title, ToolTip, Hint, Position, IgnorePreviousVersion, ref errors)` returns `ICommandGroup` and reports `swCreateCommandGroupErrors`. A Title such as `"&Help\\MyApp Help"` (C#) places the menu under an existing menu; otherwise it appears under Tools.
- SOLIDWORKS caches toolbar layouts in the registry per UserID. When the items of a group change, assign a new UserID, or call `ICommandManager.GetGroupDataFromRegistry` and pass IgnorePreviousVersion True when the stored IDs differ.
- `ICommandGroup.AddCommandItem2(Name, Position, Hint, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, UserID, MenuTBOption)` takes callback and enable method names as strings resolved on the object passed to `SetAddinCallbackInfo2`; the methods must be public. They take no parameters, or one string parameter written in the call string (`"OnCommand(1)"`) so one method can serve many items. Enable methods return 0 (disabled), 1 (enabled), 2 (selected, disabled) or 3 (selected, enabled).
- ImageListIndex is zero-based into `ICommandGroup.IconList` (six image sizes; `MainIconList` for the group icon); -1 is allowed only for `swMenuItem` items. Set `ICommandGroup.HasMenu` and `ICommandGroup.HasToolbar`, then call `ICommandGroup.Activate`.
- Remove groups in `DisconnectFromSW` with `ICommandManager.RemoveCommandGroup2(UserID, RuntimeOnly)`. Context menus come from `ICommandManager.AddContextMenu`; shortcut menus from `ISldWorks.RegisterThirdPartyPopupMenu` and `ISldWorks.AddItemToThirdPartyPopupMenu2`.
## Task panes and other hosted controls
- `ISldWorks.CreateTaskpaneView3(ImageList, ToolTip)` takes paths to six images (20, 32, 40, 64, 96, 128 pixels, PNG or BMP); the template expects `TaskPane_<size>.png` next to the DLL.
- `ITaskpaneView.AddControl(ProgID, "")` hosts an ActiveX control. A .NET `UserControl` qualifies when it is `ComVisible(true)`, has its own `[Guid]` and `[ProgId]`, a public parameterless constructor, and was registered with `RegAsm /codebase`; the returned object casts to the control class, which is how the template wires the button event.
- Without COM registration of the control, create the WinForms control yourself and pass its handle to `ITaskpaneView.DisplayWindowFromHandlex64`.
- Delete the view with `ITaskpaneView.DeleteView` in `DisconnectFromSW`.
- FeatureManager and model-view tabs use the same idea: `IModelViewManager.CreateFeatureMgrControl4`, `IModelViewManager.AddControl3` and `IModelViewManager.DisplayWindowFromHandlex64`.
## PropertyManager pages
- Implement `IPropertyManagerPage2Handler9` in a `ComVisible(true)` class, create the page with `ISldWorks.CreatePropertyManagerPage(Title, Options, Handler, out Errors)` (`swPropertyManagerPageOptions_e`, `swPropertyManagerPageStatus_e`), add group boxes with `IPropertyManagerPage2.AddGroupBox` and controls with `IPropertyManagerPage2.AddControl2` or `IPropertyManagerPageGroup.AddControl2`, then show it with `IPropertyManagerPage2.Show2`.
- Create pages with `swPropertyManagerOptions_LockedPage`: SOLIDWORKS can crash if a handler returns after the page has closed.
- Controls only hold live values while the page is visible; copy them into your own fields in handlers before the page closes.
## Events
- Application events: cast `ISldWorks` to the `SldWorks` class and subscribe with the delegate types, for example `((SldWorks)swApp).ActiveModelDocChangeNotify += new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnActiveModelChanged)`. Handlers return int (0).
- Document events are per instance: subscribe to each open `PartDoc`, `AssemblyDoc` or `DrawingDoc` and to documents opened later (`DSldWorksEvents_FileOpenPostNotifyEventHandler`, `DSldWorksEvents_FileNewNotify2EventHandler`), and drop them on `DPartDocEvents_DestroyNotify2EventHandler` and its assembly and drawing equivalents. The SDK template's `EventHandling.cs` implements this bookkeeping.
- Objects with events: `ISldWorks`, `IPartDoc`, `IAssemblyDoc`, `IDrawingDoc`, `IModelView`, `IFeatMgrView`, `IMouse`, `ITaskpaneView`, `ISWPropertySheet`, `IMotionStudy`. Unsubscribe everything in `DisconnectFromSW`.
- `swapi.py find FileOpenPostNotify --kind e` locates delegate signatures.
## Standalone applications
- Mark `Main` with `[STAThread]`. Attach to a running session with `Marshal.GetActiveObject("SldWorks.Application")`, or start one with `Activator.CreateInstance(Type.GetTypeFromProgID("SldWorks.Application"))`.
- A session your program starts closes when the program ends unless you hand it to the user with `ISldWorks.UserControl`; it can only be hidden while `UserControl` is False and no visible documents are open (closing behavior of background sessions is under [batch performance](correctness-rules.md#batch-performance)). The template calls `ISldWorks.ExitApp` only for sessions it started.
- Release per-file objects in loops ([COM object lifetime](correctness-rules.md#com-object-lifetime)) and pass the full path to `ISldWorks.CloseDoc`.
- For `net8.0-windows`: reference the same interop DLLs by HintPath. `Marshal.GetActiveObject` does not exist in .NET 5 and later, so attach through the running object table yourself or start SOLIDWORKS with `Activator.CreateInstance`. Add-ins still require `net48`.
## VB.NET differences
- Attributes use angle brackets (`<ComVisible(True)>`, `<Guid("...")>`), the class declares `Implements ISwAddin`, and events are wired with `AddHandler`.
- Parameterized properties are called directly (`swExt.CustomPropertyManager("")`), while C# uses accessor methods (`swExt.get_CustomPropertyManager("")`).
- VB.NET `Integer` is 32-bit like C# `int`, unlike VBA `Integer`. By-reference error arguments are plain variables passed to ByRef parameters.
- The SDK installs a `SwVBAddin` project template alongside `SwCSharpAddin`; the C# templates here translate line by line.
## Distribution
- Ship the add-in DLL, its icons, and `SolidWorksTools.dll` if you use the SDK template's `BitmapHandler`. An installer either runs RegAsm `/codebase` or writes the COM registration plus the `Addins` keys (default value, `Description`, `Title`) itself; the help walks through a Visual Studio Installer Projects setup.
- Build against the oldest interop release you support and keep every member's `since` within that release ([version availability](correctness-rules.md#version-availability)).
## Sources
- `markdown/sldworksapiprogguide/Overview/Using_SolidWorks_C__Add-In_Wizard_to_Create_C__Add-In.md`
- `markdown/sldworksapiprogguide/Overview/SolidWorks_CSharp_and_VB.NET__Project_Templates.md`
- `markdown/sldworksapiprogguide/Overview/Using_SolidWorks_VB.NET_Add-In_Wizard_to_Create_VB.NET_Add-In.md`
- `markdown/sldworksapiprogguide/Overview/Using_SwAddin_to_Create_a_SolidWorks_Addin.md`
- `markdown/sldworksapiprogguide/Overview/Add-in_Callbacks.md`
- `markdown/sldworksapiprogguide/Overview/Add-in_Toolbars.md`
- `markdown/sldworksapiprogguide/Overview/Add-in_Icons.md`
- `markdown/sldworksapiprogguide/Overview/Add-in_Shortcut_Menus.md`
- `markdown/sldworksapiprogguide/Overview/CommandManager_and_CommandGroups.md`
- `markdown/sldworksapiprogguide/Overview/Using_PropertyManagerPage2_and_the_Related_Objects.md`
- `markdown/sldworksapiprogguide/Overview/Events.md`
- `markdown/sldworksapiprogguide/Overview/Programming_Events.md`
- `markdown/sldworksapiprogguide/Overview/ComVisibleAttribute_in_VSTA_macros.md`
- `markdown/sldworksapiprogguide/Overview/Monitor_Loading_of_.NET_Interop_Assemblies.md`
- `markdown/sldworksapiprogguide/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.md`
- `markdown/sldworksapiprogguide/Overview/Instantiate_ActiveX_Controls_as_Tabs.md`
- `markdown/sldworksapiprogguide/GettingStarted/Visual_C__Standalone_and_Add-in_Applications.md`
- `markdown/sldworksapiprogguide/GettingStarted/Visual_Basic_.NET_Standalone_and_Add-in_Applications.md`
- `markdown/sldworksapiprogguide/Miscellaneous/Create_Setup_Project_to_Distribute_SolidWorks_Add-in.md`
- `markdown/swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin.md`
- `markdown/swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin~ConnectToSW.md`
- `markdown/swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin~DisconnectFromSW.md`
- `markdown/sldworksapi/Connect_to_SOLIDWORKS_Session_CSharp.md`
- `markdown/sldworksapi/Create_TaskPaneView_Add-in_Example_CSharp.md`
- `markdown/sldworksapi/Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddControl.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroupDataFromRegistry.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md`
