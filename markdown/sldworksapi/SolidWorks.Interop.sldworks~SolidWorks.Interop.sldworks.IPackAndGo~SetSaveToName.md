---
title: "SetSaveToName Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "SetSaveToName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.html"
---

# SetSaveToName Method (IPackAndGo)

Obsolete. Superseded by

[IPackAndGo::SetSaveToName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSaveToName( _
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

value = instance.SetSaveToName(Override, SaveToName)
```

### C#

```csharp
System.bool SetSaveToName(
   System.bool Override,
   System.string SaveToName
)
```

### C++/CLI

```cpp
System.bool SetSaveToName(
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

[PackAndGo::SetSaveToName](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~SetSaveToName.html)

.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)

[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

[IPackAndGo::GetSaveToName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetSaveToName.html)

[IPackAndGo::FlattenToSingleFolder Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
