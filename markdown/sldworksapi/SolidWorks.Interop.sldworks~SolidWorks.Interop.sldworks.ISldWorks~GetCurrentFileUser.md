---
title: "GetCurrentFileUser Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCurrentFileUser"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentFileUser.html"
---

# GetCurrentFileUser Method (ISldWorks)

Gets the name of the user who has the the specified document open.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentFileUser( _
   ByVal FilePathName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.String

value = instance.GetCurrentFileUser(FilePathName)
```

### C#

```csharp
System.string GetCurrentFileUser(
   System.string FilePathName
)
```

### C++/CLI

```cpp
System.String^ GetCurrentFileUser(
   System.String^ FilePathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Full path and filename of the document

## VBA Syntax

See [SldWorks::GetCurrentFileUser](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCurrentFileUser.html).

## Examples

**Visual Basic for Applications (VBA)**

**'-----------------------------------**

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

Set swApp = Application.SldWorks

' Substitute your path and filename

Debug.Print swApp.GetCurrentFileUser("C:\temp\b&r.sldprt")

End Sub

**'-----------------------------------**

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
