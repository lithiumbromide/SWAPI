---
title: "GetBuildNumbers2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetBuildNumbers2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers2.html"
---

# GetBuildNumbers2 Method (ISldWorks)

Gets the build, major revision, and hot fix numbers of the SOLIDWORKS Design application.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetBuildNumbers2( _
   ByRef BaseVersion As System.String, _
   ByRef CurrentVersion As System.String, _
   ByRef HotFixes As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim BaseVersion As System.String
Dim CurrentVersion As System.String
Dim HotFixes As System.String

instance.GetBuildNumbers2(BaseVersion, CurrentVersion, HotFixes)
```

### C#

```csharp
void GetBuildNumbers2(
   out System.string BaseVersion,
   out System.string CurrentVersion,
   out System.string HotFixes
)
```

### C++/CLI

```cpp
void GetBuildNumbers2(
   [Out] System.String^ BaseVersion,
   [Out] System.String^ CurrentVersion,
   [Out] System.String^ HotFixes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseVersion`: Major revision number
- `CurrentVersion`: Build number
- `HotFixes`: Hot fix numbers

## VBA Syntax

See [SldWorks::GetBuildNumbers2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetBuildNumbers2.html).

## Examples

[Get Build Numbers (VBA)](Get_Build_Numbers_Example_VB.htm)
[Get Build Numbers (VB.NET)](Get_Build_Numbers_Example_VBNET.htm)
[Get Build Numbers (C#)](Get_Build_Numbers_Example_CSharp.htm)

## Remarks

Example outputs:

SOLIDWORKS major revision number: SW2009_a1

SOLIDWORKS build number: d080407.062

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html)
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.html)
[ISldWorks::IGetVersionHistoryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetVersionHistoryCount.html)
[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.html)

## Availability

SOLIDWORKS 2011 SP05, Revision Number 19.5
