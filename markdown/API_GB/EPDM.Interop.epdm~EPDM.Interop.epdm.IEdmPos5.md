---
title: "IEdmPos5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmPos5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html"
---

# IEdmPos5 Interface

Allows you to identify the position of an element in a list of elements.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmPos5
```

### C#

```csharp
public interface IEdmPos5
```

### C++/CLI

```cpp
public interface class IEdmPos5
```

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)

## Remarks

This object indicates the current position in a list of elements.

Typically you obtain this object using an object's "get first" method and then enumerate the list of elements by passing an IEdmPos5 object to an object's "get next" method.

## Accessors

[IEdmCard5::GetFirstControlPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetFirstControlPosition.html)

[IEdmCard5::GetNextControl](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetNextControl.html)

[IEdmCategoryMgr6::GetFirstCategoryPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetFirstCategoryPosition.html)

[IEdmCategoryMgr6::GetNextCategory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetNextCategory.html)

[IEdmDictionary5::LongFindKeys](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindKeys.html)

[IEdmDictionary5::LongFindValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindValues.html)

[IEdmDictionary5::LongGetFirstPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetFirstPosition.html)

[IEdmDictionary5::LongGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetNextAssoc.html)

[IEdmDictionary5::StringFindKeys](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindKeys.html)

[IEdmDictionary5::StringFindValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindValues.html)

[IEdmDictionary5::StringGetFirstPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetFirstPosition.html)

[IEdmDictionary5::StringGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetNextAssoc.html)

[IEdmEnumeratorCustomReference5::GetFirstRefPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetFirstRefPosition.html)

[IEdmEnumeratorCustomReference5::GetNextRef](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetNextRef.html)

[IEdmEnumeratorVersion5::GetFirstLabelPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstLabelPosition.html)

[IEdmEnumeratorVersion5::GetFirstRevisionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstRevisionPosition.html)

[IEdmEnumeratorVersion5::GetFirstVersionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstVersionPosition.html)

[IEdmEnumeratorVersion5::GetNextLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextLabel.html)

[IEdmEnumeratorVersion5::GetNextRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextRevision.html)

[IEdmEnumeratorVersion5::GetNextVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextVersion.html)

[IEdmFile5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFirstFolderPosition.html)

[IEdmFile5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetNextFolder.html)

[IEdmFolder5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstFilePosition.html)

[IEdmFolder5::GetFirstLabelPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstLabelPosition.html)

[IEdmFolder5::GetFirstSubFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstSubFolderPosition.html)

[IEdmFolder5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextFile.html)

[IEdmFolder5::GetNextLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextLabel.html)

[IEdmFolder5::GetNextSubFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextSubFolder.html)

[IEdmInbox5::GetFirstMessagePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetFirstMessagePosition.html)

[IEdmInbox5::GetNextMessage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetNextMessage.html)

[IEdmLabel5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFilePosition.html)

[IEdmLabel5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFolderPosition.html)

[IEdmLabel5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFile.html)

[IEdmLabel5::GetNextFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFileID.html)

[IEdmLabel5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolder.html)

[IEdmLabel5::GetNextFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolderID.html)

[IEdmPos5::Clone](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~Clone.html)

[IEdmReference5::GetFirstChildPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetFirstChildPosition.html)

[IEdmReference5::GetFirstParentPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetFirstParentPosition.html)

[IEdmReference5::GetNextChild](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextChild.html)

[IEdmReference5::GetNextParent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextParent.html)

[IEdmSelectionList5::GetHeadPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetHeadPosition.html)

[IEdmSelectionList5::GetNext](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetNext.html)

[IEdmState5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetFirstFilePosition.html)

[IEdmState5::GetFirstTransitionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetFirstTransitionPosition.html)

[IEdmState5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextFile.html)

[IEdmState5::GetNextTransition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextTransition.html)

[IEdmStrLst5::GetHeadPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5~GetHeadPosition.html)

[IEdmStrLst5::GetNext](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5~GetNext.html)

[IEdmTemplateMgr5::GetFirstTemplatePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5~GetFirstTemplatePosition.html)

[IEdmTemplateMgr5::GetNextTemplate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5~GetNextTemplate.html)

[IEdmUserGroup5::GetFirstUserPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetFirstUserPosition.html)

[IEdmUserGroup5::GetNextUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetNextUser.html)

[IEdmUserMgr5::GetFirstLoggedInUserPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstLoggedInUserPosition.html)

[IEdmUserMgr5::GetFirstUserGroupPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstUserGroupPosition.html)

[IEdmUserMgr5::GetFirstUserPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstUserPosition.html)

[IEdmUserMgr5::GetNextLoggedInUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextLoggedInUser.html)

[IEdmUserMgr5::GetNextUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUser.html)

[IEdmUserMgr5::GetNextUserGroup](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUserGroup.html)

[IEdmVariable5::GetFirstAttributePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~GetFirstAttributePosition.html)

[IEdmVariable5::GetNextAttribute](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~GetNextAttribute.html)

[IEdmVariableMgr5::GetFirstVariablePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetFirstVariablePosition.html)

[IEdmVariableMgr5::GetNextVariable](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetNextVariable.html)

[IEdmVariableValue5::GetFirstAttributePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetFirstAttributePosition.html)

[IEdmVariableValue5::GetNextAttribute](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetNextAttribute.html)

[IEdmVersion5::GetFirstRevisionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetFirstRevisionPosition.html)

[IEdmVersion5::GetNextRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetNextRevision.html)

[IEdmWorkflow5::GetFirstStatePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~GetFirstStatePosition.html)

[IEdmWorkflow5::GetFirstTransitionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~GetFirstTransitionPosition.html)

[IEdmWorkflow5::GetNextState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~GetNextState.html)

[IEdmWorkflow5::GetNextTransition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~GetNextTransition.html)

[IEdmWorkflow6::GetFirstStatePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetFirstStatePosition.html)

[IEdmWorkflow6::GetFirstTransitionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetFirstTransitionPosition.html)

[IEdmWorkflow6::GetNextState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetNextState.html)

[IEdmWorkflow6::GetNextTransition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetNextTransition.html)

[IEdmWorkflowMgr6::GetFirstWorkflowPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetFirstWorkflowPosition.html)

[IEdmWorkflowMgr6::GetNextWorkflow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetNextWorkflow.html)

## See Also

[IEdmPos5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
