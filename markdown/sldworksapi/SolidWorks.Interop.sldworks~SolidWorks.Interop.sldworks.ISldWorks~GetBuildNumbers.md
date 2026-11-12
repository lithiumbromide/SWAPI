---
title: "GetBuildNumbers Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetBuildNumbers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers.html"
---

# GetBuildNumbers Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::GetBuildNumbers2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetBuildNumbers2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetBuildNumbers( _
   ByRef BaseVersion As System.String, _
   ByRef CurrentVersion As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim BaseVersion As System.String
Dim CurrentVersion As System.String

instance.GetBuildNumbers(BaseVersion, CurrentVersion)
```

### C#

```csharp
void GetBuildNumbers(
   out System.string BaseVersion,
   out System.string CurrentVersion
)
```

### C++/CLI

```cpp
void GetBuildNumbers(
   [Out] System.String^ BaseVersion,
   [Out] System.String^ CurrentVersion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseVersion`: SOLIDWORKS major revision number
- `CurrentVersion`: SOLIDWORKS build number

## VBA Syntax

See [SldWorks::GetBuildNumbers](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetBuildNumbers.html).

## Examples

**Visual Basic for Applications (VBA)**

'-------------------------

Option Explicit

Dim swApp as SldWorks.SldWorks

Dim BaseVersion as String

Dim CurrentVersion as String

Sub main()

Set swApp = Application.SldWorks

swApp.**GetBuildNumbers** BaseVersion, CurrentVersion

Debug.Print "SOLIDWORKS major revision number: " & BaseVersion

Debug.Print "SOLIDWORKS build number: " & CurrentVersion

End Sub

'------------------------------------------

**Output**

SOLIDWORKS major revision number: SW2009_a1

SOLIDWORKS build number: d080407.062

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html)
[ISldWorks::IGetVersionHistoryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetVersionHistoryCount.html)
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.html)
[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
