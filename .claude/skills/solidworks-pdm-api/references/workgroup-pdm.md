# Workgroup PDM (PDMWorks) API
SOLIDWORKS Workgroup PDM is the legacy project-based data management product; its API is a separate COM library (`PDMWorks.Interop.pdmworks` for .NET, type library objects without the `I` prefix for VBA and VB6). Use this file to read or port old code, never to write new vault automation; new work targets the PDM Professional API in [vault-programming.md](vault-programming.md). The API received no new functionality in recent releases.
## Object model
- `IPDMWConnection` is the root: create it with `CreateObject("PDMWorks.PDMWConnection")`, call `Login(user, password, server)` (optional request port 40000 and data port 30000; returns 0 on success), work, then `Logout`.
- The logged-in object model is a snapshot of the vault; after any change by the UI or the API (check-in, new project, note) call `Refresh` before reading again.
- Collections are VB-style and support `For Each`: `Documents`, `Projects`, `Users`, `Groups`, `Statuses`, `AdminDefinedProperties`.
- `IPDMWDocument`: `Name`, `Number`, `Description`, `Revision`, `Owner`, `project`, `Properties` (`IPDMWProperties` of `IPDMWProperty` `Name`/`Value`, written with `Update`), `Configurations` (`IPDMWConfiguration`), `References` and `WhereUsed` (`IPDMWLink`), `Notes`, `Revisions`, plus actions `TakeOwnership`, `ReleaseOwnership`, `ChangeStatus(lifecycleStatus)`, `ChangeProject`, `BumpRevision`, `Save`, `SaveAsPDF`, `AddNote`.
- `IPDMWProject`: `Name`, `Documents`, `SubProjects`, `CreateSubProject`, `SetUserPermissions`.
- `GetSpecificDocument(name, revision)` returns one document version (latest when the revision is empty).
## Check-in and search
- `CheckIn(filename, project, number, description, note, revisionOption, revision, lifecycle, retainOwnership, references)` checks in a closed document and returns the new `IPDMWDocument`. The caller must own the document (`TakeOwnership` first; failure throws Document ownership was denied). It works only where the Workgroup PDM Contributor or add-in client and the API DLL are installed, needs `pdmworks_libFNP.dll` to be findable (add its folder to `PATH`), supports SOLIDWORKS files saved in SOLIDWORKS 99 or later, uses `revision` only when `revisionOption` is `PDMWRevisionOptionType.Other`, and uses `references` only for Word and Excel documents; check in other referenced files one by one.
- Search: `GetSearchOptionsObject` returns `IPDMWSearchOptions` (`IgnoreCase`, `IgnoreLinks`, `IncludeHiddenDocuments`, `SearchConfigSpecificProperties`, `SearchOnlyChildrenOf`); add conditions with `SearchCriteria.AddCriteria(PDMWAndOr, PDMWPropertyType, propertyName, PDMWConditionType, value)`, run `Search(options)` and read `IPDMWSearchResult` (`Name`, `Number`, `Revision`, `Status`, `project`, `Document`). Criteria can be saved and reloaded with `SaveToFile` and `LoadFromFile`.
## Errors and versions
Methods return 0 or throw; in VBA trap errors with `On Error` and read `Err.Number` and `Err.Description`. Superseded members keep the base name with a higher number and are marked obsolete; call the newest one.
## Porting to PDM Professional
| Workgroup PDM | PDM Professional |
| --- | --- |
| `IPDMWConnection.Login` | `EdmVault5.LoginAuto` or `Login` |
| projects | folders (`IEdmFolder5`) |
| `IPDMWDocument.Properties` | card variables (`IEdmEnumeratorVariable5`) |
| ownership and `CheckIn` | `LockFile` and `UnlockFile` or the batch interfaces |
| lifecycle status (`ChangeStatus`) | workflow transitions (`IEdmFile13.ChangeState3`) |
| `Search` with criteria | `IEdmSearch5` and successors |
| `References`, `WhereUsed` | `IEdmFile5.GetReferenceTree` |
## Sources
- `markdown/pdmworksapi/Welcome-pdmworksapi.md`
- `markdown/pdmworksapi/GettingStarted-pdmworksapi.md`
- `markdown/pdmworksapi/ReleaseNotes-pdmworksapi.md`
- `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Login.md`
- `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.md`
- `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Search.md`
- `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~GetSpecificDocument.md`
- `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~TakeOwnership.md`
- `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeStatus.md`
- `markdown/pdmworksapi/Create_Search_Criteria_and_Search_Vault_Example_VB.md`
- `markdown/pdmworksapi/Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.md`
- `markdown/pdmworksapivb6/PDMWorks_gettingstarted.md`
