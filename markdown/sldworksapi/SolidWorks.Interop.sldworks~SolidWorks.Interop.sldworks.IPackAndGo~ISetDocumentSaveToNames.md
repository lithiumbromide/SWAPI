---
title: "ISetDocumentSaveToNames Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "ISetDocumentSaveToNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html"
---

# ISetDocumentSaveToNames Method (IPackAndGo)

Sets the paths and filenames of the documents to save in Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetDocumentSaveToNames( _
   ByVal NameCount As System.Integer, _
   ByRef NameList As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim NameCount As System.Integer
Dim NameList As System.String
Dim value As System.Boolean

value = instance.ISetDocumentSaveToNames(NameCount, NameList)
```

### C#

```csharp
System.bool ISetDocumentSaveToNames(
   System.int NameCount,
   ref System.string NameList
)
```

### C++/CLI

```cpp
System.bool ISetDocumentSaveToNames(
   System.int NameCount,
   System.String^% NameList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameCount`: Number of documents comprising the model
- `NameList`: - in-process, unmanaged C++: Pointer to an array of strings containing the paths and filenames to which to save the model's documents
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the paths and filenames are set, false if not

## Remarks

The number, order, and type of documents must match the array returned by [IPackAndGo::IGetDocumentNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~IGetDocumentNames.html). You cannot change the filename of a document if the document is a virtual component. Duplicate files are not allowed.

To remove a file from Pack and Go, specify an empty string for that file's element in the NameList array. To override the paths and filenames set by this method, use [IPackAndGo::SetSaveToName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~SetSaveToName.html).

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::IGetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.html)
[IPackAndGo::SetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
