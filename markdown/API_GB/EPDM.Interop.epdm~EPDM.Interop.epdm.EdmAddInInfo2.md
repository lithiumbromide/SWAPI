---
title: "EdmAddInInfo2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddInInfo2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2.html"
---

# EdmAddInInfo2 Structure

Provides SOLIDWORKS PDM Professional with information about your add-in.

## Syntax

### Visual Basic

```vb
Public Structure EdmAddInInfo2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmAddInInfo2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmAddInInfo2 : public System.ValueType
```

## Examples

struct EdmAddInInfo2{
string [mbsAddInName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mbsAddInName.html);
string [mbsCompany](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mbsCompany.html);
string [mbsDescription](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mbsDescription.html);
integer [mlAddInVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mlAddInVersion.html);
integer [mlRequiredVersionMajor](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mlRequiredVersionMajor.html);
integer [mlRequiredVersionMinor](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mlRequiredVersionMinor.html);
string [mbsClassID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mbsClassID.html);
string [mbsModulePath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2~mbsModulePath.html);
};

## Examples

[Install Add-in (VB.NET)](Load_Addin_Example_VBNET.htm)
[Install Add-in (C#)](Load_Addin_Example_CSharp.htm)

## Remarks

Extends [EdmAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo.html) and is returned by [IEdmAddInMgr6::GetAddInInfo2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~GetAddInInfo2.html).

The data is displayed in the [Administrate Add-ins dialog box](AdminDlg.htm). If your add-in relies on features in a specific version of SOLIDWORKS PDM Professional, make it impossible to load the add-in in older versions of SOLIDWORKS PDM Professional by populating the mlRequiredVersionMajor and mlRequiredVersionMinor members.

If your add-in relies on features in a specific version of SOLIDWORKS PDM Professional, make it impossible to load the add-in in other versions of SOLIDWORKS PDM Professional by populating the mlRequiredVersionMajor and mlRequiredVersionMinor members.

| To restrict your add-in to run only in PDM Pro version... | Populate mlRequiredVersionMajor with... | Populate mlRequiredVersionMinor with... |
| --- | --- | --- |
| 2019 SP05 | 27 | 5 |
| 2020 SP03 | 28 | 3 |
| 2021 SP0 | 29 | 0 |

In general, you can find the major and minor versions for the PDM client version you are running in the Build number field of SOLIDWORKS PDM Administration Tool's **Help > About**.

C++ programmers must set string members to strings allocated with the Win32 function SysAllocString.

## See Also

[EdmAddInInfo2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
