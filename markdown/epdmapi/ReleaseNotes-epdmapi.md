---
title: "Release Notes"
project: "SOLIDWORKS PDM Professional API Help"
interface: ""
member: ""
kind: "topic"
source: "epdmapi/ReleaseNotes-epdmapi.html"
---

# Release Notes

This topic provides you with quick access to the enhancements made to SOLIDWORKS PDM Professional API.

- [SOLIDWORKS PDM Professional API 2025](#2025)
- [SOLIDWORKS PDM Professional API 2024](#2024)
- [SOLIDWORKS PDM Professional API 2023 SP01](#2023_sp01)
- [SOLIDWORKS PDM Professional API 2022](#2022)
- [SOLIDWORKS PDM Professional API 2021 SP04](#2021_sp04)
- [SOLIDWORKS PDM Professional API 2021 SP03](#2021_sp03)
- [SOLIDWORKS PDM Professional API 2021](#PDMPro2021)
- [SOLIDWORKS PDM Professional API 2020](#2020)
- [SOLIDWORKS PDM Professional API 2019 SP04](#2019SP04)
- [SOLIDWORKS PDM Professional API 2019 SP03](#2019SP03)
- [SOLIDWORKS PDM Professional API 2019](#2019)
- [SOLIDWORKS PDM Professional API 2018 SP04](#2018_sp04)
- [SOLIDWORKS PDM Professional API 2018 SP03](#2018SP03)
- [SOLIDWORKS PDM Professional API 2018](#2018)
- [SOLIDWORKS PDM Professional API 2017 SP01](#2017SP01)
- [SOLIDWORKS PDM Professional API 2017](#2017)
- [SOLIDWORKS PDM Professional API 2016](#2016)
- [SOLIDWORKS PDM Professional API 2015 SP04](#2015SP04)
- [SOLIDWORKS PDM Professional API 2015 SP03](#2015_SP03)
- [SOLIDWORKS PDM Professional API 2015 SP02](#2015_sp02)
- [SOLIDWORKS PDM Professional API 2015](#2015)
- [SOLIDWORKS PDM Professional API 2014](#2014)
- [SOLIDWORKS PDM Professional API 2013](#2013)
- [SOLIDWORKS PDM Professional API 2012](#2012)
- [SOLIDWORKS PDM Professional API 2011](#2011)
- [SOLIDWORKS PDM Professional API 2010](#2010)
- [SOLIDWORKS PDM Professional API 2009](#2009)
- [SOLIDWORKS PDM Professional API 2008](#2008)
- [SOLIDWORKS PDM Professional API 2007 SP03](#2007SP03)
- [SOLIDWORKS PDM Professional API 2007](#2007)
- [SOLIDWORKS PDM Professional API version 6.5](#6.5)
- [SOLIDWORKS PDM Professional API version 6.4](#6.4)
- [SOLIDWORKS PDM Professional API version 6.3](#6.3)

###### SOLIDWORKS PDM Professional API 2025

##### New interfaces

- [IEdmBomMgr4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4.html)
- [IEdmHistory4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4.html)

###### SOLIDWORKS PDM Professional API 2024

##### New interfaces and methods

- [IEdmBatchChangeState6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState6.html)
- [IEdmVault22::ADRunSync](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~ADRunSync.html)
- [IEdmVault22::ClearLogs](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~ClearLogs.html)
- [IEdmVault22::GetColumnSets](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetColumnSets.html)
- [IEdmVault22::GetCurrentColumnSet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetCurrentColumnSet.html)
- [IEdmVault22::SetColumnSetID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~SetColumnSetID.html)

##### New structure

- [EdmColumnSet](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmColumnSet.html)

###### SOLIDWORKS PDM Professional API 2023 SP01

##### New interface and method

- [IEdmFile18::GetThumbnail3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18~GetThumbnail3.html)

  (retrieves a file's thumbnail handle; obsoletes IEdmFile15::GetThumbnail2)

###### SOLIDWORKS PDM Professional API 2022

##### New interfaces

- [IEdmBomView4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView4.html)

  (rename a named BOM)
- [IEdmFolder13](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder13.html)

  (destroy deleted files by specifying EDMDeletedItems)
- [IEdmSerNoGen8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen8.html)

  (set the next counter value for serial numbers)
- [IEdmUser11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11.html)

  (specify user settings)
- [IEdmUserGroup9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9.html)

  (specify user group settings)

###### SOLIDWORKS PDM Professional API 2021 SP04

##### New interface

- [IEdmRefItem2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2.html)

  (get old and new paths for references that have been moved or renamed by another client)

##### New structure

- [EdmUpdatedRefPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUpdatedRefPath.html)

###### SOLIDWORKS PDM Professional API 2021 SP03

##### New interfaces

- [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html)

  (create a SOLIDWORKS BOM with any number of rows and columns and add it to a non-SOLIDWORKS document)
- [IEdmSWBom](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
- [IEdmSWBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomCell.html)
- [IEdmSWBomColumn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomColumn.html)
- [IEdmSWBomRow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomRow.html)

###### SOLIDWORKS PDM Professional API 2021

##### New functionality and interfaces

- Ability to display minor progress during callbacks. See

  [IEdmCallback8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback8.html)

  .
- Ability to retrieve results of a specified favorite search. See

  [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html)

  and

  [IEdmSearchResult6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6.html)

  .

###### SOLIDWORKS PDM Professional API 2020

##### New functionality and interfaces

- Support for BOM in Web 2. Get whether a specified user has permission to see a specified layout and get all of the BOM layouts in the vault. See

  [IEdmBomMgr2::CanSeeBomLayout](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~CanSeeBomLayout.html)

  and

  [IEdmBomMgr2::GetBomLayouts2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~GetBomLayouts2.html)

  .
- Support for file history in Web 2. Get the sorted history and the event description for a specified history item. See

  [IEdmHistory3::GetEventDescription](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetEventDescription.html)

  and

  [IEdmHistory3::GetSortedHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetSortedHistory.html)

  .
- Extended search functionality includes the ability to:

  - Create an extended search object. See

    [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html)

    .
  - Use new search syntax. See

    [Search Syntax](SearchSyntax-epdmapi.html)

    .
  - Add a multi-variable search condition. See

    [IEdmSearch9::AddMultipleVariableCondition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~AddMultiVariableCondition.html)

    .
  - Get search syntax errors. See

    [IEdmSearch9::GetSyntaxErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~GetSyntaxErrors.html)

    .
  - Use search syntax in existing IEdmSearch* properties and method parameters. See

    [IEdmSearch5::FileName](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~FileName.html)

    ,

    [IEdmSearch5::VersionComment](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~VersionComment.html)

    ,

    [IEdmSearch5::State](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~State.html)

    ,

    [IEdmSearch6::SetToken](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~SetToken.html)

    , and

    [IEdmSearch8::AddVariable2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html)

    .
- Get whether a document has cut list items. See

  [IEdmFile17::HasCutlistItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile17~HasCutlistItems.html)

  .
- Get and set whether focus is on the data card view. See

  [IEdmCardView64::IsFocusOnDataCard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView64~IsFocusOnDataCard.html)

  and

  [IEdmCardView64::SetFlagIsFocusOnDataCard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView64~SetFlagIsFocusOnDataCard.html)

  .
- Get whether a BOM row is a virtual component. See

  [IEdmBomCell2::IsVirtual](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell2~IsVirtual.html)

  .

##### New structure

- [EdmBomLayout2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout2.html)

###### SOLIDWORKS PDM Professional API 2019 SP04

##### New functionality and interface

- Create a file label. See

  [IEdmFile16::CreateLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16~CreateLabel.html)

  .

###### SOLIDWORKS PDM Professional API 2019 SP03

##### New functionality and interface

- Get all controls in a file or folder data card. See

  [IEdmCard7:GetAllControls](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7~GetAllControls.html)

  .

###### SOLIDWORKS PDM Professional API 2019

##### New functionality and interfaces

- Add users by login type to the vault. See

  [IEdmUserMgr10::AddUsers3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10~AddUsers3.html)

  .
- Get whether a specified user must add a state change comment for specified workflow transitions for specified documents. See

  [IEdmVault20::GetTransitionCommentPermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20~GetTransitionCommentPermissions.html)

  .
- Get specified files from a vault. See

  [IEdmVault20::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20~GetFiles.html)

  .
- Get the archive server log. See

  [IEdmVault20::GetArchiveServerLog](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20~GetArchiveServerLog.html)

  .

##### New structure

- [EdmDocIds](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2018 SP04

##### New functionality and interfaces

- Get and run a task add-in that is installed in the Administration tool. See

  [IEdmTaskMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html)

  .
- Get a file's thumbnail by file version. See

  [IEdmFile15::GetThumbnail2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15~GetThumbnail2.html)

  .

##### New structure

- [EdmTaskInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo.html)

###### SOLIDWORKS PDM Professional API 2018 SP03

##### New functionality and interfaces

- Create configuration values for drawings or other files lacking properties at the configuration level. See

  [IEdmFile14::GenerateDefaultConfigValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14~GenerateDefaultConfigValues.html)

  .
- Get the ID of the view in which a file is checked out. See

  [IEdmFile14::LockedOnViewID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14~LockedOnViewID.html)

  .

###### SOLIDWORKS PDM Professional API 2018

##### New functionality and interfaces

- Remove a PDM add-in. See

  [IEdmAddInMgr9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr9.html)

  .
- Get a list of values associated with a drop-down control on a data card. See

  [IEdmCardControl7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7.html)

  .
- Add custom tabs to a PDM vault view in File Explorer using a PDM add-in. The add-in:

  - implements hooks to allow third-parties to display their user interfaces in a custom tab.
  - supports custom tab names and icons.
  - supports multiple custom tabs.
  - programmatically removes custom tabs.
  - See

    [IEdmCmdMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6.html)

    .
- Change the state of a file using a specific transition. See

  [IEdmFile13](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html)

  .
- Get the thumbnail of a file. See

  [IEdmFile13](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html)

  .
- Restore deleted items from the recycle bin to the vault view. See

  [IEdmFolder11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11.html)

  .
- Construct more complicated search criteria using comparators and boolean operators. See

  [IEdmSearch8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html)

  .
- Call the Set Revision command to update a revision table in a SOLIDWORKS drawing in this vault. See

  [IEdmVault19](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html)

  .
- Copy an assembly tree of referenced parts and drawings to a destination folder. See

  [IEdmVault19](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html)

##### New structures

- [EdmCopyTreeOptions](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions.html)
- [EdmDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems.html)
- [EdmSimpleXRefInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSimpleXRefInfo.html)

###### SOLIDWORKS PDM Professional API 2017 SP01

##### New interfaces

- [IEdmVault18](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault18.html)

###### SOLIDWORKS PDM Professional API 2017

##### New interfaces

- [IEdmBatchListing4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4.html)
- [IEdmBomView3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView3.html)
- [IEdmEnumeratorCustomReference7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7.html)
- [IEdmEnumeratorVersion7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7.html)
- [IEdmFile12](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12.html)
- [IEdmFolder10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder10.html)
- [IEdmHistory2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2.html)
- [IEdmRevision7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7.html)
- [IEdmTemplate6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate6.html)
- [IEdmUserMgr9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html)
- [IEdmVersion8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8.html)
- [IEdmVault17](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault17.html)

##### New structures

- [EdmListFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html)
- [EdmStatePermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission.html)
- [EdmTransitionPermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission.html)

###### SOLIDWORKS PDM Professional API 2016

- SOLIDWORKS Enterprise PDM is now called SOLIDWORKS PDM, and the API is only available in SOLIDWORKS PDM Professional.

##### New interfaces

- [IEdmFolder9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9.html)
- [IEdmReference11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference11.html)
- [IEdmVault16](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault16.html)

###### SOLIDWORKS PDM Professional API 2015 SP04

##### New interfaces

- [IEdmBatchChangeState5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5.html)
- [IEdmEnumeratorVariable10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable10.html)

###### SOLIDWORKS PDM Professional API 2015 SP03

##### New interface

- [IEdmVault15](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault15.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2015 SP02

##### New interfaces

- [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html)
- [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html)
- [IEdmFile10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10.html)
- [IEdmFile11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile11.html)
- [IEdmTransition10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition10.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2015

- In:
- - 2015 SP0 and later, licenses are shared among all vaults that use the same SolidNetwork License Server (SNL). See

    [IEdmVault14::InstallLicense2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14~InstallLicense2.html)

    .
  - 2014 and earlier, licenses were shared among all vaults that were in the same SQL Server instance. IEdmVault14::InstallLicense2 obsoletes and replaces

    [IEdmVault11::InstallLicense](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~InstallLicense.html)

    .I
- Includes a new primary interop assembly (also called an interop) called

  EPDM.Interop.EPDMResultCode.dll

  for

  [return codes](ReturnCodes.htm)

  and for use with stand-alone applications. See

  [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm)

  for more information.

##### New interfaces

- [IEdmEnumeratorVersion6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6.html)
- [IEdmFile9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile9.html)
- [IEdmFolder8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8.html)
- [IEdmReference10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference10.html)
- [IEdmRevision6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6.html)
- [IEdmVault14](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14.html)
- [IEdmVersion6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6.html)
- [IEdmVersion7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion7.html)

###### SOLIDWORKS PDM Professional API 2014

- SOLIDWORKS Enterprise PDM API Help has been upgraded to be consistent with all of the other SOLIDWORKS API Help systems. For example, SOLIDWORKS Enterprise PDM API Help now includes syntax for VB.NET, C#, and managed C++ and a

  Send Feedback

  link on most Help topics. Additionally, SOLIDWORKS Enterprise PDM API Help:

  - contains updated

    Stand-alone Applications

    and

    Add-in Applications

    books and Help topics.
  - includes C# and VB.NET add-in and stand-alone code samples that you can recreate in Microsoft Visual Studio. If you use the local version of SOLIDWORKS Enterprise PDM API Help, then click the Index tab and type

    C# add-ins

    ,

    C# examples

    ,

    VB.NET add-ins

    , or

    VB.NET examples

    to quickly locate these examples. Additional examples will appear in subsequent releases.
  - is now available on the:

    - SOLIDWORKS Help menu,

      Help > API Help > SOLIDWORKS Enterprise PDM

      API Help

      .
    - internet,

      help.solidworks.com

      > API Help (English only

      )

      > SOLIDWORKS Enterprise PDM

      API Help

      .
  - SOLIDWORKS Enterprise PDM includes a primary interop assembly (also called an interop) called

    EPDM.Interop.epdm.dll

    for use with stand-alone applications

    .

    See

    [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm)

    for more information.
- Any application not supplied and supported by SOLIDWORKS Corporation that logs into SOLIDWORKS Enterprise PDM or directly accesses the database must ensure that sufficient SOLIDWORKS Enterprise PDM licenses are available when the same user is not logged into a local view.

  To make this easier to program and to comply with the

  [SOLIDWORKS End User License Agreement (EULA)](http://www.solidworks.com/sw/eula.htm)

  , SOLIDWORKS Enterprise PDM API 2014 includes a new login method called

  [IEdmVault13::LoginEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13~LoginEx.html)

  . This method ensures that licenses are properly consumed by the application.

##### New structure

- [EdmListRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListRef.html)

##### New method

- [IEdmVault13::LoginEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13~LoginEx.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2013

##### New interfaces

- [IEdmAddCustomRefs2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2.html)
- [IEdmBatchUnlock2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock2.html)
- [IEdmEnum](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum.html)
- [IEdmEnumeratorCustomReference6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6.html)
- [IEdmFindUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html)
- [IEdmImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage.html)
- [IEdmTransition8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition8.html)
- [IEdmUser10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10.html)
- [IEdmUserMgr8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8.html)
- [IEdmBatchChangeState2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2012

##### New interfaces

- [IEdmBatchDelete3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3.html)
- [IEdmEnumeratorVariable9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9.html)
- [IEdmFolder7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2011

##### New interfaces

- [IEdmCmdNode](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode.html)
- [IEdmLabel6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel6.html)
- [IEdmMenu7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu7.html)
- [IEdmUpdateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences.html)
- [IEdmVariableMgr7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr7.html)
- [IEdmGetOpCallback2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2.html)
- [IEdmReference8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8.html)
- [IEdmReference9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9.html)
- [IEdmState7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState7.html)
- [IEdmTransition7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7.html)
- [IEdmUser8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser8.html)
- [IEdmUserGroup7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup7.html)
- [IEdmVault12](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault12.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2010

##### New functionality

You can now program[items](Items.htm)and[tasks](tasks.htm).

##### New interfaces

- [IEdmAddInMgr8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8.html)
- [IEdmBatchItemGeneration](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
- [IEdmBatchItemGeneration2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2.html)
- [IEdmBatchItemReferenceUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate.html)
- [IEdmBatchRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html)
- [IEdmClearLocalCache2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache2.html)
- [IEdmFile8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8.html)
- [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
- [IEdmReference7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html)
- [IEdmSelectionList6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6.html)
- [IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
- [IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
- [IEdmUser7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7.html)
- [IEdmUserGroup6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6.html)
- [IEdmUserMgr7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
- [IEdmVault11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2009

##### New interfaces

- [IEdmBatchAdd2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd2.html)
- [IEdmBatchChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
- [IEdmBatchDelete2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2.html)
- [IEdmBatchListing2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2.html)
- [IEdmBom](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html)
- [IEdmBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html)
- [IEdmBomMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr.html)
- [IEdmBomView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html)
- [IEdmFile7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html)
- [IEdmMenu6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2008

##### New and changed functionality

- Visual Basic 6 is no longer supported. All add-ins must now be multi-threaded; for example, create your add-ins using the Visual Studio .NET development environment.
- The recommended way of accessing variables has changed. See

  [IEdmEnumeratorVariable8::CloseFile.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8~CloseFile.html)

##### New interfaces

- [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
- [IEdmClearLocalCache](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache.html)
- [IEdmAddInMgr7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr7.html)
- [IEdmHistoryUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate.html)
- [IEdmEnumeratorVariable8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html)

  [Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API 2007 SP03

##### New functionality

Support for[64-bit add-ins](64bit.htm)for the 64-bit version is included in this release.

##### New interface

- [IEdmRevisionMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2.html)

###### SOLIDWORKS PDM Professional API 2007

##### New interfaces

- [IEdmRevisionMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr.html)
- [IEdmSearch6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6.html)
- [IEdmUserMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6.html)
- [IEdmVariableMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API version 6.5

Conisio has been re-branded as SOLIDWORKS Enterprise PDM; however, an OEM-version of the product sold under the name Conisio still exists. Both of these products share the same API.

##### New and changed functionality

- The name of the type library has changed from

  ConisioLib

  to

  EdmLib

  .
- The name of the API has changed from

  Conisio 6.4 Type Library

  to

  PDMWorks Enterprise 6.5 Type Library

  .

  NOTE:

  The change in the name of the type library might require you to recompile existing applications. However, the names of all interfaces, structures, methods, properties, and enumerations are unchanged.

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional version 6.4

##### New functionality

- [Debugging add-ins](DebugAddins.htm)

  has improved.
- You can

  [create add-ins:](DotNetAddIns.htm)

  - using the Microsoft Visual Studio.NET development environment.
  - [that add menu commands to the SOLIDWORKS PDM Professional Administration tool menu](AddInAdminMenu.htm)

    .

##### New interfaces

- [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)
- [IEdmBatchListing](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
- [IEdmCard6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard6.html)
- [IEdmHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html)
- [IEdmRawReferenceMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html)
- [IEdmRefItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)
- [IEdmRefItemContainer](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer.html)
- [IEdmSerNoGen7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7.html)
- [IEdmSerNoValue](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoValue.html)
- [IEdmVariableValue6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue6.html)
- [IEdmVault8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8.html)

[Back to top](ReleaseNotes-epdmapi.html#Top)

###### SOLIDWORKS PDM Professional API version 6.3

##### New interfaces

- [IEdmAddCustomRefs](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
- [IEdmBatchAddFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html)
- [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
- [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html)
- [IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html)
- [IEdmCardView63](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView63.html)
- [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html)

  [Back to top](ReleaseNotes-epdmapi.html#Top)
