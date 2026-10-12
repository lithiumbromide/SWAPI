---
title: "GetOpenFileName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetOpenFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.html"
---

# GetOpenFileName Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::GetOpenFileName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOpenFileName( _
   ByVal DialogTitle As System.String, _
   ByVal InitialFileName As System.String, _
   ByVal FileFilter As System.String, _
   ByRef OpenOptions As System.Integer, _
   ByRef ConfigName As System.String, _
   ByRef DisplayName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DialogTitle As System.String
Dim InitialFileName As System.String
Dim FileFilter As System.String
Dim OpenOptions As System.Integer
Dim ConfigName As System.String
Dim DisplayName As System.String
Dim value As System.String

value = instance.GetOpenFileName(DialogTitle, InitialFileName, FileFilter, OpenOptions, ConfigName, DisplayName)
```

### C#

```csharp
System.string GetOpenFileName(
   System.string DialogTitle,
   System.string InitialFileName,
   System.string FileFilter,
   out System.int OpenOptions,
   out System.string ConfigName,
   out System.string DisplayName
)
```

### C++/CLI

```cpp
System.String^ GetOpenFileName(
   System.String^ DialogTitle,
   System.String^ InitialFileName,
   System.String^ FileFilter,
   [Out] System.int OpenOptions,
   [Out] System.String^ ConfigName,
   [Out] System.String^ DisplayName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DialogTitle`: Title of the dialog
- `InitialFileName`: Path and file name of the file to open
- `FileFilter`: File name extension of the file to open
- `OpenOptions`: Not used
- `ConfigName`: Name of the configuration
- `DisplayName`: Recommended file name to use

### Return Value

Path and file name of the file to open

## VBA Syntax

See [SldWorks::GetOpenFileName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetOpenFileName.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetOpenedFileInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenedFileInfo.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
