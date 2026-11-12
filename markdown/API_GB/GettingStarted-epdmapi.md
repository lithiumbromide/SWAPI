---
title: "Getting Started"
project: "SOLIDWORKS PDM Professional API Help"
interface: ""
member: ""
kind: "topic"
source: "API_GB/GettingStarted-epdmapi.html"
---

# Getting Started

##### SOLIDWORKS PDM Professional Application Programming Interface

SOLIDWORKS PDM Professional’s application programming interface (API) gives you access to most of the functionality in SOLIDWORKS PDM Professional. For example, you can programmatically:

- Manage:

  - [Vaults](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html) and their [views](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVaultView.html)
  - [Users](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html) and [user groups](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)
  - File and folder [cards](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html) and their [views](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5.html)
  - [File references](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
  - [Card variables](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5.html) and [attributes](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAttribute5.html)
  - [Workflows](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html), [states](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html), and [transitions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html)
  - [Tasks](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
- Access:

  - Vault [items](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
  - [History](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html) of files and folders
  - [Versions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html) and [revisions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5.html) of files
  - [Templates](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5.html) installed in the vault
- [Search](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html) vaults and browse vault [folders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
- Check files [in](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) and [out](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) of the vault
- Send [messages](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5.html) to users
- Create [add-ins](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)

See the [Release Notes](ReleaseNotes-epdmapi.html) for the updates made to recent releases of the SOLIDWORKS PDM Professional API.

##### Applications

You can write two types of applications using this API:

1. [Stand-alone applications](StandAloneApp.htm) (**.exe** and **.dll**) that are called by other programs to use various features of SOLIDWORKS PDM Professional.
2. [Add-in applications](AddInApp.htm) that are called by SOLIDWORKS PDM Professional when users perform actions like check in or check out of a file, add a file to the vault, change the state of a file, etc.

##### Primary Assembly Interops

SOLIDWORKS PDM Professional includes two primary interop assemblies (also called interops) for use with stand-alone SOLIDWORKS PDM Professional applications:

- **EPDM.Interop.epdm.dll**
- **EPDM.interop.EPDMResultCode.dll**

The interops are stored in the top folder of your SOLIDWORKS PDM Professional installation.

- 32-bit interops are shipped with the 32-bit version of SOLIDWORKS PDM Professional.
- 64-bit interops are shipped with the 64-bit version of SOLIDWORKS PDM Professional.

See [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm) for more information.

##### See Also

[Return Codes](ReturnCodes.htm)

[TroubleShooting Guide](Troubleshooting_Guide.htm)
