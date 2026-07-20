---
title: "System Options and Document Properties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/System_Options_and_Document_Properties.htm"
---

# System Options and Document Properties

You can get and set SOLIDWORKS system options and document
properties (also called user preferences) using SOLIDWORKS API enumerators
and methods.

As of SOLIDWORKS 2020 SP03.1, SOLIDWORKS can also run on the**3D**EXPERIENCE
platform as[SOLIDWORKS Connected](SOLIDWORKS_Connected.htm). User
preferences that are specific to or not supported in SOLIDWORKS Connected are
annotated as such. If you try to set a user preference that is unsupported in
SOLIDWORKS Connected, the action is blocked. To find these user preferences,
enter SOLIDWORKS Connected (in double quotes) in the Search tab.

To determine which enumerator corresponds with which system option or
document property, you can:

- change a system or document setting in the user
  interface while[recording
  a macro](../GettingStarted/SolidWorks_Macros.htm). Then edit the macro to identify the name and value of the
  enumerator that corresponds to the setting you just changed and to also
  identify the name of the method used to change (i.e., set) it. See the[System Options and Document Properties Get/Set Methods](#Get_Set)table at the end of this topic for a list of methods that get and set system-option
  and document-property enumerators.

  - or -
- locate the system option or document property
  in the SOLIDWORKS user interface and click the link that corresponds to
  it in the[Settings and Enumerators](#System)table in this topic. Each link opens a topic that
  contains a:

Remember to reset any option or property back to its original state
after the operation completes. System-option settings persist across SOLIDWORKS
sessions.

Settings and Enumerators

NOTE:Unlinked
text indicates that an enumerator does not exist for that system option,
document property, manager pane option, or menu item. Unlinked text is shown to help you more
easily map the text in the table with the text shown on the specified
tabs, manager panes, toolbars, and menus in the user interface.

(Table)=========================================================

| Tools > Options > System
Options tab | Tools >
Options > Document Properties tab | File menu | View menu | Insert menu | Tools menu | Window menu | Toolbars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Appears on tab: General 3DEXPERIENCE Integration (SOLIDWORKS Connected only) MBD (SOLIDWORKS only) Drawings - Display Style - Area Hatch/Fill - Performance Colors Sketch - Relations/Snaps Display Selection Performance Assemblies External
References Default
Templates File
Locations FeatureManager Spin
Box Increments View Backup/Recover (Backup for SOLIDWORKS only) Touch Hole
Wizard/Toolbox File
Explorer (SOLIDWORKS only) Search (SOLIDWORKS only) Collaboration (SOLIDWORKS only) Messages/Errors/Warnings Synchronize Settings (SOLIDWORKS Connected only) Import Export Does not appear on tab: Miscellaneous | Appears on tab: Drafting
Standard Annotations - Balloons - Datums - Geometric Tolerances - Location Label (drawings only) - Notes - Revision Clouds - Surface Finishes - Weld
Symbols Borders ( drawings only ) Dimensions - Angle - Angular Running - Arc
Length - Chamfer - Diameter - Hole
Callout - Linear - Ordinate - Radius Centerlines/Center
Marks (drawings only) DimXpert (drawings only) Tables - Bend (parts and drawings only) - Bill
of Materials - General - Hole (drawings only) - Punch (drawings only) - Revision (drawings only) - Title Block Table (parts and assemblies only) - Weld (drawings only) DimXpert (parts and assemblies only) - Size Dimension - Location Dimension - Chain Dimension - Geometric Tolerance - Chamfer Controls - Display Options Views (drawings only) - Auxiliary - Detail - Section - Orthographic - Other Virtual
Sharps Detailing Drawing Sheets ( drawings only ) Grid/Snap Units Line
Font (drawings only) Line Style (drawings only) Line
Thickness (drawings only) Model
Display (parts and assemblies only) Material
Properties (parts only) Image
Quality Sheet Metal MBD (parts only) Sheet
Metal Weldments Plane
Display (parts and assemblies only) Configurations (parts and assemblies only) Mates (assemblies only) Performance (drawings only) Does not appear on tab: - Miscellaneous | > Open > Files of type > Mesh
Files >
Options >
System Options > Import > STL/OBJ/OFF/PLY/PLY2 >
VRML > Options >
System Options > Import > VRML >
3D Manufacturing Format > Options >
System Options > Import > 3MF >
IDF > Options >
System Options > Import > IDF > Inventor, Catia V5, ProE/Creo, Unigraphics/NX,
or Solid Edge > Options >
System Options > Import > Inventor/Catia V5/Creo/NX/Solid Edge > STEP AP203/214/242, IGES, or ACIS > Options >
System Options > Import > STEP/IGES/ACIS > SLDXML > Options > System Options > Import > SLDXML > other type of file >
Options >
System Options >
Import > General > Save As >
Save as type >
Parasolid or Parasolid Binary > Options > System Options > Export > Parasolid > Save > Export (sheet metal parts only) > IGES >
Options > System Options > Export > IGES 5.3 >
STEP AP203 or STEP AP214 >
Options > System Options > Export > STEP >
IFC 2x3 or IFC 4 >
Options > System Options > Export > IFC > ACIS >
Options > System Options > Export > ACIS >
VRML >
Options > System Options > Export > VRML >
STL >
Options > System Options > Export > STL > VDAFS > Options > System Options > Export > VDA > 3D Manufacturing Format (*.3mf) > Options > System Options > Export > 3MF >
Additive Manufacturing File (*.amf) > Options > System Options > Export > AMF > Polygon File Format (*.ply) > Options > System Options > Export > PLY > eDrawings >
Options > System Options > Export > EDRW/ EPRT/ EASM >
Adobe Portable
Document Format > Save as
3D PDF > Options > System Options > Export > 3DPDF >
Options > System Options > Export > PDF >
Adobe Photoshop Files, Portable Network Graphics, JPEG, or Tif >
Options > System Options > Export > TIF/PSD/JPG/PNG >
Dwg or Dxf ( parts
and drawings
only ) >
Options > System Options > Export > DXF/DWG > Part (assemblies
only) >
Options > System Options > Export > SLDPRT from assembly > Page Setup > Print > Margins > Line
Thickness > Print3D | > Display > Modify > Filter Modified Components ( only for assemblies opened in Large Design
Review mode with one or more modified components ) > Hide / Show > User Interface | > Mate ( assemblies only ) | > Component Selection ( assemblies only ) > Select Identical Components > Sketch Entities > Corner
Rectangle or Center Rectangle or 3 Point Corner Rectangle or 3 Point Center
Rectangle or Parallelogram > Sketch Tools > Trim > Evaluate > Mass
Properties > Customize > Toolbars > Mouse Gestures | > Viewport | Sketch Ink |

[Back to top](#Top)

System Options
and Document Properties Get/Set Methods

(Table)=========================================================

| System Options | Document Properties |
| --- | --- |
| ISldWorks::GetUserPreferenceDoubleValue ISldWorks::SetUserPreferenceDoubleValue ISldWorks::GetUserPreferenceIntegerValue ISldWorks::SetUserPreferenceIntegerValue ISldWorks::GetUserPreferenceStringListValue ISldWorks::SetUserPreferenceStringListValue ISldWorks::GetUserPreferenceStringValue ISldWorks::SetUserPreferenceStringValue ISldWorks::GetUserPreferenceToggle ISldWorks::SetUserPreferenceToggle ISldWorks::DownloadFromMySolidWorksSettings (download settings from
SOLIDWORKS Connected) ISldWorks::UploadToMySolidWorksSettings (Upload settings to SOLIDWORKS
Connected) | IModelDocExtension::GetUserPreferenceDouble IModelDocExtension::SetUserPreferenceDouble IModelDocExtension::GetUserPreferenceDoubleValueRange IModelDocExtension::GetUserPreferenceInteger IModelDocExtension::SetUserPreferenceInteger IModelDocExtension::GetUserPreferenceString IModelDocExtension::SetUserPreferenceString IModelDocExtension::GetUserPreferenceTextFormat IModelDocExtension::SetUserPreferenceTextFormat IModelDocExtension::GetUserPreferenceToggle IModelDocExtension::SetUserPreferenceToggle |

[Back to top](#Top)
