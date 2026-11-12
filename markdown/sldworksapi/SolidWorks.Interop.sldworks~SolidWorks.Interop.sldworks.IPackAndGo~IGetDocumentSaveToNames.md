---
title: "IGetDocumentSaveToNames Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "IGetDocumentSaveToNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.html"
---

# IGetDocumentSaveToNames Method (IPackAndGo)

Gets the paths and filenames to which to save the model's documents for Pack and Go set by [IPackAndGo::ISetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDocumentSaveToNames( _
   ByVal NameCount As System.Integer, _
   ByRef NameList As System.String, _
   ByRef StatusList As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim NameCount As System.Integer
Dim NameList As System.String
Dim StatusList As System.Integer
Dim value As System.Boolean

value = instance.IGetDocumentSaveToNames(NameCount, NameList, StatusList)
```

### C#

```csharp
System.bool IGetDocumentSaveToNames(
   System.int NameCount,
   out System.string NameList,
   out System.int StatusList
)
```

### C++/CLI

```cpp
System.bool IGetDocumentSaveToNames(
   System.int NameCount,
   [Out] System.String^ NameList,
   [Out] System.int StatusList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameCount`: Number of documents comprising the model
- `NameList`: - in-process, unmanaged C++: Pointer to an array of strings containing the paths and filenames of the model's documents
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `StatusList`: Array containing the types of documents as defined in [swPackAndGoDocumentStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPackAndGoDocumentStatus_e.html)

### Return Value

True if the paths and filenames of the model's documents are returned, false if not

## Remarks

Before calling this method, call [IPackAndGo::GetDocumentNamesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.html) to get the value of NameCount.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)
[IPackAndGo::GetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
