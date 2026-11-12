---
title: "GetDocumentSaveToNames Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "GetDocumentSaveToNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.html"
---

# GetDocumentSaveToNames Method (IPackAndGo)

Gets the paths and filenames to which to save the model's documents for Pack and Go set by [IPackAndGo::SetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentSaveToNames( _
   ByRef PathNameList As System.Object, _
   ByRef DocumentStatusList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim PathNameList As System.Object
Dim DocumentStatusList As System.Object
Dim value As System.Boolean

value = instance.GetDocumentSaveToNames(PathNameList, DocumentStatusList)
```

### C#

```csharp
System.bool GetDocumentSaveToNames(
   out System.object PathNameList,
   out System.object DocumentStatusList
)
```

### C++/CLI

```cpp
System.bool GetDocumentSaveToNames(
   [Out] System.Object^ PathNameList,
   [Out] System.Object^ DocumentStatusList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathNameList`: Array of strings containing the path and filenames to which to save the model's documents (see **Remarks**)
- `DocumentStatusList`: Array containing the types of documents as defined in [swPackAndGoDocumentStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPackAndGoDocumentStatus_e.html)

### Return Value

True if the paths and filenames of the model's documents are returned, false if not

## VBA Syntax

See [PackAndGo::GetDocumentSaveToNames](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~GetDocumentSaveToNames.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## Remarks

The order and number of documents must match the order of the array returned by [IPackAndGo::GetDocumentNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~GetDocumentNames.html). If a [prefix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~AddPrefix.html) or [suffix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~AddSuffix.html) is set, then the filenames include it. You can set both a prefix and suffix for the filenames.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::IGetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.html)
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
