---
title: "SetDocumentSaveToNames Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "SetDocumentSaveToNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html"
---

# SetDocumentSaveToNames Method (IPackAndGo)

Sets the paths and filenames of the documents for Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDocumentSaveToNames( _
   ByVal PathNameList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim PathNameList As System.Object
Dim value As System.Boolean

value = instance.SetDocumentSaveToNames(PathNameList)
```

### C#

```csharp
System.bool SetDocumentSaveToNames(
   System.object PathNameList
)
```

### C++/CLI

```cpp
System.bool SetDocumentSaveToNames(
   System.Object^ PathNameList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathNameList`: Array of paths and filenames to which to save the model's documents

### Return Value

True if the paths and filenames are set, false if not

## VBA Syntax

See [PackAndGo::SetDocumentSaveToNames](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~SetDocumentSaveToNames.html).

## Remarks

The number, order, and type of documents to save must match the array returned by [IPackAndGo::GetDocumentNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~GetDocumentNames.html). You cannot change the filename of a document if the document is a virtual component. Duplicate files are not allowed.

To remove a file from Pack and Go, specify an empty string for that file's element in the PathNameList array. To override the paths and filenames set by this method, use [IPackAndGo::SetSaveToName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~SetSaveToName.html).

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::GetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.html)
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)
[IPackAndGo::FlattenToSingleFolder Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
