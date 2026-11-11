---
title: "IApplication Interface Members"
project: ""
interface: "IApplication_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html"
---

# IApplication Interface Members

The following tables list the members exposed by [IApplication](Interop.dsAutomation~Interop.dsAutomation.IApplication.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | IsResetDrawingScales | Gets or sets whether to enable the Reset Drawing Scales option. |
| Property | TemporaryEntityMode | Gets or sets temporary entity mode on or off. |
| Property | Visible | Gets or sets whether to show the DraftSight application. |
| Property | WindowState | Gets or sets the state of the DraftSight application window. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AbortRunningCommand | Aborts the command that is executing. |
| Method | AddCommandContextMenu | Adds a menu item to the specified command's context-sensitive menu. |
| Method | AddDefaultContextMenu | Adds a menu item to the DraftSight default context-sensitive menu. |
| Method | AddMenu | Obsolete. Superseded by IWorkspace::AddMenu . |
| Method | AddObjectContextMenu | Adds a menu item to the specified object type's context-sensitive menu. |
| Method | AddToolbar | Obsolete. Superseded by IWorkspace::AddToolbar . |
| Method | AddWorkspace | Adds the specified workspace to the list of DraftSight user-interface workspaces. |
| Method | CloseDocument | Closes the specified document. |
| Method | CreateColorPicker | Gets access to the DraftSight color picker, which allows users to assign standard and custom LineColors directly to entities, by Layer , or by Block . |
| Method | CreateCommand | Obsolete. Superseded by IApplication::CreateCommand2 . |
| Method | CreateCommand2 | Obsolete. Superseded by IApplication::CreateCommand3 and IApplication::CreateCommand4 . |
| Method | CreateCommand3 | Creates the specified command for the command window with support for the specified context-sensitive (F1) help. |
| Method | CreateCommand4 | Creates the specified command for the command window with support for the specified context-sensitive (F1) help. |
| Method | CreateCustomPropertyControl | Obsolete. Superseded by IApplication::CreateCustomPropertyControl2 . |
| Method | CreateCustomPropertyControl2 | Creates a custom tab. |
| Method | CreateLineStyle | Creates a simple LineStyle . |
| Method | CreateTracker | Creates a tracker, the mechanism that draws temporary entities along the cursor's path when prompting a user for a value, keyword, or selection. |
| Method | CreateUserCommand | Creates a command for a menu item and toolbar. |
| Method | ExitApplication | Exits DraftSight. |
| Method | ExportToSvg | Obsolete. Superseded by IApplication::ExportToSvg2 . |
| Method | ExportToSvg2 | Exports the specified drawing file to the specified SVG file. |
| Method | GetActiveDocument | Gets the active document. |
| Method | GetActiveWorkspace | Gets the active workspace for the DraftSight user interface. |
| Method | GetApplicationOptions | Gets access to DraftSight application options. |
| Method | GetColorByIndex | Gets the LineColor using the specified index within the Standard Colors. |
| Method | GetCommandMessage | Gets the message in the command window. |
| Method | GetContextMenuItems | Gets the top-level context-sensitive menu items added by IApplication::AddCommandContextMenu , IApplication::AddDefaultContextMenu , and IApplication::AddObjectContextMenu . |
| Method | GetDocuments | Gets the open documents. |
| Method | GetDrawingSupportFiles | Gets access to the DraftSight options that get and set default paths and file names for these drawing-support files: alternate font, drawing, drawing template, external references, font mapping, library, LineStyle, and RichLineStyle. |
| Method | GetEntityHelper | Gets the IEntityHelper interface. |
| Method | GetFileDialogManager | Gets a file dialog manager. |
| Method | GetHWND | Gets the DraftSight application window handle. |
| Method | GetHWND64 | Gets the 64-bit window handle of this DraftSight application. |
| Method | GetInterfaceFiles | Gets access to the DraftSight options that get and set default paths for these user-interface files: alias, custom icon, main customization, and custom menu. |
| Method | GetLanguage | Gets the name of the language supported by this DraftSight installation. |
| Method | GetLineStyleListFromFile | Gets the names of the simple LineStyles and their descriptions contained in the specified LineStyle file. |
| Method | GetMacroManager | Gets the macro manager, which manages macro recording and which is available in DraftSight Premium only. |
| Method | GetMainWindow | Gets the DraftSight application window. |
| Method | GetMathUtility | Gets the IMathUtility interface. |
| Method | GetMenuItems | Obsolete. Superseded by IWorkspace::GetMenuItems . |
| Method | GetMessageFolder | Gets the path of DraftSight's messages folder. |
| Method | GetNamedColor | Gets the named LineColor. |
| Method | GetObjectType | Gets the type of specified object. |
| Method | GetPreviewBitmap | Gets the preview bitmap of the specified document. |
| Method | GetPreviewBitmapBytes | Gets a byte array of the preview bitmap for the specified document. |
| Method | GetPreviewBitmapFile | Gets the preview bitmap of the specified document and saves it as a Windows bitmap file (. bmp ) using the specified file name. |
| Method | GetPreviewOfEntities | Creates a preview bitmap of the specified entities and returns a byte array of the bitmap. |
| Method | GetPrintManager | Gets the interface for printing. |
| Method | GetProfileManager | Gets the interface to the Profile Manager. |
| Method | GetRecentFiles | Gets the paths and file names of the files most recently opened in DraftSight. |
| Method | GetReferenceManager | Gets a Reference Manager object. |
| Method | GetRGBColor | Gets the LineColor for the specified RGB (Red, Green, Blue) color model values. |
| Method | GetRunningCommand | Gets the name of the executing command. |
| Method | GetSystemFiles | Gets access to the DraftSight options that get and set these system files: dictionary, font, Help, log, and support. |
| Method | GetToolbars | Obsolete. Superseded by IWorkspace::GetToolbars . |
| Method | GetVersion | Gets the version of DraftSight. |
| Method | GetWebLink | Gets the web URL of the landing page of an online HTML help system. |
| Method | GetWorkspace | Gets the specified workspace for the DraftSight user interface. |
| Method | GetWorkspaces | Gets all workspaces in the specified user-interface state. |
| Method | IsTemporaryEntity | Gets whether the specified entity is a temporary entity. |
| Method | IsWebHelpEnabled | Gets whether DraftSight web help is enabled. |
| Method | NewDocument | Creates a new document using the specified template. |
| Method | OpenChmHelp | Opens the specified help topic in the specified CHM file. |
| Method | OpenDocument | Obsolete. Superseded by IApplication::OpenDocument2 . |
| Method | OpenDocument2 | Opens the specified document. |
| Method | OpenHelp | Opens the specified system help topic in the specified system help. |
| Method | OpenWebHelp | Opens the specified web help URL. |
| Method | Recover | Recovers a damaged drawing file. |
| Method | RegisterOnIdleNotify | Post an event to the event queue. |
| Method | RemoveCommand | Removes the specified command. |
| Method | RemoveUserInterface | Removes an add-in's user interface from the DraftSight user interface. |
| Method | RunCommand | Obsolete. Superseded by IApplication::RunCommand2 . |
| Method | RunCommand2 | Runs the specified command. |
| Method | RunScript | Runs the specified script. |
| Method | Zoom | Zooms to a region of the drawing determined by the specified range and entities. |

[Top](#topBookmark)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event ActiveDocumentChangedNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ActiveDocumentChangedNotifyEventHandler.html)
[IApplication Event DestroyNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_DestroyNotifyEventHandler.html)
[IApplication Event FileNewNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileNewNotifyEventHandler.html)
[IApplication Event FileOpenPostNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPostNotifyEventHandler.html)
[IApplication Event FileOpenPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPreNotifyEventHandler.html)
