---
title: "SetSaveToName2 Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "SetSaveToName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.html"
---

# SetSaveToName2 Method (IPackAndGo)

Overrides the paths and filenames of the documents set by

[IPackAndGo::SetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html)

or

[IPackAndGo::ISetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)

with the specified path or the path and name of the Zip file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSaveToName2( _
   ByVal Override As System.Boolean, _
   ByVal SaveToName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim Override As System.Boolean
Dim SaveToName As System.String
Dim value As System.Boolean

value = instance.SetSaveToName2(Override, SaveToName)
```

### C#

```csharp
System.bool SetSaveToName2(
   System.bool Override,
   System.string SaveToName
)
```

### C++/CLI

```cpp
System.bool SetSaveToName2(
   System.bool Override,
   System.String^ SaveToName
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Override`: True to override the paths and filenames of the documents set by

[IPackAndGo::SetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html)

or

[IPackAndGo::ISetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)

, false to not
- `SaveToName`: Path or the path and filename of the Zip file to use to override the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames

### Return Value

True if the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames are overridden, false if not

## VBA Syntax

See

[PackAndGo::SetSaveToName2](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~SetSaveToName2.html)

.

## Examples

[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)

[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)

## Remarks

The difference between this method and the now obsolete IPackAndGo::SetSaveToName is that this method supports saving to minimal folders. It saves to any folder structure as defined by[IPackAndGo::FolderStructureOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FolderStructureOption.html).

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)

[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

[IPackAndGo::GetSaveToName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetSaveToName.html)

[IPackAndGo::FlattenToSingleFolder Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
