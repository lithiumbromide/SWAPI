# Document Manager API
Reading and changing SOLIDWORKS files without running SOLIDWORKS (custom properties, configurations, references, tables, previews), based on the template in [../assets/docmgr/](../assets/docmgr/).
## Contents
- [When to use it](#when-to-use-it)
- [License key](#license-key)
- [Installation and references](#installation-and-references)
- [Opening and closing documents](#opening-and-closing-documents)
- [Interface families](#interface-families)
- [Custom properties](#custom-properties)
- [References](#references)
- [Tables, views and previews](#tables-views-and-previews)
- [Version compatibility](#version-compatibility)
- [Bulk processing](#bulk-processing)
## When to use it
- Metadata of many files (properties, configuration names, references, BOM tables, previews) without opening models: no geometry is loaded and no SOLIDWORKS session is needed, so thousands of files take minutes instead of hours.
- Not for geometry, rebuilds, exports or evaluated values that SOLIDWORKS has not saved yet; use the SOLIDWORKS API for those ([files-and-properties.md](files-and-properties.md)).
- Module `swdocmgrapi`; look members up with `swapi.py find QUERY --module swdocmgrapi`.
## License key
- Every application needs a Document Manager license key, available to subscription customers through the SOLIDWORKS customer portal. Request the categories you need: Basic, Previews, DimXpert, Geometry Streams, XML Streams, Tessellation; members outside the key's categories fail.
- Keys are tied to a major release: a key opens files saved by its release or older and must be renewed for each new major release; opening a newer file fails with `swDmDocumentOpenErrorNoLicense` or `swDmDocumentOpenErrorFutureVersion`.
- Never hardcode the key or ship it in software or shared source, as the license terms forbid sharing it outside the company. The template reads it from the environment variable `SW_DM_LICENSE_KEY`; when a user pastes a key into the conversation, keep it out of code meant for sharing and tell them to set the variable instead.
## Installation and references
- The API is the COM server `SwDocumentMgr.dll`, installed and registered with SOLIDWORKS under `<disk>:\Program Files\Common Files\SOLIDWORKS Shared`. On machines without SOLIDWORKS, copy `SwDocumentMgr.dll` and `zlib.dll` (both redistributable) into one folder, install the Visual C++ 2015 redistributable (and MSXML for component APIs), and register with `regsvr32` from an elevated prompt.
- Reference `SolidWorks.Interop.swdocumentmgr.dll` from `install_dir\api\redist` with Embed Interop Types False, and build x64 ([dotnet-addins.md](dotnet-addins.md#project-and-interop-references)).
## Opening and closing documents
- `SwDMClassFactory factory = new SwDMClassFactory();` then `ISwDMClassFactory.GetApplication(licenseKey)` returns the application; create it once per process.
- `ISwDMApplication.GetDocument(FullPathName, SwDmDocumentType, allowReadOnly, out SwDmDocumentOpenError)` opens by path; pass True for allowReadOnly unless you save. It returns null when the file is open read-write elsewhere; test the result and decode `SwDmDocumentOpenError` (`swDmDocumentOpenErrorFileNotFound`, `swDmDocumentOpenErrorFileReadOnly`, `swDmDocumentOpenErrorNoLicense`, `swDmDocumentOpenErrorFutureVersion`, `swDmDocumentOpenErrorNonSW`). `ISwDMApplication2.GetDocument2` opens from an `IStream` or `IStorage`.
- Pick the type from the extension (`swDmDocumentPart`, `swDmDocumentAssembly`, `swDmDocumentDrawing`).
- Save changes with `ISwDMDocument.Save` or `ISwDMDocument.SaveAs`, which return `SwDmDocumentSaveError`.
- Always call `ISwDMDocument.CloseDoc`, in a finally block, because open documents keep file handles and must be closed before `ISwDMApplication.CopyDocument` or `ISwDMApplication.MoveDocument`.
## Interface families
- Members are spread over numbered interfaces: `ISwDMDocument` to `ISwDMDocument29`, `ISwDMConfiguration` to `ISwDMConfiguration18`, `ISwDMConfigurationMgr` and `ISwDMConfigurationMgr2`, `ISwDMApplication` to `ISwDMApplication4`. `GetDocument` returns the base type; cast to the number that declares the member you need (`(ISwDMDocument17)doc`).
- `swapi.py members ISwDMDocument --family` shows which interface declares each member; check `since` against the oldest Document Manager release you support ([version availability](correctness-rules.md#version-availability)).
- Configurations: cast `ISwDMDocument.ConfigurationManager` to `ISwDMConfigurationMgr2` and use `ISwDMConfigurationMgr2.GetConfigurationNames2` and `ISwDMConfigurationMgr2.GetConfigurationByName2` (2019 and later, with `SwDMConfigurationError` results); the older `GetConfigurationNames` and `GetConfigurationByName` are obsolete. Configuration names come from `ISwDMConfiguration7.Name2`.
## Custom properties
- File level: `ISwDMDocument.GetCustomPropertyNames`, then `ISwDMDocument17.GetCustomProperty2(name, out SwDmCustomInfoType)` for the evaluated value, `ISwDMDocument5.GetCustomPropertyValues` for the value plus its link source, or `ISwDMDocument3.GetAllCustomPropertyNamesAndValues` for everything in one call.
- Configuration level: the same pattern on `ISwDMConfiguration.GetCustomPropertyNames`, `ISwDMConfiguration14.GetCustomProperty2`, `ISwDMConfiguration5.GetCustomPropertyValues` and `ISwDMConfiguration4.GetAllCustomPropertyNamesAndValues`.
- Values are evaluated as of the last save in SOLIDWORKS: a linked or equation property changed through Document Manager shows its new evaluated value only after SOLIDWORKS opens and saves the file. `GetCustomProperty2` returns values without the `fromparent+` prefix that `GetCustomProperty` adds for externally referenced values.
- Asking for a name that does not exist is an error path; read the names first, as the template does, and match case-insensitively.
- Writing: `ISwDMDocument.AddCustomProperty(name, SwDmCustomInfoType, value)`, `ISwDMDocument29.SetCustomProperty2` (2023 and later; `ISwDMDocument.SetCustomProperty` is obsolete), `ISwDMDocument.DeleteCustomProperty`, and the configuration equivalents (`ISwDMConfiguration.AddCustomProperty`, `ISwDMConfiguration18.SetCustomProperty2`, `ISwDMConfiguration.DeleteCustomProperty`); then `Save`. Check `ISwDMDocument22.IsCustomPropertyEditable` for linked properties.
- Cut-list items expose their own properties through `ISwDMCutListItem` and `ISwDMCutListItem2`.
## References
- Create search options with `ISwDMApplication.GetSearchOptionObject`, add folders with `ISwDMSearchOption.AddSearchPath` and set `ISwDMSearchOption.SearchFilters`, then call `ISwDMDocument21.GetAllExternalReferences5`, which also returns broken-reference flags, virtual flags, time stamps and imported paths.
- Repoint a reference with `ISwDMDocument.ReplaceReference`, then save.
## Tables, views and previews
- Tables in drawings: `ISwDMDocument10.GetTableNames(SwDmTableType)` (for example `swDmTableTypeBOM`), `ISwDMDocument10.GetTable(name)`, then `ISwDMTable.GetRowCount`, `ISwDMTable.GetColumnCount` and `ISwDMTable.GetCellText`.
- Views and sheets: `ISwDMDocument10.GetViews`, `ISwDMSheet4.GetViews`.
- Previews (Previews license category): `ISwDMDocument10.GetPreviewPNGBitmap`, `ISwDMConfiguration7.GetPreviewPNGBitmap` and `ISwDMSheet2.GetPreviewPNGBitmap`, each with a `SwDmPreviewError` result.
## Version compatibility
- `ISwDMDocument.GetVersion` returns the file's internal version number, mapped to releases in [versions.md](versions.md#file-version-numbers). Files from SOLIDWORKS 99 or earlier are not supported.
- `ISwDMApplication.GetLatestSupportedFileVersion` returns the newest version the installed DLL can read; compare before batch runs to report unreadable files up front.
- Document Manager release notes and member availability use their own product prefix (`SOLIDWORKS Document Manager API 2019 SP0`); `since` values read the same way as for the main API.
## Bulk processing
- One application object for the whole run; for each file: `GetDocument` read-only, read, `CloseDoc` in finally, log failures with the decoded open error and continue.
- Process files sequentially unless you have measured a gain from parallel work; thread safety of `SwDocumentMgr.dll` is not documented.
- Write output incrementally (the template streams CSV) so a crash late in a long run keeps earlier results.
## Sources
- `markdown/swdocmgrapi/GettingStarted-swdocmgrapi.md`
- `markdown/swdocmgrapi/ReleaseNotes-swdocmgrapi.md`
- `markdown/swdocmgrapi/Code_Example_CSharp.md`
- `markdown/swdocmgrapi/Get_Configuration-Specific_Custom_Properties_Example_CSharp.md`
- `markdown/swdocmgrapi/Get_BOM_Tables_Example_CSharp.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2~GetDocument2.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md`
