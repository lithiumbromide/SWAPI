---
title: "Macros"
project: ""
interface: ""
member: ""
kind: "topic"
source: "draftsightapi/Macros.htm"
---

# Macros

The quickest and easiest way to start programming with the DraftSight API is to record a macro, which contains the DraftSight API calls that correspond to the actions performed interactively in DraftSight. This Help topic identifies the supported macro-recording programming languages and DraftSight interfaces and describes how to interactively and programmatically record macros.

- [Supported languages](#SupportedLangauges)
- [Supported interfaces](#SupportedInterfaces)
- [Interactively record macros](#Interactive)
- [Programmatically record macros](#Programmatic)

**NOTES**:

- Macro recording is available in DraftSight Premium only.
- You must use Microsoft Visual Studio 2008 to edit, debug, and build C++ Native, C#, VB, and C++ COM macro projects.

##### Supported languages

You can save macros as Microsoft Visual Studio 2008 projects, VBA script files, and JavaScript HTML files. Thus, you should be familiar with at least one of the following programming or scripting languages before using the macro recording feature of DraftSight:

- C++ Native (*.**vcproj**): Creates a Microsoft Visual Studio 2008 project and an add-in (.**dll**) in which you implement a command that executes the generated macro code. If you edit and rebuild the add-in after loading it, then you must close and restart DraftSight to reload the add-in.
- C# (*.**csproj**): Creates a Microsoft Visual Studio 2008 project and an external application (.**exe**) that executes the generated macro code that you can edit, rebuild, and rerun the project without closing DraftSight.
- JavaScript (*.**html**): Creates an HTML file from which you execute the generated JavaScript macro code. Open the HTML file in a web browser and click the button to execute the macro.
- VB (*.**vbproj**): Creates a Microsoft Visual Studio 2008 project and an external application (.**exe**) that you can edit, rebuild, and rerun the project without closing DraftSight. This type of Microsoft Visual Studio project is also commonly referred to as a VB.NET project.
- C++ COM (*.**vcproj**): Creates a Microsoft Visual Studio 2008 project and add-in (.**dll**) in which you implement a command that executes the generated macro code. If you edit and rebuild the add-in after loading it, then you must close and restart DraftSight to reload the add-in.
- VBA (*.**swb**): Creates a script file that you can:

  - Open, edit, debug, and run in the SOLIDWORKS VBA Integrated Development Environment (IDE).
  - Import into any Microsoft Office product that supports macros.

[Back to top](#Top)

##### Supported interfaces

This release supports recording macros for these interfaces:

- [IAlignedDimension](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension.html)
- [IAngularDimension](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension.html)
- [IApplicationOptions](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html) (only valid when [high-level of detail](#MacroLocation) set)
- [IArcLengthDimension](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension.html)
- [IAttributeDefinition](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
- [IAttributeInstance](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
- [IBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
- [IBlockInstance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
- [ICircle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
- [ICircleArc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
- [ICommandMessage](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html) (only valid when [high-level of detail](#MacroLocation) set)
- [ICustomCoordinateSystem](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
- [ICustomCoordinateSystemManager](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
- [IDiameterDimension](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)
- [IDimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager.html)
- [IEllipseArc](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
- [IEmbeddedObject](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
- [IExternalReference](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
- [IFace](Interop.dsAutomation~Interop.dsAutomation.IFace.html)
- [IGroup](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
- [IHatch](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
- [IInfiniteLine](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
- [IJoggedDimension](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension.html)
- [ILayer](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
- [ILeader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
- [ILine](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
- [ILineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Name.html)
- [IModel](Interop.dsAutomation~Interop.dsAutomation.IModel.html)
- [IModelNamedView](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
- [INamedView](Interop.dsAutomation~Interop.dsAutomation.INamedView.html)
- [INote](Interop.dsAutomation~Interop.dsAutomation.INote.html)
- [IOrdinateDimension](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension.html)
- [IPoint](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
- [IPolyFaceMesh](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
- [IPolygonMesh](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
- [IPolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
- [IPolyLine3D](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
- [IRadialDimension](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension.html)
- [IRay](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
- [IReferenceImage](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
- [IRegion](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
- [IRichLine](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
- [IRichLineStyle](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
- [IRotatedDimension](Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension.html)
- [ISelectionFilter](Interop.dsAutomation~Interop.dsAutomation.ISelectionFilter.html)
- [ISelectionManager](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
- [IShape](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
- [ISheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
- [ISheetNamedView](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html)
- [ISimpleNote](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
- [ISketchManager](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
- [ISolid](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
- [ISpline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
- [ITable](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
- [ITableStyle](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
- [ITextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
- [ITolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
- [ITrace](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
- [ITransparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html)
- [IViewManager](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
- [IViewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
- [IViewTile](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)

[Back to top](#Top)

##### Interactively record macros

Typically to interactively record a DraftSight macro:

1. Plan the interactive DraftSight actions before recording the macro.
2. Set the [location](#MacroLocation) where to save the macro's Microsoft Visual Studio 2008 project, JavaScript HTML file, or VBA .**swb** file.
3. Set the [level of detail](#MacroLocation) to appear in the macro's Microsoft Visual Studio 2008 project, JavaScript HTML file, or VBA .**swb** file.
4. [Record](#RecordMacro) the interactive DraftSight actions.

  NOTE: If you are unfamiliar with recording DraftSight macros, perform the interactive DraftSight actions a couple of times before starting to record the macro to eliminate possible extraneous actions such as zooming in or out of the drawing, panning, etc.
5. [Stop and save](#RecordMacro) the macro in the language you selected.

  A Microsoft Visual Studio 2008 project, JavaScript HTML file, or VBA .**swb** file is created upon saving the macro at the location specified in step 2.
6. Open the macro's Microsoft Visual Studio 2008 project, JavaScript HTML file in Notepad or any HTML editor, or VBA .**swb** file in the SOLIDWORKS VBA IDE or Microsoft Office VBA Editor.
7. [Edit, build, run, debug, rebuild, and rerun](#EditMacro), as needed, the macro. Repeat this step until the macro is executing as intended.
8. Save the macro's Microsoft Visual Studio 2008 project, JavaScript HTML file, or VBA .**swb** file.

[Back to top](#Top)

###### Interactively set macro location and level of detail

To set the location where to save DraftSight API macros and the level of detail to record:

1. Click **Tools > Options** to open the Options - System Options dialog.
2. Click the **System Options** button.
3. Expand **Macro Recording**.
4. Expand **Location**.
5. Type the path of the location where to save macros.
  - or -
  Click **Browse**, navigate to the folder where to save macros, and click **Select Folder**.

  The location where to save macros is stored in the sysvar APIPATH.
6. Expand **Level of detail**.
7. Select the level of detail to appear in the macro:

  - **Low**: Minimal code required to emulate interactive actions and execute.
  - **High**: Verbose code, including intermediate steps, required to emulate interactive actions and execute.

    **NOTE:** Data recorded in macros for methods that expect users to input data at the prompt in the command window, e.g., [ISketchManager::InsertCircle](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircle.html), are ignored when executing the macro. Instruct your users to examine the command window to determine if they must input data at the prompt in the command window when recording macros with the high-level of detail option selected. You might also want to delete the lines of code in the macro that prompt for data.

  The level of detail is stored in the sysvar APILEVEL.
8. Click **OK** to close the Options - System Options dialog.

[Back to top](#Top)

###### Interactively record and save a macro

To record and save a macro:

1. Click **Tools > Macro > Record** or type **_RECORDMACRO** in the command window.
2. Perform the interactive actions that you want to record.
3. When you are done recording, click **Tools > Macro > Stop** or type **_STOPMACRO** in the command window to stop and save the macro.
4. Type a name for the macro in **File Name** and select the language to which to save the generated macro code in **Save as type**.
5. Click **Save** to save the macro in the location specified in step 5 in the previous procedure.

###### Interactively edit, build, run, debug, rebuild, rerun, and save a macro

To edit, build, run, debug, rebuild, rerun, and save a macro:

1. Open the macro project in Microsoft Visual Studio 2008, JavaScript HTML file in Notepad or any HTML editor, or the VBA .**swb** file in the SOLIDWORKS VBA IDE or any Microsoft Office VBA Editor, in the location specified in step 5 in the **Set macro location and level of detail** procedure.
2. Edit the macro code to delete any extraneous lines of code, add lines of code for actions not performed interactively while recording the macro, reformat the code, etc.
3. Build, if needed, and run the project or file to test it.
4. Debug, rebuild, if needed, and rerun the project or file again. Repeat this step until the macro is executing as intended.
5. Save the project.

[Back to top](#Top)

##### Programmatically record macros

###### Programmatically start and stop macros

The DraftSight API includes two methods to programmatically start and stop macro recording:

- [IMacroManager::StartMacroRecording](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~StartMacroRecording.html)
- [IMacroManager::StopMacroRecording](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~StopMacroRecording.html) (You specify the project or file name for the macro when you use this method.)

These methods are useful if you want your add-in application to record and play back DraftSight macros. For example, if your add-in application allows end users to change dimension styles, then end users might want to record and play back the operations in a macro. This would allow end users to easily change dimension styles in a large number of files by playing back the macro.

###### Programmatically set macro location and level of detail

The DraftSight API includes properties for programmatically getting and setting:

- Language in which to record a macro. See [IMacroManager::Language](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~Language.html).
- Level of detail in which to record a macro. See [IMacroManager::LevelOfDetail](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~LevelOfDetail.html).
- Path where to save the macro. See [IMacroManager::SavePath](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~SavePath.html).

[Back to top](#Top)
