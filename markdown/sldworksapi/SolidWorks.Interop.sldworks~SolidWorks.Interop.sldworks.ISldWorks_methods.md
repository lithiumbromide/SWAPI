---
title: "ISldWorks Interface Methods"
project: "SOLIDWORKS API Help"
interface: "ISldWorks_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_methods.html"
---

# ISldWorks Interface Methods

For a list of all members of this type, see[ISldWorks members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateDoc | Obsolete. Superseded by ISldWorks::ActivateDoc2 and ISldWorks::IActivateDoc3 . |
| Method | ActivateDoc2 | Obsolete. Superseded by ISldWorks::ActivateDoc3 . |
| Method | ActivateDoc3 | Activates a loaded document and rebuilds it as specified. |
| Method | ActivateTaskPane | Activates the specified task pane. |
| Method | AddCallback | Registers a general purpose callback handler. |
| Method | AddFileOpenItem | Obsolete. Superseded by ISldWorks::AddFileOpenItem3 . |
| Method | AddFileOpenItem2 | Obsolete. Superseded by ISldWorks::AddFileOpenItem3 . |
| Method | AddFileOpenItem3 | Adds file types to the File > Open dialog box. |
| Method | AddFileSaveAsItem | Obsolete. Superseded by ISldWorks::AddFileSaveAsItem2 . |
| Method | AddFileSaveAsItem2 | Adds a file type to the SOLIDWORKS File > Save As dialog box. |
| Method | AddItemToThirdPartyPopupMenu | Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in. |
| Method | AddItemToThirdPartyPopupMenu2 | Adds menu items to a pop-up (shortcut) menu in a SOLIDWORKS add-in. |
| Method | AddMenu | Adds a menu item to a SOLIDWORKS menu for DLL applications. |
| Method | AddMenuItem | Obsolete. Superseded by ISldWorks::AddMenuItem3 . |
| Method | AddMenuItem2 | Obsolete. Superseded by ISldWorks::AddMenuItem3 . |
| Method | AddMenuItem3 | Obsolete. Superseded by ISldWorks::AddMenuItem4 . |
| Method | AddMenuItem4 | Obsolete. Superseded by ISldWorks::AddMenuItem5 . |
| Method | AddMenuItem5 | Adds a menu item and image to the SOLIDWORKS user interface. |
| Method | AddMenuPopupItem | Obsol ete. Superseded by ISldWorks::AddMenuPopupItem2 . |
| Method | AddMenuPopupItem2 | Obsolete. Superseded by ISldWorks::AddMenuPopupItem3 and ISldWorks::AddMenuPopupItem4 . |
| Method | AddMenuPopupItem3 | Adds a menu item and zero or more submenus to shortcut menus of entities of the specified type in documents of the specified type. |
| Method | AddMenuPopupItem4 | Adds a menu item and zero or more submenus to shortcut menus of features of the specified type in documents of the specified type. |
| Method | AddToolbar | Obsolete. Superseded by ISldWorks::AddToolbar4 . |
| Method | AddToolbar2 | Obsolete. Superseded by ISldWorks::AddToolbar4 . |
| Method | AddToolbar3 | Obsolete. Superseded by ISldWorks::AddToolbar4 . |
| Method | AddToolbar4 | Obsolete. Superseded by ISldWorks::AddToolbar5 . |
| Method | AddToolbar5 | Creates a Windows-style dockable toolbar. |
| Method | AddToolbarCommand | Obsolete. Superseded by ISldWorks::AddToolbarCommand2 . |
| Method | AddToolbarCommand2 | Specifies the application functions to call when a toolbar button is clicked or sets a separator. |
| Method | AllowFailedFeatureCreation | Sets whether to allow the creation of a feature that has rebuild errors. |
| Method | ArrangeIcons | Arranges the icons in SOLIDWORKS. |
| Method | ArrangeWindows | Arranges the open windows in SOLIDWORKS. |
| Method | BlockSkinning | Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window. |
| Method | CallBack | Allows an out-of-process executable or a SOLIDWORKS macro to call back a function in a SOLIDWORKS add-in DLL. |
| Method | CheckpointConvertedDocument | Saves the specified open document if its version is older than the version of the SOLIDWORKS product being used. |
| Method | CloseAllDocuments | Closes all open documents in the SOLIDWORKS session. |
| Method | CloseAndReopen | Closes and reopens the specified drawing document without unloading its references from memory. |
| Method | CloseAndReopen2 | Closes and reopens the specified drawing document without unloading its references from memory. |
| Method | CloseDoc | Closes the specified document. |
| Method | CloseUserNotification | Closes the specified user notification. |
| Method | Command | Opens the specified dialog or file. |
| Method | CopyAppearance | Copies the appearance of the specified entity to the clipboard. |
| Method | CopyDocument | Copies a document and optionally updates references to it. |
| Method | CreateNewWindow | Creates a client window containing the active document. |
| Method | CreatePropertyManagerPage | Creates a PropertyManager page. |
| Method | CreateTaskpaneView | Obsolete. Superseded by ISldworks::CreateTaskpaneView2 . |
| Method | CreateTaskpaneView2 | Obsolete. Superseded by ISldworks::CreateTaskpaneView3 . |
| Method | CreateTaskpaneView3 | Creates an application-level Task Pane view. |
| Method | DateCode | Obsolete. Superseded by ISldWorks::RevisionNumber . |
| Method | DefineAttribute | Creates an attribute definition, which is the first step in generating attributes. |
| Method | DefineMessageBar | Called by a SOLIDWORKS add-in, creates a message bar definition object. |
| Method | DefineUserNotification | Called by a SOLIDWORKS add-in, creates a user notification definition object. |
| Method | DisplayStatusBar | Sets whether to display the status bar. |
| Method | DocumentVisible | Allows the application to control the display of a document in a window upon creation or retrieval. |
| Method | DownloadFromMySolidWorksSettings | Downloads the specified SOLIDWORKS Connected settings to SOLIDWORKS Desktop. |
| Method | DragToolbarButton | Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or ICommandGroup toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar. |
| Method | DragToolbarButtonFromCommandID | Copies a button to a toolbar using a command ID. |
| Method | EnablePhotoWorksProgressiveRender | Obsolete. Not superseded. |
| Method | EnableStereoDisplay | Obsolete and not superseded. Functionality no longer implemented. |
| Method | EnumDocuments | Obsolete. Superseded by ISldWorks::EnumDocuments2 . |
| Method | EnumDocuments2 | Gets a list of documents currently open in the application. |
| Method | ExitApp | Shuts down SOLIDWORKS. |
| Method | ExportHoleWizardItem | Exports data for the specified Hole Wizard standard. |
| Method | ExportToolboxItem | Exports data for the specified Toolbox standard. |
| Method | Frame | Gets the SOLIDWORKS main frame. |
| Method | Get3DExperienceState | Gets the current state of SOLIDWORKS Connected . |
| Method | GetActiveConfigurationName | Gets the name of the active configuration in the specified SOLIDWORKS document. |
| Method | GetActiveDisplayPane | Gets the active Display Pane. |
| Method | GetAddInObject | Gets an add-in object for the specified SOLIDWORKS add-in. |
| Method | GetApplySelectionFilter | Gets the current state of the selection filter. |
| Method | GetBatchUploadedFilesInfo | Gets the files uploaded to 3DEXPERIENCE during a batch process. |
| Method | GetBuildNumbers | Obsolete. Superseded by ISldWorks::GetBuildNumbers2 . |
| Method | GetBuildNumbers2 | Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application. |
| Method | GetButtonPosition | Gets the center coordinates of the specified SOLIDWORKS toolbar button. |
| Method | GetCollisionDetectionManager | Gets the collision detection manager. |
| Method | GetColorTable | Gets a color table from the SOLIDWORKS application. |
| Method | GetCommandID | Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button). |
| Method | GetCommandManager | Gets the CommandManager for the specified add-in. |
| Method | GetConfigurationCount | Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed. |
| Method | GetConfigurationNames | Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed. |
| Method | GetCurrentFileUser | Gets the name of the user who has the the specified document open. |
| Method | GetCurrentLanguage | Gets the current language used by SOLIDWORKS. |
| Method | GetCurrentLicenseType | Gets the type of license for the current SOLIDWORKS session. |
| Method | GetCurrentMacroPathFolder | Gets the name of the folder where the macro resides. |
| Method | GetCurrentMacroPathName | Gets the path name for the macro currently running. |
| Method | GetCurrentWorkingDirectory | Gets the current working directory being used by the SOLIDWORKS application. |
| Method | GetDataFolder | Gets the data directory name currently used by SOLIDWORKS. |
| Method | GetDocumentCount | Gets the number of open documents in the current SOLIDWORKS session. |
| Method | GetDocumentDependencies | Obsolete. Superseded by ISldWorks::GetDocumentDependencies2 . |
| Method | GetDocumentDependencies2 | Gets all of the model dependencies for a document. |
| Method | GetDocumentDependenciesCount | Obsolete. Superseded by ISldWorks::IGetDocumentDependenciesCount2 . |
| Method | GetDocuments | Gets the open documents in this SOLIDWORKS session. |
| Method | GetDocumentTemplate | Gets the name of document template that can be used in ISldWorks::NewDocument or ISldWorks::INewDocument2 . |
| Method | GetDocumentVisible | Gets the visibility of the document to open. |
| Method | GetEnvironment | Gets the IEnvironment object. |
| Method | GetErrorMessages | Gets the last 20 messages issued by SOLIDWORKS in the current SOLIDWORKS session. |
| Method | GetExecutablePath | Gets the path to the SOLIDWORKS executable, sldworks.exe . |
| Method | GetExportFileData | Gets the data interface for the specified file type to which to export one or more drawing sheets. |
| Method | GetFilePLMID | Gets the Product Lifecycle Management (PLM) ID of the specified file stored in 3DEXPERIENCE. |
| Method | GetFirstDocument | Gets the document opened first in this SOLIDWORKS session. |
| Method | GetGtolFormatData | Gets the Gtol format and XML schema versions supported by this version of SOLIDWORKS. |
| Method | GetGtolFrameXMLSchema | Gets the XML schema for Gtol frame symbol XML. |
| Method | GetHoleStandardsData | Gets the hole standards for the specified hole type. |
| Method | GetImageSize | Gets: small, medium, and large image sizes suitable for the current DPI setting of the display device. default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting. |
| Method | GetImportFileData | Gets the IGES or DXF/DWG import data for the specified file. |
| Method | GetInterfaceBrightnessThemeColors | Gets the theme and colors of the SOLIDWORKS background. |
| Method | GetLastSaveError | Gets the last save error issued by Microsoft in the current session. |
| Method | GetLastToolbarID | Gets the ID of the last toolbar added to the CommandManager . |
| Method | GetLatestSupportedFileVersion | Gets the version number that this instance of SOLIDWORKS reads and writes. |
| Method | GetLineStyles | Gets all of the line styles in the specified file. |
| Method | GetLocalizedMenuName | Gets a localized menu name for the specified menu ID. |
| Method | GetMacroMethods | Gets the names of the modules in the specified macro. |
| Method | GetMassProperties | Obsolete. Superseded by ISldWorks::GetMassProperties2 and ISldWorks::IGetMassProperties2 . |
| Method | GetMassProperties2 | Gets the mass properties from the specified document for the specified configuration. |
| Method | GetMaterialDatabaseCount | Gets the number of material databases. |
| Method | GetMaterialDatabases | Gets the names of the material databases. |
| Method | GetMaterialSchemaPathName | Gets the path for the XML material schema file. |
| Method | GetMathUtility | Gets IMathUtility . |
| Method | GetMenuStrings | Gets the name of the parent menu of the specified menu command. |
| Method | GetModeler | Gets the IModeler interface. |
| Method | GetMouseDragMode | Gets whether the specified command-mouse mode is in effect. |
| Method | GetOpenDocSpec | Gets the specifications to use when opening a model document. |
| Method | GetOpenDocument | Gets the open document with the specified name. |
| Method | GetOpenDocumentByName | Gets the open document with the specified name. |
| Method | GetOpenedFileInfo | Gets the name of the last model successfully opened by SOLIDWORKS and the options that were in effect when it opened. |
| Method | GetOpenFileName | Obsolete. Superseded by ISldWorks::GetOpenFileName2 . |
| Method | GetOpenFileName2 | Prompts the user for the name of the file to open. |
| Method | GetPreviewBitmap | Gets the preview bitmap (.bmp) for the specified configuration, regardless if the SOLIDWORKS document is open or closed. |
| Method | GetPreviewBitmapFile | Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the specified filename. |
| Method | GetProcessID | Gets the process ID for the current SOLIDWORKS session. |
| Method | GetRayTraceRenderer | Get a ray-trace rendering engine. |
| Method | GetRecentFiles | Gets a list of the most recently used files. |
| Method | GetRoutingSettings | Gets routing settings. |
| Method | GetRunningCommandInfo | Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the user-interface. |
| Method | GetSafeArrayUtility | Gets the ISafeArrayUtility object. |
| Method | GetSaveTo3DExperienceOptions | Initializes save options for a SOLIDWORKS Connected document. |
| Method | GetSearchFolders | Gets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents . |
| Method | GetSelectionFilter | Gets the current selection filter settings for the specified item type. |
| Method | GetSelectionFilters | Gets all active selection filters. |
| Method | GetSSOFormattedURL | Formats the specified URL for single sign-on. |
| Method | GetTemplateSizes | Gets the sheet properties from a template document. |
| Method | GetToolbarDock | Obsolete. Superseded by ISldWorks::GetToolbarDock2 . |
| Method | GetToolbarDock2 | Gets the docking state of the toolbar. |
| Method | GetToolbarState | Obsolete. Superseded by ISldWorks::GetToolbarState2 . |
| Method | GetToolbarState2 | Gets the state of the toolbar. |
| Method | GetToolbarVisibility | Gets whether this toolbar is visible. |
| Method | GetUserPreferenceDoubleValue | Gets system default user preference values. |
| Method | GetUserPreferenceIntegerValue | Gets system default user preference values. |
| Method | GetUserPreferenceStringListValue | Gets the name of the DXF mapping file. |
| Method | GetUserPreferenceStringValue | Gets system default user preference values. |
| Method | GetUserPreferenceToggle | Gets document default user preference values. |
| Method | GetUserProgressBar | Gets a progress indicator. |
| Method | GetUserTypeLibReferenceCount | Gets the number of user-specified type library references. |
| Method | GetUserUnit | Gets an empty IUserUnit object of the specified type. |
| Method | HideBubbleTooltip | Hides the bubble ToolTip displayed by ISldWorks::ShowBubbleTooltipAt2 . |
| Method | HideToolbar | Obsolete. Superseded by ISldWorks::HideToolbar2 . |
| Method | HideToolbar2 | Hides a toolbar created with ISldWorks::AddToolbar5 . |
| Method | IActivateDoc | Obsolete. Superseded by ISldWorks::ActivateDoc2 and ISldWorks::IActivateDoc3 . |
| Method | IActivateDoc2 | Obsolete. Superseded by ISldWorks::ActivateDoc2 and ISldWorks::IActivateDoc3 . |
| Method | IActivateDoc3 | Activates a document that has already been loaded. This file becomes the active document, and this method returns a pointer to that document object. |
| Method | ICopyDocument | Copies a document and optionally updates references to it. |
| Method | ICreatePropertyManagerPage | Creates a PropertyManager page. |
| Method | IDefineAttribute | Creates an attribute definition, which is the first step in generating attributes. |
| Method | IEnableStereoDisplay | Obsolete and not superseded. Functionality no longer implemented. |
| Method | IGetColorTable | Gets a color table from the SOLIDWORKS application. |
| Method | IGetConfigurationNames | Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed. |
| Method | IGetDocumentDependencies | Obsolete. Superseded by ISldWorks::IGetDocumentDependencies2 . |
| Method | IGetDocumentDependencies2 | Gets all of the model dependencies for a document. |
| Method | IGetDocumentDependenciesCount2 | Gets the size of the array needed for a call to ISldWorks::IGetDocumetnDependencies2 . |
| Method | IGetDocuments | Gets the open documents is this SOLIDWORKS session. |
| Method | IGetEnvironment | Gets the IEnvironment object. |
| Method | IGetFirstDocument | Obsolete. Superseded by ISldWorks::IGetFirstDocument2 . |
| Method | IGetFirstDocument2 | Gets the document opened first in this SOLIDWORKS session. |
| Method | IGetMassProperties | Obsolete. Superseded by ISldWorks::GetMassProperties2 and ISldWorks::IGetMassProperties2 . |
| Method | IGetMassProperties2 | Gets the mass properties from the specified document for the specified configuration. |
| Method | IGetMaterialDatabases | Gets the names of the material databases. |
| Method | IGetMathUtility | Gets the IMathUtility interface. |
| Method | IGetModeler | Gets the IModeler interface. |
| Method | IGetOpenDocumentByName | Obsolete. Superseded ISldWorks::IGetOpenDocumentByName2 . |
| Method | IGetOpenDocumentByName2 | Gets the open document with the specified name. |
| Method | IGetRayTraceRenderer | Get a ray-trace rendering engine. |
| Method | IGetSelectionFilters | Gets all active selection filters. |
| Method | IGetSelectionFiltersCount | Gets the number of active selection filters. |
| Method | IGetTemplateSizes | Gets the sheet properties from a template document. |
| Method | IGetUserTypeLibReferences | Gets the specified user-specified type library references. |
| Method | IGetUserUnit | Gets an empty IUserUnit object of the specified type. |
| Method | IGetVersionHistoryCount | Gets the size of the array required to hold data returned by ISldWorks::IVersionHistory . |
| Method | IMoveDocument | Moves a document and optionally updates references to it. |
| Method | ImportHoleWizardItem | Imports data for the specified Hole Wizard standard. |
| Method | ImportToolboxItem | Imports data for the specified Toolbox standard. |
| Method | INewAssembly | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | INewDocument | Obsolete. Superseded by ISldWorks::INewDocument2 . |
| Method | INewDocument2 | Creates a new document based on the specified template. |
| Method | INewDrawing | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | INewDrawing2 | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | INewPart | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | InstallQuickTipGuide | Implements your add-in's copy of the Quick Tips . |
| Method | IOpenDoc | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | IOpenDoc2 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | IOpenDoc3 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | IOpenDoc4 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | IOpenDoc5 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | IOpenDocSilent | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | IRemoveUserTypeLibReferences | Removes the user-specified type library references. |
| Method | IsBackgroundProcessingCompleted | Gets whether SOLIDWORKS has finished background processing a drawing document that requires a lot of CPU time to open. |
| Method | IsCommandEnabled | Gets whether the specified command is enabled. |
| Method | ISetSelectionFilters | Sets the status for multiple selection filters. |
| Method | ISetUserTypeLibReferences | Sets the user-specified type library references. |
| Method | IsRapidDraft | Gets whether the specified drawing file is in SOLIDWORKS Detached format. |
| Method | IsSame | Gets whether the two specified objects are the same object. |
| Method | IsTaskPaneExpanded | Gets whether the Task Pane is expanded. |
| Method | IsTaskPaneVisible | Gets whether the Task Pane is visible. |
| Method | IVersionHistory | Gets a list of strings indicating the versions in which a model was saved. |
| Method | LoadAddIn | Loads the specified add-in in SOLIDWORKS. |
| Method | LoadAdminSettingsFile | Loads the specified *.sldsettings file into SOLIDWORKS Connected . |
| Method | LoadFile | Obsolete. Superseded by ISldWorks::LoadFile4 . |
| Method | LoadFile2 | Obsolete. Superseded by ISldWorks::LoadFile4 . |
| Method | LoadFile3 | Obsolete. Superseded by ISldWorks::LoadFile4 . |
| Method | LoadFile4 | Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect. |
| Method | MoveDocument | Moves a document and optionally updates references to it. |
| Method | NewAssembly | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | NewDocument | Creates a new document based on the specified template. |
| Method | NewDrawing | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | NewDrawing2 | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | NewPart | Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2 . |
| Method | OpenDoc | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | OpenDoc2 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | OpenDoc3 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | OpenDoc4 | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | OpenDoc6 | Opens an existing document and returns a pointer to the document object. |
| Method | OpenDoc7 | Opens an existing document and returns a pointer to the document object. |
| Method | OpenDocSilent | Obsolete. Superseded by ISldWorks::OpenDoc6 . |
| Method | PasteAppearance | Applies to the specified entity an appearance that has been copied to the clipboard. |
| Method | PostMessageToApplication | Posts a message to the application that invoked this method. |
| Method | PostMessageToApplicationx64 | Posts a message to the application that invoked this method in 64-bit applications. |
| Method | PreSelectDwgTemplateSize | Establishes which template to use when creating a drawing. |
| Method | PresetNewDrawingParameters | Presets the drawing template and sheet size parameters to avoid showing the Sheet Format/Size dialog when creating a new drawing document in the user-interface. |
| Method | PreviewDoc | Displays a preview of a document to the specified window. |
| Method | PreviewDocx64 | Displays a preview of a document to the specified window in 64-bit applications. |
| Method | QuitDoc | Closes the specified document without saving changes. |
| Method | RecordLine | Adds a line of code to a VBA macro and the SOLIDWORKS journal file. |
| Method | RecordLineCSharp | Adds a line of code to a C# macro and the SOLIDWORKS journal file. |
| Method | RecordLineVBnet | Adds a line of code to a VB.NET macro and the SOLIDWORKS journal file. |
| Method | RefreshQuickTipWindow | Tells the SOLIDWORKS application that your add-in's state has changed and triggers a query for the current URL page. |
| Method | RefreshTaskpaneContent | Refreshes the view of the Design Library tab in the Task Pane. |
| Method | RegisterThirdPartyPopupMenu | Registers a third-party pop-up (shortcut) menu. |
| Method | RegisterTrackingDefinition | Registers a tracking definition. |
| Method | RemoveCallback | Unregisters a general purpose callback handler. |
| Method | RemoveFileOpenItem | Obsolete. Superseded by ISldWorks::RemoveFileOpenItem2 . |
| Method | RemoveFileOpenItem2 | Removes a file type from the File > Open dialog box that was added using ISldWorks::AddFileOpenItem3 . |
| Method | RemoveFileSaveAsItem | Obsolete. Superseded by ISldWorks::RemoveFileSaveAsItem2 . |
| Method | RemoveFileSaveAsItem2 | Removes a file type from the File > Save As dialog box that was added using ISldWorks::AddFileSaveAsItem2 . |
| Method | RemoveFromMenu | Removes: the specified command from all main frame menus or a toolbar or both the specified command's parent menus |
| Method | RemoveFromPopupMenu | Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut menus and pop-up menus) for the specified document types. |
| Method | RemoveItemFromThirdPartyPopupMenu | Removes a menu item and icon from a third-party pop-up (shortcut) menu. |
| Method | RemoveMenu | Removes a menu item from the specified document frame. |
| Method | RemoveMenuPopupItem | Obsolete. Superseded by ISldWorks::RemoveMenuPopupItem2 . |
| Method | RemoveMenuPopupItem2 | Removes an item on a pop-up (shortcut) menu. |
| Method | RemoveToolbar | Obsolete. Superseded by ISldWorks::RemoveToobar2 . |
| Method | RemoveToolbar2 | Removes a toolbar created with ISldWorks::AddToolbar5 . |
| Method | RemoveUserMenu | Obsolete. Superseded by ISldWorks::RemoveMenu . |
| Method | RemoveUserTypeLibReferences | Removes the user-specified type library references. |
| Method | ReplaceReferencedDocument | Replaces a referenced document. |
| Method | ResetPresetDrawingParameters | Resets SOLIDWORKS back to its default behavior after calling ISldWorks::PresetNewDrawingParameters (i.e., display Sheet Format/Size dialog when opening a new drawing document). |
| Method | ResetUntitledCount | Resets the index of untitled documents. |
| Method | RestoreSettings | Restores the specified SOLIDWORKS settings from the specified *.sldreg file. |
| Method | ResumeSkinning | Resumes skinning windows. |
| Method | RevisionNumber | Gets the version number of this SOLIDWORKS installation. |
| Method | RunAttachedMacro | Runs the specified attached macro, module, and procedure. |
| Method | RunBatchSaveProcess | Batch saves files to 3DEXPERIENCE. |
| Method | RunCommand | Runs the specified SOLIDWORKS command. |
| Method | RunJournalCmd | Do not use. |
| Method | RunMacro | Obsolete. Superseded by ISldWorks::RunMacro2 . |
| Method | RunMacro2 | Runs a macro from a project file. |
| Method | SaveSettings | Saves the specified SOLIDWORKS settings to the specified *.sldreg file. |
| Method | SendMsgToUser | Obsolete. Superseded by ISldWorks::SendMsgToUser2 . |
| Method | SendMsgToUser2 | Displays a message box containing a message to the user, who is required to interact with it before continuing. |
| Method | SetAddinCallbackInfo | Obsolete. Superseded by ISldWorks::SetAddinCallbackInfo2 . |
| Method | SetAddinCallbackInfo2 | Sets add-in callback commands. |
| Method | SetApplySelectionFilter | Sets the current state of the selection filter. |
| Method | SetCurrentWorkingDirectory | Sets the current working directory to be used by SOLIDWORKS. |
| Method | SetMissingReferencePathName | Sets the missing reference file name. Use with the SOLIDWORKS event ReferenceNotFoundNotify . |
| Method | SetMouseDragMode | Sets the command-mouse mode. |
| Method | SetMultipleFilenamesPrompt | Sets the new filenames to open in response to the ISldWorks PromptForMultipleFileNamesNotify event. |
| Method | SetNewFilename | Sets the name of the new SOLIDWORKS file. |
| Method | SetPromptFilename | Obsolete. Superseded by ISldWorks::SetPromptFilename2 . |
| Method | SetPromptFilename2 | Sets the file to open in response to a SOLIDWORKS event. |
| Method | SetSearchFolders | Sets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents . |
| Method | SetSelectionFilter | Sets the current selection filter values for the specified item type. |
| Method | SetSelectionFilters | Sets the status for multiple selection filters. |
| Method | SetThirdPartyPopupMenuState | Sets whether to show or hide a third-party popup (shortcut) menu. |
| Method | SetToolbarDock | Obsolete. Superseded by ISldWorks::SetToolbarDock2 . |
| Method | SetToolbarDock2 | Sets the docking state of the toolbar. |
| Method | SetToolbarVisibility | Sets whether the specified toolbar is visible. |
| Method | SetUserPreferenceDoubleValue | Sets system default user preference values. |
| Method | SetUserPreferenceIntegerValue | Sets system default user preference values. |
| Method | SetUserPreferenceStringListValue | Sets the name of the DXF mapping files. |
| Method | SetUserPreferenceStringValue | Sets system default user preference values. |
| Method | SetUserPreferenceToggle | Sets system default user preference values. |
| Method | ShowBatchSaveTo3DExperienceDlg | Opens a dialog to save files in the specified folder to 3DEXPERIENCE. |
| Method | ShowBubbleTooltip | Displays a bubble ToolTip and flashes the specified toolbar button. |
| Method | ShowBubbleTooltipAt | Obsolete. Superseded by ISldWorks::ShowBubbleTooltipAt2 . |
| Method | ShowBubbleTooltipAt2 | Displays a bubble ToolTip at the specified location. |
| Method | ShowHelp | Displays the specified Help topic. |
| Method | ShowThirdPartyPopupMenu | Sets where to show a third-party pop-up (shortcut) menu. |
| Method | ShowToolbar | Obsolete. Superseded by ISldWorks::ShowToolbar2 . |
| Method | ShowToolbar2 | Obsolete. Not superseded. |
| Method | ShowUserNotification | Shows the specified user notification for a SOLIDWORKS add-in. |
| Method | SolidWorksExplorer | Starts SOLIDWORKS Explorer. |
| Method | UnInstallQuickTipGuide | Uninstalls your add-in's Quick Tips |
| Method | UnloadAddIn | Unloads the specified add-in from SOLIDWORKS. |
| Method | UploadToMySolidWorksSettings | Uploads the specified SOLIDWORKS Desktop settings to SOLIDWORKS Connected . |
| Method | VersionHistory | Gets a list of strings indicating the versions in which a model was saved. |

[Top](#topBookmark)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
