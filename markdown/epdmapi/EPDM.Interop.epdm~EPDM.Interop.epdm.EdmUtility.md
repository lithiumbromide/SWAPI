---
title: "EdmUtility Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUtility"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html"
---

# EdmUtility Enumeration

Constants that are passed to the [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html) to create utility interfaces of various kinds.

## Syntax

### Visual Basic

```vb
Public Enum EdmUtility
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUtility : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUtility : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmUtil_AddCustomRefs | 8 = IEdmAddCustomRefs |
| EdmUtil_BatchAdd | 16 = IEdmBatchAdd |
| EdmUtil_BatchAddFolders | 14 = IEdmBatchAddFolders |
| EdmUtil_BatchChangeState | 22 = IEdmBatchChangeState |
| EdmUtil_BatchDelete | 20 = IEdmBatchDelete |
| EdmUtil_BatchGet | 12 = IEdmBatchGet |
| EdmUtil_BatchItemGeneration | 23 = IEdmBatchItemGeneration |
| EdmUtil_BatchItemReferenceUpdate | 25 = IEdmBatchItemReferenceUpdate |
| EdmUtil_BatchList | 13 = IEdmBatchListing |
| EdmUtil_BatchRefVars | 26 = IEdmBatchRefVars |
| EdmUtil_BatchUnlock | 6 = IEdmBatchUnlock |
| EdmUtil_BatchUpdate | 2 = IEdmBatchUpdate |
| EdmUtil_BomMgr | 24 = IEdmBomMgr |
| EdmUtil_CategoryMgr | 5 = IEdmCategoryMgr6 |
| EdmUtil_ClearLocalCache | 19 = IEdmClearLocalCache |
| EdmUtil_FindUser | 29 = IEdmFindUser |
| EdmUtil_History | 17 = IEdmHistory |
| EdmUtil_HistoryUpdate | 21 = IEdmHistoryUpdate |
| EdmUtil_RawReferenceMgr | 15 = IEdmRawReferenceMgr |
| EdmUtil_RevisionMgr | 18 = IEdmRevisionMgr |
| EdmUtil_Search | 1 = IEdmSearch5 (creates regular search objects only; to create an advanced search object, use IEdmVault21::CreateSearch2 ) |
| EdmUtil_SerNoGen | 11 = IEdmSerNoGen6 |
| EdmUtil_TaskMgr | 30 = IEdmTaskMgr |
| EdmUtil_TemplateMgr | 10 = IEdmTemplateMgr5 |
| EdmUtil_UpdateReferences | 27 = IEdmUpdateReferences |
| EdmUtil_UserMgr | 3 = IEdmUserMgr5 |
| EdmUtil_VariableMgr | 9 = IEdmVariableMgr5 |
| EdmUtil_WorkflowMgr | 4 = IEdmWorkflowMgr6 |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
