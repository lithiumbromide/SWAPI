---
title: "EdmUnlockOpMsg Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockOpMsg"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockOpMsg.html"
---

# EdmUnlockOpMsg Enumeration

Types of constant passed to [IEdmUnlockOpCallback::MsgBox](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~MsgBox.html) when the caller should either display a message to the user or process the message in some other way.

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockOpMsg
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockOpMsg : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockOpMsg : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Euom_AdminUndoLock | 5 = You are logged in as Admin and are trying to undo the check-out flag on a file checked out by another user |
| Euom_AdminUnlock | 8 = You are logged in as Admin and are trying to check in a file that is checked out by another user |
| Euom_CircularReference | 9 = The files checked have circular references |
| Euom_DocumentDoesNotMeetConditionsInAnyCategory | 11 = The document cannot be unlocked because it does not meet the conditions of any category |
| Euom_DocumentDoesNotMeetConditionsInAnyWorkflow | 10 = The document cannot be unlocked because it does not meet the conditions of any workflow |
| Euom_DuplicateUniqueVar | 1 = The file has a unique variable with a duplicate value |
| Euom_LocalFileNotFound | 6 = The local copy of the file was not found |
| Euom_LocalFileShareError | 7 = Sharing violation accessing the local copy of the file |
| Euom_MissingMandatoryVar | 2 = The file cannot be checked in, because the file contains a unique and constrained variable with a value that is already used elsewhere |
| Euom_UndoLockModified | 4 = The file about whose check out you about to undo, has been modified |
| Euom_UnknownFileFormat | 3 = SOLIDWORKS PDM Professional cannot read references or variables from the file, because its file format is unknown |

## Remarks

This constant tells which message to display.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
