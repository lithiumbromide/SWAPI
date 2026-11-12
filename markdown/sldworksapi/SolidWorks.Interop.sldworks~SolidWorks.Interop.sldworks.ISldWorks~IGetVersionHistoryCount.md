---
title: "IGetVersionHistoryCount Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetVersionHistoryCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetVersionHistoryCount.html"
---

# IGetVersionHistoryCount Method (ISldWorks)

Gets the size of the array required to hold data returned by [ISldWorks::IVersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IVersionHistory.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVersionHistoryCount( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Integer

value = instance.IGetVersionHistoryCount(FileName)
```

### C#

```csharp
System.int IGetVersionHistoryCount(
   System.string FileName
)
```

### C++/CLI

```cpp
System.int IGetVersionHistoryCount(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full pathname of the model for which to get the version history

### Return Value

Size of array required for [ISldWorks::IVersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IVersionHistory.html)

## VBA Syntax

See [SldWorks::IGetVersionHistoryCount](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetVersionHistoryCount.html).

## Remarks

If the file is not found or an error occurs, then this method returns 0.

To get the version history of a document that is currently open, use [IModelDoc2::VersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~VersionHistory.html) or [IModelDoc2::IVersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IVersionHistory.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
