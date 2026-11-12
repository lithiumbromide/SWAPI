---
title: "GetRecentFiles Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetRecentFiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRecentFiles.html"
---

# GetRecentFiles Method (ISldWorks)

Gets a list of the most recently used files.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRecentFiles() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetRecentFiles()
```

### C#

```csharp
System.object GetRecentFiles()
```

### C++/CLI

```cpp
System.Object^ GetRecentFiles();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

List of most recently used files (see **Remarks**)

## VBA Syntax

See [SldWorks::GetRecentFiles](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetRecentFiles.html).

## Examples

```vb
'----------------------------------------
Option Explicit
Sub main()
    Dim swApp               As SldWorks.SldWorks
    Dim vFileArr            As Variant
    Dim i                   As Long
    Set swApp = Application.SldWorks

    vFileArr = swApp.GetRecentFiles

    For i = 0 To UBound(vFileArr) Step 2
        Debug.Print vFileArr(i + 1) & " --> " & vFileArr(i)
    Next i
End Sub
'----------------------------------------
```

## Remarks

The list is returned in pairs of files. For each pair, the first item is the fully qualified path to the file. The second item is just the filename, as it appears in the most recent used list in the SOLIDWORKS File menu.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
