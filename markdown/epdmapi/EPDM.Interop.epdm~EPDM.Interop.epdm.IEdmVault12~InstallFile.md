---
title: "InstallFile Method (IEdmVault12)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault12"
member: "InstallFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault12~InstallFile.html"
---

# InstallFile Method (IEdmVault12)

Installs administrative export files (*.CEX) and card files (*.CRD).

## Syntax

### Visual Basic

```vb
Sub InstallFile( _
   ByVal bsPath As System.String, _
   ByVal lEdmInstallFileFlags As System.Integer, _
   ByVal oInstallArg As System.Object _
)
```

### C#

```csharp
void InstallFile(
   System.string bsPath,
   System.int lEdmInstallFileFlags,
   System.object oInstallArg
)
```

### C++/CLI

```cpp
void InstallFile(
   System.String^ bsPath,
   System.int lEdmInstallFileFlags,
   System.Object^ oInstallArg
)
```

### Parameters

- `bsPath`: Path to the file to install
- `lEdmInstallFileFlags`: Combination of [EdmInstallFileFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmInstallFileFlags.html) bits
- `oInstallArg`: ID of folder where to install the file; valid only if bsPath contains the path to a card file

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault12 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault12.html)
[IEdmVault12 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault12_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
