---
title: "IDocumentSpecification Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html"
---

# IDocumentSpecification Interface Members

The following tables list the members exposed by [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AddToRecentDocumentList | Gets or sets whether to add the opened document to the Recent Documents list. |
| Property | AutoRepair | Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened. |
| Property | ComponentList | Gets or sets the selected components to load when opening an assembly document. |
| Property | ConfigurationName | Gets or sets the name of the configuration to load when opening a model document. |
| Property | CriticalDataRepair | Gets or sets whether to automatically repair critical data errors in the file to be opened. |
| Property | DetailingMode | Gets or sets whether this drawing document is in detailing mode. |
| Property | DisplayState | Gets or sets the name of the display state to use when opening a model document. |
| Property | DocumentType | Gets or sets the type of model document to open. |
| Property | Error | Gets or sets the file load errors when opening a model document. |
| Property | FileName | Gets or sets the path and filename of the model document to open. |
| Property | IgnoreHiddenComponents | Gets or sets whether to load hidden components when opening an assembly or drawing document. |
| Property | InteractiveAdvancedOpen | Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document. |
| Property | InteractiveComponentSelection | Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the displayed components. |
| Property | LightWeight | Gets or sets whether to open an assembly or drawing document with lightweight parts. |
| Property | LoadExternalReferencesInMemory | Gets or sets whether to load external references in memory when opening a document. |
| Property | LoadModel | Gets or sets whether to load the model if the document is a detached drawing. |
| Property | PLMObjectSpecification | Gets the specification of this SOLIDWORKS Design connected to the 3DEXPERIENCE platform document. |
| Property | Query | Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API. |
| Property | ReadOnly | Gets or sets whether the model document is opened read-only or read-write. |
| Property | Selective | Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode. |
| Property | SheetName | Gets or sets the name of the sheet in a drawing document to open. |
| Property | Silent | Gets or sets whether to open the model document silently. |
| Property | UseLightWeightDefault | Gets or sets whether to use the system default lightweight setting. |
| Property | UseSpeedPak | Gets or sets whether to open an assembly document using the SpeedPak option. |
| Property | ViewOnly | Gets or sets whether to open the assembly document in Large Design Review mode. |
| Property | Warning | Gets or sets any file load warnings when opening a model document. |

[Top](#topBookmark)

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISldWorks::OpenDoc6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
