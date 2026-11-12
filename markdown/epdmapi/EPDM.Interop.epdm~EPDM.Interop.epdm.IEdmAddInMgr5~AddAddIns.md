---
title: "AddAddIns Method (IEdmAddInMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr5"
member: "AddAddIns"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5~AddAddIns.html"
---

# AddAddIns Method (IEdmAddInMgr5)

Installs add-ins in SOLIDWORKS PDM Professional.

## Syntax

### Visual Basic

```vb
Sub AddAddIns( _
   ByVal bsPathList As System.String, _
   ByVal lEdmAddAddInFlags As System.Integer, _
   ByRef poReserved As System.Object _
)
```

### C#

```csharp
void AddAddIns(
   System.string bsPathList,
   System.int lEdmAddAddInFlags,
   ref System.object poReserved
)
```

### C++/CLI

```cpp
void AddAddIns(
   System.String^ bsPathList,
   System.int lEdmAddAddInFlags,
   System.Object^% poReserved
)
```

### Parameters

- `bsPathList`: Linefeed-separated list of path and file names of add-in files
- `lEdmAddAddInFlags`: Add-in option as defined in [EdmAddAddInFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddAddInFlags.html)
- `poReserved`: Nothing or null

## Examples

See the [IEdmAddInMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html) examples.

## See Also

[IEdmAddInMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html)
[IEdmAddInMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5_members.html)
[IEdmAddInMgr9::RemoveAddIn Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr9~RemoveAddIn.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
